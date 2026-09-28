from datetime import datetime, timezone

import httpx

from .domain import ServiceError


class GitHubClient:
    def __init__(self, token: str = '', transport=None):
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'RelatedBugIssueFinder',
                   'X-GitHub-Api-Version': '2026-03-10'}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        self.client = httpx.Client(base_url='https://api.github.com', headers=headers, timeout=30, transport=transport)

    def close(self):
        self.client.close()

    def get(self, path: str, **params):
        try:
            response = self.client.get(path, params=params)
        except httpx.RequestError as exc:
            raise ServiceError('github_network', 'GitHub에 연결하지 못했습니다. 잠시 후 다시 시도하세요.', 502) from exc
        if response.status_code in (403, 429):
            limited = response.status_code == 429 or response.headers.get('x-ratelimit-remaining') == '0' or 'rate limit' in response.text.lower() or 'retry-after' in response.headers
            raise ServiceError('github_rate_limit' if limited else 'github_forbidden',
                               'GitHub API 호출 제한에 도달했습니다.' if limited else 'GitHub 접근이 거부되었습니다.', 429 if limited else 403,
                               reset_at=response.headers.get('x-ratelimit-reset'), retry_after=response.headers.get('retry-after'))
        if response.status_code == 404:
            raise ServiceError('repository_not_found', '공개 저장소를 찾을 수 없습니다. URL을 확인하세요.', 404)
        if response.status_code == 401:
            raise ServiceError('github_token_invalid', '서버의 GitHub 토큰을 확인하세요.', 401)
        if response.is_redirect:
            raise ServiceError('repository_moved', '저장소 주소가 변경되었습니다. GitHub의 현재 주소를 입력하세요.', 400)
        if response.is_error:
            raise ServiceError('github_error', f'GitHub API 오류 ({response.status_code})', 502)
        return response

    def fetch(self, repository: str, max_pages: int, progress=None) -> dict:
        info = self.get(f'/repos/{repository}').json()
        if info.get('private'):
            raise ServiceError('private_repository', 'MVP는 공개 저장소만 지원합니다.', 400)
        items, fetched, partial = [], 0, False
        path = f'/repos/{repository}/issues'
        params = {'state': 'all', 'sort': 'created', 'direction': 'desc', 'per_page': 100}
        for page in range(1, max_pages + 1):
            response = self.get(path, **params)
            batch = response.json()
            fetched += len(batch)
            items.extend(x for x in batch if 'pull_request' not in x)
            has_next = 'next' in response.links
            partial = has_next and page == max_pages
            if progress:
                progress({'page': page, 'fetched_count': fetched, 'issue_count': len(items)})
            if not has_next:
                break
            next_url = httpx.URL(response.links['next']['url'])
            allowed_paths = {f'/repos/{repository}/issues', f"/repositories/{info.get('id')}/issues"}
            if next_url.scheme != 'https' or next_url.host != 'api.github.com' or next_url.path not in allowed_paths:
                raise ServiceError('github_pagination_invalid', 'GitHub의 다음 페이지 주소를 확인할 수 없습니다.', 502)
            path, params = next_url.path, dict(next_url.params)
        # Deduplicate if upstream changes while paging; retain deterministic newest copy.
        items = list({x['number']: x for x in reversed(items)}.values())
        return {'repository': repository, 'issues': items, 'fetched_count': fetched,
                'issue_count': len(items), 'partial': partial, 'pages': page,
                'collected_at': datetime.now(timezone.utc).isoformat()}
