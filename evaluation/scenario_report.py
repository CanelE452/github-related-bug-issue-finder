"""Publish small audit artifacts. Raw issue bodies and blind full-text HTML stay local."""
import csv
import html
import json
import shutil
import statistics
from collections import Counter
from pathlib import Path

from evaluation.scenario_eval import ROOT, corpus, digest, doc_id, jsonl, read, rows, verify, write


def md(value):
    return html.escape(str(value)).replace('|', '\\|').replace('\n', ' ')


def save_csv(path, records):
    if not records:
        return
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0])); w.writeheader(); w.writerows(records)


def report(args):
    directory = Path(args.run_dir); manifest = verify(directory)
    output = ROOT / 'docs' / 'experiments' / 'scenario_pilot_v1' / directory.name
    output.mkdir(parents=True, exist_ok=True)
    plots = output / 'images'; plots.mkdir(exist_ok=True)
    config = manifest['config']; cases = rows(directory / 'cases.jsonl')
    queries = {q['query_id']: q for q in rows(directory / 'queries.jsonl')}
    runs = rows(directory / 'runs.jsonl'); core = [r for r in runs if r['kind'] == 'core']
    snapshots = {repo: read(directory / meta['file']) for repo, meta in manifest['snapshots'].items()}
    documents = {doc_id(repo, x['number']): x for repo, s in snapshots.items() for x in s['issues']}
    raw_ids = set(documents)
    bug_ids = {doc_id(repo, x['number']) for repo, s in snapshots.items() for x in corpus(s, 'C_bug', config['bug_labels'])['issues']}
    execution = read(directory / 'execution.json'); sample = read(directory / 'resource-sample.json')
    status = read(directory / 'status.json'); review = read(directory / 'review_manifest.json')
    timing = rows(directory / 'timings.jsonl')
    cold = rows(directory / 'cold-timings.jsonl') if (directory / 'cold-timings.jsonl').exists() else []
    sanitized = []
    for r in runs:
        record = {k: v for k, v in r.items() if k != 'chunk_diagnostics'}
        record['ranked_results'] = [{**x, 'url': documents[x['doc_id']]['html_url'], 'title': documents[x['doc_id']]['title'], 'human_grade': None} for x in r['ranked_results']]
        sanitized.append(record)
    jsonl(output / 'rankings.jsonl', sanitized)
    jsonl(output / 'queries.jsonl', queries.values())
    jsonl(output / 'cases.jsonl', cases)
    # No author objects, full bodies, access tokens, local paths, or unrelated working diff.
    public_manifest = {k: manifest[k] for k in ['created_at','config','config_hash','code_revision','code_hashes','working_diff_hash','environment','snapshots','historical_probes','cases_hash','queries_hash','cases_frozen_at','core_cases','total_queries']}
    public_manifest['snapshot_availability'] = 'Raw snapshots are gitignored. Exact replay requires the original local run directory; fresh collection may differ.'
    write(output / 'manifest.json', public_manifest)
    write(output / 'execution.json', execution)
    write(output / 'diagnostics.json', read(directory / 'diagnostics.json'))
    write(output / 'resource-sample.json', sample)
    write(output / 'review_manifest.json', review)
    write(output / 'status.json', status)
    for file in ['human_reviews.csv','query_reviews.csv','baseline-tests.txt','pilot-tests.txt','metrics.csv','review_receipt.json']:
        if (directory / file).exists():
            if file.endswith('-tests.txt'):
                text=(directory/file).read_text(encoding='utf-8').replace(str(ROOT),'[workspace]').replace(ROOT.as_posix(),'[workspace]')
                (output/file).write_text(text,encoding='utf-8')
            else: shutil.copyfile(directory / file, output / file)
    stats = []
    for scope in config['scopes']:
        for method in config['methods']:
            for variant in ['A_ko_symptom','B_ko_context','C_en_context']:
                subset = [r for r in core if r['corpus_scope'] == scope and r['method'] == method and queries[r['query_id']]['variant'] == variant]
                stats.append({'scope':scope,'method':method,'variant':variant,'case_families':len(subset),
                              'execution_errors':sum(r['status']=='execution_error' for r in subset),
                              'source_reference_in_top5':sum(r['reference_doc_rank'] is not None and r['reference_doc_rank']<=5 for r in subset),
                              'hit_at_5':None,'pooled_ndcg_at_5':None,'quality_status':'UNJUDGED'})
    save_csv(output / 'reference-diagnostics.csv', stats)
    save_csv(output / 'search-times.csv', [{k:r[k] for k in ['query_id','case_id','repository','corpus_scope','method','kind','status','elapsed_ms']} for r in runs + timing])
    save_csv(output / 'cold-times.csv', [{k:r.get(k) for k in ['repository','method','status','elapsed_ms','process_wall_ms','note']} for r in cold])
    chunk_rows=[]
    for r in core:
        for d in r.get('chunk_diagnostics',[]):
            chunk_rows.append({'query_id':r['query_id'],'scope':r['corpus_scope'],'method':r['method'],
                               **{k:d[k] for k in ['doc_id','doc_tokens','doc_chunks','query_chunks','document_chunk','query_chunk']},
                               'human_span_classification':None})
    save_csv(output / 'chunk-diagnostics.csv', chunk_rows)
    scope_ids = [{'repository':repo,'scope':scope,'doc_id':doc_id(repo,x['number'])} for repo,s in snapshots.items() for scope in config['scopes'] for x in corpus(s,scope,config['bug_labels'])['issues']]
    save_csv(output / 'scope-documents.csv', scope_ids)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    figure, axis = plt.subplots(figsize=(9,4.2))
    positions = np.arange(len(config['repositories']))
    axis.bar(positions-.18, [manifest['snapshots'][r]['issue_count'] for r in config['repositories']], .36, label='C_raw: issues excluding PRs', color='#5969e5')
    axis.bar(positions+.18, [manifest['snapshots'][r]['bug_count'] for r in config['repositories']], .36, label='C_bug: original bug type/label',color='#f0a456')
    for container in axis.containers: axis.bar_label(container, padding=4)
    axis.set_xticks(positions, ['OpenCV','Transformers']);axis.set_ylim(0,480);axis.set_ylabel('Documents');axis.legend(frameon=False)
    axis.set_title('Frozen latest 20 pages: partial collection, not entire repositories')
    figure.tight_layout();figure.savefig(plots/'corpus-coverage.png',dpi=170);plt.close(figure)
    qids=[q['query_id'] for q in queries.values() if q['case_id'].startswith(('O-','T-'))]
    columns=[(s,m) for s in config['scopes'] for m in config['methods']]
    lookup={(r['query_id'],r['corpus_scope'],r['method']):r for r in core}
    data=np.array([[min(lookup[(q,s,m)]['reference_doc_rank'] or 51,51) for s,m in columns] for q in qids])
    figure,axis=plt.subplots(figsize=(9,14));im=axis.imshow(data,vmin=1,vmax=51,cmap='YlOrRd',aspect='auto')
    axis.set_xticks(range(6),[s+'\n'+m for s,m in columns]);axis.set_yticks(range(len(qids)),qids)
    for i,qid in enumerate(qids):
        for j,(scope,method) in enumerate(columns):
            rank=lookup[(qid,scope,method)]['reference_doc_rank'];label='-' if rank is None else str(rank)
            axis.text(j,i,label,ha='center',va='center',fontsize=8,color='white' if data[i,j]>32 else '#333')
    axis.set_title('Source-issue recovery ranks (diagnostic; NOT relevance accuracy)\n- = absent from scope or ranking; colors capped at rank 51')
    figure.colorbar(im,ax=axis,label='Rank (lower is better; clipped at 51)',fraction=.03,pad=.03)
    figure.tight_layout();figure.savefig(plots/'reference-ranks.png',dpi=150);plt.close(figure)
    figure, axes=plt.subplots(1,2,figsize=(11,4.5))
    groups=[[r['elapsed_ms'] for r in timing if r['method']==m and r['status']=='ok'] for m in config['methods']]
    axes[0].boxplot(groups,tick_labels=config['methods']);axes[0].set_yscale('log');axes[0].set_ylabel('Milliseconds (log scale)');axes[0].set_title('Warm query timing: 6 cases x 3 repeats')
    if cold:
        axes[1].bar(range(len(cold)),[r['process_wall_ms']/1000 for r in cold],color=['#5969e5','#3eac9b','#f0a456']*2)
        axes[1].set_xticks(range(len(cold)),[r['repository'].split('/')[0]+'\n'+r['method'] for r in cold],rotation=25,ha='right')
    axes[1].set_ylabel('Seconds');axes[1].set_title('Fresh-process wall time: one sample each\nOS cache uncontrolled; no re-embedding')
    figure.tight_layout();figure.savefig(plots/'latency.png',dpi=170);plt.close(figure)
    lines=['# GitHub Issue 검색 상황 질의 파일럿 — 2026-10-01', '',
           f'현재 상태: **{status["status"]}**. 실제 수집·고정 모델 검색·검토 자료 생성은 수행했습니다. 사람이 질의와 문서 관련성을 판정하지 않았으므로 검색 품질 평가는 완료되지 않았습니다.', '',
           '이 실행은 기존 Issue에서 신고자의 증상을 재구성한 **개발 표본 12개**입니다. 실제 신규 사용자 문제, 중복 판별, 현재 버그 재현 또는 해결 가능성을 검증한 결과로 일반화할 수 없습니다.', '',
           '## 수행 범위', '', '| 항목 | 실제 실행 |', '|---|---|',
           f'| 기준 코드 | `{manifest["code_revision"]}` + manifest에 기록된 소스 파일 해시 |',
           '| 알고리즘 | 기존 양의 IDF BM25, multilingual-e5-small, 같은 가중치 RRF(60, 상위 50개) |',
           f'| 모델 | `{config["model"]}` / revision `{config["model_revision"]}` |',
           '| 길이 처리 | 448토큰, 64토큰 중첩, 가장 높은 구간 간 코사인 유사도 |',
           f'| GitHub API 호출 | {len(rows(directory/"http.jsonl"))} / {config["max_http_calls"]}; 재시도·토큰 교체 없음 |',
           f'| 핵심 검색 | {len(core)} / 216 (12사례 × 3입력 × 3방법 × 2범위) |',
           f'| 역사 사례 점검 | {sum(r["kind"]=="historical" for r in runs)} / 12; 핵심 평균에서 제외 |',
           f'| 시간 측정 | warm {len(timing)} / 54, cold {len(cold)} / 6 |',
           '| D_error_only | 선택 실험 미실행 |',
           f'| 실행 오류 | {sum(r["status"]=="execution_error" for r in runs)} / {len(runs)} 검색 |',
           f'| 계산 시간 | {execution.get("compute_with_cold_seconds",execution["compute_seconds"]):.1f}초 / 5,400초; 모델/표본/인덱스/검색/cold 포함, 문서 작성·테스트 제외 |',
           f'| 사람 검토 | 0명; {review["items"]}개의 질의-문서 쌍, 핵심 36질의 미판정 |',
           '| Hit@5 / pooled nDCG@5 | **null — 미판정**; 0으로 대체하지 않음 |',
           '| 웹 비교 / 요약 | PENDING_MANUAL_STUDY / NOT_APPLICABLE_YET(요약 미구현) |', '',
           '## 데이터 범위와 필터', '',
           '| 저장소 | API 항목(PR 포함) | C_raw | C_bug | PR 제외 | 생성 시각 범위(UTC) | 부분 수집 |', '|---|---:|---:|---:|---:|---|---|']
    for repo, meta in manifest['snapshots'].items():
        lines.append(f'| {repo} | {meta["fetched_count"]} | {meta["issue_count"]} | {meta["bug_count"]} | {meta["fetched_count"]-meta["issue_count"]} | {meta["oldest_created"]} — {meta["newest_created"]} | {meta["partial"]} |')
    lines += ['', '![실제 수집 문서 수](images/corpus-coverage.png)', '',
              '두 범위 모두 같은 스냅샷이며 레이블·본문을 바꾸지 않았습니다. Bug는 기본 레이블 `bug` 또는 type.name=Bug의 대소문자 무시 일치입니다. C_raw는 평가 대조용이며 서비스의 Bug 필터를 전체 Issue로 바꾸지 않았습니다.', '',
              '| 사례 | 원문 | 분류(검토 전) | Bug 범위에 원문 존재 |', '|---|---|---|---|']
    for c in cases:
        if c['cohort']!='core_development':continue
        did=doc_id(c['repository'],c['reference_number'])
        lines.append(f'| {c["case_id"]} | [#{c["reference_number"]}]({c["source_urls"][0]}) | {c["stratum"]} | {did in bug_ids} |')
    covered=sum(c['source_doc_ids'][0] in bug_ids for c in cases if c['cohort']=='core_development')
    lines += ['',f'개발 표본의 참고 원문은 C_raw에 12/12, C_bug에 {covered}/12개 있습니다. 이 수는 표본 내 필터 관찰이며 전체 저장소의 정답 수집률이 아닙니다. Bug 필터에서 빠진 사례도 216개 핵심 실행과 검토 과제에 남겼습니다.', '',
              '역사 사례 OpenCV #17687과 Transformers #24694는 각각 두 범위에서 원문 존재 여부를 별도로 확인했습니다:']
    for c in cases:
        if c['cohort']=='historical_probe':lines.append(f'- [{c["repository"]}#{c["reference_number"]}]({c["source_urls"][0]}): C_raw={c["source_doc_ids"][0] in raw_ids}, C_bug={c["source_doc_ids"][0] in bug_ids}. 개별 조회한 원문을 검색 인덱스에 주입하지 않았습니다.')
    lines += ['', '## 순위 관찰 — 정확도 아님', '',
              '아래 수치는 질의 작성에 사용한 원문 Issue가 상위 5개에 돌아오는지를 보여줍니다. 다른 결과가 더 직접 관련될 수 있으므로 Hit@5, Recall@5, 해결 성공률로 해석하지 않습니다. 작성자는 원문을 읽었고 결과 순위·댓글·제안된 수정은 질의 작성에 사용하지 않았습니다.', '',
              '| 범위 | 방법 | A 한국어 증상 | B 한국어 조건 추가 | C 영어 동일 정보 |', '|---|---|---:|---:|---:|']
    for scope in config['scopes']:
        for method in config['methods']:
            counts=[x['source_reference_in_top5'] for x in stats if x['scope']==scope and x['method']==method]
            lines.append(f'| {scope} | {method} | {counts[0]}/12 | {counts[1]}/12 | {counts[2]}/12 |')
    lines += ['', '![원문 회수 순위 진단](images/reference-ranks.png)', '',
              '전체 질의 문자열·원문 링크·상위 5개 제목/상태/레이블/링크/방식별 점수는 [사례별 결과](casebook.md)에 있습니다. Top-20 및 실행 상태·해시는 [rankings.jsonl](rankings.jsonl)에 기록했습니다. 모든 관련성 등급은 `UNJUDGED`입니다.', '',
              '## 시간·자원 관찰', '', '| 방법 | Warm 표본 수 | 중앙값(ms) | 최소—최대(ms) |', '|---|---:|---:|---:|']
    for method, values in zip(config['methods'],groups):
        lines.append(f'| {method} | {len(values)} | {statistics.median(values):.2f} | {min(values):.2f}—{max(values):.2f} |')
    lines += ['', '![실제 시간 측정](images/latency.png)', '',
              'Warm은 공유 모델/문서 인덱스가 준비된 프로세스에서 새 질의 인코딩까지 측정했습니다. 메모리 벡터 적재 상태의 영향을 포함하며 서비스 전체 응답 시간이나 운영 P95가 아닙니다. Cold는 별도 프로세스 시작부터 모델/인덱스 적재·검색·종료까지의 1회 관찰이며 OS 파일 캐시는 통제하지 않았습니다.', '',
              f'20개 문서 표본의 인덱싱 추정은 {sample["estimated_index_seconds"]:.1f}초, 전체 {sample["all_documents"]}개 문서 / {sample["all_chunks"]}개 구간입니다. 표본 RSS 관찰 최고치는 {max(x["rss_bytes"] for x in sample["sample"])/1024**2:.1f} MiB입니다. 이것은 표본 시점 RSS이며 전체 실행 최고 메모리로 보고하지 않습니다.', '',
              '## 계획과 차이·아직 하지 않은 작업', '',
              '- 후보 상한 48보다 1개 많은 **49개**를 원문/메타데이터로 검토했습니다. 첫 48개에 기능 요청·통합 triage 등이 많아 같은 수집 범위에서 고정 시드 순서의 다음 후보 1개를 추가했습니다. API 범위 확대와 순위에 따른 사례 교체는 없었습니다. [선택 감사 기록](../../../../evaluation/scenario_pilot_v1/selection-audit.json)을 공개합니다.',
              '- 유형별 두 사례씩 구성했지만 작성자의 잠정 분류입니다. 특히 T-E2의 override 부재와 T-S1의 설정 전달은 조건형과 겹칠 수 있어 사람 검토에서 우선 확인해야 합니다. 독립 원인/중복 관계 전체를 검증하지 않았습니다.',
              '- 질의는 Issue의 증상을 재구성했습니다. 한국어 표현의 충실성, B↔C 정보 동등성, 원인·해결 누출 여부는 사람이 아직 확인하지 않았습니다. 첨부 이미지는 실행·열람하지 않았으며 이미지 없이는 이해할 수 있는지의 전체 corpus 판단도 미완료입니다.',
              '- E1 표현/무관 정보, E2 조건 대조, E3 인증 무정답 실험은 사람 검토 조건이 충족되지 않아 실행하지 않았습니다. 준비 상태와 재개 조건은 [diagnostics.json](diagnostics.json) 및 README에 기록했습니다. E4 구간 위치·길이는 계산했고 증상/환경/템플릿 분류는 미판정입니다.',
              '- 운영 데이터·서비스 모델 캐시는 덮어쓰지 않았습니다. 원문·벡터·전체 본문을 포함한 blind HTML은 로컬 gitignored 폴더에 보존합니다. GitHub 공개 파일로 원문 작성자 객체·토큰·전체 본문·개인 경로는 내보내지 않았습니다.',
              '- 첨부 문서의 push 금지는 사용자의 이번 “push해줘” 요청으로 대체했습니다. 평가 코드와 소형 보고서만 게시하며 기존 미커밋 코드 리뷰/UI 변경은 포함하지 않습니다.', '',
              '## 지금 내릴 수 있는 결정', '',
              f'1. Bug 필터에서 참고 원문 {12-covered}개가 빠지고 역사 원문 2개도 이번 최신 수집 범위 밖입니다. 먼저 **수집 범위/레이블 안내**를 확인해야 합니다. 모든 검색 실패를 모델 문제로 볼 수 없습니다.',
              '2. 방법·언어별 원문 회수 순위가 달라도 일반 관련성 개선의 근거가 되지는 않습니다. **36질의와 풀링 문서 사람 검토를 먼저 완료**하고, 같은 원인 가족을 최종 평가로 재사용하지 않습니다.',
              '3. 긴 문서에서 최대 유사도 구간을 기록했지만 아직 그 구간이 실제 증상인지 판정하지 않았습니다. **E4 근거 구간을 검토한 뒤** 길이/입력 처리 변경 필요성을 결정합니다.', '',
              '## 확인·재현', '',
              '실행 명령과 사람 검토 칸의 의미는 [파일럿 README](../../../../evaluation/scenario_pilot_v1/README.md)에 있습니다. 원문 snapshot은 기본 Git 제외이므로 정확히 같은 데이터의 재실행은 이 컴퓨터의 원래 run 폴더가 필요합니다. GitHub의 해시·질의·범위 ID·순위·CSV로 이번 결과를 감사할 수 있으며, 새 수집은 시점에 따라 달라집니다.', '',
              '기존 테스트: [baseline-tests.txt](baseline-tests.txt). 추가 계약 및 전체 테스트: [pilot-tests.txt](pilot-tests.txt). 테스트 통과는 검색 관련성/버그 해결을 증명하지 않습니다.', '',
              '사람 검토 후 `score`는 provenance/해시를 검사하고 실제 판정만 계산합니다. 프로그램은 사람의 신원을 인증하지 못하므로 형식 검증을 실제 신원 확인으로 과장하지 않습니다.']
    (output/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    book=['# 사례별 질의와 실제 Top-5', '', '개발 표본이며 질의·관련성은 사람 검토 전입니다. 원문 회수는 정답 판정이 아닙니다. 점수는 BM25/코사인/RRF 각각의 척도이며 확률이나 공통 척도가 아닙니다.', '']
    for c in cases:
        book += [f'## {c["case_id"]} — {c["cohort"]}', '', f'참고 원문: [{c["repository"]}#{c["reference_number"]}]({c["source_urls"][0]}). 유형: `{c["stratum"]}`.', '',md(c.get('stratum_reason','이미 노출된 역사 사례, 핵심 표본 평균에서 제외.')), '']
        for q in [q for q in queries.values() if q['case_id']==c['case_id']]:
            book += [f'### {q["variant"]}', '', '```text',q['query_text'],'```', '', '| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |', '|---|---|---:|---|---|---:|---|']
            for r in [r for r in sanitized if r['query_id']==q['query_id']]:
                if not r['ranked_results']:
                    book.append(f'| {r["corpus_scope"]} | {r["method"]} | — | {r["status"]} | — | — | UNJUDGED |')
                for x in r['ranked_results'][:5]:
                    d=documents[x['doc_id']];labels=', '.join(y['name'] if isinstance(y,dict) else y for y in d['labels'])
                    book.append(f'| {r["corpus_scope"]} | {r["method"]} | {x["rank"]} | [{md(d["title"][:100])}]({x["url"]}) | {md(d["state"]+"; "+labels)} | {x["score"]:.6f} | UNJUDGED |')
            book.append('')
    (output/'casebook.md').write_text('\n'.join(book)+'\n',encoding='utf-8')
    print(json.dumps({'report':output.relative_to(ROOT).as_posix(),'status':status['status'],'core_runs':len(core),'review_pairs':review['items']}))
