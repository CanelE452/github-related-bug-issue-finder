# Issue Finder

한국어·영어 문제 설명과 선택적인 오류 메시지·환경 정보로 공개 GitHub 저장소의 관련 Bug Issue를 찾는 로컬 웹 앱입니다.

**React + FastAPI + SQLite + BM25 + multilingual-e5-small + RRF**. 로그 파싱·정규화·자동 중복 확정·해결책 생성은 포함하지 않습니다.

## 빠른 실행 — Windows PowerShell

Python 3.11+와 Node.js 20.19+가 필요합니다. 명령은 프로젝트 루트에서 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt

# CPU 기반 다국어 검색 (BM25만 사용할 경우 생략)
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r backend\requirements-semantic.txt
.\.venv\Scripts\python.exe -m scripts.prepare_model

Copy-Item .env.example .env
npm.cmd --prefix frontend install
npm.cmd --prefix frontend run build
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

- 앱: <http://127.0.0.1:8000>
- API 문서: <http://127.0.0.1:8000/docs>
- 상태 확인: <http://127.0.0.1:8000/api/health>

기존 `.env`가 있으면 덮어쓰지 말고 필요한 설정만 수정하세요. 서버는 **단일 프로세스**로 실행합니다. 다중 uvicorn worker는 지원하지 않습니다.

Linux/macOS에서는 `.venv/bin/python`, `npm`을 사용합니다. 실제 검증 환경의 Python 패키지는 `backend/requirements-lock.txt`, npm 패키지는 `frontend/package-lock.json`에 기록합니다. CPU PyTorch 설치 후 lock 파일로 정확한 환경을 재현할 수 있습니다.

## 사용 순서

1. 공개 저장소 URL을 입력합니다. 예: `https://github.com/huggingface/transformers`.
2. 필요하면 **분석 설정**에서 추가 Bug 레이블을 입력합니다. 예: `type: bug`.
3. **저장소 분석**을 누릅니다. 첫 다국어 분석에서는 모델 다운로드와 CPU 인덱싱에 시간이 걸립니다.
4. 문제 설명을 한국어 또는 영어로 입력합니다. 오류 메시지와 환경은 선택 사항입니다.
5. Hybrid, 의미 기반, 키워드 검색 중 하나를 선택합니다. 결과에서 GitHub 원문을 확인합니다.

BM25만 먼저 실행하려면 다국어 의존성을 설치하지 않고 **다국어 검색 준비**를 해제한 뒤 **키워드 · BM25**를 선택하세요. BM25만으로 한국어 설명과 영어 문서 사이의 의미 일치를 기대하지 않습니다.

## GitHub 설정과 수집 범위

`.env`의 `GITHUB_TOKEN`에 선택적으로 토큰을 설정할 수 있습니다. 토큰은 서버에서만 읽고 브라우저에 전달하지 않습니다. 비공개 저장소는 지원하지 않습니다.

- 최신 생성순 **최대 20페이지 × 100개 응답 항목**을 가져옵니다. 이 한도에는 PR도 포함됩니다.
- GitHub가 제공하는 `Link: rel=next`를 따라 커서 페이지네이션을 처리합니다. 대형 저장소에서 임의의 `page=20` 요청은 거부될 수 있습니다.
- PR을 제외하고 Issue의 `type.name == Bug` 또는 설정된 레이블의 대소문자 무시 일치로 필터링합니다. 기본 레이블은 `bug`입니다.
- 댓글은 검색 본문에 포함하지 않습니다. 일반 검색에는 제목과 본문만 사용합니다.
- 수집 완료 후 하나의 SQLite 트랜잭션으로 교체합니다. 네트워크 실패·호출 제한 시 기존 스냅샷이 유지됩니다.
- 기본은 캐시 재사용입니다. 레이블만 바꾸면 원본 캐시에 새 필터를 적용합니다. **GitHub에서 새로 수집**을 선택해야 원격 데이터를 갱신합니다.
- Bug가 0개이면 안내를 표시합니다. 전체 Issue로 자동 확장하지 않습니다. 수집 건수와 부분 수집 표시를 확인하세요.

## 검색 방식

| 방식 | 동작 |
|---|---|
| BM25 | `rank-bm25` Okapi, k1=1.5, b=0.75. 작은 corpus에서도 음수 IDF가 순위를 뒤집지 않도록 positive Robertson IDF 사용 |
| Semantic | `intfloat/multilingual-e5-small`, query/passage 접두사, L2 정규화 벡터의 코사인 유사도 |
| Hybrid | 각 방식 Top-50의 `1 / (60 + rank)` 합산. 같은 가중치, 번호로 동점 순서 고정 |

원문 경로, 숫자, 버전, 오류 코드는 삭제하지 않습니다. BM25는 기술 토큰 전체와 구성 단어를 보존하며, 일치 토큰이 없는 문서는 후보에서 제외합니다.

임베딩은 질의와 문서를 각각 448토큰, 중첩 64토큰으로 분할합니다. 모든 구간 쌍 중 가장 높은 코사인 유사도를 Issue 점수로 사용합니다. 장문 문서가 유리해질 수 있으므로 실패 분석 시 길이 편향도 확인합니다. 점수는 **중복 확률이 아니며 방식 간 직접 비교할 수 없습니다**.

모델은 첫 실행에서 Hugging Face commit SHA를 고정하여 `data/embeddings`에 기록합니다. 텍스트 해시·모델 버전·분할 설정이 캐시 키에 포함됩니다. 다른 모델 버전을 사용하려면 `.env`의 `ISSUE_FINDER_MODEL_REVISION`을 바꾸고 재분석합니다. 추론은 로컬 CPU에서 수행하며 입력을 외부 LLM API로 보내지 않습니다.

## API

```http
POST /api/repositories/analyze
{"repository_url":"https://github.com/huggingface/transformers","extra_bug_labels":["bug"],"refresh":false,"prepare_semantic":true}

202 {"job_id":"…","repository":"huggingface/transformers"}
```

`GET /api/repositories/jobs/{job_id}`로 상태를 조회합니다. `queued → fetching → indexing_bm25 → indexing_semantic → completed/failed` 순서이며 캐시 사용 시 수집 단계가 생략됩니다. 다국어 준비 실패는 `semantic_error`로 표시하고 BM25는 유지합니다. 서버 재시작 시 미완료 작업은 `interrupted`로 표시합니다.

```http
POST /api/search
{"repository":"huggingface/transformers","problem":"모델 로딩 중 GPU 메모리가 부족해요","error":"CUDA out of memory","environment":"Python 3.12","method":"hybrid","top_k":5}
```

`method`: `bm25 | semantic | hybrid`. `problem`은 필수, `top_k`는 1~20. 결과에 검색 방식, 점수 유형, 스냅샷 버전, 수집 시각, 부분 수집 여부가 포함됩니다. 준비되지 않은 인덱스는 409, 입력 오류는 422를 반환합니다. 작업 실패 시 job의 구조화된 error를 확인합니다.

## 개발 및 테스트

```powershell
.\.venv\Scripts\python.exe -m pytest -q
npm.cmd --prefix frontend run build

# 개발 시 별도 터미널 두 개
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
npm.cmd --prefix frontend run dev
```

개발 UI는 <http://127.0.0.1:5173>, `/api`는 Vite 프록시로 FastAPI에 연결됩니다. 외부 CDN 없이도 시스템 글꼴로 사용할 수 있으며, 웹 글꼴 로딩은 선택적인 표시 개선입니다.

테스트에는 외부 네트워크 없이 실행하는 API·저장소·검색·분할·평가 검증이 포함됩니다. 테스트의 가짜 임베딩 모델은 캐시와 순위 결합만 검증하며 실제 다국어 품질 검증으로 간주하지 않습니다.

## 평가

```powershell
# 두 저장소 조사 및 실제 데이터 캐시
.\.venv\Scripts\python.exe -m evaluation.survey
# 조사 결과의 selection 저장소로 실행
.\.venv\Scripts\python.exe -m evaluation.evaluate --repository huggingface/transformers --split validation --output evaluation/output/validation
.\.venv\Scripts\python.exe -m evaluation.evaluate --repository huggingface/transformers --split test --output evaluation/output/test
```

네트워크/API 제한을 줄이려면 `--reuse-cache`를 사용합니다. `--pages 1` 같은 작은 범위도 가능하지만 기본 서비스·평가 범위와 다름을 보고해야 합니다. BM25만 실행할 때는 `--methods bm25`를 붙입니다.

상세 데이터 계약과 한계는 [평가 문서](docs/evaluation.md), 구조는 [아키텍처](docs/architecture.md), 실제 실행 결과는 [검증 보고서](docs/validation.md)를 참고하세요.

## 파일과 범위

- `backend/app`: GitHub 수집, SQLite, 검색, 비동기 작업 상태 API
- `frontend/src`: 한국어 웹 UI
- `evaluation`: 중복 관계 조사, 그룹 분리, 평가 JSON·CSV
- `data`: 로컬 원본 스냅샷·모델·임베딩 캐시 (Git 제외)
- `docs`: 구조·평가·검증 기록

공개 서비스용 인증, 사용자별 저장소 격리, 작업 큐 서버, 자동 주기 동기화, 배포는 이번 로컬 MVP의 범위에 포함하지 않습니다.
