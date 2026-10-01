"""Machine-only exploratory evidence and metrics must never become human approvals."""
from copy import deepcopy
from datetime import datetime,timezone
from types import SimpleNamespace

import pytest

from backend.app.domain import issue_text
from backend.app.storage import digest
from evaluation.machine_pilot import validate_annotations,scores


@pytest.fixture
def sample_machine():
    doc={'title':'Compile failure','body':'error: compiler symbol missing','html_url':'https://github.com/r/a/issues/1'}
    pool={'query_id':'Q','doc_id':'r/a#1','review_item_id':'item','query_sha256':digest('Q'),'document_sha256':digest(issue_text(doc))}
    annotation={**pool,'reviewer_type':'machine','assessment_status':'AI_EXPLORATORY_NOT_HUMAN_VALIDATED','grade':2,
                'evidence_scope':'title_body','evidence_quote':'compiler symbol missing','evidence_url':doc['html_url'],
                'reason':'synthetic machine fixture','recorded_at':datetime.now(timezone.utc).isoformat()}
    return SimpleNamespace(plan={'reviewer_type':'machine','human_approvals_created':0,'query_ids':['Q']},
                           annotations=[annotation],data={'pool':[pool],'documents':{'r/a#1':doc}})


def test_machine_evidence_keeps_provenance_and_inputs(sample_machine):
    x=sample_machine;before=deepcopy((x.plan,x.annotations,x.data))
    assert validate_annotations(x.plan,x.annotations,x.data)=={'Q':{'r/a#1':2}}
    assert (x.plan,x.annotations,x.data)==before


@pytest.mark.parametrize('change', ['human','hash','quote','incomplete','duplicate','boolean_grade'])
def test_invalid_machine_evidence_is_rejected(sample_machine,change):
    x=sample_machine
    if change=='human':x.annotations[0]['reviewer_type']='human'
    elif change=='hash':x.annotations[0]['document_sha256']='wrong'
    elif change=='quote':x.annotations[0]['evidence_quote']='invented evidence'
    elif change=='incomplete':x.annotations=[]
    elif change=='duplicate':x.annotations*=2
    elif change=='boolean_grade':x.annotations[0]['grade']=True
    with pytest.raises(ValueError):validate_annotations(x.plan,x.annotations,x.data)


def test_machine_metric_uses_full_pool_and_keeps_unavailable_idcg():
    grades={'A':2,'B':0,'C':0,'D':0,'E':0,'F':2}
    result=scores(['A','B','C','D','E'],grades)
    assert result['ai_hit_at_5']==1 and result['ai_mrr_at_5']==1
    assert result['ai_pooled_ndcg_at_5']==pytest.approx(.6131471927654584)
    assert scores(['B'],{'B':0})['ai_pooled_ndcg_at_5'] is None
    with pytest.raises(ValueError):scores(['unassessed'],grades)
