import time

import httpx
import pytest
from fastapi.testclient import TestClient

from backend.app.config import Settings
from backend.app.domain import ServiceError
from backend.app.github import GitHubClient
from backend.app.main import create_app
from backend.tests.conftest import issue


def wait_job(client, job_id):
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        job = client.get('/api/repositories/jobs/' + job_id).json()
        if job['status'] in {'completed', 'failed'}:
            return job
        time.sleep(.01)
    raise AssertionError('Job did not finish')


def test_github_pagination_and_pr_exclusion():
    calls = []
    def handle(request):
        calls.append(request)
        if request.url.path == '/repos/a/b':
            return httpx.Response(200, json={'private': False})
        if request.url.params.get('page', '1') == '1':
            return httpx.Response(200, json=[issue(1), issue(2, pull_request={})], headers={'Link': '<https://api.github.com/repos/a/b/issues?page=2>; rel="next"'})
        return httpx.Response(200, json=[issue(3)])
    client = GitHubClient(transport=httpx.MockTransport(handle))
    result = client.fetch('a/b', 20)
    assert result['fetched_count'] == 3 and result['issue_count'] == 2
    assert not result['partial']
    assert calls[1].url.params['state'] == 'all'
    assert calls[1].url.params['direction'] == 'desc'
    limited = client.fetch('a/b', 1)
    assert limited['partial']
    client.close()


@pytest.mark.parametrize(('code', 'headers', 'expected'), [(403, {'X-RateLimit-Remaining': '0'}, 'github_rate_limit'), (429, {}, 'github_rate_limit'), (404, {}, 'repository_not_found'), (401, {}, 'github_token_invalid'), (403, {}, 'github_forbidden')])
def test_github_errors(code, headers, expected):
    client = GitHubClient(transport=httpx.MockTransport(lambda _: httpx.Response(code, headers=headers, json={})))
    with pytest.raises(ServiceError) as exc:
        client.fetch('a/b', 1)
    assert exc.value.code == expected
    client.close()


def test_github_network_error():
    def fail(request):
        raise httpx.ConnectError('offline', request=request)
    client = GitHubClient(transport=httpx.MockTransport(fail))
    with pytest.raises(ServiceError) as exc:
        client.fetch('a/b', 1)
    assert exc.value.code == 'github_network'


def test_large_repository_cursor_links():
    requests = []
    def handle(request):
        requests.append(request)
        if request.url.path == '/repos/a/b':
            return httpx.Response(200, json={'id': 123, 'private': False})
        if 'after' not in request.url.params:
            return httpx.Response(200, json=[issue(1)], headers={'Link': '<https://api.github.com/repositories/123/issues?after=cursor-value&per_page=100>; rel="next"'})
        return httpx.Response(200, json=[issue(2)])
    client = GitHubClient(transport=httpx.MockTransport(handle))
    result = client.fetch('a/b', 20)
    assert result['issue_count'] == 2
    assert requests[-1].url.params['after'] == 'cursor-value'
    assert requests[-1].url.path == '/repositories/123/issues'
    client.close()


class UnavailableSemantic:
    def ready(self, _):
        return False
    def prepare(self, *args):
        raise ServiceError('model_unavailable', 'Model unavailable', 503)
    def scores(self, *args):
        raise ServiceError('semantic_not_ready', 'Not ready', 409)


def test_jobs_cache_refresh_failure_and_restart(tmp_path, sample_snapshot):
    class GitHub:
        count = 0
        failing = False
        def fetch(self, *args):
            self.count += 1
            if self.failing:
                raise ServiceError('github_network', 'Network down', 502)
            return sample_snapshot
        def close(self):
            pass
    github = GitHub()
    settings = Settings(data_dir=tmp_path)
    app = create_app(settings, github=github, semantic=UnavailableSemantic())
    with TestClient(app) as client:
        assert client.post('/api/search', json={'repository':'example/library', 'problem':'CUDA'}).status_code == 409
        request = {'repository_url': 'https://github.com/example/library'}
        job = wait_job(client, client.post('/api/repositories/analyze', json=request).json()['job_id'])
        assert job['status'] == 'completed' and job['available_methods'] == ['bm25']
        assert job['semantic_error']['code'] == 'model_unavailable'
        request['prepare_semantic'] = False
        job = wait_job(client, client.post('/api/repositories/analyze', json=request).json()['job_id'])
        assert job['cache_hit'] and github.count == 1
        github.failing = True
        request['refresh'] = True
        job = wait_job(client, client.post('/api/repositories/analyze', json=request).json()['job_id'])
        assert job['status'] == 'failed' and job['error']['code'] == 'github_network'
        r = client.post('/api/search', json={'repository':'example/library', 'problem':'CUDA', 'method':'bm25'})
        assert r.status_code == 200 and r.json()['results'][0]['number'] == 1
        assert client.post('/api/search', json={'repository':'other/library', 'problem':'CUDA', 'method':'bm25'}).status_code == 409
        assert client.post('/api/search', json={'repository':'example/library', 'problem':'   '}).status_code == 422
        assert client.post('/api/search', json={'repository':'example/library', 'problem':'CUDA','top_k':21}).status_code == 422
        assert client.get('/api/repositories/jobs/missing').status_code == 404
    with TestClient(create_app(settings, github=github, semantic=UnavailableSemantic())) as client:
        assert client.post('/api/search', json={'repository':'example/library','problem':'CUDA','method':'bm25'}).status_code == 200


def test_no_bug_and_filter_change_uses_cached_raw_issues(tmp_path, sample_snapshot):
    sample_snapshot['issues'] = [issue(1, labels=[{'name':'type: bug'}])]
    class GitHub:
        def fetch(self, *args):
            return sample_snapshot
        def close(self):
            pass
    with TestClient(create_app(Settings(data_dir=tmp_path), github=GitHub(), semantic=UnavailableSemantic())) as client:
        request = {'repository_url':'example/library', 'prepare_semantic':False}
        job = wait_job(client, client.post('/api/repositories/analyze', json=request).json()['job_id'])
        assert job['error']['code'] == 'no_bug_issues'
        request['extra_bug_labels'] = ['Type: Bug']
        job = wait_job(client, client.post('/api/repositories/analyze', json=request).json()['job_id'])
        assert job['status'] == 'completed' and job['bug_issue_count'] == 1
