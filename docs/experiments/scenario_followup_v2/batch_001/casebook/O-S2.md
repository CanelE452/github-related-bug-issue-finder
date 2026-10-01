# O-S2 · opencv/opencv

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [opencv/opencv#30090](https://github.com/opencv/opencv/issues/30090)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
출시된 OpenCV 버전의 온라인 문서를 찾을 수 없고 문서 링크가 이전 버전으로 갑니다.</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `44` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | bm25 / 6.77074946 | UNJUDGED | unreviewed [] |

| 2 | [Warnings in Windows for ARM build in 4.x · #30095](https://github.com/opencv/opencv/issues/30095) | bm25 / 0.13248294 | UNJUDGED | unreviewed [] |

| 3 | [Cannot link OpenCV 5 statically to native code on Android · #29342](https://github.com/opencv/opencv/issues/29342) | bm25 / 0.13196417 | UNJUDGED | unreviewed [] |

| 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode · #29761](https://github.com/opencv/opencv/issues/29761) | bm25 / 0.13161867 | UNJUDGED | unreviewed [] |

| 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | bm25 / 0.13094509 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `71` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02987737 | UNJUDGED | unreviewed [] |

| 3 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | rrf / 0.02913851 | UNJUDGED | unreviewed [] |

| 4 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | rrf / 0.02847471 | UNJUDGED | unreviewed [] |

| 5 | [modules/core/src/hal_internal.cpp:540:48: error: expected unqualified-id before &#x27;_Complex&#x27; · #29452](https://github.com/opencv/opencv/issues/29452) | rrf / 0.02825871 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `116` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.87997431 | UNJUDGED | unreviewed [] |

| 2 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | cosine_similarity / 0.86624408 | UNJUDGED | unreviewed [] |

| 3 | [OpenBLAS detection broken on Fedora/RHEL (headers not found &amp; serial library linked) · #28049](https://github.com/opencv/opencv/issues/28049) | cosine_similarity / 0.86457819 | UNJUDGED | unreviewed [] |

| 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | cosine_similarity / 0.86405349 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | cosine_similarity / 0.86244798 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | bm25 / 6.48243170 | UNJUDGED | unreviewed [] |

| 2 | [Warnings in Windows for ARM build in 4.x · #30095](https://github.com/opencv/opencv/issues/30095) | bm25 / 0.00525870 | UNJUDGED | unreviewed [] |

| 3 | [Cannot link OpenCV 5 statically to native code on Android · #29342](https://github.com/opencv/opencv/issues/29342) | bm25 / 0.00524654 | UNJUDGED | unreviewed [] |

| 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode · #29761](https://github.com/opencv/opencv/issues/29761) | bm25 / 0.00523674 | UNJUDGED | unreviewed [] |

| 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | bm25 / 0.00521695 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02987737 | UNJUDGED | unreviewed [] |

| 3 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | rrf / 0.02928693 | UNJUDGED | unreviewed [] |

| 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | rrf / 0.02913851 | UNJUDGED | unreviewed [] |

| 5 | [modules/core/src/hal_internal.cpp:540:48: error: expected unqualified-id before &#x27;_Complex&#x27; · #29452](https://github.com/opencv/opencv/issues/29452) | rrf / 0.02843889 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.87997431 | UNJUDGED | unreviewed [] |

| 2 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | cosine_similarity / 0.86624408 | UNJUDGED | unreviewed [] |

| 3 | [OpenBLAS detection broken on Fedora/RHEL (headers not found &amp; serial library linked) · #28049](https://github.com/opencv/opencv/issues/28049) | cosine_similarity / 0.86457819 | UNJUDGED | unreviewed [] |

| 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | cosine_similarity / 0.86405349 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | cosine_similarity / 0.86244798 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
OpenCV 4.14.0은 출시됐는데 wiki의 4.x 문서 링크는 4.13.0으로 이동합니다. 5.0 문서 페이지의 버전 선택 메뉴에도 4.14.0은 없고 4.13.0만 보입니다.

[ENVIRONMENT]
온라인 wiki 및 docs.opencv.org의 문서 메뉴</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | rrf / 0.02752976 | UNJUDGED | unreviewed [] |

| 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | rrf / 0.02741784 | UNJUDGED | unreviewed [] |

| 5 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | rrf / 0.02633403 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.90013504 | UNJUDGED | unreviewed [] |

| 2 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | cosine_similarity / 0.89911234 | UNJUDGED | unreviewed [] |

| 3 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | cosine_similarity / 0.88212472 | UNJUDGED | unreviewed [] |

| 4 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | cosine_similarity / 0.87981701 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV.Js link is broken · #29818](https://github.com/opencv/opencv/issues/29818) | cosine_similarity / 0.87611198 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | bm25 / 29.14196907 | UNJUDGED | unreviewed [] |

| 2 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | bm25 / 22.56034036 | UNJUDGED | unreviewed [] |

| 3 | [Breaking changes in mcc modules API not documented in OpenCV 5.0 migration guide · #29705](https://github.com/opencv/opencv/issues/29705) | bm25 / 21.05962027 | UNJUDGED | unreviewed [] |

| 4 | [Python: HoughLinesP return shape changed from (N, 1, 4) to (N, 4) in OpenCV 5.0 · #29637](https://github.com/opencv/opencv/issues/29637) | bm25 / 20.84623661 | UNJUDGED | unreviewed [] |

| 5 | [cv::boundingRect called with cv::Mat_&lt;bool&gt; throws exception in 5.0.0, works in 4.x · #29578](https://github.com/opencv/opencv/issues/29578) | bm25 / 17.42347941 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | rrf / 0.03009050 | UNJUDGED | unreviewed [] |

| 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | rrf / 0.02911605 | UNJUDGED | unreviewed [] |

| 3 | [ctest(opencv_test_imgproc ..............***Failed) · #28382](https://github.com/opencv/opencv/issues/28382) | rrf / 0.02759802 | UNJUDGED | unreviewed [] |

| 4 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13 · #28554](https://github.com/opencv/opencv/issues/28554) | rrf / 0.02738971 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02512484 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.90013504 | UNJUDGED | unreviewed [] |

| 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | cosine_similarity / 0.87981701 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | cosine_similarity / 0.87369084 | UNJUDGED | unreviewed [] |

| 4 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13 · #28554](https://github.com/opencv/opencv/issues/28554) | cosine_similarity / 0.87235606 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV 5 cannot link to zlib · #29325](https://github.com/opencv/opencv/issues/29325) | cosine_similarity / 0.87216586 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [cv::boundingRect called with cv::Mat_&lt;bool&gt; throws exception in 5.0.0, works in 4.x · #29578](https://github.com/opencv/opencv/issues/29578) | bm25 / 14.13105958 | UNJUDGED | unreviewed [] |

| 2 | [cv::connectedComponentsWithStats asserts on input mask of type CV_Bool · #29593](https://github.com/opencv/opencv/issues/29593) | bm25 / 13.86627616 | UNJUDGED | unreviewed [] |

| 3 | [cv::distanceTransform throws exception on input mask of type CV_Bool · #29596](https://github.com/opencv/opencv/issues/29596) | bm25 / 13.64546750 | UNJUDGED | unreviewed [] |

| 4 | [Some OpenCL tests fail on Ubuntu 26.04 LTS · #28919](https://github.com/opencv/opencv/issues/28919) | bm25 / 11.67067405 | UNJUDGED | unreviewed [] |

| 5 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 failed on MSVC · #29072](https://github.com/opencv/opencv/issues/29072) | bm25 / 11.42511113 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
OpenCV 4.14.0 has been released, but the wiki link for the 4.x documentation redirects to 4.13.0. The version menu on the 5.0 documentation page also shows 4.13.0 and does not list 4.14.0.

[ENVIRONMENT]
Online wiki and the documentation version menu at docs.opencv.org</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | cosine_similarity / 0.93551260 | UNJUDGED | unreviewed [] |

| 2 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | cosine_similarity / 0.90919209 | UNJUDGED | unreviewed [] |

| 3 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens) · #28549](https://github.com/opencv/opencv/issues/28549) | cosine_similarity / 0.90217555 | UNJUDGED | unreviewed [] |

| 4 | [DNN: ONNX Conv import fails when kernel_shape is omitted (spec-compliant models) · #28321](https://github.com/opencv/opencv/issues/28321) | cosine_similarity / 0.90067887 | UNJUDGED | unreviewed [] |

| 5 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | cosine_similarity / 0.90029365 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | rrf / 0.02985075 | UNJUDGED | unreviewed [] |

| 4 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens) · #28549](https://github.com/opencv/opencv/issues/28549) | rrf / 0.02957165 | UNJUDGED | unreviewed [] |

| 5 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | rrf / 0.02866503 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [OpenCV 4.14.0 documentation is not available. · #30090](https://github.com/opencv/opencv/issues/30090) | bm25 / 102.75513876 | UNJUDGED | unreviewed [] |

| 2 | [doc: Broken links for nightly and portal documentation on Wiki · #29263](https://github.com/opencv/opencv/issues/29263) | bm25 / 48.99163523 | UNJUDGED | unreviewed [] |

| 3 | [Python: HoughLinesP return shape changed from (N, 1, 4) to (N, 4) in OpenCV 5.0 · #29637](https://github.com/opencv/opencv/issues/29637) | bm25 / 39.35884521 | UNJUDGED | unreviewed [] |

| 4 | [computeECC mishandles unsigned input: 3-channel values saturate and self-correlation can exceed 1 🤖🤖🤖 · #30046](https://github.com/opencv/opencv/issues/30046) | bm25 / 38.65275519 | UNJUDGED | unreviewed [] |

| 5 | [Breaking changes in mcc modules API not documented in OpenCV 5.0 migration guide · #29705](https://github.com/opencv/opencv/issues/29705) | bm25 / 38.51258835 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens) · #28549](https://github.com/opencv/opencv/issues/28549) | cosine_similarity / 0.90217555 | UNJUDGED | unreviewed [] |

| 2 | [DNN: ONNX Conv import fails when kernel_shape is omitted (spec-compliant models) · #28321](https://github.com/opencv/opencv/issues/28321) | cosine_similarity / 0.90067887 | UNJUDGED | unreviewed [] |

| 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball - · #28904](https://github.com/opencv/opencv/issues/28904) | cosine_similarity / 0.90029365 | UNJUDGED | unreviewed [] |

| 4 | [Cannot link OpenCV 5 statically to native code on Android · #29342](https://github.com/opencv/opencv/issues/29342) | cosine_similarity / 0.89999628 | UNJUDGED | unreviewed [] |

| 5 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | cosine_similarity / 0.89577997 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens) · #28549](https://github.com/opencv/opencv/issues/28549) | rrf / 0.03226646 | UNJUDGED | unreviewed [] |

| 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | rrf / 0.03151365 | UNJUDGED | unreviewed [] |

| 3 | [IPP HAL warpAffine INTER_NEAREST is not bit-exact with the native implementation (CV_16S vs CV_16U give different results) · #29279](https://github.com/opencv/opencv/issues/29279) | rrf / 0.02828323 | UNJUDGED | unreviewed [] |

| 4 | [Face Landmark Detector with LBF fails on 5.0.0 but works on 4.14.0 · #29703](https://github.com/opencv/opencv/issues/29703) | rrf / 0.02649573 | UNJUDGED | unreviewed [] |

| 5 | [Cannot link OpenCV 5 statically to native code on Android · #29342](https://github.com/opencv/opencv/issues/29342) | rrf / 0.02604167 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [computeECC mishandles unsigned input: 3-channel values saturate and self-correlation can exceed 1 🤖🤖🤖 · #30046](https://github.com/opencv/opencv/issues/30046) | bm25 / 32.68290109 | UNJUDGED | unreviewed [] |

| 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp · #29694](https://github.com/opencv/opencv/issues/29694) | bm25 / 32.36482531 | UNJUDGED | unreviewed [] |

| 3 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens) · #28549](https://github.com/opencv/opencv/issues/28549) | bm25 / 29.47899143 | UNJUDGED | unreviewed [] |

| 4 | [IPP HAL warpAffine INTER_NEAREST is not bit-exact with the native implementation (CV_16S vs CV_16U give different results) · #29279](https://github.com/opencv/opencv/issues/29279) | bm25 / 27.89485739 | UNJUDGED | unreviewed [] |

| 5 | [Face Landmark Detector with LBF fails on 5.0.0 but works on 4.14.0 · #29703](https://github.com/opencv/opencv/issues/29703) | bm25 / 27.20638755 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
