"""Optional three-document feedback, deliberately separate from evaluation qrels."""
import base64
import hashlib
import json
import random
import re
from pathlib import Path

from backend.app.storage import digest
from evaluation.followup_review import ASSETS


def quick_package(directory, queries, pool, documents, seed):
    available = [q for q in queries.values() if any(p['query_id'] == q['query_id'] for p in pool)]
    if not available:
        raise ValueError('No query with review documents available')
    query = next((q for q in available if q['query_id'] == 'T-E1:B_ko_context'), available[0])
    candidates = [p for p in pool if p['query_id'] == query['query_id']]
    random.Random(seed).shuffle(candidates)
    items = []
    for item in candidates[:3]:
        doc = documents[item['doc_id']]
        if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/\d+', doc['html_url']):
            raise ValueError('Unsafe issue URL')
        items.append({**{k:item[k] for k in ('review_item_id','doc_id','document_sha256')},
                      'title':doc['title'], 'body':doc.get('body') or '', 'url':doc['html_url']})
    payload = {'purpose':'optional_ui_feedback_not_evaluation_qrels',
               'query':{k:query[k] for k in ('query_id','query_sha256','query_text')}, 'items':items,
               'selection':'one frozen query; seeded sample of up to three common-pool documents; no rank selection'}
    payload['sample_id'] = digest(payload)
    script = (ASSETS/'quick-review.js').read_text(encoding='utf-8')
    css = (ASSETS/'review.css').read_text(encoding='utf-8')
    script_hash = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
    encoded = base64.b64encode(json.dumps(payload,ensure_ascii=False).encode()).decode()
    page = '''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'sha256-SCRIPT_HASH'; style-src 'unsafe-inline'; base-uri 'none'; object-src 'none'; form-action 'none'">
<title>Issue Finder · 간단 확인</title><style>CSS
body{max-width:900px}.optional{background:#e0f2fe;border-radius:12px;padding:18px;line-height:1.8}.quick-card pre{max-height:300px;overflow:auto}.quick-card h2{font-size:18px}#quick-progress{font-weight:600}button.primary{background:#4338ca;color:white}
</style><body><header><h1>질문 1개 · 이슈 최대 3개만 확인</h1>
<p>이름 입력 없이, 도움이 되는지만 선택하면 됩니다. 일부만 답해도 저장할 수 있습니다.</p></header>
<div class="optional"><strong>검토는 선택 사항입니다.</strong><br>앱 작동 확인에는 사람 검토가 필요 없습니다. 검색 결과가 실제로 도움이 되는지 확인할 때만 사용합니다. 모르면 ‘잘 모르겠어요’를 선택하거나 건너뛰세요. 이 작은 표본으로 전체 정확도를 확정하지 않습니다.</div>
<main><section><h2>이런 오류가 났다면 아래 이슈가 도움이 되나요?</h2><pre id="quick-query"></pre></section>
<div class="actions"><button id="quick-download" class="primary">답변 CSV 저장</button><button id="quick-skip">검토 건너뛰기</button></div>
<p id="quick-progress"></p><p id="quick-message" role="status"></p><div id="quick-download-links"></div><div id="quick-cards"></div></main>
<footer>선택한 답변만 이 브라우저에 임시 저장됩니다. CSV에는 이름·검토자 식별명·자동 판정이 없습니다. 원문과 명령은 실행하지 않습니다.</footer>
<script id="quick-payload" type="application/octet-stream">PAYLOAD</script><script>SCRIPT</script></body></html>'''
    for key,value in [('SCRIPT_HASH',script_hash),('CSS',css),('PAYLOAD',encoded),('SCRIPT',script)]:
        page = page.replace(key,value,1)
    directory = Path(directory);directory.mkdir(parents=True,exist_ok=True)
    path = directory/'review.html';path.write_text(page,encoding='utf-8',newline='\n')
    return path,payload
