# O-C2 · opencv/opencv

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [opencv/opencv#29636](https://github.com/opencv/opencv/issues/29636)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
ChArUco 보드에서 마커는 검출되는데 체스보드 코너는 검출되지 않습니다.</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03041475 | UNJUDGED | unreviewed [] |

| 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | rrf / 0.02938653 | UNJUDGED | unreviewed [] |

| 4 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.86647695 | UNJUDGED | unreviewed [] |

| 2 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.85788941 | UNJUDGED | unreviewed [] |

| 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | cosine_similarity / 0.84942341 | UNJUDGED | unreviewed [] |

| 4 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.84742135 | UNJUDGED | unreviewed [] |

| 5 | [Protobuf 6 support · #28325](https://github.com/opencv/opencv/issues/28325) | cosine_similarity / 0.84563017 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 10.59881187 | UNJUDGED | unreviewed [] |

| 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 8.00247830 | UNJUDGED | unreviewed [] |

| 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | bm25 / 6.26477174 | UNJUDGED | unreviewed [] |

| 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 2.66720063 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03062179 | UNJUDGED | unreviewed [] |

| 3 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.86647695 | UNJUDGED | unreviewed [] |

| 2 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.85788941 | UNJUDGED | unreviewed [] |

| 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined · #29265](https://github.com/opencv/opencv/issues/29265) | cosine_similarity / 0.84942341 | UNJUDGED | unreviewed [] |

| 4 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.84742135 | UNJUDGED | unreviewed [] |

| 5 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | cosine_similarity / 0.84548271 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 10.05999742 | UNJUDGED | unreviewed [] |

| 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 7.76428540 | UNJUDGED | unreviewed [] |

| 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 2.89732019 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
동일 파라미터의 8x6 ChArUco 보드 중 OpenCV로 생성한 보드에서는 마커와 코너가 모두 검출됩니다. calib.io로 생성한 보드에서는 마커만 검출되고 코너가 나오지 않습니다. CharucoDetector.detectBoard를 사용합니다.

[ENVIRONMENT]
opencv-python 4.14.0.94; macOS ARM; DICT_4X4_50, square length 35 mm, marker length 24 mm</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | rrf / 0.03151365 | UNJUDGED | unreviewed [] |

| 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03079839 | UNJUDGED | unreviewed [] |

| 5 | [Fails to build · #29435](https://github.com/opencv/opencv/issues/29435) | rrf / 0.02598701 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 92.34386173 | UNJUDGED | unreviewed [] |

| 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | bm25 / 40.27147538 | UNJUDGED | unreviewed [] |

| 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 27.83529073 | UNJUDGED | unreviewed [] |

| 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 26.39284647 | UNJUDGED | unreviewed [] |

| 5 | [AVFOUNDATION backend issue on iOSSimulator · #28666](https://github.com/opencv/opencv/issues/28666) | bm25 / 25.57859079 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.91226959 | UNJUDGED | unreviewed [] |

| 2 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.89293194 | UNJUDGED | unreviewed [] |

| 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | cosine_similarity / 0.88731134 | UNJUDGED | unreviewed [] |

| 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | cosine_similarity / 0.88698077 | UNJUDGED | unreviewed [] |

| 5 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | cosine_similarity / 0.88640118 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 4 | [Fails to build · #29435](https://github.com/opencv/opencv/issues/29435) | rrf / 0.02734664 | UNJUDGED | unreviewed [] |

| 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | rrf / 0.02686096 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 94.01652556 | UNJUDGED | unreviewed [] |

| 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 27.24951298 | UNJUDGED | unreviewed [] |

| 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 26.88178256 | UNJUDGED | unreviewed [] |

| 4 | [AVFOUNDATION backend issue on iOSSimulator · #28666](https://github.com/opencv/opencv/issues/28666) | bm25 / 24.65381364 | UNJUDGED | unreviewed [] |

| 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 23.75234500 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.91226959 | UNJUDGED | unreviewed [] |

| 2 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.89293194 | UNJUDGED | unreviewed [] |

| 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | cosine_similarity / 0.88731134 | UNJUDGED | unreviewed [] |

| 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors · #28241](https://github.com/opencv/opencv/issues/28241) | cosine_similarity / 0.88698077 | UNJUDGED | unreviewed [] |

| 5 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp · #29278](https://github.com/opencv/opencv/issues/29278) | cosine_similarity / 0.88065583 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
For 8x6 ChArUco boards with the same parameters, the OpenCV-generated board produces both markers and corners. A board generated with calib.io produces markers but no corners. I use CharucoDetector.detectBoard.

[ENVIRONMENT]
opencv-python 4.14.0.94; macOS ARM; DICT_4X4_50, square length 35 mm, marker length 24 mm</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 177.50171456 | UNJUDGED | unreviewed [] |

| 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | bm25 / 105.61574945 | UNJUDGED | unreviewed [] |

| 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 60.23394478 | UNJUDGED | unreviewed [] |

| 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 34.62968805 | UNJUDGED | unreviewed [] |

| 5 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (regression in 4.14.0) · #30017](https://github.com/opencv/opencv/issues/30017) | bm25 / 33.06742500 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | rrf / 0.03105441 | UNJUDGED | unreviewed [] |

| 4 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | rrf / 0.03100962 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.92726880 | UNJUDGED | unreviewed [] |

| 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | cosine_similarity / 0.90580022 | UNJUDGED | unreviewed [] |

| 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0) · #28953](https://github.com/opencv/opencv/issues/28953) | cosine_similarity / 0.90543783 | UNJUDGED | unreviewed [] |

| 4 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.90518284 | UNJUDGED | unreviewed [] |

| 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | cosine_similarity / 0.89974391 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | bm25 / 177.86835379 | UNJUDGED | unreviewed [] |

| 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | bm25 / 57.18546179 | UNJUDGED | unreviewed [] |

| 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | bm25 / 35.52228766 | UNJUDGED | unreviewed [] |

| 4 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | bm25 / 29.52826400 | UNJUDGED | unreviewed [] |

| 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel format changes mid-stream · #29699](https://github.com/opencv/opencv/issues/29699) | bm25 / 28.98009001 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | rrf / 0.03175403 | UNJUDGED | unreviewed [] |

| 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | rrf / 0.03151365 | UNJUDGED | unreviewed [] |

| 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 5 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | rrf / 0.02837302 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Charuco corner detection fails, while markers are detected. · #29636](https://github.com/opencv/opencv/issues/29636) | cosine_similarity / 0.92726880 | UNJUDGED | unreviewed [] |

| 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12 · #28028](https://github.com/opencv/opencv/issues/28028) | cosine_similarity / 0.90580022 | UNJUDGED | unreviewed [] |

| 3 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings · #28512](https://github.com/opencv/opencv/issues/28512) | cosine_similarity / 0.90518284 | UNJUDGED | unreviewed [] |

| 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0 · #29692](https://github.com/opencv/opencv/issues/29692) | cosine_similarity / 0.89974391 | UNJUDGED | unreviewed [] |

| 5 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco markers · #28783](https://github.com/opencv/opencv/issues/28783) | cosine_similarity / 0.89464730 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
