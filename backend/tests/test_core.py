import numpy as np
import pytest

from backend.app.config import Settings
from backend.app.domain import ServiceError, bug_labels, is_bug, query_text, repository_name
from backend.app.search import SearchEngine, fuse, tokenize
from backend.app.semantic import SemanticSearch, chunk_text
from backend.app.storage import Store
from backend.tests.conftest import issue


@pytest.mark.parametrize('value', ['http://github.com/a/b', 'https://evil.test/a/b', 'https://github.com/a/b/issues', 'a/..', 'a/b?q=1', 'https://user@github.com/a/b'])
def test_repository_rejects_invalid(value):
    with pytest.raises(ValueError):
        repository_name(value)


def test_repository_and_filter():
    assert repository_name('https://github.com/Owner/Repo.git/') == 'owner/repo'
    labels = bug_labels(['Type: Bug'])
    assert is_bug(issue(1, labels=[{'name': 'TYPE: BUG'}]), labels)
    assert is_bug(issue(1, labels=[], type={'name': 'Bug'}), labels)
    assert not is_bug(issue(1, pull_request={}), labels)
    assert not is_bug(issue(1, labels=[{'name': 'debug'}]), labels)


def test_tokenization_preserves_signal():
    tokens = tokenize('ERR_CONNECTION_RESET cudaMalloc torch.compile Python3.12 C:\\Users\\alice\\train.py PID=123')
    assert {'err_connection_reset', 'cudamalloc', 'torch.compile', 'python3.12', '123'} <= set(tokens)
    assert 'alice' in tokens  # No noise normalization.


def test_search_filter_exact_empty_and_restart(tmp_path, sample_snapshot):
    store = Store(tmp_path)
    snapshot = store.save(sample_snapshot)
    search = SearchEngine(store, None)
    assert search.search('example/library', 'ERR_CONNECTION_RESET', 'bm25')['results'][0]['number'] == 2
    assert search.search('example/library', 'CUDA', 'bm25')['results'][0]['number'] == 1
    assert search.search('example/library', 'unmatchedzz', 'bm25')['results'] == []
    assert search.search('example/library', query_text('화면이 멈춰요'), 'bm25')['results'] == []
    assert SearchEngine(Store(tmp_path), None).search('example/library', 'numerical', 'bm25')['results'][0]['number'] == 4
    assert all(n != 1 for n, _ in search.ranking(snapshot, 'CUDA', 'bm25', exclude=1))
    with pytest.raises(ServiceError, match='분석'):
        search.search('another/repo', 'CUDA', 'bm25')


def test_tiny_corpus_and_rrf(tmp_path, sample_snapshot):
    sample_snapshot['issues'] = [issue(1)]
    store = Store(tmp_path)
    store.save(sample_snapshot)
    result = SearchEngine(store, None).search('example/library', 'CUDA', 'bm25')
    assert result['results'][0]['score'] > 0
    assert fuse([(1, 100), (2, 5)], [(2, .1), (3, .09)])[0][0] == 2
    assert fuse([], [(7, .2)])[0][0] == 7


class Tokenizer:
    def encode(self, text, **kwargs):
        return text.split()
    def decode(self, ids, **kwargs):
        return ' '.join(ids)


class Model:
    tokenizer = Tokenizer()
    def __init__(self):
        self.calls = []
    def encode(self, texts, **kwargs):
        self.calls += texts
        return np.array([[1., 0.] if ('CUDA' in text or '메모리' in text) else [0., 1.] for text in texts], dtype=np.float32)


def test_chunking_keeps_tail_and_overlap():
    text = ' '.join(map(str, range(1000)))
    chunks = chunk_text(text, Tokenizer())
    assert len(chunks) == 3
    assert chunks[0].split()[-64:] == chunks[1].split()[:64]
    assert chunks[-1].split()[-1] == '999'
    assert chunk_text('', Tokenizer()) == ['']


def test_semantic_cache_revision_and_prefix(tmp_path, sample_snapshot):
    settings = Settings(data_dir=tmp_path)
    store = Store(tmp_path)
    snapshot = store.save(sample_snapshot)
    semantic = SemanticSearch(settings)
    semantic.model, semantic.revision = Model(), 'test-immutable-sha'
    bugs = [x for x in snapshot['issues'] if is_bug(x, ['bug'])]
    semantic.prepare(snapshot, bugs)
    assert all(x.startswith('passage: ') for x in semantic.model.calls)
    count = len(semantic.model.calls)
    semantic.prepare(snapshot, bugs)
    assert len(semantic.model.calls) == count
    assert semantic.scores(snapshot, '메모리 오류')[1] == 1
    assert semantic.model.calls[-1].startswith('query: ')
    restarted = SemanticSearch(settings)
    restarted.model, restarted.revision = Model(), 'test-immutable-sha'
    assert restarted.ready(snapshot)
    assert restarted.scores(snapshot, '메모리 오류')[1] == 1
    restarted.revision = 'different'
    with pytest.raises(ServiceError) as exc:
        restarted.scores(snapshot, 'CUDA')
    assert exc.value.code == 'model_revision_changed'
    changed = {**snapshot, 'version': 'different'}
    assert not restarted.ready(changed)


def test_hybrid_excludes_self_before_top50(tmp_path, sample_snapshot):
    store = Store(tmp_path)
    snapshot = store.save(sample_snapshot)
    class Scores:
        def scores(self, snapshot, query):
            return {1: .9, 2: .8, 4: .7}
    result = SearchEngine(store, Scores()).ranking(snapshot, 'CUDA', 'hybrid', exclude=1)
    assert [n for n, _ in result] == [2, 4]
