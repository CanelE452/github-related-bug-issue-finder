# O-C1 · opencv/opencv

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [opencv/opencv#28207](https://github.com/opencv/opencv/issues/28207)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
OpenCV Java로 영상을 읽을 때 NVIDIA 하드웨어 디코더가 사용되지 않습니다.</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.88398826 | UNJUDGED | unreviewed [] |

| 2 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.88148707 | UNJUDGED | unreviewed [] |

| 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.87935090 | UNJUDGED | unreviewed [] |

| 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | cosine_similarity / 0.87357175 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | cosine_similarity / 0.87346929 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `4` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [cv::cuda::resize failed with Continuous GpuMat · #28407](https://github.com/opencv/opencv/issues/28407) | bm25 / 7.15655501 | UNJUDGED | unreviewed [] |

| 2 | [Dynamic CUDA support · #29318](https://github.com/opencv/opencv/issues/29318) | bm25 / 5.69166327 | UNJUDGED | unreviewed [] |

| 3 | [[Windows] RTX 5070 Ti (Blackwell sm_120) - setup and deployment notes · #28924](https://github.com/opencv/opencv/issues/28924) | bm25 / 5.64236114 | UNJUDGED | unreviewed [] |

| 4 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 5.47797701 | UNJUDGED | unreviewed [] |

| 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | bm25 / 5.29133594 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03175403 | UNJUDGED | unreviewed [] |

| 2 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | rrf / 0.03100962 | UNJUDGED | unreviewed [] |

| 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2 · #28784](https://github.com/opencv/opencv/issues/28784) | rrf / 0.02848485 | UNJUDGED | unreviewed [] |

| 4 | [[bug] Incorrect result from the `cv::createHanningWindow()` function · #29634](https://github.com/opencv/opencv/issues/29634) | rrf / 0.02774589 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02731327 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.88398826 | UNJUDGED | unreviewed [] |

| 2 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.88148707 | UNJUDGED | unreviewed [] |

| 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.87935090 | UNJUDGED | unreviewed [] |

| 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | cosine_similarity / 0.87357175 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | cosine_similarity / 0.87346929 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [cv::cuda::resize failed with Continuous GpuMat · #28407](https://github.com/opencv/opencv/issues/28407) | bm25 / 7.34536300 | UNJUDGED | unreviewed [] |

| 2 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 5.83897851 | UNJUDGED | unreviewed [] |

| 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | bm25 / 5.70166629 | UNJUDGED | unreviewed [] |

| 4 | [5.x: cv::addWeighted segfaults (null kernel pointer) for 8U/8S/16U/16S/16F/16BF/32F inputs with dtype=CV_64F, and for CV_Bool inputs with any dtype · #29880](https://github.com/opencv/opencv/issues/29880) | bm25 / 3.16951300 | UNJUDGED | unreviewed [] |

| 5 | [Some OpenCL tests fail on Ubuntu 26.04 LTS · #28919](https://github.com/opencv/opencv/issues/28919) | bm25 / 2.14641735 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 2 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2 · #28784](https://github.com/opencv/opencv/issues/28784) | rrf / 0.02943723 | UNJUDGED | unreviewed [] |

| 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02840451 | UNJUDGED | unreviewed [] |

| 5 | [Unable to build with CUDA · #28952](https://github.com/opencv/opencv/issues/28952) | rrf / 0.02808327 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
FFmpeg에서 h264_cuvid로 같은 영상을 직접 디코딩하면 GPU 디코더가 동작하지만, OpenCV Java VideoCapture에서는 동작하지 않습니다. CAP_FFMPEG와 VIDEO_ACCELERATION_ANY를 선택했고 OPENCV_FFMPEG_CAPTURE_OPTIONS로 video_codec=h264_cuvid를 지정했습니다.

[ENVIRONMENT]
Ubuntu 24.04; FFmpeg 6.1; OpenCV 4.12.0; NVIDIA RTX 5060</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 111.70346797 | UNJUDGED | unreviewed [] |

| 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | bm25 / 41.58616814 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 39.12842655 | UNJUDGED | unreviewed [] |

| 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 34.52083546 | UNJUDGED | unreviewed [] |

| 5 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read · #29722](https://github.com/opencv/opencv/issues/29722) | bm25 / 31.08187564 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.91577989 | UNJUDGED | unreviewed [] |

| 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | cosine_similarity / 0.89702272 | UNJUDGED | unreviewed [] |

| 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.89111233 | UNJUDGED | unreviewed [] |

| 4 | [4.13.0 build error both on Windows and Linux when using cuda13.2 · #28784](https://github.com/opencv/opencv/issues/28784) | cosine_similarity / 0.89033866 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | cosine_similarity / 0.88885605 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read · #29722](https://github.com/opencv/opencv/issues/29722) | rrf / 0.03030999 | UNJUDGED | unreviewed [] |

| 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | rrf / 0.03011775 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | rrf / 0.02804284 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 114.56239075 | UNJUDGED | unreviewed [] |

| 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 38.20814517 | UNJUDGED | unreviewed [] |

| 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 34.28469715 | UNJUDGED | unreviewed [] |

| 4 | [cv::cuda::resize failed with Continuous GpuMat · #28407](https://github.com/opencv/opencv/issues/28407) | bm25 / 30.57560138 | UNJUDGED | unreviewed [] |

| 5 | [[iOS] VideoWriter::release() causes NSInvalidArgumentException on OpenCV 4.12.0 (works in 4.8.0) · #28165](https://github.com/opencv/opencv/issues/28165) | bm25 / 26.84886320 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.91577989 | UNJUDGED | unreviewed [] |

| 2 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.89111233 | UNJUDGED | unreviewed [] |

| 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2 · #28784](https://github.com/opencv/opencv/issues/28784) | cosine_similarity / 0.89033866 | UNJUDGED | unreviewed [] |

| 4 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | cosine_similarity / 0.88885605 | UNJUDGED | unreviewed [] |

| 5 | [Last IPP HAL refactoring introduced invalid memory access issue on Windows · #29166](https://github.com/opencv/opencv/issues/29166) | cosine_similarity / 0.88809144 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | rrf / 0.03079839 | UNJUDGED | unreviewed [] |

| 3 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | rrf / 0.02970951 | UNJUDGED | unreviewed [] |

| 4 | [Compilation Errors during build · #28629](https://github.com/opencv/opencv/issues/28629) | rrf / 0.02943723 | UNJUDGED | unreviewed [] |

| 5 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | rrf / 0.02866503 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Decoding the same video directly with FFmpeg and h264_cuvid uses the GPU decoder, but OpenCV Java VideoCapture does not. I selected CAP_FFMPEG and VIDEO_ACCELERATION_ANY, and set OPENCV_FFMPEG_CAPTURE_OPTIONS to video_codec=h264_cuvid.

[ENVIRONMENT]
Ubuntu 24.04; FFmpeg 6.1; OpenCV 4.12.0; NVIDIA RTX 5060</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 189.04722409 | UNJUDGED | unreviewed [] |

| 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | bm25 / 77.64343084 | UNJUDGED | unreviewed [] |

| 3 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | bm25 / 66.15968529 | UNJUDGED | unreviewed [] |

| 4 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 66.15103189 | UNJUDGED | unreviewed [] |

| 5 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read · #29722](https://github.com/opencv/opencv/issues/29722) | bm25 / 64.24800505 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read · #29722](https://github.com/opencv/opencv/issues/29722) | rrf / 0.03151365 | UNJUDGED | unreviewed [] |

| 4 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | rrf / 0.03125763 | UNJUDGED | unreviewed [] |

| 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | rrf / 0.02963126 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.93371451 | UNJUDGED | unreviewed [] |

| 2 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read · #29722](https://github.com/opencv/opencv/issues/29722) | cosine_similarity / 0.91327310 | UNJUDGED | unreviewed [] |

| 3 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | cosine_similarity / 0.90971607 | UNJUDGED | unreviewed [] |

| 4 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.90717226 | UNJUDGED | unreviewed [] |

| 5 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | cosine_similarity / 0.90520877 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | bm25 / 189.18009955 | UNJUDGED | unreviewed [] |

| 2 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | bm25 / 66.36910249 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | bm25 / 64.54701155 | UNJUDGED | unreviewed [] |

| 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 61.03484956 | UNJUDGED | unreviewed [] |

| 5 | [AVFoundation seeking drifts for non-integer frame rates · #28831](https://github.com/opencv/opencv/issues/28831) | bm25 / 44.80084315 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | rrf / 0.03077652 | UNJUDGED | unreviewed [] |

| 4 | [AVFoundation seeking drifts for non-integer frame rates · #28831](https://github.com/opencv/opencv/issues/28831) | rrf / 0.03009050 | UNJUDGED | unreviewed [] |

| 5 | [Windows11+Opencv4.13-build-issue · #28608](https://github.com/opencv/opencv/issues/28608) | rrf / 0.02921109 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [can&#x27;t using h264_cuvid decoder when using java api · #28207](https://github.com/opencv/opencv/issues/28207) | cosine_similarity / 0.93371451 | UNJUDGED | unreviewed [] |

| 2 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;: · #29458](https://github.com/opencv/opencv/issues/29458) | cosine_similarity / 0.90717226 | UNJUDGED | unreviewed [] |

| 3 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second · #28638](https://github.com/opencv/opencv/issues/28638) | cosine_similarity / 0.90520877 | UNJUDGED | unreviewed [] |

| 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value · #28598](https://github.com/opencv/opencv/issues/28598) | cosine_similarity / 0.90287876 | UNJUDGED | unreviewed [] |

| 5 | [Last IPP HAL refactoring introduced invalid memory access issue on Windows · #29166](https://github.com/opencv/opencv/issues/29166) | cosine_similarity / 0.90253556 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
