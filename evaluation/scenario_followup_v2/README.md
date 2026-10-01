# Follow-up v2

부모 `scenario_pilot_v1/run_001`은 읽기 전용입니다. 운영 검색은 바꾸지 않습니다. 사용자 요청에 따라 새 브랜치 없이 **main**에 게시합니다.

## 실행

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_followup audit --parent-run data/scenario_pilot_v1/run_001 --out data/scenario_followup_v2/batch_001
.venv/Scripts/python.exe -m evaluation.scenario_followup prepare-review --batch data/scenario_followup_v2/batch_001
.venv/Scripts/python.exe -m evaluation.scenario_followup diagnose --batch data/scenario_followup_v2/batch_001
.venv/Scripts/python.exe -m evaluation.scenario_followup reproduce --batch data/scenario_followup_v2/batch_001
.venv/Scripts/python.exe -m evaluation.scenario_followup resume --batch data/scenario_followup_v2/batch_001 --query-reviews data/scenario_followup_v2/batch_001/review/query_reviews.csv --reviews data/scenario_followup_v2/batch_001/review/human_reviews.csv
.venv/Scripts/python.exe -m evaluation.scenario_followup verify-publication --batch data/scenario_followup_v2/batch_001
```

CSV 양식의 미작성 항목은 미판정입니다. `review/review.html`은 Chrome에서 직접 열거나 다음 서버에서 사용할 수 있습니다. 실제 38질의·429쌍 CSV 다운로드와 CLI 재입력을 확인했습니다. Codex 안쪽 브라우저에서는 다운로드가 실제 파일로 저장되지 않는 경우가 확인되어 Chrome을 권장합니다. GitHub에서 HTML을 실행하는 배포는 추가하지 않습니다.

```powershell
.venv/Scripts/python.exe -m http.server 8787 --bind 127.0.0.1 --directory data/scenario_followup_v2/batch_001/review
```

검토자 식별명·사전 노출 입력 → 질문/문서 답변 저장 → CSV 두 개 다운로드 → `resume`에 실제 경로 지정. 저장하지 않은 입력은 반영되지 않습니다. 저장 시각은 실제 버튼 클릭 시각입니다. 원문 텍스트는 `textContent`로 표시하고 외부 스크립트는 허용하지 않습니다. CSV의 수식 시작 문자는 export에서만 apostrophe로 보호하고 importer는 자유 입력 필드의 보호를 해제합니다. 원래 질의/문서 내용 해시는 바꾸지 않습니다. 검토자 신원을 인증하는 시스템은 아닙니다.

## 구현 대응

| 기능 | 파일 |
|---|---|
| 보존 감사·입력별 append-only 채점 round·CLI | `evaluation/scenario_followup.py` |
| 공통 풀·부분 판정·불일치·동일 분모 채점 | `evaluation/followup_scoring.py` |
| 정적 HTML과 CSV 저장 | `evaluation/followup_review.py`, `review.js`, `review.css` |
| 고정 캐시 재현·기계적 진단·단일 변경/행동 실행 | `evaluation/followup_retrieval.py` |
| 동적 보고·원자료·PNG·링크/해시 검사 | `evaluation/followup_report.py` |

## 사람 근거가 있을 때만 실행

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_followup run-approved --batch data/scenario_followup_v2/batch_001 --experiment K1 --approval-file PATH_TO_ACTUAL_HUMAN_APPROVAL.json
```

`--experiment`는 K1/R1/E1/E2/E3 중 하나입니다. 모든 승인에는 실제 `reviewer_type=human`, `reviewer_id`, 시간대 있는 `reviewed_at`, `reason`이 필요합니다. AI가 생성한 가짜 승인을 넣으면 안 됩니다. 실행 전 기준선 재현이 통과해야 합니다. 실제 승인 원본을 내용 해시별로 보존합니다. 실행 후 새 문서는 추가 검토 대상으로 남습니다. 실행 가능한 도구와 사람 검토를 통과한 실험 결과는 구분합니다.

- K1/R1: JSON의 `query_id`, `query_sha256`, `scope`, `direct_doc_id`, `competitor_doc_id`가 현재 사람 qrels와 연결되어야 합니다. 실제 승인 질의의 2점 문서가 baseline Top-5 밖에 있고 덜 관련한 경쟁 문서가 Top-5 안에 있어야 합니다. 범위 누락은 이 게이트가 아닙니다. K1은 직접 문서에서 누락된 기술 토큰이 재현되어야 합니다. R1은 실제 전체 순위에서 창 절단 기여 손실을 추가 검사합니다. K1은 질의 토큰만, R1은 창 크기만 바꿉니다.
- E1: 상위 JSON에 `queries` 배열. 최대 8개 기존 `E1-variants.draft.json`만 허용합니다. 각 행에 동결 draft 필드와 `repository`, 실제 검토 출처, `approved=yes`, `equivalent_to_base=yes`를 넣습니다. base B도 실제 승인되어야 합니다. 새 문서 관련성을 자동으로 공유하지 않습니다.
- E2: 저장소당 한 쌍의 새 질의, 전체 최대 4개. 각 질의에 새 `query_id`, `query_sha256`, `case_id`, `repository`, `problem/error/environment/query_text`, 실제 검토 출처, `approved=yes`, 동일 `pair_id`, 서로 다른 `condition`, `condition_evidence` 배열이 필요합니다. 각 근거는 `doc_id`, 실제 원문 `document_sha256`, `evidence_scope=title_body`, 실제 `evidence_quote`, `evidence_url` 및 실제 사람 출처입니다. 양쪽 근거가 없으면 실행하지 않습니다.
- E3: 저장소당 새 질의 하나, 최대 2개. 새 질의 필드는 E2와 같으며 `control_documents`에 최대 20개 문서의 실제 사람 출처, `doc_id`, 원문 해시, 제목/본문 인용·URL·범위, 질의별 숫자 grade 0/1/2를 넣습니다. 미판정·댓글 전용은 인증되지 않습니다. plus에 2점이 있어야 하고 모든 2점을 제거한 minus가 비어 있으면 실행하지 않습니다. minus의 후보 반환은 오류율/검색 실패로 계산하지 않습니다.

실행 예산은 [config.json](config.json)에 먼저 동결합니다. 모델·필터·순위 가중치 탐색은 추가하지 않습니다. K1/R1 새 Top-5는 공통 풀을 확장합니다. 같은 확장 풀의 재검토 전에는 개선을 확정하지 않습니다. 행동 실험은 별도 로컬 결과와 검토 패키지를 생성하며 확정 품질 집계는 사람 판정이 필요합니다.

실제 검토가 아직 없으므로 첫 게시 상태는 검토 대기입니다. 실패 게이트를 열거나 E1/E2/E3를 실행한 것처럼 보고하지 않습니다. 수동 웹 비교는 원래 `manual_web_study.template.csv`의 실제 참가자 기록으로 진행하며 과제당 동일 5분 상한을 먼저 확인합니다. 지금 참가자 기록·성공·시간은 만들지 않았습니다.

공개 재집계에는 `metrics_by_query.csv`, `metrics_summary.csv`, `review_progress.csv`, `figure_data/`를 사용합니다. 정확한 원문 임베딩 재실행에는 로컬 부모 스냅샷·모델 캐시가 필요합니다. 과거 파일의 `code_hashes`를 새로운 scorer로 갱신하지 않습니다.
