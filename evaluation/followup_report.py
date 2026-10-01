"""Reports/PNG from actual frozen rows and current human review round."""
import html
import os
import re
import shutil
from pathlib import Path

from backend.app.config import ROOT
from backend.app.storage import digest
from evaluation.scenario_eval import read, rows, sha_file, now
from evaluation.scenario_followup import batch_data, save, save_rows, save_csv


def md(value):return html.escape(str(value)).replace('|','\\|').replace('\n',' ')


def public_text(text):
    text=re.sub(r'(?i)\b[A-Z]:[\\/][^\s`"<>]+','[LOCAL_PATH]',text)
    text=re.sub(r'/(?:home|Users|root)/[^\s`"<>]+','[LOCAL_PATH]',text)
    text=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[EMAIL]',text)
    text=re.sub(r'\b(?:gh[pousr]_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+)\b','[TOKEN]',text)
    return text


def progress_records(score):
    return [{'unit':'core_queries','approved':score['approved_queries'],'complete':score['complete_queries'],'pending':score['planned_queries']-score['complete_queries'],'total':score['planned_queries'],'human_reviewers':score['human_reviewers']},
            {'unit':'document_pairs','approved':None,'complete':score['judged_pairs'],'pending':score['pool_pairs']-score['judged_pairs'],'total':score['pool_pairs'],'human_reviewers':score['human_reviewers']}]


def figures(output,score,diagnostics,rrf):
    os.environ['MPLCONFIGDIR']=str(ROOT/'data/scenario_followup_v2/mpl-cache')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':11,'figure.dpi':150,'savefig.facecolor':'white'})
    images=output/'images';images.mkdir(exist_ok=True);specs=[]
    def emit(name,source,fig,rows_used):
        fig.savefig(images/name,bbox_inches='tight');plt.close(fig)
        specs.append({'image':'images/'+name,'data':source,'source_sha256':sha_file(output/source),'rows_used':rows_used,'generator':'evaluation/followup_report.py','generator_sha256':sha_file(ROOT/'evaluation/followup_report.py'),'command':'python -m evaluation.scenario_followup report --batch data/scenario_followup_v2/batch_001'})
    p=progress_records(score);save_csv(output/'figure_data/review-progress.csv',p)
    fig,ax=plt.subplots(figsize=(8,3.7));labels=['Core queries','Query/document pairs'];complete=[r['complete'] for r in p];pending=[r['pending'] for r in p]
    ax.barh(labels,complete,color='#10b981',label='Completed');ax.barh(labels,pending,left=complete,color='#cbd5e1',label='Pending')
    for i,r in enumerate(p):ax.text(max(x['total'] for x in p)*.5,i,f"{r['complete']} / {r['total']} complete",ha='center',va='center')
    ax.set_title(f"Review progress · {score['human_reviewers']} human reviewers");ax.set_xlabel('Count (pending is not a quality score)');ax.legend(loc='lower right');emit('review-progress.png','figure_data/review-progress.csv',fig,len(p))
    coverage=diagnostics.get('coverage',[])
    if coverage:
        save_csv(output/'figure_data/source-coverage.csv',coverage);fig,ax=plt.subplots(figsize=(8,4));positions=range(len(coverage))
        ax.bar([x-.18 for x in positions],[r['raw_documents'] for r in coverage],width=.36,label='C_raw',color='#64748b');ax.bar([x+.18 for x in positions],[r['bug_documents'] for r in coverage],width=.36,label='C_bug',color='#6366f1')
        for x,r in enumerate(coverage):
            ax.text(x-.18,r['raw_documents']+5,str(r['raw_documents']),ha='center');ax.text(x+.18,r['bug_documents']+5,str(r['bug_documents']),ha='center')
        ax.set_xticks(list(positions),[r['repository']+f"\nKnown core references: raw {r['raw_reference_n']}/{r['core_reference_n']}, Bug {r['bug_reference_n']}/{r['core_reference_n']}" for r in coverage]);ax.set_ylabel('Frozen issues');ax.set_title('Collected subset and Bug selection · not whole repositories');ax.legend();ax.set_ylim(0,max(r['raw_documents'] for r in coverage)*1.2);emit('source-coverage.png','figure_data/source-coverage.csv',fig,len(coverage))
    token=diagnostics.get('tokens',[])
    if token:
        token_data=[{'query_id':r['query_id'],'scope':r['scope'],'candidate_tokens':' '.join(r['ascii_boundary_candidates']),'tokens_in_corpus':' '.join(r['candidates_in_corpus']),'in_reference_count':len(r['candidates_in_reference'])} for r in token if r['ascii_boundary_candidates']]
        save_csv(output/'figure_data/token-diagnostic.csv',token_data,['query_id','scope','candidate_tokens','tokens_in_corpus','in_reference_count'])
        selected=[r for r in token_data if r['scope']=='C_raw']
        fig,ax=plt.subplots(figsize=(9,max(3,len(selected)*.28)));ax.barh([r['query_id'] for r in selected],[r['in_reference_count'] for r in selected],color='#818cf8');ax.set_xlabel('Boundary candidate tokens found in frozen reference');ax.set_title('Token trace · diagnostic only, relevance unjudged');emit('token-diagnostic.png','figure_data/token-diagnostic.csv',fig,len(token_data))
    if rrf:
        refs=[r for r in rrf if r.get('is_reference')];save_csv(output/'figure_data/rrf-contributions.csv',refs)
        fig,ax=plt.subplots(figsize=(9,4));labels=[r['query_id'].split(':')[0]+' / '+r['scope'] for r in refs];lex=[r['lexical_rrf_term'] for r in refs];sem=[r['semantic_rrf_term'] for r in refs]
        ax.barh(labels,lex,label='Lexical term',color='#64748b');ax.barh(labels,sem,left=lex,label='Semantic term',color='#818cf8')
        for i,r in enumerate(refs):ax.text(r['fused_score']+.00025,i,f"BM25 {r['bm25_rank']} · semantic {r['semantic_rank']} · fused {r['fused_rank']}",va='center',fontsize=9)
        ax.set_xlim(0,max(r['fused_score'] for r in refs)*2);ax.set_xlabel('RRF contribution (k=60, window=50)');ax.set_title('Reference document contributions · relevance unjudged');ax.legend();emit('rrf-contributions.png','figure_data/rrf-contributions.csv',fig,len(refs))
    # Quality graphs require completed common pools. Never draw nulls as zero.
    eligible=[r for r in score['summary'] if r['repository']=='ALL' and r['stratum']=='ALL' and r['comparison_n']]
    if eligible:
        save_csv(output/'figure_data/quality-by-input.csv',eligible);fig,ax=plt.subplots(figsize=(10,5));labels=[r['method']+'/'+r['scope']+'/'+r['variant'].split('_')[0] for r in eligible];ax.bar(range(len(eligible)),[r['hit_at_5'] for r in eligible],color='#6366f1');ax.set_xticks(range(len(labels)),labels,rotation=70,ha='right');ax.set_ylabel('Hit@5');ax.set_ylim(0,1);ax.set_title('Common completed queries only · n shown in source CSV');emit('quality-by-input.png','figure_data/quality-by-input.csv',fig,len(eligible))
        judged=[r for r in eligible if r['pooled_ndcg_at_5'] is not None]
        if judged:
            save_csv(output/'figure_data/ndcg-by-input.csv',judged);fig,ax=plt.subplots(figsize=(10,5));ax.bar(range(len(judged)),[r['pooled_ndcg_at_5'] for r in judged],color='#6366f1');ax.set_xticks(range(len(judged)),[r['method']+'/'+r['scope']+'/'+r['variant'].split('_')[0] for r in judged],rotation=70,ha='right');ax.set_ylim(0,1);ax.set_ylabel('Pooled nDCG@5');ax.set_title('Shared C_raw pool IDCG · completed judgments only');emit('ndcg-by-input.png','figure_data/ndcg-by-input.csv',fig,len(judged))
    save(output/'figure_data/generation.json',{'generated_at':now(),'pool_version':score['pool_version'],'qrels_version':score['qrels_version'],'figures':specs})


def report(batch):
    batch=Path(batch);d=batch_data(batch);current=read(batch/'current-round.json');round_dir=batch/'rounds'/current['round_id'];score=read(round_dir/'score.json');resolved=read(round_dir/'qrels.json');receipt=read(round_dir/'receipt.json')
    output=ROOT/'docs/experiments/scenario_followup_v2'/batch.name;output.mkdir(parents=True,exist_ok=True)
    diagnostics=read(batch/'diagnostics.json') if (batch/'diagnostics.json').exists() else {}
    diagnostics['coverage']=[{'repository':repo,'raw_documents':len(d['scopes'][(repo,'C_raw')]['issues']),'bug_documents':len(d['scopes'][(repo,'C_bug')]['issues']),'partial':d['manifest']['snapshots'][repo]['partial']} for repo in d['snapshots']]
    for r in diagnostics['coverage']:
        reference_ids={did for c in d['cases'].values() if c['repository']==r['repository'] and c['cohort']=='core_development' for did in c['source_doc_ids']}
        raw_ids={f'{r["repository"]}#{x["number"]}' for x in d['scopes'][(r['repository'],'C_raw')]['issues']};bug_ids={f'{r["repository"]}#{x["number"]}' for x in d['scopes'][(r['repository'],'C_bug')]['issues']}
        r.update(core_reference_n=len(reference_ids),raw_reference_n=len(reference_ids&raw_ids),bug_reference_n=len(reference_ids&bug_ids))
    rrf=read(batch/'rrf-contributions.json') if (batch/'rrf-contributions.json').exists() else []
    for r in rrf:r['is_reference']=r['doc_id'] in d['cases'][d['queries'][r['query_id']]['case_id']]['source_doc_ids']
    reproduction=read(batch/'reproduction.json') if (batch/'reproduction.json').exists() else {'status':'PENDING','conditions':0}
    budget=read(batch/'budget.json') if (batch/'budget.json').exists() else {'logical_conditions':0,'http_calls':0}
    save(output/'lineage.json',{**d['lineage'],**receipt,'review_html_code_hashes':{f.name:sha_file(f) for f in (ROOT/'evaluation/scenario_followup_v2').glob('review.*')},'parent_not_modified':True})
    experiment_receipts=[read(p) for p in sorted((batch/'experiments').glob('*/receipt.json'))] if (batch/'experiments').exists() else []
    experiment_states={r['experiment']:r['status'] for r in experiment_receipts}
    save(output/'status.json',{'status':score['state'],'human_reviewers':score['human_reviewers'],'single_human_reviewer':score['single_human_reviewer'],'review_pairs':score['pool_pairs'],'judged_pairs':score['judged_pairs'],'planned_queries':score['planned_queries'],'complete_queries':score['complete_queries'],'comparison_queries':score['comparison_queries'],
                             'stages':{'preservation':'VERIFIED','scoring':'IMPLEMENTED_TESTED','review_html':'READY','human_review':score['state'],'mechanical_audit':'COMPLETE' if diagnostics.get('tokens') else 'PENDING','reproduction':reproduction['status'],
                                       'K1':experiment_states.get('K1','DEFERRED_NO_VALIDATED_FAILURE'),'R1':experiment_states.get('R1','DEFERRED_NO_VALIDATED_FAILURE'),'E1':experiment_states.get('E1','AWAITING_EQUIVALENCE_REVIEW'),'E2':experiment_states.get('E2','BLOCKED_CONDITION_EVIDENCE'),'E3':experiment_states.get('E3','NO_CERTIFIED_CONTROL'),'manual_study':'PENDING_MANUAL_STUDY','summary':'NOT_APPLICABLE_YET'},
                             'quality_figures':'GENERATED' if score['comparison_queries'] else 'NOT_GENERATED_PENDING_REVIEW','screenshot':'CAPTURED' if (batch/'review-screen.png').exists() else 'screenshot_unavailable','budget':budget})
    save_csv(output/'metrics_by_query.csv',score['by_query']);save_csv(output/'metrics_summary.csv',score['summary']);save_csv(output/'review_progress.csv',progress_records(score))
    paired=[];baseline={(r['query_id'],r['corpus_scope'],r['method']):r for r in score['by_query'] if r['method'] in {'bm25','semantic','hybrid'}}
    for r in score['by_query']:
        bm={'K1_bm25':'bm25','K1_hybrid':'hybrid','R1_hybrid':'hybrid'}.get(r['method']);old=baseline.get((r['query_id'],r['corpus_scope'],bm))
        if not old or not r['common_comparison_eligible'] or not old['common_comparison_eligible']:continue
        hit=r['hit_at_5']-old['hit_at_5'];ndcg=r['pooled_ndcg_at_5']-old['pooled_ndcg_at_5'] if r['pooled_ndcg_at_5'] is not None and old['pooled_ndcg_at_5'] is not None else None
        values=[hit]+([ndcg] if ndcg is not None else [])
        decision='mixed' if min(values)<0<max(values) else 'worse' if min(values)<0 else 'improved' if max(values)>0 else 'tie'
        paired.append({'query_id':r['query_id'],'scope':r['corpus_scope'],'baseline_method':bm,'candidate_method':r['method'],'pool_version':r['pool_version'],'qrels_version':r['qrels_version'],'hit_difference':hit,'ndcg_difference':ndcg,'decision':decision})
    save_csv(output/'paired_changes.csv',paired,['query_id','scope','baseline_method','candidate_method','pool_version','qrels_version','hit_difference','ndcg_difference','decision'])
    counts={r['experiment']:r['conditions'] for r in experiment_receipts}
    save_csv(output/'experiments.csv',[{'stage':k,'status':v,'executed_conditions':reproduction['conditions'] if k=='reproduction' else counts.get(k,0),'saved_parent_conditions_reused':len([r for r in d['runs'] if r['kind']=='core']) if k=='scoring' else 0} for k,v in read(output/'status.json')['stages'].items()])
    save(output/'reproduction.json',reproduction);save(output/'budget.json',budget)
    save_csv(output/'scope-audit.csv',diagnostics.get('scope',[]));save_csv(output/'token-audit.csv',diagnostics.get('tokens',[]));save_csv(output/'rrf-contributions.csv',rrf)
    qrels={(r['query_id'],r['doc_id']):r for r in resolved['qrels']};catalog={};chunk_rows=[]
    local_chunks=rows(batch/'chunk-evidence.local.jsonl') if (batch/'chunk-evidence.local.jsonl').exists() else []
    for r in local_chunks:
        did=r['doc_id'];eid='chunkdoc_'+digest(did)[:16]
        if eid not in catalog:
            original=' '.join(r['document_span'].split()[:16]);masked=public_text(original)
            catalog[eid]={'evidence_id':eid,'kind':'decoded_max_similarity_segment','doc_id':did,'url':d['documents'][did]['html_url'],'query_id':r['query_id'],'document_chunk':r['document_chunk'],'query_chunk':r['query_chunk'],'short_segment':masked,
                          'source_document_sha256':digest(__import__('backend.app.domain',fromlist=['issue_text']).issue_text(d['documents'][did])),'original_segment_sha256':digest(original),'public_segment_sha256':digest(masked),'masked':original!=masked,'restricted_evidence':original!=masked,'human_classification':None}
        chunk_rows.append({k:v for k,v in r.items() if k not in {'document_span','query_span','evidence_id'}}|{'example_evidence_id':eid,'same_example_chunk':r['document_chunk']==catalog[eid]['document_chunk'],'full_span_location':'gitignored frozen parent runs.jsonl'})
    for row in resolved['qrels']:
        for evidence in row['evidence']:
            if not evidence.get('evidence_quote'):continue
            eid='human_'+digest([row['review_item_id'],evidence])[:16];original=' '.join(evidence['evidence_quote'].split()[:20]);masked=public_text(original)
            catalog[eid]={'evidence_id':eid,'kind':'actual_human_quote','doc_id':row['doc_id'],'query_id':row['query_id'],'url':evidence['evidence_url'],'short_segment':masked,'source_document_sha256':row['document_sha256'],'original_segment_sha256':digest(original),'public_segment_sha256':digest(masked),'masked':original!=masked,'restricted_evidence':original!=masked,'human_reason':public_text(evidence['reason']),'scope':evidence['evidence_scope']}
    save_rows(output/'evidence_catalog.jsonl',list(catalog.values()));save_csv(output/'chunk-audit.csv',chunk_rows)
    # Local whole bodies stay untracked. Public review queue contains identifiers and blank answers.
    queue=output/'review_queue';queue.mkdir(exist_ok=True)
    for name in ['query_reviews.csv','human_reviews.csv']:
        if (batch/'review'/name).exists():shutil.copyfile(batch/'review'/name,queue/name)
    save_csv(queue/'review_times.csv',[],['case_id','reviewer_id','started_at','finished_at','seconds','exposure'])
    (queue/'README.md').write_text('검토는 로컬 HTML에서 작성합니다. 이 공개 보고서에는 검색 순위가 보여 블라인드 자료가 아닙니다. CSV의 미작성 행은 미판정입니다. 파일 이름에 completed가 있어도 자동으로 완료 처리하지 않습니다. 원문 전체는 gitignored 로컬 스냅샷에만 있습니다.\n',encoding='utf-8',newline='\n')
    case_links=[];traces=[]
    all_runs=d['runs']+(rows(batch/'new-runs.jsonl') if (batch/'new-runs.jsonl').exists() else [])
    for c in d['cases'].values():
        cid=c['case_id'];case_runs=[r for r in all_runs if r['case_id']==cid];case_links.append(f"- [{cid} · {c['repository']}](casebook/{cid}.md)")
        selected=[];parts=[f"# {cid} · {c['repository']}",f"cohort: `{c['cohort']}`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.", '참고 원문: '+', '.join(f'[{md(did)}]({url})' for did,url in zip(c['source_doc_ids'],c['source_urls'])),f"질의 작성 사전 노출: {md(c['author_exposure'])}"]
        for q in d['queries'].values():
            if q['case_id']!=cid:continue
            approval=resolved['approval'][q['query_id']];parts += [f"## {q['variant']}",f"승인: `{approval['approved']}` · {approval['reason']} · 실제 검토 노출: {md(approval['exposure'])}", '<pre>'+html.escape(q['query_text'])+'</pre>']
            for r in case_runs:
                if r['query_id']!=q['query_id']:continue
                parts += [f"### {r['corpus_scope']} · {r['method']}",f"실행 상태: `{r['status']}` · 참고 원문 순위: `{r.get('reference_doc_rank')}` (관련성 정답이라는 뜻 아님)", '| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |','|---|---|---|---|---|']
                for item in r['ranked_results'][:5]:
                    doc=d['documents'][item['doc_id']];judgment=qrels.get((q['query_id'],item['doc_id']),{});grade=judgment.get('grade');reason=judgment.get('reason','unreviewed');evidence_ids=[e['evidence_id'] for e in catalog.values() if e.get('kind')=='actual_human_quote' and e.get('query_id')==q['query_id'] and e['doc_id']==item['doc_id']]
                    human='UNJUDGED' if grade is None else str(grade);parts.append(f"| {item['rank']} | [{md(public_text(doc['title']))} · #{doc['number']}]({doc['html_url']}) | {item['score_type']} / {item['score']:.8f} | {human} | {md(reason)} {md(evidence_ids)} |")
                    selected.append({**{k:r[k] for k in ['run_id','query_id','query_sha256','repository','method','corpus_scope','kind','status']},**item,'title':public_text(doc['title']),'url':doc['html_url'],'human_grade':grade,'judgment_reason':reason,'pool_version':score['pool_version'],'qrels_version':score['qrels_version']})
                did=c['source_doc_ids'][0];inraw=did in d['documents'];inbug=any(f'{c["repository"]}#{x["number"]}'==did for x in d['scopes'][(c['repository'],'C_bug')]['issues'])
                traces.append({'case_id':cid,'query_id':q['query_id'],'method':r['method'],'scope':r['corpus_scope'],'reference_doc_id':did,'in_C_raw':inraw,'in_C_bug':inbug,'reference_rank':r.get('reference_doc_rank'),'retrieval_status':r['status'],'mechanical_observation':'outside_collection' if not inraw else 'excluded_by_bug_filter' if r['corpus_scope']=='C_bug' and not inbug else 'no_lexical_match' if r['status']=='no_lexical_match' else 'rank_recorded','human_relevance':qrels.get((q['query_id'],did),{}).get('grade'),'cause_confirmed':False})
        parts += ['## 판단과 다음 단계', '범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.']
        target=output/'casebook'/f'{cid}.md';target.parent.mkdir(exist_ok=True);target.write_text('\n\n'.join(parts)+'\n',encoding='utf-8',newline='\n');save_rows(output/'rankings'/f'{cid}.jsonl',selected)
    save_csv(output/'failure_trace.csv',traces)
    (output/'casebook.md').write_text('# 전체 사례집\n\n순위가 보이는 사후 보고 자료입니다. 검토자는 로컬 HTML을 사용하세요.\n\n'+'\n'.join(case_links)+'\n',encoding='utf-8',newline='\n')
    figures(output,score,diagnostics,rrf)
    if (batch/'review-screen.png').exists():shutil.copyfile(batch/'review-screen.png',output/'images/review-screen.png')
    tests=output/'tests';tests.mkdir(exist_ok=True)
    if (batch/'baseline-tests.txt').exists():
        original=(batch/'baseline-tests.txt').read_text(encoding='utf-8-sig')
        (tests/'dirty-worktree-baseline.txt').write_text(public_text(original),encoding='utf-8',newline='\n')
        save(tests/'dirty-worktree-baseline.provenance.json',{'source_sha256':sha_file(batch/'baseline-tests.txt'),'public_sha256':sha_file(tests/'dirty-worktree-baseline.txt'),'masked':original!=public_text(original),'command':'python -m pytest -q','exit_code':0,'note':'Original local dirty worktree baseline; unrelated edits included, not publication tree validation.'})
    for filename in ['ui-test-log.json','ui-blank-downloads.json']:
        if (batch/filename).exists():shutil.copyfile(batch/filename,tests/filename)
    status=read(output/'status.json');table='\n'.join(f'| {k} | {v} |' for k,v in status['stages'].items())
    report_text=f'''# 사람 검토·후속 실험 v2 — {batch.name}

현재 상태: **{score['state']}**. 실제 검토자 {score['human_reviewers']}명, 판정 {score['judged_pairs']}/{score['pool_pairs']}쌍, 공통 비교 가능 질의 {score['comparison_queries']}/{score['planned_queries']}개. 분모가 0인 품질 지표는 null이며 0%가 아닙니다.

| 단계 | 실제 상태 |
|---|---|
{table}

## 실행 결과와 근거

부모 [run_001](../../scenario_pilot_v1/run_001/report.md)의 {d['lineage']['preserved_parent_files']}개 파일을 바이트 SHA-256으로 보존했습니다. 검색 버전과 새 채점·보고 버전은 [lineage.json](lineage.json)에 따로 기록했습니다. 기존 핵심 순위 {len([r for r in d['runs'] if r['kind']=='core'])}조건은 재추론하지 않고 읽었습니다. 재현 검사 {reproduction['conditions']}조건: **{reproduction['status']}**. [실제 비교](reproduction.json), [예산·인코딩 횟수](budget.json).

검색 방식별 공식 Hit@5와 pooled nDCG@5는 질의 승인과 모든 공통 풀 판정이 완료된 동일 질의만 집계합니다. Top-5 밖의 미판정 문서도 분모에 필요합니다. confirmed_hit는 확정 평균과 분리합니다. unavailable·댓글 전용·검토자 불일치는 미확정이며 0점이 아닙니다. 1점만으로 nDCG가 높을 수 있어 Hit@5와 같이 읽어야 합니다.

질의 승인 {score['approved_queries']}/{score['planned_queries']} · 공통 풀 완료 {score['complete_queries']}/{score['planned_queries']} · 실제 비교 {score['comparison_queries']}/{score['planned_queries']}. [질의별 수치·미판정 사유](metrics_by_query.csv), [같은 분모 집계](metrics_summary.csv), [검토 진행](review_progress.csv).

[전체 사례와 실제 질의·Top-5](casebook.md) · [사례별 소형 순위](rankings/) · [근거 카탈로그](evidence_catalog.jsonl). 12개 개발 가족과 번역/변형·역사 사례를 독립 표본으로 합치지 않습니다. 사람 판정 없이 성공·악화·무차이를 만들지 않았습니다. [짝 비교](paired_changes.csv)는 실제 검증 가능한 비교가 없으면 빈 표입니다.

기계적 관찰: [범위](scope-audit.csv), [한국어 기술 토큰](token-audit.csv), [RRF 기여분](rrf-contributions.csv), [최대 유사도 구간](chunk-audit.csv), [문서별 추적](failure_trace.csv). 이는 관련성 판정이나 실패 원인 확정이 아닙니다. 범위 밖/필터 밖의 참고 원문과, 유용한 다른 문서가 검색되지 않는 실패는 구분합니다. 최대 구간의 짧은 예시는 문서별 하나이며 다른 구간에는 same_example_chunk=false를 표시합니다.

## 실제 자료에서 생성한 그림

![검토 진행](images/review-progress.png)
![수집 범위](images/source-coverage.png)
![기술 토큰 관찰](images/token-diagnostic.png)
![RRF 기여분](images/rrf-contributions.png)

그림별 원자료·사용 행·해시·생성 명령은 [figure_data/generation.json](figure_data/generation.json)에 있습니다. 품질 그림 상태: **{status['quality_figures']}**. 신규 후보에 대한 짝 지연·행동 검사 그림은 실행과 검토가 있을 때만 생성합니다. 기존 지연과 새 측정의 차이를 후보 개선으로 주장하지 않습니다.

## 사람이 작성할 검토와 재개

로컬 `data/scenario_followup_v2/{batch.name}/review/review.html`을 Chrome에서 여세요. 실제 Chrome CSV 38행·429행 다운로드와 CLI 재입력을 확인했습니다. Codex 안쪽 브라우저에서는 다운로드가 실제 파일로 저장되지 않는 경우가 있어 Chrome을 권장합니다. 질문 검토와 관련성 검토를 각각 CSV로 내려받아 실제 경로를 지정합니다. 미작성 행은 그대로 두어도 됩니다. 브라우저 임시 저장은 백업을 대신하지 않으므로 CSV를 저장하세요. 질문 원문과 근거를 먼저 확인하고 순위가 보이는 사례집을 읽었다면 exposure에 표시하세요. 공개 [빈 양식](review_queue/)은 완료 판정이 아닙니다.

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_followup resume --batch data/scenario_followup_v2/{batch.name} --query-reviews "$env:USERPROFILE/Downloads/query_reviews.completed.csv" --reviews "$env:USERPROFILE/Downloads/human_reviews.completed.csv"
.venv/Scripts/python.exe -m evaluation.scenario_followup report --batch data/scenario_followup_v2/{batch.name}
.venv/Scripts/python.exe -m evaluation.scenario_followup verify-publication --batch data/scenario_followup_v2/{batch.name}
```

검토자가 둘 이상이면 각자의 행을 review_item_id+reviewer_id로 유지합니다. 불일치는 실제 사람의 adjudications CSV로 조정합니다. 프로그램은 신원을 인증하지 않습니다. 원본 검토 파일 사본은 내용 해시별 inputs/에 보존하고 새 round에 채점합니다. 풀에 새 후보가 생기면 baseline까지 같은 확장 풀로 재채점해야 합니다.

K1/R1 및 E1/E2/E3는 [실행 도구·승인 입력 계약](../../../../evaluation/scenario_followup_v2/README.md)이 검증하는 사람 근거가 있을 때만 실행합니다. 현재 게이트 미충족 단계를 완료로 보고하지 않습니다. 운영 검색·필터·모델을 바꾸지 않았습니다.

## 검증·게시와 한계

[테스트 로그](tests/)에는 기존 미커밋 변경을 포함한 baseline과 게시 소스 트리 검사를 구분합니다. 신규 구현은 부분 검토 수식, ID/해시, 판정 불일치, 풀 확장, HTML 안전성, 게이트를 테스트합니다. 합성 fixture는 실제 검색 정답에 포함하지 않습니다. 재개 명령은 미작성 CSV로 실제 실행해 검토 대기 상태를 확인했습니다.

공개 자료로 순위·수치·보고를 감사할 수 있습니다. 정확한 임베딩 재실행에는 gitignored 동결 스냅샷과 고정 모델 캐시가 필요합니다. 전체 저장소나 일반 관련성을 대표하지 않는 12개 재구성 개발 사례입니다. 원문 작성 시 원인·해결책을 읽은 노출 가능성과 실제 검토 노출을 기록합니다. 구 run·질의·사람 원본은 덮어쓰지 않았습니다. 사용자 요청에 따라 main에만 게시하며 강제 push/자동 병합은 하지 않습니다.
'''
    (output/'report.md').write_text(report_text,encoding='utf-8',newline='\n')
    (output/'README.md').write_text(f'# {batch.name} · {score["state"]}\n\n실제 사람 {score["human_reviewers"]}명 · 검토 {score["judged_pairs"]}/{score["pool_pairs"]}쌍 · 비교 {score["comparison_queries"]}/{score["planned_queries"]}질의.\n\n[보고서와 실행·재개 명령](report.md) · [전체 사례집](casebook.md) · [원자료와 그림 생성 조건](figure_data/) · [테스트](tests/)\n\n![실제 검토 화면](images/review-screen.png)\n\n![검토 진행](images/review-progress.png)\n\n품질 수치는 사람 판정의 공통 분모가 갖춰질 때만 계산합니다. 부모 run_001은 보존했습니다.\n',encoding='utf-8',newline='\n')
    artifact_manifest(output)
    return output


def artifact_manifest(output):
    records=[{'path':p.relative_to(output).as_posix(),'bytes':p.stat().st_size,'sha256':sha_file(p)} for p in sorted(output.rglob('*')) if p.is_file() and p.name!='artifact_manifest.json']
    save(output/'artifact_manifest.json',{'created_at':now(),'files':records,'self_excluded':True})


def verify_publication(batch):
    batch=Path(batch);batch_data(batch);output=ROOT/'docs/experiments/scenario_followup_v2'/batch.name;manifest=read(output/'artifact_manifest.json');count=0
    expected={r['path'] for r in manifest['files']}
    actual={p.relative_to(output).as_posix() for p in output.rglob('*') if p.is_file() and p.name!='artifact_manifest.json'}
    if expected!=actual:raise ValueError('public artifact inventory mismatch')
    for r in manifest['files']:
        path=output/r['path']
        if not path.exists() or path.stat().st_size!=r['bytes'] or sha_file(path)!=r['sha256']:raise ValueError('public artifact hash/size mismatch')
        if r['path'].startswith('rankings/') and r['bytes']>250*1024:raise ValueError('split ranking output exceeds 250 KiB')
        if path.suffix=='.png':
            from PIL import Image
            with Image.open(path) as image:image.verify()
        if path.suffix=='.md':
            for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
                if target.startswith(('http:','https:','#')):continue
                if not (path.parent/target.split('#')[0]).exists():raise ValueError(f'broken relative link: {r["path"]}: {target}')
        count+=1
    status=read(output/'status.json');progress=__import__('evaluation.followup_scoring',fromlist=['csv_rows']).csv_rows(output/'review_progress.csv')
    if int(progress[0]['complete'])!=status['complete_queries']:raise ValueError('status/progress mismatch')
    print({'public_files':count,'hashes_links_png':'VERIFIED','parent_preservation':'VERIFIED'})
