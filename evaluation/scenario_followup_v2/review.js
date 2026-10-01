'use strict';
const $ = id => document.getElementById(id);
const P = JSON.parse(new TextDecoder().decode(Uint8Array.from(atob($('payload').textContent), c => c.charCodeAt(0))));
const key = 'issue-finder-review-v2:' + P.pool_version;
let state = {documents:{}, queries:{}, history:[], times:{}, reviewer:'', exposure:''};
try { const previous = localStorage.getItem(key); if (previous) state = {...state,...JSON.parse(previous)}; } catch (_) { $('message').textContent = '임시 저장을 사용할 수 없습니다. 작업 후 CSV를 꼭 저장하세요.'; }
function persist() { state.reviewer=$('reviewer').value;state.exposure=$('exposure').value;try { localStorage.setItem(key,JSON.stringify(state)); } catch (_) { $('message').textContent='임시 저장 실패. CSV로 저장하세요.'; } }
function option(select,value,label) { const node=document.createElement('option');node.value=value;node.textContent=label;select.appendChild(node); }
function profile() { const id=$('reviewer').value.trim(), exposure=$('exposure').value;if (!id || !exposure) throw Error('검토자 식별명과 사전 노출을 먼저 입력해주세요.');return {reviewer_type:'human',reviewer_id:id,exposure,reviewed_at:new Date().toISOString(),review_status:'reviewed'}; }
function guard(fn) { try { fn();persist();progress(); } catch (error) { $('message').textContent=error.message; } }
const recordKey=(id)=>id+'|'+$('reviewer').value.trim();
const currentQuery=()=>P.queries.find(x=>x.query_id===$('query').value);
const currentDocument=()=>P.items.find(x=>x.review_item_id===$('document').value);
function progress() { const qs=new Set(Object.values(state.queries).map(x=>x.query_id)).size,ds=new Set(Object.values(state.documents).map(x=>x.review_item_id)).size;$('progress').textContent=`질문 ${qs} / ${P.queries.length} · 문서 ${ds} / ${P.items.length} (독립 답변 ${Object.keys(state.queries).length+Object.keys(state.documents).length}개)`; }
function loadDocument() {
 const d=currentDocument();if (!d){$('itemId').textContent='';$('title').textContent='동결 검색 범위에 검토 문서가 없습니다.';$('body').textContent='역사 사례 원문은 이번 검색 범위 밖입니다. 핵심 평가에는 포함하지 않습니다.';$('source').removeAttribute('href');return;}const r=state.documents[recordKey(d.review_item_id)]||{};
 $('itemId').textContent='검토 ID: '+d.review_item_id;$('title').textContent=d.title;$('body').textContent=d.body||'(빈 본문)';$('source').href=d.url;
 for (const [id,field] of [['grade','grade'],['condition','condition_relation'],['scope','evidence_scope'],['quote','evidence_quote'],['docReason','reason']]) $(id).value=r[field]||'';
 if(r.evidence_scope==='unavailable')$('grade').value='unavailable';$('evidenceUrl').value=r.evidence_url||d.url;
}
function loadQuery() {
 const q=currentQuery(),r=state.queries[recordKey(q.query_id)]||{};
 $('queryText').textContent=q.query_text;$('siblings').textContent=P.queries.filter(x=>x.case_id===q.case_id).map(x=>x.variant+'\n'+x.query_text).join('\n\n');
 for(const [id,field] of [['faithful','symptom_faithful'],['leakage','no_solution_leakage'],['information','information_change_checked'],['queryReason','reason']])$(id).value=r[field]||'';
 $('document').replaceChildren();P.items.filter(x=>x.query_id===q.query_id).forEach((d,i)=>option($('document'),d.review_item_id,`${i+1}. ${d.title}`));loadDocument();progress();
}
function loadCase() { $('query').replaceChildren();P.queries.filter(x=>x.case_id===$('case').value).forEach(q=>option($('query'),q.query_id,q.variant));loadQuery(); }
function saveQuery() {
 const q=currentQuery(),p=profile();const answers={symptom_faithful:$('faithful').value,no_solution_leakage:$('leakage').value,information_change_checked:$('information').value};
 if(Object.values(answers).some(x=>!['yes','no'].includes(x))||!$('queryReason').value.trim())throw Error('세 질문에 답하고 실제 검토 이유를 적어주세요.');
 const row={query_id:q.query_id,query_sha256:q.query_sha256,...answers,...p,reason:$('queryReason').value.trim()};
 state.queries[recordKey(q.query_id)]=row;state.history.push({kind:'query',...row});$('message').textContent='질문 답변을 저장했습니다. CSV로 내려받아주세요.';
}
function saveDocument() {
 const d=currentDocument(),p=profile(),grade=$('grade').value,scope=$('scope').value,quote=$('quote').value.trim(),reason=$('docReason').value.trim(),url=$('evidenceUrl').value.trim(),condition=$('condition').value;
 if(!grade||!scope||!condition||!reason)throw Error('관련성·조건·근거 범위·이유를 입력해주세요.');
 if((grade==='unavailable') !== (scope==='unavailable'))throw Error('확인 불가는 관련성과 근거 범위를 함께 선택해주세요.');
 if(scope!=='unavailable'&&(!quote||url.split('#')[0]!==d.url))throw Error('실제 인용과 해당 Issue의 근거 URL이 필요합니다.');
 const normalize=s=>s.replace(/\s+/g,' ').trim();if(scope==='title_body'&&!normalize(d.title+'\n'+d.body).includes(normalize(quote)))throw Error('근거 인용이 고정된 제목·본문에 없습니다. 원문을 그대로 가져오세요.');
 const row={review_item_id:d.review_item_id,query_id:d.query_id,query_sha256:d.query_sha256,doc_id:d.doc_id,document_sha256:d.document_sha256,grade:grade==='unavailable'?'':grade,condition_relation:condition,evidence_scope:scope,evidence_quote:quote,evidence_url:url,reason,...p};
 state.documents[recordKey(d.review_item_id)]=row;state.history.push({kind:'document',...row});$('message').textContent='문서 답변을 저장했습니다. CSV로 내려받아주세요.';
}
function cell(value) { let s=String(value??'');if(/^\s*[=+@-]/.test(s))s="'"+s;return '"'+s.replace(/"/g,'""')+'"'; }
function download(name,fields,rows) { const text='\uFEFF'+[fields,...rows.map(r=>fields.map(f=>r[f]??''))].map(row=>row.map(cell).join(',')).join('\r\n')+'\r\n';const a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(text);a.download=name;a.textContent=name+' 내려받기';a.style.display='block';$('downloadLinks').appendChild(a);a.click();$('message').textContent=name+' 저장을 요청했습니다. 자동 저장이 안 되면 아래 내려받기 링크를 누르세요.'; }
function exportRows(kind) { const saved=Object.values(state[kind]);const isQuery=kind==='queries',ids=new Set(saved.map(r=>isQuery?r.query_id:r.review_item_id));const rows=[...saved];
 for(const x of isQuery?P.queries:P.items)if(!ids.has(isQuery?x.query_id:x.review_item_id))rows.push(isQuery?{query_id:x.query_id,query_sha256:x.query_sha256,review_status:'unreviewed'}:{review_item_id:x.review_item_id,query_id:x.query_id,query_sha256:x.query_sha256,doc_id:x.doc_id,document_sha256:x.document_sha256,review_status:'unreviewed',evidence_url:x.url});
 download(isQuery?'query_reviews.completed.csv':'human_reviews.completed.csv',isQuery?P.query_fields:P.document_fields,rows);
}
$('reviewer').value=state.reviewer;$('exposure').value=state.exposure;
for(const c of P.cases)option($('case'),c.case_id,c.case_id+' · '+c.repository+(c.cohort==='core_development'?'':c.cohort==='historical_probe'?' · 역사 사례':' · 별도 '+c.cohort));
for(const e of document.querySelectorAll('.yesno')){option(e,'','선택해주세요');option(e,'yes','예');option(e,'no','아니요');}
$('case').onchange=loadCase;$('query').onchange=loadQuery;$('document').onchange=loadDocument;
$('reviewer').onchange=()=>{persist();loadQuery();};$('exposure').onchange=persist;
$('saveQuery').onclick=()=>guard(saveQuery);$('saveDocument').onclick=()=>guard(saveDocument);
$('exportQueries').onclick=()=>exportRows('queries');$('exportDocuments').onclick=()=>exportRows('documents');
$('exportHistory').onclick=()=>download('review_history.csv',['kind',...new Set([...P.query_fields,...P.document_fields])],state.history);
$('exportTimes').onclick=()=>download('review_times.csv',['case_id','reviewer_id','started_at','finished_at','seconds','exposure'],Object.values(state.times));
$('startTime').onclick=()=>guard(()=>{const p=profile(),id=$('case').value,k=id+'|'+p.reviewer_id;const prior=state.times[k];if(prior)throw Error('이 사례의 시작 시각은 이미 기록되어 있습니다.');state.times[k]={case_id:id,reviewer_id:p.reviewer_id,started_at:p.reviewed_at,finished_at:'',seconds:'',exposure:p.exposure};$('message').textContent='실제 시작 시각을 기록했습니다.';});
$('finishTime').onclick=()=>guard(()=>{const p=profile(),r=state.times[$('case').value+'|'+p.reviewer_id];if(!r||r.finished_at)throw Error('먼저 검토를 시작해주세요. 완료한 시간은 덮어쓰지 않습니다.');r.finished_at=p.reviewed_at;r.seconds=(Date.parse(r.finished_at)-Date.parse(r.started_at))/1000;$('message').textContent='실제 완료 시각을 기록했습니다.';});
$('selectedQuote').onclick=()=>{const s=getSelection();const parent=s?.anchorNode?.parentElement;if(s&&s.toString()&&(parent?.closest('#body')||parent?.closest('#title'))){$('quote').value=s.toString();}else $('message').textContent='제목·본문에서 근거 문장을 선택해주세요.';};
loadCase();
