from backend.app.storage import Store
from evaluation.evaluate import eligible_pairs, rank_metrics, split_pairs
from evaluation.survey import explicit_duplicate


def test_only_explicit_maintainer_evidence():
    comment = {'body':'Duplicate of #123', 'author_association':'MEMBER'}
    assert explicit_duplicate(comment, 'a/b') == [123]
    assert explicit_duplicate({**comment, 'author_association':'NONE'}, 'a/b') == []
    assert explicit_duplicate({**comment, 'body':'Related to #123'}, 'a/b') == []
    assert explicit_duplicate({**comment, 'body':'Duplicate of https://github.com/a/b/issues/9'}, 'a/b') == [9]
    assert explicit_duplicate({**comment, 'body':'Duplicate of https://github.com/other/b/issues/9'}, 'a/b') == []


def test_groups_keep_chains_and_translations_together():
    pairs = [{'repository':'a/b','query_number':i,'target_number':i-1} for i in range(2, 20, 2)]
    pairs += [{'repository':'a/b','query_number':30,'target_number':2}, {'repository':'a/b','query_number':2,'target_number':1,'language':'ko'}]
    result = split_pairs(pairs)
    assert len({p['split'] for p in result if p['query_number'] in {2, 30}}) == 1
    assert result == split_pairs(pairs)
    assert set(p['split'] for p in result) == {'validation', 'test'}


def test_metrics_and_exclusions(tmp_path, sample_snapshot):
    assert rank_metrics([1, 2, None]) == {'count':3,'recall_at_1':1/3,'recall_at_5':2/3,'mrr':.5}
    assert rank_metrics([])['mrr'] is None
    snapshot = Store(tmp_path).save(sample_snapshot)
    base = {'repository':'example/library','query_number':2,'source_url':'https://github.com/example/library/issues/2#issuecomment-1'}
    pairs = [{**base,'target_number':1}, {**base,'target_number':3}, {**base,'target_number':99}, {**base,'target_number':1,'language':'ko','query_text':'한국어'}]
    valid, excluded = eligible_pairs(pairs, snapshot)
    assert len(valid) == 1
    assert {x['reason'] for x in excluded} == {'target_excluded_by_bug_filter','target_outside_snapshot','korean_query_requires_human_review'}
