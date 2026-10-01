# 상황 질의 파일럿 v1

OpenCV·Transformers의 공개 Issue에서 12개 개발 사례를 골라 BM25·다국어 임베딩·Hybrid 검색을 비교하는 별도 CLI입니다. 앱의 저장소 필터·순위 알고리즘은 유지하고 검색 문서 집합 선택만 분리했습니다.

현재 결과는 **사람 검토 전 순위 관찰**입니다. 원문을 재구성한 질의가 원문을 회수하는지는 검색 정확도나 버그 해결 성공률이 아닙니다.

- [실제 실행 보고서와 그래프](../../docs/experiments/scenario_pilot_v1/run_001/report.md)
- [질의별 Top-5 원문 링크](../../docs/experiments/scenario_pilot_v1/run_001/casebook.md)
- [첨부 계약 원문](protocol.md)
- [실행 설정](config.json), [질의 초안](cases.draft.json), [후보 선택 기록·계획 차이](selection-audit.json)

## 설치와 실행

프로젝트 루트에서 Python 3.12 가상환경을 사용합니다. 기존 backend·semantic 의존성에 그래프/메모리 측정 의존성을 추가합니다.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r backend/requirements.txt -r backend/requirements-semantic.txt -r evaluation/requirements-pilot.txt
.venv/Scripts/python.exe -m pytest backend/tests -q
.venv/Scripts/python.exe -m evaluation.scenario_eval --help
```

GitHub 토큰은 필요하면 서버 환경변수 `GITHUB_TOKEN`으로만 설정합니다. 토큰을 질의·config·로그·Git에 넣지 않습니다. 이 실행은 44회 API 호출을 사용했고, 재시도와 토큰 교체를 하지 않았습니다.

이 파일럿은 기존 서비스가 다운로드한 고정 revision 모델 캐시를 **읽어서** 사용합니다. `data/models/models--intfloat--multilingual-e5-small/snapshots/614241f622f53c4eeff9890bdc4f31cfecc418b3` 및 `.issue-finder-complete` 표시가 필요합니다. 캐시가 없으면 실제 모델을 준비해야 하며 가짜 임베딩으로 품질 결과를 만들지 않습니다.

새 실행은 반드시 새 폴더를 사용합니다. `run_001`의 원문·질의·순위를 덮어쓰지 않습니다.

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_eval prepare --run-dir data/scenario_pilot_v1/new_run --config evaluation/scenario_pilot_v1/config.json
```

첫 명령은 원문을 수집하고 고정 시드 후보 목록을 만듭니다. 후보 원문을 검토해 **새 수집 범위에 있는** 실제 증상 사례와 A/B/C 질의를 작성한 뒤 동결합니다. 게시된 2026-10-01 초안의 원문 번호가 새로운 최신 20페이지 밖으로 밀려났다면 그대로 재사용하지 않습니다. 설정·코드 변경도 새 실행으로 취급합니다.

이 컴퓨터의 동결한 원래 실행에서 실제 사용한 명령은 다음과 같습니다.

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_eval prepare --run-dir data/scenario_pilot_v1/run_001 --config evaluation/scenario_pilot_v1/config.json --cases evaluation/scenario_pilot_v1/cases.draft.json
.venv/Scripts/python.exe -m evaluation.scenario_eval retrieve --run-dir data/scenario_pilot_v1/run_001
.venv/Scripts/python.exe -m evaluation.scenario_eval cold --run-dir data/scenario_pilot_v1/run_001
.venv/Scripts/python.exe -m evaluation.scenario_eval export-review --run-dir data/scenario_pilot_v1/run_001
.venv/Scripts/python.exe -m evaluation.scenario_eval diagnose --run-dir data/scenario_pilot_v1/run_001
.venv/Scripts/python.exe -m evaluation.scenario_eval report --run-dir data/scenario_pilot_v1/run_001
```

`retrieve`, `cold`, `export-review`는 저장된 결과나 검토 파일을 덮어쓰지 않습니다. `prepare`는 같은 입력으로 다시 호출해도 API를 재수집하지 않습니다. 질의·원문·모델 revision·config·코드 해시가 다르면 재사용을 거부합니다. 원문·벡터·full-text 검토 HTML은 `data/` 아래 Git 제외입니다. GitHub에는 소형 JSONL/CSV/Markdown/PNG와 해시만 게시했습니다. 따라서 clone만으로 **같은 원문 스냅샷**을 복원할 수는 없습니다. 이 컴퓨터의 원래 run 폴더를 이용하거나 새 수집으로 별도 실행해야 합니다.

이번 실행은 20개 표본 측정 후 기존 서비스의 벡터 266개 문서/1,268구간을 읽기 재사용했습니다. 본문 해시, model/resolved revision, 구간 길이·중첩·접두사·pooling 설정과 캐시 키를 대조하고 float32/384차원/유한값/단위 길이를 검사했습니다. requested revision은 과거 캐시의 빈 요청과 이번의 고정 요청이 달랐지만 **resolved revision은 동일**했습니다. 이미 계산된 71개 캐시는 덮어쓰지 않았고, 운영 캐시는 수정하지 않았습니다. `cache-reuse.json`에 원본 벡터 파일 해시와 복사 건수를 기록했습니다. 실제 인덱싱 시간은 이 재사용을 포함하므로 처음부터 모든 문서를 계산하는 시간으로 해석하지 않습니다.

## 사람이 채울 파일

먼저 `data/scenario_pilot_v1/run_001/review.html`을 브라우저로 엽니다. 결과 방법·순위·점수를 가린, 고정 시드로 섞은 전체 본문 검토 자료입니다. 외부 이미지·스크립트는 실행되지 않습니다. 원문 HTML은 텍스트로 이스케이프했습니다.

검토 결과를 보존하려면 CSV를 복사해서 작성합니다. GitHub의 결과 폴더에도 같은 빈 CSV가 있습니다.

1. `query_reviews.csv`: 핵심 36질의의 증상 충실성(`symptom_faithful`), 원인/해결 누출 없음(`no_solution_leakage`), A→B 정보 추가와 B↔C 정보 동등성(`information_change_checked`)을 실제로 확인하고 `yes`로 표시합니다. 맞지 않는 질의는 승인하지 않습니다. 질의를 고쳐야 하면 과거 검색/qrels를 재사용하지 않고 새 실행을 만듭니다. 별도 역사 질의 2개도 포함되어 있지만 핵심 지표에 합치지 않습니다.
2. `human_reviews.csv`: 방법별·범위별 Top-5의 합집합과 참고 원문을 질의별로 검토합니다. 같은 문서가 여러 방법에 등장해도 한 번 판정합니다. `grade=2`는 그 질의의 주요 증상/조건을 직접 다루는 문서, `1`은 참고할 관련 정보, `0`은 관련 없음입니다. 참고 원문이라고 자동으로 2점을 주지 않습니다. 다른 직접 관련 문서도 2점으로 인정합니다.
3. 두 파일 모두 실제 `reviewer_type=human`, 검토자 ID, 실제 ISO 검토 시각, `review_status=reviewed`, 이유를 적습니다. 문서 판정은 `evidence_quote`, `evidence_url`, `condition_relation`(supports/conflicts/unknown/not_applicable), `evidence_scope`(title_body/comment_only/unavailable)도 작성합니다. 댓글에서만 확인한 근거는 제목/본문 검색 품질의 직접 근거로 합치지 않습니다. `grade` 빈칸은 미판정입니다.

실제 사람 2명의 독립 판정을 권장합니다. 1명만 검토하면 그 한계를 기록합니다. 먼저 사례 2개를 검토하며 실제 시간을 기록해 나머지 비용을 추정할 수 있습니다. 이번에는 그 시간을 측정하지 않았습니다. 프로그램은 검토 형식·해시는 검증하지만 사람의 신원을 인증하지 못합니다.

실제 판정 후 재개 명령:

```powershell
.venv/Scripts/python.exe -m evaluation.scenario_eval score --run-dir data/scenario_pilot_v1/run_001 --reviews data/scenario_pilot_v1/run_001/human_reviews.completed.csv --query-reviews data/scenario_pilot_v1/run_001/query_reviews.completed.csv
```

`score`는 실제 판정을 이용해 `qrels.jsonl`, `metrics.csv`, `review_receipt.json`, 검토 완료/부분 완료 상태를 생성합니다. 지금 게시한 `report.md`는 **미검토 실행 시점 보고서**이므로 이후 판정 수치를 자동으로 바꾼 것으로 해석하지 않습니다. 판정 후 수치 보고서는 새 판정 결과와 provenance를 반영해 별도로 작성해야 합니다.

Hit@5는 직접 관련 문서가 하나라도 있으면 1입니다. 2점이 없고 미판정이 있으면 null입니다. pooled nDCG@5는 gain=`2^grade-1`, discount=`log2(rank+1)`을 쓰고 두 scope의 공통 C_raw 판정 풀을 정규화 분모로 사용합니다. IDCG=0과 미판정 Top-5, 실행 오류는 null입니다. Bug 필터로 직접 관련 문서가 빠졌더라도 질의는 과제 분모에 남습니다. 언어·입력별 결과를 합쳐 차이를 숨기지 않습니다. 질의 변형·반복·번역을 독립 사례로 세지 않습니다.

## 추가 진단과 실사용 비교

- E0: 범위별 참고 원문 존재 여부와 순위만 실제 관찰했습니다. 실패가 수집/필터/어휘/후보/순위/직접 관련성 중 어디에서 생겼는지는 사람 판정 후 확정합니다.
- E1: [4사례 × 2변형 초안](E1-variants.draft.json)과 [정보 동등성 검토 양식](variant_reviews.template.csv)을 만들었습니다. 아직 동등성 판정을 받지 않았으므로 48회 변형 검색은 **미실행**입니다. 이 CLI 버전은 판정 수신 후 E1/E2/E3 추가 검색을 자동 실행하는 기능까지 구현하지 않았습니다. 확장은 새 버전/실행으로 처리합니다.
- E2: 조건 대조에 적합한 원문·조건 쌍의 사람이 확인한 근거가 없어 **미실행**입니다. 원문에 성공한다고 적히지 않은 설정의 정상 동작을 가정하지 않습니다.
- E3: 모든 문서를 판정한 인증 무정답 소형 집합이 없어 **미실행**입니다. 2점이나 미판정 문서가 남으면 인증할 수 없습니다.
- E4: semantic/Hybrid Top-5의 문서/질의 토큰 수, 구간 수, 최대 유사도 구간 인덱스를 CSV로 기록했습니다. 짧은 근거 구간은 로컬 `runs.jsonl`에 있으며 사람이 증상/환경/템플릿인지 분류해야 합니다.
- E5: 핵심 216회와 별도 역사 12회의 검색 시간, 대표 6질의 × 3방법 × 3반복 warm 시간, 저장소 × 방법당 한 번의 별도 프로세스 cold 시간을 기록했습니다. 전체 서비스 지연·운영 P95가 아닙니다.

[실사용 비교 양식](manual_web_study.template.csv)은 O-S1/O-C1/T-S1/T-C1의 B 입력을 대상으로 합니다. 사람이 GitHub 검색·일반 웹 검색·이 앱을 이용하는 순서를 균형 있게 바꾸고, 첫 직접 관련 문서의 URL과 근거·실제 시작/종료 시간을 기록합니다. 문서를 읽는 시간도 포함하며 이미 원문을 본 사람의 기억 효과를 기록합니다. 도구별로 같은 시간 제한을 사전에 정하고 실패를 누락하지 않습니다. 이번에는 참가자/실제 브라우저 사용 기록이 없으므로 `PENDING_MANUAL_STUDY`입니다. 일반 검색이 키워드 검색뿐이라고 가정하지 않습니다.

요약 기능은 미구현이므로 `NOT_APPLICABLE_YET`입니다. 추후 구현하면 근거의 확인 가능성·내용 충실성·조건 누락/과장 여부를 별도로 검토하며 생성 모델의 자동 점수를 사람 판정으로 대체하지 않습니다.

## 검증과 게시 범위

전체 테스트 명령: `.venv/Scripts/python.exe -m pytest backend/tests -q` — 이번 실행 47 passed, 기존 Starlette/httpx 관련 경고 1개. 가짜 벡터는 단위 테스트에만 쓰고 게시한 실제 순위에는 고정 모델을 사용했습니다.

기존 미커밋 코드 리뷰/UI 파일을 제외한 게시 대상 복사본에서도 같은 명령으로 **41 passed, 경고 1개**를 확인했습니다. GitHub에 올라간 파일 기준의 검증은 보고서의 `published-tests.txt`를 참고하세요.

원문 수집/예산은 첫 작업 제한을 적용했고, 범위나 모델/가중치를 순위를 보고 튜닝하지 않았습니다. 후보 49개 검토는 계약 상한 48개에서 벗어난 점이며 숨기지 않았습니다. 분류·번역·원문 관련성은 실제 사람 검토 전입니다. 12개는 개발 사례로 계속 취급하고 독립 최종 평가셋이라고 이름만 바꾸지 않습니다.

사용자가 이번 메시지에서 push를 요청하여 첨부 계약의 push 금지를 대체했습니다. 이번 변경은 평가 CLI·테스트·소형 보고서에 한정합니다. 기존 미커밋 코드 리뷰/화면 변경은 별도로 남겼습니다.
