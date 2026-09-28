# 재현 가능한 평가

## 정답 데이터

`evaluation.survey`는 최근 최대 20페이지의 Issue에서 중복 레이블 또는 `state_reason=duplicate` 후보를 찾습니다. 후보의 timeline에서 OWNER/MEMBER/COLLABORATOR의 **명시적인 `Duplicate of #번호` 또는 동일 저장소 Issue URL**을 읽고 출처 URL·원문을 저장합니다. 단순 레이블이나 연관 링크는 정답으로 만들지 않습니다. 마지막 duplicate 이벤트가 unmarked이면 제외하고, timeline이 2페이지를 넘어 끝까지 확인되지 않으면 제외합니다. 서로 다른 원본이 명시되면 모호한 쌍으로 취급하여 제외합니다.

이 수집기는 전체 중복 관계를 포괄하지 않습니다. 중복 레이블이 없는 관계, 다른 표현의 댓글, 다른 저장소를 가리키는 관계는 누락됩니다. 검증된 외부 쌍을 동일 JSON 계약으로 추가할 수 있습니다. 추가 시 evidence와 source_url을 확인해야 합니다.

`evaluation/verified_pairs.json`에는 GitHub의 [#47332](https://github.com/huggingface/transformers/issues/47332) 종료 상태 배너에 원본 #47333이 직접 표시된 쌍을 보관했습니다. 이 쌍은 API 레이블로 추측한 데이터가 아니며, 양쪽 Issue 모두 이번 원본 스냅샷에 포함되어 있습니다. 1개뿐이므로 평가 코드의 실제 데이터 동작 확인용입니다.

```powershell
.\.venv\Scripts\python.exe -m evaluation.evaluate --repository huggingface/transformers --pairs evaluation/verified_pairs.json --split test --output evaluation/output/verified-test
```

```json
{
  "repository": "owner/repo",
  "query_number": 200,
  "target_number": 100,
  "source_url": "https://github.com/owner/repo/issues/200#issuecomment-123",
  "evidence": "explicit_maintainer_duplicate_comment",
  "language": "en"
}
```

입력과 정답이 같은 쌍, 근거 없는 쌍, corpus 밖의 정답, Bug 필터에서 제외된 정답을 별도 제외 사유로 기록합니다. 입력은 원본 캐시의 제목·본문에서 가져옵니다. 정답 번호나 중복 선언이 본문 자체에 들어 있는지 평가 전에 검토하고, 오염된 쌍은 제거해야 합니다. 댓글은 검색 입력에 포함하지 않습니다.

## 분할과 비교

- seed=42, 연결된 duplicate 그룹의 30%를 검증용, 나머지 70%를 최종 평가용으로 배정합니다. 그룹 수가 적으면 검증용이 0개일 수 있습니다.
- 같은 canonical을 공유하거나 중복 관계로 연결된 Issue, 동일 질의의 한국어 번역은 같은 split에 둡니다.
- BM25, Semantic, Hybrid 모두 동일 스냅샷·Bug 필터·질의·정답을 사용하고 질의 Issue 자체를 **후보 제한 전에** 제외합니다.
- 모델은 사전 학습 상태로 사용하며 별도 학습 split은 없습니다. 검증 split으로 설정을 선택한 뒤 최종 test를 한 번 평가합니다.
- source pairs 파일의 해시와 snapshot version이 다르면 같은 실험 조건으로 취급하지 않습니다. 새 데이터를 수집하면 새로운 평가입니다.

## 지표

정답이 하나인 쌍을 기준으로 Recall@1, Recall@5, MRR를 계산합니다. 정답이 검색 결과에 없으면 reciprocal rank는 0입니다. Hybrid는 두 Top-50 후보의 합집합 밖 정답을 반환하지 않으므로 MRR도 후보 한도 안에서 측정됩니다. 후보 제한은 결과 보고서에 기록합니다.

JSON에는 질의별 순위·Top-5·시간·출처·제외 사유·모델 revision·설정이 포함됩니다. CSV에는 언어별·방법별 요약이 저장됩니다. 첫 검색의 모델·메모리 캐시 준비 시간이 포함될 수 있어 평균 시간은 서비스 성능 보장의 근거로 쓰지 않습니다.

50개 미만은 **탐색적 실험**입니다. 표본이 0개이면 지표를 0으로 꾸미지 않고 빈 요약과 평가 불가 상태로 남깁니다. 실제 관련성은 duplicate 여부보다 넓으므로 이 지표가 관련 Issue 검색의 모든 품질을 설명하지 않습니다. 또한 현재 시점의 본문을 쓰므로 과거 Issue 생성 시점의 온라인 성능을 재현한 것이 아닙니다.

## 한국어 평가

`evaluation/korean_queries.example.json`을 참고하여 동일 쌍의 `language: ko`, `query_text`, `reviewed_by`를 작성합니다. 사람이 의미와 오류 코드·버전 보존 여부를 검토해야 합니다. 검토자 정보가 없으면 한국어 평가에서 제외됩니다. 영어·한국어 결과를 별도로 보고합니다.

번역 모델이 만든 초안이나 에이전트의 자체 검토를 사람의 검토로 표시하지 않습니다. 사람이 검토한 문항이 확보되기 전에는 한국어 입력의 동작 확인과 정량 품질 평가를 구분합니다.

## 실패 분석

질의별 결과를 확인하여 오류 토큰, 의미 불일치, 설명 부족, 긴 본문, 버전 의존성, 전문 용어, 근거 오류로 분류합니다. 개인 경로·타임스탬프 등 노이즈가 실제 실패 원인인 경우에만 후속 normalization 실험을 제안합니다.
