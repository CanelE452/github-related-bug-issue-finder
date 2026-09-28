import pytest


def issue(number, title='CUDA GPU memory failure', body='RuntimeError: CUDA out of memory', labels=None, **extra):
    return {'number': number, 'title': title, 'body': body, 'labels': labels if labels is not None else [{'name': 'bug'}],
            'state': 'open', 'created_at': '2026-01-01T00:00:00Z', 'updated_at': '2026-01-01T00:00:00Z', **extra}


@pytest.fixture
def sample_snapshot():
    return {'repository': 'example/library', 'collected_at': '2026-01-02T00:00:00Z', 'fetched_count': 4,
            'issue_count': 4, 'partial': False, 'bug_labels': ['bug'], 'bug_issue_count': 3,
            'issues': [issue(1), issue(2, 'Connection reset', 'ERR_CONNECTION_RESET 10054 network disconnect'),
                       issue(3, 'Documentation request', 'CUDA tutorial', labels=[{'name': 'documentation'}]),
                       issue(4, 'Wrong numerical output', None)]}
