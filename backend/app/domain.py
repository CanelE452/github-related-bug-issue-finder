import re
from urllib.parse import urlparse


class ServiceError(Exception):
    def __init__(self, code: str, message: str, status: int = 400, **context):
        super().__init__(message)
        self.code, self.message, self.status, self.context = code, message, status, context

    def as_dict(self):
        return {'code': self.code, 'message': self.message, **self.context}


def repository_name(value: str) -> str:
    value = value.strip()
    if '://' in value:
        url = urlparse(value)
        if url.scheme != 'https' or url.netloc.lower() != 'github.com' or url.query or url.fragment:
            raise ValueError('https://github.com/owner/repository 형식의 공개 저장소 URL을 입력하세요.')
        value = url.path.strip('/')
    value = value.removesuffix('.git')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+', value) or value.split('/')[-1] in {'.', '..'}:
        raise ValueError('올바른 owner/repository 또는 GitHub 저장소 URL을 입력하세요.')
    return value.lower()


def bug_labels(extra: list[str]) -> list[str]:
    return sorted({'bug', *(x.strip().casefold() for x in extra if x.strip())})


def is_bug(issue: dict, labels: list[str]) -> bool:
    if 'pull_request' in issue:
        return False
    kind = issue.get('type') or issue.get('issue_type') or {}
    kind = kind.get('name', '') if isinstance(kind, dict) else kind
    names = [x.get('name', '') if isinstance(x, dict) else x for x in issue.get('labels', [])]
    return str(kind).casefold() == 'bug' or bool({x.casefold() for x in names} & set(labels))


def issue_text(issue: dict) -> str:
    return issue['title'] + '\n\n' + (issue.get('body') or '')


def query_text(problem: str, error: str = '', environment: str = '') -> str:
    return '\n\n'.join(f'[{name}]\n{text.strip()}' for name, text in
                       [('PROBLEM', problem), ('ERROR', error), ('ENVIRONMENT', environment)] if text.strip())
