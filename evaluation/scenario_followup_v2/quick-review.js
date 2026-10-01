'use strict';
const el = id => document.getElementById(id);
const Q = JSON.parse(new TextDecoder().decode(Uint8Array.from(atob(el('quick-payload').textContent), c => c.charCodeAt(0))));
const storageKey = 'issue-finder-optional-feedback:' + Q.sample_id;
let answers = {};
try { answers = JSON.parse(localStorage.getItem(storageKey) || '{}'); } catch (_) { el('quick-message').textContent = ' 임시 저장이 안 되면 CSV로 내려받아 주세요.'; }
const persist = () => { try { localStorage.setItem(storageKey, JSON.stringify(answers)); } catch (_) { el('quick-message').textContent = 'CSV로 답변을 저장해 주세요.'; } };
const progress = () => { el('quick-progress').textContent = `선택 ${Q.items.filter(d => answers[d.review_item_id]?.answer).length} / ${Q.items.length} · 여기까지만 해도 됩니다`; };
el('quick-query').textContent = Q.query.query_text;
for (const [i,d] of Q.items.entries()) {
 const section = document.createElement('section');section.className = 'quick-card';
 const heading = document.createElement('h2');heading.textContent = `${i+1}. ${d.title}`;section.appendChild(heading);
 const details = document.createElement('details'),summary = document.createElement('summary'),body = document.createElement('pre');summary.textContent = '본문 펼쳐 읽기';body.textContent = d.body || '(빈 본문)';details.append(summary,body);section.appendChild(details);
 const link = document.createElement('a');link.href = d.url;link.target = '_blank';link.rel = 'noopener noreferrer';link.textContent = 'GitHub 원문';section.appendChild(link);
 const label = document.createElement('label'),select = document.createElement('select');label.append('이 오류에 도움이 되나요? ');select.setAttribute('aria-label',`후보 ${i+1} 관련성`);
 for(const [value,text] of [['','선택 안 함'],['2','직접 도움이 돼요'],['1','조금 관련 있어요'],['0','관련 없어요'],['unsure','잘 모르겠어요']]) { const option=document.createElement('option');option.value=value;option.textContent=text;select.appendChild(option); }
 const noteLabel=document.createElement('label'),note=document.createElement('input');noteLabel.append('한 줄 의견 · 선택 ');note.setAttribute('aria-label',`후보 ${i+1} 의견`);note.placeholder='없으면 비워 두세요';
 select.value=answers[d.review_item_id]?.answer || '';note.value=answers[d.review_item_id]?.note || '';label.appendChild(select);noteLabel.appendChild(note);section.append(label,noteLabel);
 const save=()=>{ answers[d.review_item_id]={answer:select.value,note:note.value,answered_at:select.value ? new Date().toISOString() : ''};persist();progress();el('quick-message').textContent='선택을 임시 저장했습니다. 끝나면 CSV 저장을 누르세요.'; };
 select.onchange=save;note.onchange=save;el('quick-cards').appendChild(section);
}
function csvCell(value) { let text=String(value ?? '');if(/^\s*[=+@-]/.test(text))text="'"+text;return '"'+text.replace(/"/g,'""')+'"'; }
el('quick-download').onclick=()=>{
 const fields=['purpose','sample_id','query_id','query_sha256','doc_id','document_sha256','answer','note','answered_at','review_status'];
 const rows=Q.items.map(d=>{const a=answers[d.review_item_id] || {};return [Q.purpose,Q.sample_id,Q.query.query_id,Q.query.query_sha256,d.doc_id,d.document_sha256,a.answer || '',a.note || '',a.answered_at || '',a.answer ? 'manual_feedback' : 'unanswered'];});
 const text='\uFEFF'+[fields,...rows].map(row=>row.map(csvCell).join(',')).join('\r\n')+'\r\n';
 const a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(text);a.download='quick_feedback.csv';a.textContent='quick_feedback.csv 내려받기';el('quick-download-links').appendChild(a);a.click();el('quick-message').textContent='CSV 저장을 요청했습니다. 자동 저장이 안 되면 내려받기 링크를 누르세요.';
};
el('quick-skip').onclick=()=>{el('quick-cards').hidden=true;el('quick-message').textContent='검토를 건너뛰었습니다. 코드 테스트와 검색 재현 확인에는 영향이 없습니다.';};
progress();
