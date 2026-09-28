import logging
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from .config import ROOT, Settings
from .domain import ServiceError, bug_labels, is_bug, query_text
from .github import GitHubClient
from .schemas import AnalyzeRequest, SearchRequest
from .search import SearchEngine
from .semantic import SemanticSearch
from .storage import Store

logger = logging.getLogger(__name__)


def create_app(settings=None, github=None, semantic=None):
    settings = settings or Settings()
    store = Store(settings.data_dir)
    github = github or GitHubClient(settings.github_token)
    semantic = semantic or SemanticSearch(settings)
    engine = SearchEngine(store, semantic)
    executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix='indexer')
    lock, active = threading.Lock(), {}

    @asynccontextmanager
    async def lifespan(app):
        store.interrupt_jobs()
        yield
        executor.shutdown(wait=True)
        github.close()

    app = FastAPI(title='GitHub Related Bug Issue Finder', version='0.1.0', lifespan=lifespan)
    app.state.store, app.state.engine = store, engine

    @app.exception_handler(ServiceError)
    async def handle_service_error(_, exc):
        return JSONResponse(status_code=exc.status, content={'error': exc.as_dict()})

    @app.get('/api/health')
    def health():
        return {'status': 'ok', 'model': settings.model_name}

    def run(job, request):
        def update(fields):
            job.update(fields)
            store.save_job(job)
        try:
            repository = request.repository_url
            snapshot = store.get(repository)
            cached = snapshot is not None and not request.refresh
            labels = bug_labels(request.extra_bug_labels)
            if not cached:
                update({'status': 'fetching'})
                snapshot = github.fetch(repository, settings.max_pages, update)
            snapshot = {**snapshot, 'bug_labels': labels}
            update({'status': 'indexing_bm25', 'cache_hit': cached})
            issues = [x for x in snapshot['issues'] if is_bug(x, labels)]
            snapshot['bug_issue_count'] = len(issues)
            # Persist only complete, successful collections, never a half-fetched corpus.
            snapshot = store.save(snapshot)
            update({k: snapshot[k] for k in ['collected_at', 'fetched_count', 'issue_count', 'bug_issue_count', 'partial', 'version']})
            if not issues:
                raise ServiceError('no_bug_issues', '수집한 범위에 Bug Issue가 없습니다. 추가 Bug 레이블을 지정하세요.', 409)
            engine.index(snapshot)
            available = ['bm25']
            if request.prepare_semantic:
                update({'status': 'indexing_semantic', 'available_methods': available})
                try:
                    semantic.prepare(snapshot, issues, update)
                    available += ['semantic', 'hybrid']
                except ServiceError as exc:
                    update({'semantic_error': exc.as_dict()})
            elif semantic.ready(snapshot):
                available += ['semantic', 'hybrid']
            update({'status': 'completed', 'available_methods': available})
        except ServiceError as exc:
            update({'status': 'failed', 'error': exc.as_dict()})
        except Exception:
            logger.exception('Analysis failed for %s', request.repository_url)
            update({'status': 'failed', 'error': {'code': 'analysis_failed', 'message': '분석 중 오류가 발생했습니다. 서버 로그를 확인하세요.'}})
        finally:
            with lock:
                active.pop(request.repository_url, None)

    @app.post('/api/repositories/analyze', status_code=202)
    def analyze(request: AnalyzeRequest):
        with lock:
            if request.repository_url in active:
                raise ServiceError('analysis_running', '이 저장소의 분석이 진행 중입니다.', 409,
                                   job_id=active[request.repository_url])
            job = {'id': uuid.uuid4().hex, 'repository': request.repository_url, 'status': 'queued',
                   'bug_labels': bug_labels(request.extra_bug_labels), 'available_methods': []}
            active[request.repository_url] = job['id']
            store.save_job(job)
            executor.submit(run, job, request)
        return {'job_id': job['id'], 'repository': request.repository_url}

    @app.get('/api/repositories/jobs/{job_id}')
    def get_job(job_id: str):
        job = store.job(job_id)
        if not job:
            raise ServiceError('job_not_found', '분석 작업을 찾을 수 없습니다.', 404)
        return job

    @app.post('/api/search')
    def search(request: SearchRequest):
        return engine.search(request.repository, query_text(request.problem, request.error, request.environment),
                             request.method, request.top_k)

    frontend = ROOT / 'frontend' / 'dist'
    if frontend.exists():
        app.mount('/', StaticFiles(directory=frontend, html=True), name='frontend')
    return app


app = create_app()
