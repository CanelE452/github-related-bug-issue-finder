"""Formula/provenance/gating fixtures are synthetic, never experiment labels."""
import base64
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest

from backend.app.domain import issue_text
from backend.app.search import tokenize, fuse
from backend.app.storage import digest
from evaluation.followup_scoring import resolve_reviews, query_metrics, score_records, extend_pool, csv_rows
from evaluation.followup_review import package
from evaluation.quick_review import quick_package
from evaluation.followup_retrieval import k1_tokens, contribution, failure_gate, behavior_gate, Budget
from evaluation.scenario_followup import save_csv, check_preservation
from evaluation.scenario_eval import sha_file
from evaluation.followup_report import progress_records, public_text


@pytest.fixture
def sample():
    queries={'Q':{'query_id':'Q','query_sha256':digest('CMake로 실패'),'query_text':'CMake로 실패','case_id':'C','variant':'A_ko_symptom'}}
    documents={f'r/a#{i}':{'number':i,'title':'CMake failure','body':f'Frozen detail {i}','html_url':f'https://github.com/r/a/issues/{i}'} for i in range(1,7)}
    pool=[{'review_item_id':digest(['Q',did])[:16],'query_id':'Q','query_sha256':queries['Q']['query_sha256'],'doc_id':did,'document_sha256':digest(issue_text(doc))} for did,doc in documents.items()]
    human={'reviewer_type':'human','reviewer_id':'fixture-person','reviewed_at':'2026-10-01T10:00:00+09:00','reason':'synthetic fixture only','review_status':'reviewed'}
    query_rows=[{'query_id':'Q','query_sha256':queries['Q']['query_sha256'],'symptom_faithful':'yes','no_solution_leakage':'yes','information_change_checked':'yes',**human}]
    review_rows=[{**p,**human,'grade':'2' if i==0 else '0','condition_relation':'supports','evidence_scope':'title_body','evidence_quote':'CMake failure','evidence_url':documents[p['doc_id']]['html_url']} for i,p in enumerate(pool)]
    runs=[{'kind':'core','query_id':'Q','case_id':'C','repository':'r/a','method':method,'corpus_scope':scope,'status':'ok','ranked_results':[{'doc_id':f'r/a#{i}','rank':i} for i in range(1,6)]} for method in ['bm25','semantic','hybrid'] for scope in ['C_raw','C_bug']]
    return SimpleNamespace(queries=queries,documents=documents,pool=pool,human=human,query_rows=query_rows,review_rows=review_rows,runs=runs)


def resolve(s,review_rows=None,query_rows=None,adjudications=()):
    return resolve_reviews(s.pool,s.queries,{k:issue_text(v) for k,v in s.documents.items()},{k:v['html_url'] for k,v in s.documents.items()},s.review_rows if review_rows is None else review_rows,s.query_rows if query_rows is None else query_rows,adjudications)


def score(s,resolved):
    return score_records(s.runs,s.queries,{'C':{'stratum':'error_literal'}},s.pool,resolved,{('r/a','C_raw'):set(s.documents),('r/a','C_bug'):set(s.documents)})


def test_top5_external_unjudged_denominator():
    j=dict(zip('ABCDEF',[2,0,0,0,0,None]));m=query_metrics(list('ABCDE'),j,set(j),True)
    assert m['confirmed_hit']==1 and not m['pool_complete'] and m['hit_at_5'] is None and m['pooled_ndcg_at_5'] is None
    j['F']=2;m=query_metrics(list('ABCDE'),j,set(j),True)
    assert m['pooled_ndcg_at_5']==pytest.approx(0.6131471927654584)


@pytest.mark.parametrize('grade,expected_hit,expected_ndcg',[(0,0,None),(1,0,1.0),(2,1,1.0)])
def test_zero_idcg_and_partial_grade(grade,expected_hit,expected_ndcg):
    m=query_metrics(['d'],{'d':grade},{'d'},True)
    assert m['hit_at_5']==expected_hit and m['pooled_ndcg_at_5']==expected_ndcg


def test_empty_error_unapproved_and_unavailable_distinct():
    assert query_metrics([],{'d':2},{'d'},True)['hit_at_5']==0
    assert query_metrics([],{'d':2},{'d'},True,'execution_error')['reason']=='execution_error'
    assert query_metrics(['d'],{'d':2},{'d'},False)['confirmed_hit'] is None
    assert query_metrics([],{'d':None},{'d'},True)['reason']=='common_pool_incomplete'


@pytest.mark.parametrize('field',['review_item_id','query_id','doc_id','query_sha256','document_sha256'])
def test_mismatched_identity_rejected(sample,field):
    sample.review_rows[0][field]='wrong'
    with pytest.raises(ValueError,match='ID or hash mismatch'):resolve(sample)


@pytest.mark.parametrize('field,value',[('reviewer_type','machine'),('reviewer_id',''),('reviewed_at',''),('reviewed_at','2026-10-01T10:00:00'),('reason','')])
def test_actual_provenance_required(sample,field,value):
    sample.review_rows[0][field]=value
    with pytest.raises(ValueError):resolve(sample)


def test_evidence_quote_and_url_must_match(sample):
    sample.review_rows[0]['evidence_quote']='invented quotation'
    with pytest.raises(ValueError,match='quote absent'):resolve(sample)
    sample.review_rows[0]['evidence_quote']='CMake failure';sample.review_rows[0]['evidence_url']='https://github.com/r/b/issues/1'
    with pytest.raises(ValueError,match='URL'):resolve(sample)


def test_independent_disagreement_adjudication(sample):
    second={**sample.review_rows[0],'grade':'1','reviewer_id':'fixture-second'}
    result=resolve(sample,sample.review_rows+[second]);assert result['human_reviewers']==2 and result['qrels'][0]['grade'] is None and result['qrels'][0]['reason']=='reviewer_disagreement'
    adj={**sample.review_rows[0],'kind':'document','target_id':sample.pool[0]['review_item_id']}
    result=resolve(sample,sample.review_rows+[second],adjudications=iter([adj]));assert result['qrels'][0]['grade']==2 and len(result['adjudications'])==1
    with pytest.raises(ValueError,match='duplicate reviewer'):resolve(sample,sample.review_rows+[sample.review_rows[0]])


@pytest.mark.parametrize('scope',['unavailable','comment_only'])
def test_unavailable_and_comment_not_complete(sample,scope):
    sample.review_rows[0]['evidence_scope']=scope
    if scope=='unavailable':sample.review_rows[0]['grade']=''
    result=resolve(sample);assert result['qrels'][0]['grade'] is None and score(sample,result)['comparison_queries']==0


def test_pending_partial_reviewed_dynamic_state(sample):
    pending=score(sample,resolve(sample,[],[]));partial=score(sample,resolve(sample,sample.review_rows[:1]));reviewed=score(sample,resolve(sample))
    assert [x['state'] for x in [pending,partial,reviewed]]==['AWAITING_HUMAN_REVIEW','PARTIALLY_REVIEWED','REVIEWED']
    assert [progress_records(x)[1]['complete'] for x in [pending,partial,reviewed]]==[0,1,6]
    assert pending['summary'][0]['comparison_n']==0 and pending['summary'][0]['hit_at_5'] is None
    assert len({r['common_query_ids_hash'] for r in reviewed['summary']})==1 and all(r['hit_at_5']==1 for r in reviewed['summary'])


def test_filter_missing_positive_kept_in_common_denominator(sample):
    for r in sample.runs:
        if r['corpus_scope']=='C_bug':r['ranked_results']=r['ranked_results'][1:]
    result=score_records(sample.runs,sample.queries,{'C':{'stratum':'error_literal'}},sample.pool,resolve(sample),{('r/a','C_raw'):set(sample.documents),('r/a','C_bug'):set(sample.documents)-{'r/a#1'}})
    bug=[r for r in result['summary'] if r['scope']=='C_bug'];assert all(r['comparison_n']==1 and r['hit_at_5']==0 and r['known_positive_n']==0 and r['pooled_ndcg_at_5']==0 for r in bug)


def test_error_excludes_query_from_every_method_comparison(sample):
    sample.runs[0]['status']='execution_error';sample.runs[0]['ranked_results']=[]
    result=score(sample,resolve(sample));assert result['comparison_queries']==0 and all(r['comparison_n']==0 for r in result['summary'])


def test_query_universe_mismatch_rejected(sample):
    sample.runs[0]['query_id']='different'
    with pytest.raises(ValueError,match='same core query universe'):score(sample,resolve(sample))


def test_expanded_pool_requires_new_judgments(sample):
    p=extend_pool(sample.pool[:-1],sample.runs,sample.queries,{k:digest(issue_text(v)) for k,v in sample.documents.items()});assert len(p)==5
    sample.runs[0]['ranked_results'][0]['doc_id']='r/a#6';p=extend_pool(p,sample.runs,sample.queries,{k:digest(issue_text(v)) for k,v in sample.documents.items()});assert len(p)==6
    judgments={f'r/a#{i}':0 for i in range(1,6)};assert query_metrics(['r/a#1'],judgments,{x['doc_id'] for x in p},True)['pooled_ndcg_at_5'] is None


def test_history_and_repeats_not_core(sample):
    sample.runs+=[{**sample.runs[0],'kind':kind,'case_id':'historic'} for kind in ['historical','timing','E1']]
    result=score(sample,resolve(sample));assert result['core_families']==1 and result['planned_queries']==1 and len(result['by_query'])==6


def test_k1_only_mixed_identifier_additions():
    assert k1_tokens('CMake로 Gemma4에서 generate를')==['cmake로','gemma4에서','generate를','cmake','gemma4','generate']
    text='Python 3.12 RuntimeError: code 123 path/to_func-1.2'
    assert k1_tokens(text)==tokenize(text)
    assert k1_tokens('Gemma4에서 gemma4').count('gemma4')==1
    result=k1_tokens('cv::함수 Gemma-4.2에서 123에서 /a.py에서')
    assert 'gemma-4.2' in result and 'a.py' in result and '123' not in result


def test_rrf_window_and_nonmatching_docs():
    lexical=[(i,1.) for i in range(1,53)];semantic=[(52,1.)]
    row=contribution(lexical,semantic)[52];assert row['bm25_rank']==52 and row['lexical_rrf_term']==0 and row['semantic_rrf_term']==pytest.approx(1/61)
    assert row['fused_score']==dict(fuse(lexical,semantic))[52]
    assert dict(fuse(lexical,semantic,window=52))[52]>row['fused_score']
    assert 99 not in dict(fuse(lexical,semantic,window=100))


def test_human_failure_gate_not_reference_rank(sample):
    data={'queries':sample.queries,'runs':sample.runs,'documents':sample.documents,'scopes':{('r/a','C_raw'):{'issues':list(sample.documents.values())}}}
    request={**sample.human,'query_id':'Q','query_sha256':sample.queries['Q']['query_sha256'],'scope':'C_raw','direct_doc_id':'r/a#1','competitor_doc_id':'r/a#2'}
    with pytest.raises(ValueError,match='reproduction'):failure_gate('K1',request,data,resolve(sample),{'status':'PENDING'})
    with pytest.raises(ValueError,match='no validated'):failure_gate('K1',request,data,resolve(sample),{'status':'REPRODUCED'})


def test_behavior_unapproved_or_missing_evidence_blocked(sample):
    q={**sample.human,'query_id':'new','query_sha256':digest('[PROBLEM]\nsymptom'),'query_text':'[PROBLEM]\nsymptom','problem':'symptom','case_id':'newcase','repository':'r/a','approved':'yes'}
    data={'snapshots':{'r/a':{}},'queries':sample.queries,'documents':sample.documents}
    for experiment in ['E1','E2','E3']:
        with pytest.raises(ValueError):behavior_gate(experiment,{**sample.human,'queries':[q]},data,resolve(sample))
    q['approved']='no'
    with pytest.raises(ValueError,match='approval'):behavior_gate('E3',{**sample.human,'queries':[q]},data,resolve(sample))


def test_control_certification_requires_all_actual_grades(sample):
    entries=[]
    for i,doc in enumerate(list(sample.documents.values())[:2]):entries.append({**sample.human,'doc_id':f'r/a#{doc["number"]}','document_sha256':digest(issue_text(doc)),'evidence_scope':'title_body','evidence_quote':'CMake failure','evidence_url':doc['html_url'],'grade':2 if i==0 else 0})
    q={**sample.human,'query_id':'new','query_sha256':digest('[PROBLEM]\nsymptom'),'query_text':'[PROBLEM]\nsymptom','problem':'symptom','case_id':'newcase','repository':'r/a','approved':'yes','control_documents':entries}
    data={'snapshots':{'r/a':{}},'queries':sample.queries,'documents':sample.documents};request={**sample.human,'queries':[q]}
    assert len(behavior_gate('E3',request,data,resolve(sample)))==1
    entries[1]['grade']=None
    with pytest.raises(ValueError,match='complete actual'):behavior_gate('E3',request,data,resolve(sample))


def test_parent_byte_preservation(tmp_path):
    p=tmp_path/'parent';p.mkdir();f=p/'runs.jsonl';f.write_bytes(b'{"record":1}\r\n');h={'runs.jsonl':sha_file(f)}
    assert check_preservation(p,h)==1
    (tmp_path/'child').mkdir();assert check_preservation(p,h)==1
    f.write_bytes(b'{"record":1}\n')
    with pytest.raises(ValueError,match='parent directory changed'):check_preservation(p,h)


def test_review_html_payload_safe_and_no_rank_metadata(tmp_path,sample):
    sample.documents['r/a#1']['body']='</script><script>alert(1)</script>';sample.pool[0]['document_sha256']=digest(issue_text(sample.documents['r/a#1']))
    path=package(tmp_path,sample.queries,{'C':{'case_id':'C','repository':'r/a','cohort':'core_development','source_doc_ids':['r/a#1']}},sample.pool,sample.documents,1)
    page=path.read_text(encoding='utf-8');assert '</script><script>alert(1)</script>' not in page and 'textContent' in page and 'source_doc_ids' not in page
    script=(Path(__file__).parents[2]/'evaluation/scenario_followup_v2/review.js').read_text(encoding='utf-8');h=base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
    assert "script-src 'sha256-"+h+"'" in page and 'fetch(' not in script


def test_csv_formula_export_only(tmp_path):
    original={'reason':'=HYPERLINK("bad")','evidence_quote':'+function','reviewer_id':'-fixture'};p=tmp_path/'review.csv';save_csv(p,[original]);text=p.read_text(encoding='utf-8-sig')
    assert "'=HYPERLINK" in text and original['reason'].startswith('=') and csv_rows(p)==[original]


def test_quick_review_is_bounded_optional_and_separate_from_qrels(tmp_path,sample):
    frozen=deepcopy((sample.queries,sample.pool,sample.documents))
    page,payload=quick_package(tmp_path,sample.queries,sample.pool,sample.documents,11)
    assert len(payload['items'])==3 and payload['query']['query_id']=='Q'
    assert payload['purpose']=='optional_ui_feedback_not_evaluation_qrels'
    assert all('rank' not in item and 'score' not in item and 'grade' not in item for item in payload['items'])
    assert 'id="reviewer"' not in page.read_text(encoding='utf-8')
    assert 'id="quick-skip"' in page.read_text(encoding='utf-8')
    assert quick_package(tmp_path/'repeat',sample.queries,sample.pool,sample.documents,11)[1]==payload
    assert (sample.queries,sample.pool,sample.documents)==frozen


def test_quick_review_source_safety_and_small_pool(tmp_path,sample):
    sample.documents['r/a#1']['body']='</script><script>alert(1)</script>'
    page,payload=quick_package(tmp_path,sample.queries,sample.pool[:1],sample.documents,11)
    text=page.read_text(encoding='utf-8')
    assert len(payload['items'])==1 and '</script><script>alert(1)</script>' not in text
    script=(Path(__file__).parents[2]/'evaluation/scenario_followup_v2/quick-review.js').read_text(encoding='utf-8')
    h=base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
    assert "script-src 'sha256-"+h+"'" in text and 'fetch(' not in script
    sample.documents['r/a#1']['html_url']='javascript:alert(1)'
    with pytest.raises(ValueError,match='Unsafe issue URL'):
        quick_package(tmp_path,sample.queries,sample.pool[:1],sample.documents,11)


def test_public_masking_does_not_change_original():
    text=r'C:\Users\person\secret.py person@example.com';assert public_text(text)=='[LOCAL_PATH] [EMAIL]' and 'person' in text


def test_budget_enforces_phase_and_total(tmp_path):
    budget=Budget(tmp_path);budget.reserve('reproduce',12)
    with pytest.raises(ValueError,match='budget'):budget.reserve('reproduce',1)
    budget.value['compute_seconds']=5400
    with pytest.raises(ValueError,match='budget'):budget.reserve('K1',1)


def test_budget_checkpoint_reservation_idempotent(tmp_path):
    budget=Budget(tmp_path);budget.reserve('K1',4,'fixture-operation');budget.reserve('K1',4,'fixture-operation')
    assert budget.value['logical_conditions']==4
    with pytest.raises(ValueError,match='identity'):budget.reserve('K1',2,'fixture-operation')


@pytest.mark.parametrize('experiment',['K1','E2','E3'])
def test_gated_runner_executes_only_fixture_and_preserves_parent(tmp_path,monkeypatch,sample,experiment):
    from evaluation import followup_retrieval as module
    from evaluation.scenario_followup import save,save_rows
    for r in sample.runs:r['ranked_results']=[{'rank':i,'doc_id':f'r/a#{n}'} for i,n in enumerate(range(2,7),1)]
    scopes={('r/a',scope):{'repository':'r/a','issues':list(sample.documents.values()),'scope':scope,'version':digest(scope),'ids_hash':digest(sorted(sample.documents))} for scope in ['C_raw','C_bug']}
    data={'queries':sample.queries,'cases':{'C':{'case_id':'C','repository':'r/a','cohort':'core_development'}},'runs':sample.runs,'pool':sample.pool,'documents':sample.documents,'scopes':scopes,'snapshots':{'r/a':{}},'manifest':{'config':{'bug_labels':['bug'],'model_revision':'fixture-model'},'config_hash':'fixture-config','code_hashes':{}}}
    before=digest(sample.runs);save(tmp_path/'current-round.json',{'round_id':'fixture'});save(tmp_path/'rounds/fixture/qrels.json',resolve(sample));save(tmp_path/'reproduction.json',{'status':'REPRODUCED'})
    monkeypatch.setattr(module,'batch_data',lambda _:data)
    class FakeSemantic:
        def manifest_path(self,snapshot):
            p=tmp_path/(snapshot['scope']+'.manifest.json')
            if not p.exists():save(p,{'entries':[{'number':x['number'],'body_hash':digest(issue_text(x)),'file':'fixture.npy'} for x in sample.documents.values()]})
            return p
    class FakeRanks:
        def __init__(self,*args):self.indices={};self.semantic=FakeSemantic()
        def initialize_semantic(self):pass
        def full(self,q,repo,scope,*args):
            docs=data['scopes'][(repo,scope)]['issues'];lex=[(x['number'],1.0) for x in docs if x['number']!=1];sem=[(x['number'],1.0) for x in docs]
            return lex,sem
    monkeypatch.setattr(module,'FrozenRanks',FakeRanks)
    request={**sample.human,'query_id':'Q','query_sha256':sample.queries['Q']['query_sha256'],'scope':'C_raw','direct_doc_id':'r/a#1','competitor_doc_id':'r/a#2'}
    if experiment in {'E2','E3'}:
        q={**sample.human,'query_id':'NEW1','query_sha256':digest('[PROBLEM]\nsymptom'),'query_text':'[PROBLEM]\nsymptom','problem':'symptom','case_id':'newcase','repository':'r/a','approved':'yes','variant':experiment}
        evidence=[{**sample.human,'doc_id':f'r/a#{i}','document_sha256':digest(issue_text(sample.documents[f'r/a#{i}'])),'evidence_scope':'title_body','evidence_quote':'CMake failure','evidence_url':sample.documents[f'r/a#{i}']['html_url'],'grade':2 if i==1 else 0} for i in [1,2]]
        if experiment=='E3':q['control_documents']=evidence;qs=[q]
        else:q.update(pair_id='pair',condition='enabled',condition_evidence=evidence);qs=[q,{**q,'query_id':'NEW2','condition':'disabled','problem':'symptom with disabled condition','query_text':'[PROBLEM]\nsymptom with disabled condition','query_sha256':digest('[PROBLEM]\nsymptom with disabled condition')}]
        request={**sample.human,'queries':qs}
    approval=tmp_path/'approval.json';save(approval,request)
    module.run_approved(SimpleNamespace(batch=tmp_path,experiment=experiment,approval_file=approval))
    receipt=next((tmp_path/'experiments').glob('*/receipt.json'));actual=json.loads(receipt.read_text(encoding='utf-8'))
    assert actual['conditions']==(4 if experiment=='K1' else 12 if experiment=='E2' else 6) and not actual['quality_verified']
    assert digest(sample.runs)==before
    if experiment=='K1':assert (tmp_path/'new-runs.jsonl').exists()
    if experiment=='E3':
        records=[json.loads(x) for x in (receipt.parent/'runs.jsonl').read_text(encoding='utf-8').splitlines()]
        assert all(x['doc_id']!='r/a#1' for r in records if r['corpus_scope']=='control_minus' for x in r['ranked_results'])
