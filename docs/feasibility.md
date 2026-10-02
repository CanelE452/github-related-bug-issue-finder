# GitHub Related Bug Issue Finder — 주제 구현 가능성 확인

**결론: 공개 GitHub 저장소의 기존 Issue에서 한국어·영어 문제 설명과 관련된 Bug Issue를 찾아주는 주제는 구현 가능합니다.** 실제 데이터 수집과 검색 실행, 한국어 질의로 참고 원문을 찾은 사례가 있습니다. 현재 목표는 이 기능의 구현 가능성을 확인하는 것입니다.

이 결론은 모든 오류의 해결 가능성이나 전체 검색 정확도를 뜻하지 않습니다. 기존 Issue의 증상을 재구성한 개발 사례로 확인했으며, 독립적인 신규 사용자 평가를 수행한 것은 아닙니다.

## 만드는 서비스

- 입력: 공개 저장소 URL, 필수 문제 설명, 선택적 오류 메시지·실행 환경.
- 출력: 관련 Bug Issue 상위 5개와 제목·상태·레이블·본문 발췌·GitHub 원문 링크.
- 구성: React·Vite·TypeScript 화면, Python·FastAPI 서버, SQLite 캐시, BM25·다국어 임베딩·RRF 검색.
- 사용 목적: 사용자가 원문에서 비슷한 증상, 원인 조사, 우회 방법이나 수정 제안을 확인하도록 돕습니다. 자동 해결이나 수정 제안의 실행 검증은 제공하지 않습니다.

## 실제로 확인한 범위

| 확인 항목 | 저장된 실행 결과 | 근거 |
|---|---|---|
| 공개 저장소 수집·PR 제외·Bug 분류 | OpenCV Issue 387개 중 Bug 232개, Transformers Issue 390개 중 Bug 114개 | [수집 조건·건수](experiments/scenario_pilot_v1/run_001/report.md#데이터-범위와-필터) |
| 세 검색 방식 실행 | 12개 개발 사례의 3가지 입력 × 3방법 × 2검색 범위 = 핵심 216조건 실행. 역사 사례 12조건을 포함한 검색 228조건에서 실행 오류 0건 | [기존 실행 보고서](experiments/scenario_pilot_v1/run_001/report.md#수행-범위) |
| 한국어 설명·오류·환경으로 영어 원문 찾기 | 아래 OpenCV·Transformers 사례에서 BM25·Semantic·Hybrid 모두 참고 원문 1위 | [실제 질의와 Top-5](experiments/scenario_followup_v2/machine_001/casebook.md) |
| 저장 결과 재현 | 별도 재현 12조건에서 순서 일치, 점수 차이 0 | [재현 결과 JSON](experiments/scenario_followup_v2/batch_001/reproduction.json) |
| 게시 코드 검증 | 검색·API·캐시·평가 도구 등을 포함한 테스트 90개 통과, 기존 의존성 경고 1개 | [실제 테스트 로그](experiments/scenario_followup_v2/machine_001/tests/published-tree.txt) |

수집은 각 저장소 최대 20페이지의 부분 스냅샷입니다. 위 테스트는 이전 코드 게시 커밋 `14675220fdd64d75ef100d4d7f88e90ceb029c13`의 기록이며, 이번 갱신은 문서만 변경합니다.

## 대표 사례와 제한

`C_raw`는 PR을 제외한 수집 Issue 전체의 평가 대조 범위이며, `C_bug`는 Bug 필터를 통과한 범위입니다. 실제 앱은 Bug 범위를 사용합니다.

| 입력 사례 | 참고 GitHub Issue | 저장된 검색 결과 | 의미 |
|---|---|---|---|
| 한국어 빌드 문제 설명 + `posix_memalign` 선언 누락 + Windows·MinGW 환경 | [OpenCV #29350](https://github.com/opencv/opencv/issues/29350) | 두 범위 모두 세 방법에서 1위 | 오류와 환경을 포함한 질의로 같은 증상을 다루는 원문을 찾았습니다. |
| 한국어 Gemma4 영상 처리 문제 설명 + `'tuple' object has no attribute 'to'` + Transformers 환경 | [Transformers #47879](https://github.com/huggingface/transformers/issues/47879) | 두 범위 모두 세 방법에서 1위 | 한국어 설명으로 영어 Issue를 찾는 기능의 구현 사례입니다. 본문의 수정 제안은 실행 검증하지 않았습니다. |
| 한국어 Trainer 체크포인트 이동 후 종료 오류 설명 + 관련 조건 | [Transformers #48315](https://github.com/huggingface/transformers/issues/48315) | 전체 Issue 범위에서 세 방법 모두 1위. Bug 범위에서는 원문 제외 | 검색 대상에 포함되지 않은 Issue는 앱에서 찾을 수 없습니다. Bug 라벨과 수집 범위를 확인해야 합니다. |

세 사례의 질의는 원문을 읽고 재구성한 것입니다. 참고 원문이 다시 검색되는 관찰은 구현 가능성을 보여주지만, 독립적인 정확도 검증이나 실제 오류 해결 성공률로 해석할 수 없습니다. 오류·환경을 생략한 모든 한국어 설명에서도 같은 결과가 나온다는 뜻은 아닙니다.

## 그림과 원자료

![실제로 수집한 전체 Issue와 Bug Issue 수](experiments/scenario_pilot_v1/run_001/images/corpus-coverage.png)

위 그림은 실제 수집 범위를 나타냅니다. [기존 수집 보고서](experiments/scenario_pilot_v1/run_001/report.md)에 실행 조건과 건수를 남겼습니다.

![AI 예비 검토로 비교한 기존 검색 결과](experiments/scenario_followup_v2/machine_001/images/ai-comparison.png)

두 번째 그림은 3개 사례·38개 후보 쌍의 **AI 예비 판정**에 따른 기존 검색 결과 비교입니다. 사람 검증이나 전체 정확도 수치가 아닙니다. [그림 원자료](experiments/scenario_followup_v2/machine_001/summary.csv), [Top-5 원자료](experiments/scenario_followup_v2/machine_001/top5.csv), [AI 판정 근거](experiments/scenario_followup_v2/machine_001/machine_annotations.jsonl), [예비 비교의 한계](experiments/scenario_followup_v2/machine_001/report.md)를 함께 제공합니다.

AI 예비 비교는 기존 순위 **18조건을 재사용**했으며 새로운 검색 조건을 실행하지 않았습니다. Hybrid가 OpenCV 사례에서 BM25보다 낮은 예비 관련도 점수를 보인 결과도 그대로 보존했습니다.

## 현재 목표와 후속 실험의 상태

현재 목표인 **수집된 실제 Issue를 대상으로 관련 원문을 찾는 기능의 구현 가능성 확인**에는 기존 실행 기록을 근거로 사용할 수 있습니다. 사용자가 전체 관련성 검토 CSV를 작성하는 것을 이 단계의 완료 조건으로 두지 않습니다.

| 항목 | 현재 상태 |
|---|---|
| HEAD·미커밋 확인, 기존 run_001 보존 | 완료. 기존 813개 파일 보존 확인 |
| 검색 실행 버전과 채점·보고 버전 분리 | 완료 |
| 부분 검토 채점·보고서 갱신 보강과 테스트 | 완료 |
| 실제 사람 검토 파일 확인 및 미작성 시 자료 준비 | 완료. 실제 판정은 없고 HTML·CSV 양식·재개 명령 준비 |
| 기계적 분석과 기존 검색 재현 | 완료 |
| K1·R1 단일 요소 변경 실험 | 미실행. 기존 근거 게이트 유지 |
| 표현 변경 E1·조건 변경 E2·무정답 검사 E3·사용자 비교 실험 | 미실행. 이번 구현 가능성 확인의 필수 범위에서 제외 |
| 독립적인 전체 검색 품질 검증 | 미완료. AI 판정으로 사람 판정을 대체하지 않음 |

기존 [후속 평가 보고서](experiments/scenario_followup_v2/batch_001/report.md)의 검토 대기 상태와 원자료는 보존했습니다. 이번 문서는 목표를 구현 가능성 확인으로 좁힌 설명이며, 미실행 실험의 상태를 완료로 바꾸지 않습니다.

## 로컬에서 확인하기

설치와 모델 준비는 [프로젝트 실행 안내](../README.md#빠른-실행--windows-powershell)를 따릅니다. 준비된 환경에서는 프로젝트 루트에서 다음 명령으로 실행합니다.

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

1. 브라우저에서 `http://127.0.0.1:8000`을 엽니다.
2. `https://github.com/huggingface/transformers`를 입력하고 저장소를 분석합니다.
3. 문제 설명과 필요한 오류·환경을 입력하고 검색합니다.
4. 반환된 GitHub 링크에서 실제 증상과 조건이 맞는지 확인합니다.

실시간 수집 시점에 따라 참고 Issue가 최신 20페이지 밖으로 밀릴 수 있습니다. 표의 순위를 그대로 확인하려면 원래 동결 데이터와 [재현 안내](../evaluation/scenario_followup_v2/README.md)를 사용해야 합니다. 대표 사례의 본문 환경은 원문에 기록된 조건이며, 로컬 환경으로 모두 재현한 것은 아닙니다.
