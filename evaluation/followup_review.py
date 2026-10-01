"""Offline review package. Payload contains frozen text, never executable issue HTML."""
import base64
import hashlib
import json
import random
import re
from pathlib import Path

from backend.app.storage import digest

ASSETS = Path(__file__).parent / 'scenario_followup_v2'
QUERY_FIELDS = ['query_id','query_sha256','symptom_faithful','no_solution_leakage','information_change_checked','exposure','reviewer_type','reviewer_id','reviewed_at','review_status','reason']
DOCUMENT_FIELDS = ['review_item_id','query_id','query_sha256','doc_id','document_sha256','grade','condition_relation','evidence_scope','evidence_quote','evidence_url','reason','exposure','reviewer_type','reviewer_id','reviewed_at','review_status']


def package(directory, queries, cases, pool, documents, seed, filename='review.html'):
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    items = []
    for item in pool:
        doc = documents[item['doc_id']]
        url = doc['html_url']
        if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/\d+', url):
            raise ValueError('Unsafe issue URL')
        items.append({**{k:item[k] for k in DOCUMENT_FIELDS if k in item and k in {'review_item_id','query_id','query_sha256','doc_id','document_sha256'}},
                      'title':doc['title'],'body':doc.get('body') or '', 'url':url})
    random.Random(seed).shuffle(items)
    # Source/gold IDs, methods, scores and ranks are intentionally absent.
    payload = {'queries':list(queries.values()), 'cases':[{'case_id':c['case_id'],'repository':c['repository'],'cohort':c['cohort']} for c in cases.values()],
               'items':items,'pool_version':digest(pool),'query_fields':QUERY_FIELDS,'document_fields':DOCUMENT_FIELDS}
    script = (ASSETS/'review.js').read_text(encoding='utf-8')
    css = (ASSETS/'review.css').read_text(encoding='utf-8')
    script_hash = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
    encoded = base64.b64encode(json.dumps(payload,ensure_ascii=False).encode()).decode()
    page = '''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'sha256-SCRIPT_HASH'; style-src 'unsafe-inline'; base-uri 'none'; object-src 'none'; form-action 'none'">
<title>Issue Finder · 사람 검토</title><style>CSS</style>
<body><header><h1>Issue Finder · 사람 검토</h1><p>질문과 GitHub 원문을 읽고 직접 답해주세요. 순위·검색 방식·점수는 가렸습니다. 미작성 항목은 미판정으로 남습니다.</p></header>
<section class="profile"><label>검토자 식별명 <input id="reviewer" placeholder="본인이 정한 이름 또는 별칭"></label><label>사전 노출 <select id="exposure"><option value="">선택해주세요</option><option value="not_previously_exposed">이전에 결과·원인·해결책을 보지 않음</option><option value="previously_exposed">이전에 결과·원인·해결책을 봄</option><option value="unsure">기억나지 않음</option></select></label>
<p>이미 읽은 사례는 사전 노출을 기록하세요. 신원은 인증하지 않습니다. 답변은 이 브라우저에 임시 저장됩니다.</p></section>
<nav><label>사례 <select id="case"></select></label><label>질문 <select id="query"></select></label><span id="progress"></span></nav>
<div class="actions"><button id="exportQueries">질문 검토 CSV 저장</button><button id="exportDocuments">관련성 검토 CSV 저장</button><button id="exportTimes">검토 시간 CSV 저장</button><button id="exportHistory">답변 변경 이력 CSV 저장</button><button id="startTime">이 사례 검토 시작</button><button id="finishTime">이 사례 검토 완료</button></div>
<p id="message" role="status"></p><div id="downloadLinks"></div><main><section><h2>1. 이 질문이 원문을 제대로 표현하나요?</h2><pre id="queryText"></pre><details><summary>같은 사례의 다른 질문 비교</summary><pre id="siblings"></pre></details>
<p>이 사례의 문서들을 확인한 뒤, 증상·조건이 충실하고 해결책을 미리 알려주지 않는지 판단해주세요. B/C의 정보 차이도 확인합니다. 잘못된 질문이면 하나 이상 ‘아니요’를 선택하고 이유를 적으세요.</p>
<label>증상·조건을 충실하게 표현했나요? <select id="faithful" class="yesno"></select></label><label>원인·해결책이 미리 들어가지 않았나요? <select id="leakage" class="yesno"></select></label><label>다른 질문과 정보 차이를 확인했나요? <select id="information" class="yesno"></select></label>
<label>질문 검토 이유 <textarea id="queryReason" placeholder="확인한 증상·조건 또는 부정확한 부분을 적어주세요"></textarea></label><button id="saveQuery">이 질문 답변 저장</button></section>
<section><h2>2. 이 문서가 질문 해결에 얼마나 관련 있나요?</h2><label>검토 문서 <select id="document"></select></label><p id="itemId"></p><h3 id="title"></h3><a id="source" target="_blank" rel="noopener noreferrer">GitHub 원문 열기</a><pre id="body"></pre>
<p>2 = 증상·원인 확인이나 해결/원인 배제에 직접 유용, 1 = 같은 기능·주제이나 직접 근거 부족, 0 = 무관. 반대 조건도 비교에 직접 유용하면 이유와 함께 판단하세요. 읽을 수 없으면 미확정입니다.</p>
<label>관련성 <select id="grade"><option value="">선택해주세요</option><option value="2">2 · 직접 관련</option><option value="1">1 · 부분 관련</option><option value="0">0 · 무관</option><option value="unavailable">원문 확인 불가 · 미확정</option></select></label>
<label>조건 관계 <select id="condition"><option value="">선택해주세요</option><option value="supports">질문의 조건과 일치</option><option value="conflicts">반대 조건 / 차이가 있음</option><option value="unknown">알 수 없음</option><option value="not_applicable">조건 대조 해당 없음</option></select></label>
<label>근거 범위 <select id="scope"><option value="">선택해주세요</option><option value="title_body">제목·본문</option><option value="comment_only">댓글에서만 확인 · 본문 판정 대기</option><option value="unavailable">확인 불가</option></select></label>
<button id="selectedQuote">원문에서 선택한 글을 근거로 가져오기</button><label>원문 근거 인용 <textarea id="quote" placeholder="제목·본문에서 짧은 근거를 그대로 가져오세요"></textarea></label><label>근거 URL <input id="evidenceUrl"></label><label>판정 이유 <textarea id="docReason" placeholder="질문과 관련 있거나 없는 이유, 중요한 조건을 적어주세요"></textarea></label><button id="saveDocument">이 문서 답변 저장</button></section></main>
<footer>일부만 검토해도 CSV 2개를 저장할 수 있습니다. 내려받은 파일을 제공하면 같은 검색 결과로 다시 채점합니다. 질문 승인과 해당 질문의 공통 문서 목록 판정이 모두 완료된 경우만 공식 지표를 계산합니다. 원문·명령은 실행하지 않습니다.</footer>
<script id="payload" type="application/octet-stream">PAYLOAD</script><script>SCRIPT</script></body></html>'''
    for key, value in [('SCRIPT_HASH',script_hash),('CSS',css),('PAYLOAD',encoded),('SCRIPT',script)]:page = page.replace(key,value,1)
    path = directory/filename;path.write_text(page,encoding='utf-8',newline='\n')
    return path
