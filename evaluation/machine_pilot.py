"""Rescore frozen rankings with explicitly machine-authored exploratory annotations.

No human qrels, retrieval settings, gates or existing reports are changed.
The CLI never generates relevance labels: it validates the assistant's source-backed
annotations and makes their consequences reproducible.
"""
import argparse
import json
import math
import re
from datetime import datetime
from pathlib import Path

from backend.app.config import ROOT
from backend.app.domain import issue_text
from backend.app.storage import digest
from evaluation.scenario_eval import read, rows, sha_file
from evaluation.scenario_followup import batch_data, save, save_rows, save_csv


def validate_annotations(plan, annotations, data):
    if plan.get('reviewer_type') != 'machine' or plan.get('human_approvals_created') != 0:
        raise ValueError('Exploratory machine provenance required; no human approvals')
    query_ids = plan['query_ids']
    if not query_ids or len(set(query_ids)) != len(query_ids):
        raise ValueError('Distinct selected queries required')
    pool = {(p['query_id'], p['doc_id']):p for p in data['pool'] if p['query_id'] in query_ids}
    expected_queries = {q for q,_ in pool}
    if expected_queries != set(query_ids):
        raise ValueError('Selected query missing from frozen pool')
    seen = set()
    normalize = lambda s: ' '.join(s.split())
    for a in annotations:
        key = (a['query_id'],a['doc_id'])
        if key in seen or key not in pool:
            raise ValueError('Duplicate or unknown annotation')
        seen.add(key);p=pool[key];doc=data['documents'][a['doc_id']]
        if a.get('reviewer_type') != 'machine' or a.get('assessment_status') != 'AI_EXPLORATORY_NOT_HUMAN_VALIDATED':
            raise ValueError('Machine assessments must not masquerade as human review')
        if type(a.get('grade')) is not int or a['grade'] not in (0,1,2):
            raise ValueError('Explicit grade 0/1/2 required')
        for field in ('review_item_id','query_sha256','document_sha256'):
            if a[field] != p[field]:raise ValueError('Annotation ID/content hash mismatch')
        if a['document_sha256'] != digest(issue_text(doc)):
            raise ValueError('Frozen document content changed')
        if a.get('evidence_scope') != 'title_body' or not a.get('reason') or not a.get('recorded_at'):
            raise ValueError('Source scope, machine reason and recording time required')
        if datetime.fromisoformat(a['recorded_at'].replace('Z','+00:00')).tzinfo is None:
            raise ValueError('Machine recording time must include timezone')
        quote = a.get('evidence_quote','')
        if not quote or normalize(quote) not in normalize(issue_text(doc)) or a['evidence_url'] != doc['html_url']:
            raise ValueError('Literal frozen evidence and matching issue URL required')
    if seen != set(pool):raise ValueError('Full selected common pool must be assessed')
    return {qid:{a['doc_id']:a['grade'] for a in annotations if a['query_id']==qid} for qid in query_ids}


def scores(ordered_ids, grades):
    top = ordered_ids[:5]
    if len(set(top)) != len(top) or any(d not in grades for d in top):
        raise ValueError('Unique Top-5 documents must be in the assessed common pool')
    if any(type(v) is not int or v not in (0,1,2) for v in grades.values()):
        raise ValueError('Full explicit grades required')
    gains = lambda values: sum((2**g-1)/math.log2(i+2) for i,g in enumerate(values))
    dcg = gains([grades[d] for d in top]);idcg = gains(sorted(grades.values(),reverse=True)[:5])
    positive_ranks = [i for i,d in enumerate(top,1) if grades[d]==2]
    return {'ai_hit_at_5':int(bool(positive_ranks)),
            'ai_mrr_at_5':1/positive_ranks[0] if positive_ranks else 0.0,
            'ai_pooled_ndcg_at_5':dcg/idcg if idcg else None,
            'dcg_at_5':dcg,'shared_raw_pool_idcg_at_5':idcg}


def md_text(value):
    return str(value).replace('|','\\|').replace('\n',' ').replace('\r',' ')


def render(run):
    run=Path(run).resolve();plan=read(run/'plan.json');annotations=rows(run/'annotations.jsonl')
    if run.parent != (ROOT/'data/scenario_followup_v2').resolve() or not re.fullmatch(r'machine_\d+',run.name) or plan['run_id'] != run.name:
        raise ValueError('A separate machine_<number> run inside the follow-up workspace is required')
    data=batch_data(ROOT/plan['followup_batch'])
    if sha_file(data['parent']/'runs.jsonl') != plan['parent_rankings_sha256']:
        raise ValueError('Frozen ranking identity changed')
    grades=validate_annotations(plan,annotations,data)
    selected=[r for r in data['runs'] if r['kind']=='core' and r['query_id'] in grades]
    expected={(q,s,m) for q in grades for s in ('C_raw','C_bug') for m in ('bm25','semantic','hybrid')}
    if {(r['query_id'],r['corpus_scope'],r['method']) for r in selected} != expected:
        raise ValueError('All methods/scopes must share selected query universe')
    results=[];ranking_rows=[]
    for r in selected:
        qid=r['query_id'];scope=r['corpus_scope'];repo=r['repository'];g=grades[qid]
        scope_ids={f'{repo}#{d["number"]}' for d in data['scopes'][(repo,scope)]['issues']}
        s=scores([x['doc_id'] for x in r['ranked_results']],g)
        row={'assessment_kind':'AI_EXPLORATORY_NOT_HUMAN_VALIDATED','query_id':qid,'case_id':r['case_id'],
             'scope':scope,'method':r['method'],'positive_in_scope':any(d in scope_ids and grade==2 for d,grade in g.items()),
             'common_pool_size':len(g),'common_pool_hash':digest(sorted(g.items())),**s}
        results.append(row)
        for x in r['ranked_results'][:5]:
            doc=data['documents'][x['doc_id']]
            ranking_rows.append({'query_id':qid,'scope':scope,'method':r['method'],'rank':x['rank'],'doc_id':x['doc_id'],
                                 'title':doc['title'],'url':doc['html_url'],'ai_grade':g[x['doc_id']],'retrieval_score':x['score']})
    summary=[]
    for scope in ('C_raw','C_bug'):
        for method in ('bm25','semantic','hybrid'):
            cell=[r for r in results if r['scope']==scope and r['method']==method]
            eligible=[r for r in cell if r['positive_in_scope']]
            summary.append({'assessment_kind':'AI_EXPLORATORY_NOT_HUMAN_VALIDATED','scope':scope,'method':method,
                            'common_query_count':len(cell),'common_query_ids_hash':digest(sorted(grades)),
                            'positive_in_scope_queries':len(eligible),'excluded_by_scope':len(cell)-len(eligible),
                            'ai_hit_at_5':sum(r['ai_hit_at_5'] for r in cell)/len(cell),
                            'ai_mrr_at_5':sum(r['ai_mrr_at_5'] for r in cell)/len(cell),
                            'ai_pooled_ndcg_at_5':sum(r['ai_pooled_ndcg_at_5'] for r in cell)/len(cell),
                            'ai_conditional_hit_at_5':sum(r['ai_hit_at_5'] for r in eligible)/len(eligible) if eligible else None})
    output=ROOT/'docs/experiments/scenario_followup_v2'/run.name;output.mkdir(parents=True,exist_ok=True)
    if (output/'manifest.json').exists():
        old=read(output/'manifest.json')
        if old['annotations_sha256']!=sha_file(run/'annotations.jsonl') or old['plan_sha256']!=sha_file(run/'plan.json'):
            raise ValueError('Machine inputs changed: create a new run instead of overwriting')
    save(output/'plan.json',plan);save_rows(output/'machine_annotations.jsonl',annotations)
    save_csv(output/'results.csv',results);save_csv(output/'summary.csv',summary);save_csv(output/'top5.csv',ranking_rows)
    notes=[]
    for case in ['O-E1','T-E1','T-C2']:
        qid=case+':B_ko_context';q=data['queries'][qid]
        notes.extend([f'## {case}',f'```text\n{q["query_text"]}\n```',''])
        for scope in ('C_raw','C_bug'):
            for method in ('bm25','semantic','hybrid'):
                s=next(r for r in results if (r['query_id'],r['scope'],r['method'])==(qid,scope,method))
                notes.extend([f'### {scope} / {method}',f'AI Hit@5={s["ai_hit_at_5"]}; AI pooled nDCG@5={s["ai_pooled_ndcg_at_5"]:.6f}; 직접 관련 문서 범위 포함={s["positive_in_scope"]}',
                              '| 순위 | 원문 | AI 예비 등급 |','|---:|---|---:|'])
                for r in ranking_rows:
                    if (r['query_id'],r['scope'],r['method'])==(qid,scope,method):
                        notes.append(f'| {r["rank"]} | [{md_text(r["title"])}]({r["url"]}) | {r["ai_grade"]} |')
        notes.extend(['','### 공통 후보 전체의 AI 판정 근거','| 문서 | 등급 | 실제 인용 | 판정 이유 |','|---|---:|---|---|'])
        for a in annotations:
            if a['query_id']==qid:
                notes.append(f'| [{a["doc_id"]}]({a["evidence_url"]}) | {a["grade"]} | {md_text(a["evidence_quote"])} | {md_text(a["reason"])} |')
        notes.append('')
    (output/'casebook.md').write_text('# AI 예비 검토 사례집\n\n사람 판정이 아닙니다. 고정된 3개 개발 사례의 B 질의와 공통 후보만 검토했습니다.\n\n'+'\n'.join(notes),encoding='utf-8',newline='\n')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(11,4.3),sharey=True)
    methods=['bm25','semantic','hybrid'];colors=['#64748b','#6366f1','#0891b2']
    for ax,scope in zip(axes,['C_raw','C_bug']):
        values=[next(r['ai_pooled_ndcg_at_5'] for r in summary if r['scope']==scope and r['method']==m) for m in methods]
        bars=ax.bar(methods,values,color=colors);ax.bar_label(bars,fmt='%.3f',padding=4);ax.set_ylim(0,1.05)
        ax.set_title(scope+' | same 3 queries');ax.set_ylabel('AI-rated pooled nDCG@5');ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    fig.suptitle('AI exploratory convenience sample — NOT human validated',fontsize=13)
    fig.text(.5,.01,'Frozen rankings; 38 query/document assessments. Bug scope excludes the direct T-C2 issue.',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.04,1,.93]);(output/'images').mkdir(exist_ok=True);fig.savefig(output/'images/ai-comparison.png',dpi=160);plt.close(fig)
    changes=[]
    for qid in plan['query_ids']:
        for scope in ('C_raw','C_bug'):
            for baseline in ('bm25','semantic'):
                a=next(r for r in results if (r['query_id'],r['scope'],r['method'])==(qid,scope,baseline))
                b=next(r for r in results if (r['query_id'],r['scope'],r['method'])==(qid,scope,'hybrid'))
                delta=b['ai_pooled_ndcg_at_5']-a['ai_pooled_ndcg_at_5'];state='tie' if abs(delta)<1e-12 else 'better' if delta>0 else 'worse'
                changes.append({'query_id':qid,'scope':scope,'comparison':'saved hybrid vs saved '+baseline,'ai_ndcg_delta':delta,
                                'ai_result':state,'ai_hit_delta':b['ai_hit_at_5']-a['ai_hit_at_5']})
    save_csv(output/'paired_comparison.csv',changes)
    manifest={'status':'AI_EXPLORATORY_COMPLETE','human_validation':False,'human_reviewers':0,'official_quality_metrics':None,
              'selected_queries':len(grades),'annotated_pairs':len(annotations),'reused_ranking_conditions':len(results),'new_retrieval_conditions':0,
              'query_encodes':0,'document_encodes':0,'new_model_or_paid_api':False,'new_algorithm_experiments':False,
              'K1_R1_E1_E2_E3':'NOT_RUN_NO_HUMAN_EVIDENCE_GATE','parent_rankings_sha256':plan['parent_rankings_sha256'],
              'parent_manifest_sha256':sha_file(data['parent']/'manifest.json'),
              'parent_retrieval_code_hashes':data['manifest']['code_hashes'],'parent_model_revision':data['manifest']['config']['model_revision'],
              'selected_scope_versions':{f'{repo}|{scope}':v['version'] for (repo,scope),v in data['scopes'].items()},
              'annotations_sha256':sha_file(run/'annotations.jsonl'),'plan_sha256':sha_file(run/'plan.json'),'scorer_sha256':sha_file(Path(__file__)),
              'parent_preservation_files':len(read(ROOT/plan['followup_batch']/'parent-preservation.json')),
              'figure':{'source':'summary.csv','column':'ai_pooled_ndcg_at_5','generation':'python -m evaluation.machine_pilot --run '+run.relative_to(ROOT).as_posix(),
                        'source_sha256':sha_file(output/'summary.csv'),'png_sha256':sha_file(output/'images/ai-comparison.png')}}
    save(output/'manifest.json',manifest)
    table=['| 범위 | 방법 | 공통 N | AI Hit@5 | AI MRR@5 | AI pooled nDCG@5 | 직접 문서 범위 밖 |','|---|---|---:|---:|---:|---:|---:|']
    for r in summary:table.append(f'| {r["scope"]} | {r["method"]} | {r["common_query_count"]} | {r["ai_hit_at_5"]:.3f} | {r["ai_mrr_at_5"]:.3f} | {r["ai_pooled_ndcg_at_5"]:.3f} | {r["excluded_by_scope"]} |')
    report='''# AI 직접 검토 예비 비교 — machine_001

사용자의 “직접 쭉 진행” 요청에 따라 어시스턴트가 동결 원문을 읽고 **3개 사례·38개 질의/문서 쌍**을 직접 판정했습니다. 사람 판정·신원·시간·승인을 만들지 않았으며 기존 사람 qrels와 공식 지표는 변경하지 않았습니다. **이 표는 AI 판정에 의존하는 탐색적 결과입니다.**

'''+ '\n'.join(table)+'''

## 확인한 결과

- OpenCV MinGW `posix_memalign` 빌드 오류: 오류와 환경이 있는 B 질의에서는 원문 #29350이 세 방식 모두 1위입니다. AI 판정상 부분 관련 빌드 문제를 무관한 런타임 ASan 문제로 대체하는 Hybrid 결과도 있어 OpenCV의 pooled nDCG는 BM25보다 낮았습니다.
- Gemma4 영상 `tuple.to` 오류: #47879가 세 방식 모두 1위입니다. 같은 Gemma 이름이나 AttributeError라도 LoRA 분류기·Gemma1 GELU·KV cache 문제는 해당 영상 오류의 근거가 아닙니다. 본문의 수정 제안은 이 작업에서 실행 검증한 해결책이 아닙니다.
- Trainer 체크포인트 이동 후 종료 오류: #48315가 C_raw에서는 세 방식 모두 1위입니다. 동결 Bug 필터에는 이 문서가 없어 C_bug에서는 어떤 검색 알고리즘도 반환할 수 없습니다. 이 범위 누락과 순위 알고리즘 실패는 구분합니다.
- 직접 관련 문서의 Top-5 포함은 C_raw에서 3/3, C_bug에서 2/3입니다. C_bug의 직접 관련 문서가 실제 범위에 있는 2개 질의만 조건부로 보면 세 방식 모두 2/2입니다. 위 공식 분모는 범위와 방법 모두 동일한 3개 질의를 유지합니다.

성공·악화·무차이는 [실제 사례집](casebook.md), [Top-5 원자료](top5.csv), [방법별 결과](results.csv), [BM25와 Hybrid의 짝 비교](paired_comparison.csv)에 모두 남겼습니다. 이 비교는 기존 순위 간 비교이며 새 검색 설정을 실행한 before/after 실험이 아닙니다.

## 판정과 해석 조건

2점은 일치하는 증상·조건에 직접 유용한 근거, 1점은 관련 하위 기능이나 다른 오류/단계/조건으로 직접 원인 근거 부족, 0점은 넓은 단어·라이브러리·모델 이름만 겹치는 다른 기능입니다. [AI 판정 원본](machine_annotations.jsonl)의 모든 인용은 동결 제목/본문에 실제로 있고 문서·질의 해시와 URL을 코드로 검사했습니다. 인용의 존재 확인은 AI 관련성 판단 자체가 옳음을 보장하지 않습니다.

이 3개는 이미 참고 원문에서 재구성된 개발 사례를 편의 선택한 것입니다. B 질의만 검토했고 사람이 만든 독립 테스트셋이나 중복 정답 쌍이 아닙니다. 소스와 일부 순위를 이미 본 노출이 있어 블라인드 평가가 아닙니다. 3개 표본의 100%를 전체 검색 정확도로 해석하면 안 됩니다. 다른 9개 가족·A/C 질의·새 후보·일반 문제는 이 AI 품질 집계에 포함하지 않았습니다. 긴 문서는 제목과 관련 본문 구간을 읽었으며 링크 문서·댓글·상류 버그의 실제 재현까지 검증한 것은 아닙니다.

Bug 라벨·한국어 토큰·RRF를 동시에 또는 임의로 바꾸지 않았습니다. K1/R1/E1/E2/E3의 기존 사람 근거 게이트도 열지 않았습니다. 새 조회·모델 추론·학습·유료 API는 추가하지 않고 기존 18개 순위 조건만 재사용했습니다. 알려진 범위 누락을 개선이라고 꾸미거나 AI 판정을 공식 확정 지표로 옮기지 않습니다.

## 그림·재현·게시 코드 검증

![AI 예비 비교](images/ai-comparison.png)

그림의 수치는 [summary.csv](summary.csv)의 실제 값입니다. [manifest.json](manifest.json)에 원자료·그림·판정·검색 파일 해시와 생성 명령을 기록했습니다. 원문 전체·모델 캐시는 게시하지 않았습니다. [게시 코드 테스트](tests/published-tree.txt)와 [코드 바이트 증거](tests/published-tree.json)를 함께 제공합니다.

```powershell
.venv/Scripts/python.exe -m evaluation.machine_pilot --run data/scenario_followup_v2/machine_001
```

공개 수치 재집계는 `machine_annotations.jsonl`, `top5.csv`, `results.csv`, `summary.csv`로 가능합니다. 로컬 명령은 원래 동결 스냅샷과 `data/scenario_followup_v2/batch_001` 보존 자료가 필요합니다. 위 명령은 판정을 생성하지 않고 이미 기록한 AI 판정을 검증·재집계합니다. 사용자가 수행해야 하는 전체 검토는 추가하지 않았습니다.
'''
    (output/'report.md').write_text(report,encoding='utf-8',newline='\n')
    (output/'README.md').write_text('# AI 예비 비교\n\n[보고서](report.md) · [실제 사례](casebook.md) · [판정 원본](machine_annotations.jsonl) · [그림 원자료](summary.csv)\n\nAI 직접 검토 3개 사례·38쌍. 사람 검증·전체 정확도 확정이 아닙니다. 기존 검색 결과와 공식 사람 지표는 보존했습니다.\n',encoding='utf-8',newline='\n')
    from evaluation.followup_report import artifact_manifest
    artifact_manifest(output)
    print(json.dumps({'status':manifest['status'],'queries':len(grades),'machine_annotations':len(annotations),'human_reviewers':0,'new_retrieval_conditions':0}))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);args=p.parse_args();render(args.run)


if __name__=='__main__':main()
