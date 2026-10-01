"""Retrieval-path fixtures use fake vectors only here, never in pilot results."""
from copy import deepcopy
from types import SimpleNamespace

import numpy as np
import pytest

from backend.app.config import Settings
from backend.app.domain import ServiceError, query_text
from backend.app.search import SearchEngine
from backend.app.semantic import SemanticSearch
from backend.app.storage import digest
from backend.tests.conftest import issue
from backend.tests.test_core import Model
from evaluation import scenario_eval as ev


def fixture_snapshot():
    return {'repository':'example/library','version':'fixture','bug_labels':['bug'],
            'issues':[issue(1),issue(2,'Connection reset','ERR_RESET'),issue(3,'Docs','documentation',labels=[])]}


class Scores:
    def __init__(self): self.inputs=[]
    def scores(self,snapshot,text):
        self.inputs.append(text)
        return {x['number']: .9-.1*i for i,x in enumerate(snapshot['issues'])}


def manifest():
    return {'config':{'model_revision':'fixture'},'code_revision':'fixture','code_hashes':{},'config_hash':'fixture'}


def test_independent_query_actual_input_and_no_required_source():
    semantic=Scores();engine=ev.ScenarioEngine(ev.corpus(fixture_snapshot(),'C_raw',['bug']),semantic)
    for text in [query_text('메모리가 부족해서 실행이 멈춥니다.'),query_text('The application stops when memory is exhausted.')]:
        engine.ranking(text,'semantic')
        assert semantic.inputs[-1]==text and 'RuntimeError' not in semantic.inputs[-1]
    case={'case_id':'new','cohort':'new_user_task','repository':'example/library'}
    q={'query_id':'new:ko','query_text':'ERR_RESET','query_sha256':digest('ERR_RESET')}
    result=ev.make_run(engine,q,case,'bm25',manifest())
    assert result['status']=='ok' and result['reference_doc_rank'] is None


def test_service_adapter_all_method_parity():
    raw=fixture_snapshot();selected=ev.corpus(raw,'C_bug',['bug']);semantic=Scores()
    service=SearchEngine(None,semantic);adapter=ev.ScenarioEngine(selected,semantic)
    for method in ['bm25','semantic','hybrid']:
        assert service.ranking(selected,'CUDA ERR_RESET',method)==adapter.ranking('CUDA ERR_RESET',method)


def test_immutable_scope_id_and_semantic_cache_isolation(tmp_path):
    original=fixture_snapshot();before=deepcopy(original)
    original['issues'].append(issue(4,pull_request={}))
    raw=ev.corpus(original,'C_raw',['bug']);bug=ev.corpus(original,'C_bug',['bug'])
    assert len(raw['issues'])==3 and len(bug['issues'])==2
    assert original['issues'][:3]==before['issues']
    assert ev.doc_id('a/repo',1)!=ev.doc_id('b/repo',1)
    semantic=SemanticSearch(Settings(data_dir=tmp_path,model_revision='fixture'))
    semantic.model=Model();semantic.revision='fixture'
    semantic.prepare(raw,raw['issues']);semantic.prepare(bug,bug['issues'])
    assert semantic.manifest_path(raw)!=semantic.manifest_path(bug)
    assert set(semantic.scores(raw,'CUDA'))=={1,2,3}
    assert set(semantic.scores(bug,'CUDA'))=={1,2}


def test_distinct_empty_no_match_and_execution_error():
    q={'query_id':'q','query_sha256':'s','query_text':'unmatchedzz'}
    c={'case_id':'c','cohort':'core_development','repository':'example/library','reference_number':1}
    empty=fixture_snapshot();empty['issues']=[]
    engine=ev.ScenarioEngine(ev.corpus(empty,'C_bug',['bug']),Scores())
    assert ev.make_run(engine,q,c,'bm25',manifest())['status']=='empty_corpus'
    with pytest.raises(ServiceError) as error:SearchEngine(None,None).index(engine.snapshot)
    assert error.value.code=='no_bug_issues'
    engine=ev.ScenarioEngine(ev.corpus(fixture_snapshot(),'C_raw',['bug']),Scores())
    assert ev.make_run(engine,q,c,'bm25',manifest())['status']=='no_lexical_match'
    engine.ranking=lambda *args: (_ for _ in ()).throw(RuntimeError('test'))
    assert ev.make_run(engine,q,c,'bm25',manifest())['status']=='execution_error'


@pytest.mark.parametrize('mutation',['query','source','code','revision','config'])
def test_hash_mismatch_stops_reuse(tmp_path,monkeypatch,mutation):
    monkeypatch.setattr(ev,'code_hashes',lambda:{'fixture':'unchanged'})
    source=fixture_snapshot();ev.write(tmp_path/'snapshot.json',source)
    q={'query_id':'q','problem':'실행 실패','query_text':query_text('실행 실패')};q['query_sha256']=digest(q['query_text'])
    ev.jsonl(tmp_path/'queries.jsonl',[q]);ev.jsonl(tmp_path/'cases.jsonl',[])
    m={'code_hashes':ev.code_hashes(),'snapshots':{'example/library':{'file':'snapshot.json','file_hash':ev.sha_file(tmp_path/'snapshot.json')}},
       'queries_hash':digest([q]),'cases_hash':digest([]),'config':{'model_revision':'original'},'config_hash':digest({'model_revision':'original'})}
    ev.write(tmp_path/'manifest.json',m);ev.verify(tmp_path)
    if mutation=='query':q['query_text']='Changed';ev.jsonl(tmp_path/'queries.jsonl',[q])
    if mutation=='source':source['issues'][0]['body']='Changed';ev.write(tmp_path/'snapshot.json',source)
    if mutation=='code':m['code_hashes']={'fixture':'changed'};ev.write(tmp_path/'manifest.json',m)
    if mutation in {'revision','config'}:
        m['config']['model_revision']='changed';ev.write(tmp_path/'manifest.json',m)
    with pytest.raises(ValueError):ev.verify(tmp_path)


def test_multiple_positive_and_unknown_do_not_become_misses():
    assert ev.metric_values(['alternative'],{'reference':2,'alternative':2})['hit_at_5']==1
    assert ev.metric_values(['weak','wrong'],{'weak':1,'wrong':0})['hit_at_5']==0
    assert ev.metric_values(['unknown'],{})['hit_at_5'] is None
    assert ev.metric_values([],{},status='execution_error')['hit_at_5'] is None
    # A positive filtered out of Bug scope stays in the common raw denominator.
    result=ev.metric_values(['weak'],{'weak':1,'filtered_source':2},reference_ids={'weak','filtered_source'})
    import math
    assert result['hit_at_5']==0 and result['pooled_ndcg_at_5']==pytest.approx(1/(3+1/math.log2(3)))


def test_ndcg_hand_calculation_zero_gain_and_partial():
    import math
    assert ev.metric_values(['a','b'],{'a':2,'b':1})['pooled_ndcg_at_5']==1
    expected=(1+3/math.log2(3))/(3+1/math.log2(3))
    assert ev.metric_values(['b','a'],{'a':2,'b':1})['pooled_ndcg_at_5']==pytest.approx(expected)
    assert ev.metric_values(['a'],{'a':0})['pooled_ndcg_at_5'] is None
    assert ev.metric_values(['unknown'],{'positive':2})['pooled_ndcg_at_5'] is None


def test_machine_judgments_and_changed_hash_rejected():
    expected={'query_sha256':'q','document_sha256':'d'}
    item={**expected,'reviewer_type':'machine','reviewer_id':'model','reviewed_at':'2026-10-01T00:00:00Z','review_status':'reviewed',
          'grade':'2','reason':'test','evidence_quote':'text','evidence_url':'https://github.com/a/b/issues/1',
          'condition_relation':'supports','evidence_scope':'title_body'}
    with pytest.raises(ValueError):ev.validate_human_review(item,expected)
    item['reviewer_type']='human';ev.validate_human_review(item,expected)
    item['query_sha256']='changed'
    with pytest.raises(ValueError):ev.validate_human_review(item,expected)


def test_no_answer_requires_full_judgments_without_grade_two():
    assert ev.certify_no_answer(['a','b'],{'a':0,'b':1})
    assert not ev.certify_no_answer(['a','b'],{'a':0})
    assert not ev.certify_no_answer(['a','b'],{'a':0,'b':2})
    assert not ev.certify_no_answer([],{})


def test_html_is_inert_and_contains_only_public_fields():
    document={'title':'<script>alert(1)</script>','body':'<img src=x onerror=alert(2)>','html_url':'https://github.com/a/b/issues/1','private_token':'DO_NOT_RENDER'}
    result=ev.review_article('id','<script>query</script>',document)
    assert '<script>' not in result and '<img' not in result
    assert '&lt;script&gt;' in result and 'DO_NOT_RENDER' not in result
    document['html_url']='javascript:alert(1)'
    with pytest.raises(ValueError):ev.review_article('id','query',document)


def test_pool_deduplicates_repeated_runs_not_independent_families(tmp_path):
    ev.jsonl(tmp_path/'queries.jsonl',[{'query_id':'c:B','case_id':'c'}])
    ev.jsonl(tmp_path/'cases.jsonl',[{'case_id':'c','family_id':'family','source_doc_ids':['a/repo#1']}])
    run={'query_id':'c:B','kind':'core','ranked_results':[{'doc_id':'a/repo#2'}]}
    ev.jsonl(tmp_path/'runs.jsonl',[run,run,run])
    _,pooled=ev.pool_review(tmp_path)
    assert pooled=={'c:B':{'a/repo#1','a/repo#2'}}
