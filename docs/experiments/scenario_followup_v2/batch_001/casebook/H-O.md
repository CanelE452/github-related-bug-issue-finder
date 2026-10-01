# H-O · opencv/opencv

cohort: `historical_probe`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [opencv/opencv#17687](https://github.com/opencv/opencv/issues/17687)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
OpenCV에서 Windows 웹캠을 CAP_MSMF 또는 CAP_ANY로 열면 오래 걸리지만 CAP_DSHOW로 열 때는 다르게 동작합니다.

[ENVIRONMENT]
Windows 웹캠; CAP_MSMF, CAP_ANY, CAP_DSHOW 비교</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like source string · #29724](https://github.com/opencv/opencv/issues/29724) | rrf / 0.03125000 | UNJUDGED | unreviewed [] |

| 4 | [AVFoundation seeking drifts for non-integer frame rates · #28831](https://github.com/opencv/opencv/issues/28831) | rrf / 0.02778314 | UNJUDGED | unreviewed [] |

| 5 | [Heap Buffer Overflow in MJPEG Encoder mjpeg_buffer::put_bits via Small Frame (1×1) · #29112](https://github.com/opencv/opencv/issues/29112) | rrf / 0.02765065 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | cosine_similarity / 0.88254547 | UNJUDGED | unreviewed [] |

| 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.87973583 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | cosine_similarity / 0.87658304 | UNJUDGED | unreviewed [] |

| 4 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like source string · #29724](https://github.com/opencv/opencv/issues/29724) | cosine_similarity / 0.86941278 | UNJUDGED | unreviewed [] |

| 5 | [Division-by-Zero in OpenCV SGBM 3-Way Mode · #29761](https://github.com/opencv/opencv/issues/29761) | cosine_similarity / 0.86873549 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | bm25 / 74.81146236 | UNJUDGED | unreviewed [] |

| 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 67.37184311 | UNJUDGED | unreviewed [] |

| 3 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | bm25 / 56.32053771 | UNJUDGED | unreviewed [] |

| 4 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like source string · #29724](https://github.com/opencv/opencv/issues/29724) | bm25 / 53.36248814 | UNJUDGED | unreviewed [] |

| 5 | [Potential license issue with cap_msmf.cpp · #28594](https://github.com/opencv/opencv/issues/28594) | bm25 / 51.94019136 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [AVFoundation seeking drifts for non-integer frame rates · #28831](https://github.com/opencv/opencv/issues/28831) | rrf / 0.02967033 | UNJUDGED | unreviewed [] |

| 4 | [Heap Buffer Overflow in MJPEG Encoder mjpeg_buffer::put_bits via Small Frame (1×1) · #29112](https://github.com/opencv/opencv/issues/29112) | rrf / 0.02941176 | UNJUDGED | unreviewed [] |

| 5 | [Performance regression: cv::compare on Windows ~4× slower in OpenCV 4.12 vs 4.11 · #28251](https://github.com/opencv/opencv/issues/28251) | rrf / 0.02848485 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | cosine_similarity / 0.88254547 | UNJUDGED | unreviewed [] |

| 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.87973583 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | cosine_similarity / 0.87658304 | UNJUDGED | unreviewed [] |

| 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode · #29761](https://github.com/opencv/opencv/issues/29761) | cosine_similarity / 0.86873549 | UNJUDGED | unreviewed [] |

| 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | cosine_similarity / 0.86839485 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖 · #29562](https://github.com/opencv/opencv/issues/29562) | bm25 / 75.71105450 | UNJUDGED | unreviewed [] |

| 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 69.32215072 | UNJUDGED | unreviewed [] |

| 3 | [videoio: unnecessary use of get&lt;double&gt;() for integer parameters in several backends · #28498](https://github.com/opencv/opencv/issues/28498) | bm25 / 52.29081460 | UNJUDGED | unreviewed [] |

| 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 41.44657355 | UNJUDGED | unreviewed [] |

| 5 | [AVFoundation seeking drifts for non-integer frame rates · #28831](https://github.com/opencv/opencv/issues/28831) | bm25 / 38.66124201 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
