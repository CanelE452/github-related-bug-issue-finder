# GitHub Related Bug Issue Finder
## Codex 구현용 프로젝트 정리 문서

> 목적: GitHub 저장소에서 사용자가 겪고 있는 문제를 입력하면, 기존의 관련 Bug Issue를 찾아주는 웹 애플리케이션을 구현한다.  
> 핵심 방향: 단순 오류 로그 검색기가 아니라, **자연어 문제 설명 + 오류 메시지 + 환경 정보**를 이용해 관련 Issue를 검색하는 서비스로 만든다.

---

# 1. 프로젝트 배경

GitHub Issue는 오류 전용 데이터가 아니다. 하나의 저장소에는 다음과 같은 다양한 Issue가 함께 존재할 수 있다.

- Bug
- Feature
- Task
- Documentation
- Question
- Duplicate
- Enhancement
- Build / Install problem
- Regression
- Test / CI failure
- Correctness problem
- 기타 프로젝트별 사용자 정의 Issue

따라서 이 프로젝트는 전체 Issue를 그대로 검색 대상으로 사용하는 것이 아니라, 가능하면 **Bug 관련 Issue를 우선 필터링**하여 관련 문제를 찾는 방향으로 설계한다.

GitHub Issue 안의 실제 오류 정보는 보통 별도의 표준 `error_message` 필드로 제공되는 것이 아니라, `title`, `body`, `labels`, Issue type 등의 데이터 안에 포함된다.

예:

```text
Title:
CUDA crashes after updating PyTorch

Body:
### Describe the bug
After upgrading PyTorch, training crashes...

### Environment
Ubuntu 24.04
Python 3.11
PyTorch 2.x

### Relevant log output
RuntimeError: CUDA out of memory
```

---

# 2. 최상위 목표

## 목표

사용자가 특정 GitHub 저장소에서 문제를 겪었을 때,

```text
자연어 문제 설명
+
오류 메시지 (선택)
+
환경 정보 (선택)
```

를 입력하면 기존 Issue 중 관련성이 높은 Bug Issue를 Top-K로 추천한다.

예:

```text
입력:
torch.compile 사용 후 이전 버전과 결과가 다르게 나옴

출력:
#15231 torch.compile regression after update
#14890 incorrect result with compiled model
#16022 silent correctness issue in torch.compile
```

또는:

```text
입력:
RuntimeError: CUDA out of memory
training crashes when batch size is large

출력:
#18231 CUDA OOM during training
#19120 memory allocation failure after model load
#17654 CUDA memory regression
```

---

# 3. 이 프로젝트가 하지 않는 것

초기 MVP에서는 다음을 핵심 기능으로 만들지 않는다.

- 로그 이상탐지
- 시스템 로그 시계열 분석
- Drain 기반 로그 템플릿 마이닝
- 범용 로그 parser
- 모든 프로그래밍 언어의 stack trace 구조 분석
- 자동 duplicate 확정 판정
- LLM 기반 자동 해결책 생성
- PR 분석
- 코드 리뷰
- 자동 Issue 생성

특히 **로그 parser는 현재 목적에 필수적이지 않다.**

이 프로젝트의 문제는:

```text
로그에서 이상 패턴을 찾는 것
```

이 아니라,

```text
사용자가 겪은 문제와 관련된 기존 GitHub Issue를 검색하는 것
```

이다.

---

# 4. GitHub Issue 데이터 구조에서 중요한 점

## 4.1 GitHub Issues API는 오류만 반환하지 않는다

GitHub Issues API는 저장소의 Issue를 반환한다.

예상 데이터:

```json
{
  "number": 1234,
  "title": "CUDA fallback crashes on CPU-only machine",
  "body": "When CUDA is unavailable...",
  "labels": [
    {"name": "bug"},
    {"name": "cuda"}
  ],
  "state": "open",
  "html_url": "https://github.com/...",
  "created_at": "...",
  "updated_at": "..."
}
```

주의:

- Pull Request도 Issues API 결과에 포함될 수 있다.
- `pull_request` 필드가 존재하는 항목은 제외해야 한다.
- 저장소에 따라 `type=Bug`를 사용할 수도 있고, `bug` label만 사용할 수도 있다.
- 일부 저장소는 Bug 분류를 일관되게 하지 않을 수 있다.

---

# 5. Bug Issue의 형태

Bug라고 해서 반드시 오류 메시지가 존재하는 것은 아니다.

가능한 유형:

## 5.1 Runtime Exception

```text
RuntimeError
KeyError
TypeError
NullPointerException
```

## 5.2 Hard Crash

```text
Segmentation fault
Process terminated
Application exits unexpectedly
```

## 5.3 Regression

```text
이전 버전에서는 정상
새 버전에서 실패
```

## 5.4 Incorrect Result

프로그램은 실행되지만 결과가 잘못된다.

```text
Expected: 0.95
Actual: 0.21
```

이 경우 명시적인 오류 메시지가 없을 수 있다.

## 5.5 Silent Correctness Bug

오류 메시지나 crash 없이 잘못된 결과를 반환한다.

## 5.6 Build / Install Failure

```text
pip install 실패
compiler error
dependency conflict
CUDA build error
```

## 5.7 Test / CI Failure

```text
unit test failure
GitHub Actions failure
CI regression
```

## 5.8 Component-specific Bug

예:

```text
CUDA
distributed
compiler
dataloader
backend
frontend
database
```

따라서 서비스 입력을 단순히 `error log` 하나로 제한하면 Bug Issue 전체를 제대로 다루지 못한다.

---

# 6. 사용자 입력 정의

초기 UI에서는 다음 3개 입력 영역을 권장한다.

```text
1. Problem description
2. Error message / stack trace (optional)
3. Environment information (optional)
```

예:

```text
Problem:
Model crashes when running on a CPU-only machine.

Error:
RuntimeError: CUDA device not found

Environment:
Ubuntu 24.04
Python 3.11
PyTorch 2.x
```

세 입력은 내부적으로 하나의 query text로 조합할 수 있다.

예:

```text
[PROBLEM]
Model crashes when running on a CPU-only machine.

[ERROR]
RuntimeError: CUDA device not found

[ENVIRONMENT]
Ubuntu 24.04 / Python 3.11 / PyTorch 2.x
```

---

# 7. 핵심 검색 방식

## 7.1 Baseline 1: BM25

BM25는 lexical retrieval 방식이다.

장점:

- 정확한 오류 코드
- 함수명
- 파일명
- exception 이름
- 라이브러리 이름
- 버전 문자열

처럼 **정확히 일치하는 토큰**을 찾는 데 강하다.

예:

```text
ERR_CONNECTION_RESET
RuntimeError
cudaMalloc
KeyError
```

---

## 7.2 Main Model: Sentence Embedding

Sentence Transformer 계열 모델을 사용해 Issue 내용을 embedding으로 변환한다.

예:

```text
"program crashes after network disconnect"
```

와

```text
"application terminates when connection is lost"
```

는 단어가 다르더라도 의미가 비슷하므로 semantic retrieval에서 가까워질 수 있다.

기본 입력:

```text
title + body
```

초기에는 별도 fine-tuning 없이 pretrained model을 사용한다.

---

# 8. 우선 검토할 핵심 방법: Hybrid Retrieval

현재 가장 목적에 직접적인 후보는:

```text
BM25
+
Sentence Embedding
```

이다.

이유:

```text
BM25
→ exact token matching에 강함

Sentence Embedding
→ 의미적 유사성에 강함
```

둘은 서로 다른 정보를 활용한다.

예:

```text
"ERR_CONNECTION_RESET 10054"
```

같은 query는 BM25가 유리할 수 있다.

반면:

```text
"program crashes after network disconnect"
```

와

```text
"application terminates when connection is lost"
```

같은 경우 embedding이 유리할 수 있다.

---

# 9. 후보 확장: CrossEncoder Reranking

MVP 이후 확장 후보.

구조:

```text
전체 Issue
   ↓
BM25 / Sentence Embedding
   ↓
Top 20 candidate retrieval
   ↓
CrossEncoder
   ↓
Top 5 reranking
```

CrossEncoder는 모든 Issue에 적용하지 않고, 1차 검색 결과에만 적용한다.

목적:

- Top-K 후보의 순위 개선
- 의미적으로 비슷하지만 실제 관련성이 낮은 Issue 제거

MVP에서는 없어도 된다.

---

# 10. 로그 파싱에 대한 현재 판단

## 10.1 왜 처음 고려했는가

Issue의 body에는 다음과 같은 변동 정보가 포함될 수 있다.

```text
/home/minjae/project/train.py
C:\Users\john\Desktop\project\
PID=18231
2026-09-22 14:31:12
UUID
IP address
temporary path
line number
```

같은 오류라도 사용자 환경에 따라 값이 달라질 수 있다.

---

## 10.2 왜 현재는 parser를 넣지 않는가

우리의 최상위 목적은:

```text
duplicate / related issue retrieval
```

이다.

Drain 등의 로그 parser는:

```text
raw log
→ template
→ variable
```

구조를 찾는 것이 핵심이다.

이는 로그 이상탐지나 로그 분석에는 적합하지만 현재 프로젝트에는 목적 대비 복잡도가 높다.

따라서 초기 설계에서는 제외한다.

---

# 11. Noise Normalization은 조건부 후보

Parser 대신 간단한 normalization은 필요할 경우 사용할 수 있다.

예:

```text
/home/minjae/project/train.py
→ <PATH>/train.py

C:\Users\john\Desktop\test\main.py
→ <PATH>/main.py

2026-09-22 14:32:51
→ <TIMESTAMP>

PID=18321
→ PID=<NUM>

random UUID
→ <UUID>
```

하지만 이것도 처음부터 적용하지 않는다.

먼저 Raw baseline을 만든 후, 검색 실패 원인을 분석한다.

실패 원인의 상당 부분이:

- 사용자 경로
- timestamp
- UUID
- PID
- 환경별 random string

때문이라고 확인될 경우에만 normalization을 추가한다.

---

# 12. 비교 실험

최소한 다음을 비교한다.

## Experiment A — BM25

```text
title + body
→ BM25
```

## Experiment B — Sentence Transformer

```text
title + body
→ embedding
→ cosine similarity
```

## Experiment C — Hybrid

```text
BM25 score
+
Embedding similarity
```

## Experiment D — Reranker

조건부 확장:

```text
Hybrid retrieval
→ Top 20
→ CrossEncoder
→ Top 5
```

## Experiment E — Normalization

실패 분석 결과 필요성이 확인된 경우에만:

```text
Raw
vs
Normalized
```

을 비교한다.

---

# 13. 평가 데이터

가능하면 실제 GitHub duplicate 관계를 이용한다.

예:

```text
Duplicate Issue     Original Issue
#335              → #187
#401              → #212
#512              → #104
```

query:

```text
#335 내용
```

정답:

```text
#187
```

모델이 #187을 몇 번째 순위에 반환하는지 평가한다.

---

# 14. 평가 지표

## Recall@1

정답 Issue가 검색 결과 1위에 존재하는 비율.

## Recall@5

정답 Issue가 Top-5 안에 존재하는 비율.

서비스와 가장 직접적으로 연결되는 주요 지표 후보.

## MRR

Mean Reciprocal Rank.

정답 Issue가 더 높은 순위에 있을수록 높은 점수를 준다.

---

# 15. 반드시 비교해야 할 조건

실험 비교 시 다음 조건을 동일하게 유지한다.

- 동일 repository
- 동일 Issue subset
- 동일 train/evaluation split
- 동일 duplicate pair
- 동일 query
- 동일 candidate corpus
- 동일 Top-K
- 동일 filtering rule

다른 조건의 결과를 직접적인 성능 개선으로 해석하지 않는다.

---

# 16. MVP 기능

MVP에서는 기능을 최소화한다.

## 기능 1 — Repository 입력

```text
https://github.com/owner/repository
```

버튼:

```text
[Analyze Repository]
```

동작:

1. Repository 정보 확인
2. Issues API 호출
3. Pull Request 제거
4. Bug Issue 필터링
5. Issue 저장
6. 검색 index 생성

---

## 기능 2 — Bug Issue 검색

사용자 입력:

```text
Problem description
Error message (optional)
Environment (optional)
```

버튼:

```text
[Find Related Issues]
```

출력:

```text
#1421 CUDA fallback fails on CPU-only systems
Relevance: 0.89
Labels: bug, cuda

#887 Device detection failure without CUDA
Relevance: 0.82
Labels: bug, backend
```

주의:

Embedding cosine similarity를:

```text
89% duplicate probability
```

라고 표현하면 안 된다.

대신:

```text
similarity
relevance
관련도
```

등으로 표시한다.

---

## 기능 3 — GitHub 원문 이동

각 결과에서:

```text
[Open on GitHub]
```

버튼 제공.

---

# 17. 확장 기능

MVP 이후 시간과 데이터가 충분한 경우에만 추가.

- CrossEncoder reranking
- BM25 + embedding hybrid tuning
- Issue label recommendation
- 검색 결과 요약
- Issue 작성 도중 실시간 검색
- GitHub OAuth
- 검색 history
- Repository별 검색 통계
- 검색 실패 사례 분석
- Noise normalization
- Fine-tuning

---

# 18. 추천 기술 스택

## Frontend

후보:

```text
React
or
Next.js
```

초기 프로젝트에서는 React만으로 충분하다.

---

## Backend

```text
FastAPI
```

역할:

- GitHub API 요청
- Issue filtering
- 검색 API
- ML model inference
- index management

---

## Search / ML

### Lexical

```text
BM25
```

Python 후보:

```text
rank-bm25
```

또는 Elasticsearch/OpenSearch는 확장 시 고려.

### Semantic

```text
sentence-transformers
```

### Optional reranking

```text
CrossEncoder
```

---

## Storage

초기:

```text
SQLite
```

또는 단순 JSON/Parquet cache.

Issue 수가 많지 않다면 별도의 vector database는 처음부터 필요하지 않다.

확장 시:

```text
FAISS
```

등을 고려할 수 있다.

---

# 19. 제안 아키텍처

```text
┌────────────────────────────┐
│          Frontend          │
│ React                      │
├────────────────────────────┤
│ Repository URL input       │
│ Problem input              │
│ Error input                │
│ Environment input          │
│ Search result list         │
└──────────────┬─────────────┘
               │
               │ HTTP
               ↓
┌────────────────────────────┐
│          FastAPI           │
├────────────────────────────┤
│ GitHub Client              │
│ Issue Filter               │
│ Search Service             │
│ Model Service              │
│ Index Service              │
└───────┬────────────┬───────┘
        │            │
        ↓            ↓
 GitHub REST API    Search
                    ├─ BM25
                    ├─ Embedding
                    └─ Hybrid
```

---

# 20. 추천 Backend API

## Repository 분석

```http
POST /api/repositories/analyze
```

Request:

```json
{
  "repository_url": "https://github.com/pytorch/pytorch"
}
```

Response 예시:

```json
{
  "repository": "pytorch/pytorch",
  "issue_count": 1200,
  "bug_issue_count": 580,
  "indexed": true
}
```

---

## 관련 Issue 검색

```http
POST /api/search
```

Request:

```json
{
  "repository": "pytorch/pytorch",
  "problem": "model crashes on CPU-only machine",
  "error": "RuntimeError: CUDA device not found",
  "environment": "Ubuntu 24.04, Python 3.11",
  "top_k": 5
}
```

Response:

```json
{
  "results": [
    {
      "number": 1421,
      "title": "CUDA fallback fails on CPU-only systems",
      "url": "https://github.com/...",
      "labels": ["bug", "cuda"],
      "score": 0.89
    }
  ]
}
```

---

# 21. 내부 데이터 모델

Issue record 예시:

```json
{
  "repository": "owner/repo",
  "number": 123,
  "title": "...",
  "body": "...",
  "state": "open",
  "labels": ["bug", "cuda"],
  "issue_type": "Bug",
  "html_url": "...",
  "created_at": "...",
  "updated_at": "...",
  "is_pull_request": false
}
```

검색용 text:

```text
title + "\n\n" + body
```

추후 필요 시:

```text
title
body
labels
environment
error block
```

을 따로 저장할 수 있다.

---

# 22. Bug Issue Filtering

순서 후보:

```text
1. pull_request 필드가 있으면 제외

2. issue type == Bug 이면 포함

3. label에 bug가 있으면 포함

4. repository별 custom bug label을 설정 가능하게 확장
```

주의:

모든 repository가 동일한 Issue type / label 규칙을 사용하지 않는다.

따라서 필터는 repository별로 동작을 확인해야 한다.

---

# 23. 프로젝트 개발 순서

## Step 1 — GitHub API 연결

구현:

- repository URL parsing
- Issue list fetch
- pagination
- Pull Request filtering
- basic cache

완료 조건:

```text
지정 repository에서 Issue 데이터를 안정적으로 수집할 수 있음
```

---

## Step 2 — Bug filtering

구현:

```text
type == Bug
label == bug
```

우선 적용.

repository별 분류 품질 확인.

---

## Step 3 — BM25 baseline

구현:

```text
query
→ BM25
→ Top-K
```

이 단계에서 웹 UI까지 연결해도 된다.

---

## Step 4 — Sentence Transformer

구현:

```text
Issue text
→ embedding cache

query
→ query embedding
→ cosine similarity
→ Top-K
```

BM25와 동일 query로 비교 가능하게 만든다.

---

## Step 5 — Hybrid Retrieval

후보 방식:

```text
normalized BM25 score
+
normalized embedding score
```

가중치:

```text
score = alpha * lexical + (1-alpha) * semantic
```

주의:

alpha 값은 근거 없이 최종값으로 고정하지 않는다.

개발 단계에서는 여러 값으로 비교하되 evaluation set에서 선택한다.

---

## Step 6 — Evaluation

실제 duplicate pair 확보.

평가:

```text
Recall@1
Recall@5
MRR
```

BM25 / Embedding / Hybrid 비교.

---

## Step 7 — 실패 사례 분석

잘못 검색된 query를 샘플링해 다음 원인을 분류한다.

예:

```text
exact error token mismatch
semantic mismatch
too little description
very long stack trace
version-specific problem
repository-specific terminology
path/timestamp noise
incorrect ground truth
```

이 결과가 다음 기능 추가 여부를 결정한다.

---

# 24. Phase 2 게이트

## Gate A — 데이터 품질

확인할 것:

- Bug Issue가 충분한가?
- duplicate 관계가 충분한가?
- Issue body가 비어 있지 않은가?
- 한 repository에 지나치게 편향되어 있지 않은가?

---

## Gate B — Baseline 필요성

BM25 성능이 이미 매우 높다면:

```text
embedding / hybrid 추가 가치
```

가 작은지 확인한다.

반대로 embedding만 좋아도 lexical 정보가 필요한 query가 있는지 본다.

---

## Gate C — Parser 필요성

다음이 실제 실패 원인으로 충분히 나타나는 경우에만 검토:

- personal path
- timestamp
- UUID
- PID
- random environment string
- long stack trace noise

그렇지 않으면 parser / normalization을 추가하지 않는다.

---

# 25. 현재 판정

| 후보 | 판정 | 이유 |
|---|---|---|
| BM25 | 유지 | 필수 lexical baseline |
| Sentence Transformer | 유지 | semantic retrieval 핵심 |
| BM25 + Embedding Hybrid | 우선 유지 | exact token + semantic 정보 결합 |
| CrossEncoder | 조건부 유지 | MVP 이후 reranking |
| Noise Normalization | 보류 | 실제 실패 원인 확인 후 판단 |
| Drain / Log Parser | 기각(MVP) | 최상위 목적과 직접성이 낮음 |
| Fine-tuning | 보류 | pretrained baseline 확인 후 필요성 판단 |
| LLM Summary | 보류 | 검색 핵심 기능 아님 |

---

# 26. 프로젝트 발표 스토리

## 1. 문제

대형 GitHub repository에는 많은 Issue가 존재하며, 사용자가 자신과 관련된 기존 Bug Issue를 찾기 어렵다.

## 2. 기존 접근

Keyword 검색은 정확한 오류 코드나 함수명에는 강하지만 표현이 달라지면 놓칠 수 있다.

## 3. 추가 문제

Bug Issue는 단순 오류 메시지만 포함하지 않는다.

다음이 섞여 있다.

```text
자연어 설명
오류 메시지
환경 정보
stack trace
버전
component 정보
```

## 4. 제안

Lexical retrieval과 semantic retrieval을 함께 비교하고 결합한다.

```text
BM25
+
Sentence Embedding
```

## 5. 평가

실제 duplicate Issue pair를 이용해:

```text
Recall@1
Recall@5
MRR
```

을 평가한다.

## 6. 최종 서비스

사용자가 문제를 입력하면 관련 Bug Issue Top-K를 추천하는 웹 애플리케이션을 제공한다.

---

# 27. 남은 확인 사항

아직 확정되지 않은 내용:

1. 어떤 GitHub repository를 실험 대상으로 사용할지
2. Bug Issue 수
3. 실제 duplicate pair 수
4. repository별 Issue type / label 사용 방식
5. 사용할 Sentence Transformer 모델
6. hybrid score 결합 방법
7. CrossEncoder 사용 여부
8. normalization 필요성
9. 평가용 repository를 하나로 할지 여러 개로 할지

이 항목들은 구현 전에 데이터 확인이 필요하다.

---

# 28. Codex에 줄 핵심 구현 원칙

1. 처음부터 복잡한 구조를 만들지 않는다.
2. 먼저 GitHub API → Bug Issue 수집 → BM25 baseline을 완성한다.
3. 그다음 pretrained Sentence Transformer를 추가한다.
4. 동일 데이터에서 BM25와 embedding을 비교한다.
5. 이후 hybrid retrieval을 구현한다.
6. parser, normalization, reranker는 필요성이 확인되기 전까지 추가하지 않는다.
7. 모든 실험 결과는 동일한 query/corpus/ground truth에서 비교한다.
8. cosine similarity를 duplicate probability로 표현하지 않는다.
9. GitHub Issues API에서 Pull Request를 반드시 분리한다.
10. repository마다 Bug label/type 규칙이 다를 수 있으므로 하드코딩하지 않는다.
11. 각 단계마다 동작 확인 가능한 작은 테스트를 추가한다.
12. README에 실행 방법, API 설정, 데이터 흐름, 모델 구조, 평가 방법을 기록한다.

---

# 29. 추천 초기 디렉터리 구조

```text
github-related-issue-finder/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api/
│  │  │  ├─ repositories.py
│  │  │  └─ search.py
│  │  ├─ services/
│  │  │  ├─ github_service.py
│  │  │  ├─ issue_filter.py
│  │  │  ├─ bm25_service.py
│  │  │  ├─ embedding_service.py
│  │  │  └─ hybrid_search.py
│  │  ├─ models/
│  │  │  └─ schemas.py
│  │  └─ storage/
│  │     └─ repository.py
│  ├─ tests/
│  └─ requirements.txt
│
├─ frontend/
│  ├─ src/
│  │  ├─ components/
│  │  ├─ pages/
│  │  └─ api/
│  └─ package.json
│
├─ evaluation/
│  ├─ build_duplicate_pairs.py
│  ├─ evaluate_bm25.py
│  ├─ evaluate_embedding.py
│  └─ evaluate_hybrid.py
│
├─ data/
│  └─ .gitkeep
│
├─ docs/
│  ├─ architecture.md
│  └─ evaluation.md
│
├─ .env.example
├─ .gitignore
├─ README.md
└─ PROJECT_SPEC.md
```

---

# 30. 첫 Codex 작업 범위

첫 작업에서는 아래까지만 구현한다.

```text
[1] repository URL 입력
[2] GitHub REST API로 Issue 가져오기
[3] Pull Request 제외
[4] Bug Issue 후보 필터링
[5] 로컬 저장/cache
[6] BM25 검색
[7] FastAPI search endpoint
[8] 최소 테스트
[9] README 실행 방법
```

아직 하지 않는다:

```text
Sentence Transformer
Hybrid
CrossEncoder
Normalization
Frontend 고도화
Fine-tuning
```

첫 단계가 정상 동작한 뒤 다음 단계로 넘어간다.

---

# 31. 최종 MVP 정의

MVP 완료 조건:

```text
1. 사용자가 GitHub repository URL을 입력할 수 있다.
2. 서버가 해당 repository의 Issue를 가져온다.
3. PR을 제거한다.
4. Bug Issue를 필터링한다.
5. 검색 index를 생성한다.
6. 사용자가 문제 설명을 입력할 수 있다.
7. BM25 또는 semantic retrieval로 관련 Issue Top-5를 반환한다.
8. 결과에서 GitHub 원문으로 이동할 수 있다.
9. 최소한 BM25와 semantic retrieval의 성능을 비교할 수 있다.
10. 평가 결과가 Recall@1 / Recall@5 / MRR로 저장된다.
```

---

# 32. 프로젝트 한 문장 정의

> **GitHub repository의 Bug Issue를 대상으로, 사용자의 자연어 문제 설명과 선택적 오류·환경 정보를 이용해 관련 기존 Issue를 검색하는 AI 기반 웹 애플리케이션. Lexical BM25와 semantic embedding을 비교하고 결합하여 실제 duplicate Issue retrieval 성능을 평가한다.**
