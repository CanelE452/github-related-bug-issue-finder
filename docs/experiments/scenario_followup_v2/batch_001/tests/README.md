# 게시 코드 테스트

최종 게시 코드: **80 passed, 1 warning**. 실행 명령과 코드·테스트 파일별 SHA-256은 [published-tree.json](published-tree.json), 실제 출력은 [published-tree.txt](published-tree.txt)에 있습니다. 스테이징된 코드만 Git archive로 분리해 검사했으며, 기존 미커밋 코드 리뷰 기능은 포함하지 않았습니다.

앞선 실행도 보존했습니다.

- [첫 실행](published-tree-attempt-001.txt): 기본 Windows 임시 폴더 접근 권한 오류. 테스트 전용 새 작업공간 경로를 지정했습니다.
- [두 번째 실행](published-tree-attempt-002.txt): 78개 통과·2개 실패. 깊은 임시 경로와 임베딩 캐시 파일명이 Windows 경로 제한을 넘었습니다. 전용 임시 경로를 짧게 바꾼 뒤 전체 게시 코드 테스트가 통과했습니다.
- [세 번째 실행](published-tree-attempt-003.txt): 80개 통과. Git archive가 Windows 줄바꿈 설정을 적용함을 확인해, 최종 실행에서는 자동 변환을 끄고 게시할 Git blob 바이트와 코드·테스트 해시가 정확히 일치하도록 했습니다. 최종 실행도 80개 통과했습니다.
- Git index 쓰기에 필요한 권한 없이 실행한 한 번의 호출은 테스트 시작 전에 거부됐습니다. 허용된 저장소 메타데이터 접근으로 재실행했습니다.

FastAPI/Starlette의 httpx 사용 중단 예고 경고 1건은 남아 있습니다. 이번 평가 작업에서 기존 운영 의존성은 변경하지 않았습니다.

[검토 화면 검증](ui-test-log.json)은 합성 입력을 이용한 UI 기능 검사이며 사람의 관련성 판정이 아닙니다. [실제 빈 CSV 다운로드·재입력 검사](ui-blank-downloads.json)는 Chrome에서 38질의·429쌍 파일이 저장됐음을 확인합니다. 미작성 CSV로는 품질 점수를 확정하지 않습니다.
