# 사례별 질의와 실제 Top-5

개발 표본이며 질의·관련성은 사람 검토 전입니다. 원문 회수는 정답 판정이 아닙니다. 점수는 BM25/코사인/RRF 각각의 척도이며 확률이나 공통 척도가 아닙니다.

## O-E1 — core_development

참고 원문: [opencv/opencv#29350](https://github.com/opencv/opencv/issues/29350). 유형: `error_literal`.

빌드 중 실제 선언 누락 오류. 별도 성공 설정의 비교가 아닌 컴파일 예외 중심.

### A_ko_symptom

```text
[PROBLEM]
CMake로 OpenCV 빌드 파일을 만든 뒤 MinGW로 컴파일하면 중간에 빌드가 멈춥니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.031258 | UNJUDGED |
| C_raw | hybrid | 2 | [SIGSEGV in TSDF integrate](https://github.com/opencv/opencv/issues/29763) | closed; bug | 0.029631 | UNJUDGED |
| C_raw | hybrid | 3 | [Unable to build with CUDA](https://github.com/opencv/opencv/issues/28952) | closed; bug, category: build/install, category: gpu/cuda (contrib) | 0.028382 | UNJUDGED |
| C_raw | hybrid | 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.028219 | UNJUDGED |
| C_raw | hybrid | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.028219 | UNJUDGED |
| C_raw | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.885001 | UNJUDGED |
| C_raw | semantic | 2 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.884599 | UNJUDGED |
| C_raw | semantic | 3 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.883488 | UNJUDGED |
| C_raw | semantic | 4 | [Out-of-bounds read in AVX2 bilateralFilter 32f path](https://github.com/opencv/opencv/issues/28254) | closed; bug, optimization | 0.882311 | UNJUDGED |
| C_raw | semantic | 5 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.881503 | UNJUDGED |
| C_raw | bm25 | 1 | [Warnings in Windows for ARM build in 4.x](https://github.com/opencv/opencv/issues/30095) | open; bug, category: build/install, platform: win32 | 0.132483 | UNJUDGED |
| C_raw | bm25 | 2 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.131964 | UNJUDGED |
| C_raw | bm25 | 3 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.131619 | UNJUDGED |
| C_raw | bm25 | 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.130945 | UNJUDGED |
| C_raw | bm25 | 5 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.130846 | UNJUDGED |
| C_bug | hybrid | 1 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.031258 | UNJUDGED |
| C_bug | hybrid | 2 | [SIGSEGV in TSDF integrate](https://github.com/opencv/opencv/issues/29763) | closed; bug | 0.029631 | UNJUDGED |
| C_bug | hybrid | 3 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.028694 | UNJUDGED |
| C_bug | hybrid | 4 | [Unable to build with CUDA](https://github.com/opencv/opencv/issues/28952) | closed; bug, category: build/install, category: gpu/cuda (contrib) | 0.028577 | UNJUDGED |
| C_bug | hybrid | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.028405 | UNJUDGED |
| C_bug | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.885001 | UNJUDGED |
| C_bug | semantic | 2 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.884599 | UNJUDGED |
| C_bug | semantic | 3 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.883488 | UNJUDGED |
| C_bug | semantic | 4 | [Out-of-bounds read in AVX2 bilateralFilter 32f path](https://github.com/opencv/opencv/issues/28254) | closed; bug, optimization | 0.882311 | UNJUDGED |
| C_bug | semantic | 5 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.881503 | UNJUDGED |
| C_bug | bm25 | 1 | [Warnings in Windows for ARM build in 4.x](https://github.com/opencv/opencv/issues/30095) | open; bug, category: build/install, platform: win32 | 0.005259 | UNJUDGED |
| C_bug | bm25 | 2 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.005247 | UNJUDGED |
| C_bug | bm25 | 3 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.005237 | UNJUDGED |
| C_bug | bm25 | 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.005217 | UNJUDGED |
| C_bug | bm25 | 5 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.005214 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
CMake로 OpenCV 빌드 파일을 만든 뒤 mingw32-make로 컴파일하면 두 곳에서 같은 선언 누락 오류로 빌드가 멈춥니다. 추가 빌드 설정은 하지 않았습니다.

[ERROR]
error: 'posix_memalign' was not declared in this scope

[ENVIRONMENT]
OpenCV 5.0.0, Windows 11, MinGW GCC 16.1.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 72.429830 | UNJUDGED |
| C_raw | bm25 | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 31.090369 | UNJUDGED |
| C_raw | bm25 | 3 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing &lt;cstdint&gt; in ADE)](https://github.com/opencv/opencv/issues/29564) | closed; bug | 27.159343 | UNJUDGED |
| C_raw | bm25 | 4 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | closed; bug, category: build/install, platform: win32 | 24.275286 | UNJUDGED |
| C_raw | bm25 | 5 | [solvePnPRefineLM/VVS: out-of-bounds read, silent no-op, and exception when rvec/tvec are row vectors](https://github.com/opencv/opencv/issues/29747) | closed; bug, category: calib3d | 23.235723 | UNJUDGED |
| C_raw | hybrid | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.031514 | UNJUDGED |
| C_raw | hybrid | 3 | [CMake: opencv_world with core and imgproc fails with &quot;Unknown CMake command ocv_imgcodecs_configure_](https://github.com/opencv/opencv/issues/29778) | closed; category: build/install | 0.028577 | UNJUDGED |
| C_raw | hybrid | 4 | [allocation/write-width mismatch in AKAZE generateDescriptorSubsample when descriptor_channels &lt; 3](https://github.com/opencv/opencv/issues/29613) | closed; bug | 0.028083 | UNJUDGED |
| C_raw | hybrid | 5 | [oob read in Domain_Filter::compute_NCfilter when cv::stylization is given a single-column image](https://github.com/opencv/opencv/issues/29614) | closed; bug | 0.027619 | UNJUDGED |
| C_raw | semantic | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.929615 | UNJUDGED |
| C_raw | semantic | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.902415 | UNJUDGED |
| C_raw | semantic | 3 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.898633 | UNJUDGED |
| C_raw | semantic | 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.895527 | UNJUDGED |
| C_raw | semantic | 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.893588 | UNJUDGED |
| C_bug | bm25 | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 67.346751 | UNJUDGED |
| C_bug | bm25 | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 27.792485 | UNJUDGED |
| C_bug | bm25 | 3 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing &lt;cstdint&gt; in ADE)](https://github.com/opencv/opencv/issues/29564) | closed; bug | 22.808445 | UNJUDGED |
| C_bug | bm25 | 4 | [solvePnPRefineLM/VVS: out-of-bounds read, silent no-op, and exception when rvec/tvec are row vectors](https://github.com/opencv/opencv/issues/29747) | closed; bug, category: calib3d | 21.075658 | UNJUDGED |
| C_bug | bm25 | 5 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | closed; bug, category: build/install, platform: win32 | 20.873417 | UNJUDGED |
| C_bug | hybrid | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.031514 | UNJUDGED |
| C_bug | hybrid | 3 | [allocation/write-width mismatch in AKAZE generateDescriptorSubsample when descriptor_channels &lt; 3](https://github.com/opencv/opencv/issues/29613) | closed; bug | 0.028665 | UNJUDGED |
| C_bug | hybrid | 4 | [oob read in Domain_Filter::compute_NCfilter when cv::stylization is given a single-column image](https://github.com/opencv/opencv/issues/29614) | closed; bug | 0.028191 | UNJUDGED |
| C_bug | hybrid | 5 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.027623 | UNJUDGED |
| C_bug | semantic | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.929615 | UNJUDGED |
| C_bug | semantic | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.902415 | UNJUDGED |
| C_bug | semantic | 3 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.898633 | UNJUDGED |
| C_bug | semantic | 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.895527 | UNJUDGED |
| C_bug | semantic | 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.893588 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
After generating the OpenCV build files with CMake, mingw32-make stops compilation in two places with the same missing declaration error. I have not added extra build settings.

[ERROR]
error: 'posix_memalign' was not declared in this scope

[ENVIRONMENT]
OpenCV 5.0.0, Windows 11, MinGW GCC 16.1.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.938026 | UNJUDGED |
| C_raw | semantic | 2 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.908415 | UNJUDGED |
| C_raw | semantic | 3 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.906090 | UNJUDGED |
| C_raw | semantic | 4 | [OpenCV v_lut_pairs SSE Intrinsic Misaligned Memory Access](https://github.com/opencv/opencv/issues/28597) | closed; wontfix, category: core | 0.904894 | UNJUDGED |
| C_raw | semantic | 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.900403 | UNJUDGED |
| C_raw | hybrid | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.030769 | UNJUDGED |
| C_raw | hybrid | 3 | [OpenCV v_lut_pairs SSE Intrinsic Misaligned Memory Access](https://github.com/opencv/opencv/issues/28597) | closed; wontfix, category: core | 0.028783 | UNJUDGED |
| C_raw | hybrid | 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.028531 | UNJUDGED |
| C_raw | hybrid | 5 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.028177 | UNJUDGED |
| C_raw | bm25 | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 101.616327 | UNJUDGED |
| C_raw | bm25 | 2 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | closed; bug, category: build/install, platform: win32 | 44.730794 | UNJUDGED |
| C_raw | bm25 | 3 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing &lt;cstdint&gt; in ADE)](https://github.com/opencv/opencv/issues/29564) | closed; bug | 43.503879 | UNJUDGED |
| C_raw | bm25 | 4 | [dnn: vendored MLAS cannot be built on Windows/x86 — CMakeLists assumes a GCC driver (OpenCV 5.0.0)](https://github.com/opencv/opencv/issues/29885) | open; bug, category: build/install, platform: win32, category: 3rdparty | 41.843416 | UNJUDGED |
| C_raw | bm25 | 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 39.422341 | UNJUDGED |
| C_bug | semantic | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.938026 | UNJUDGED |
| C_bug | semantic | 2 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.908415 | UNJUDGED |
| C_bug | semantic | 3 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.906090 | UNJUDGED |
| C_bug | semantic | 4 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.900403 | UNJUDGED |
| C_bug | semantic | 5 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.899778 | UNJUDGED |
| C_bug | hybrid | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | closed; bug, category: build/install | 0.030777 | UNJUDGED |
| C_bug | hybrid | 3 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.028860 | UNJUDGED |
| C_bug | hybrid | 4 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | closed; bug, category: core | 0.028629 | UNJUDGED |
| C_bug | hybrid | 5 | [dnn: vendored MLAS cannot be built on Windows/x86 — CMakeLists assumes a GCC driver (OpenCV 5.0.0)](https://github.com/opencv/opencv/issues/29885) | open; bug, category: build/install, platform: win32, category: 3rdparty | 0.028475 | UNJUDGED |
| C_bug | bm25 | 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | closed; bug, category: build/install, platform: win32 | 94.100874 | UNJUDGED |
| C_bug | bm25 | 2 | [dnn: vendored MLAS cannot be built on Windows/x86 — CMakeLists assumes a GCC driver (OpenCV 5.0.0)](https://github.com/opencv/opencv/issues/29885) | open; bug, category: build/install, platform: win32, category: 3rdparty | 38.621000 | UNJUDGED |
| C_bug | bm25 | 3 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | closed; bug, category: build/install, platform: win32 | 37.511210 | UNJUDGED |
| C_bug | bm25 | 4 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing &lt;cstdint&gt; in ADE)](https://github.com/opencv/opencv/issues/29564) | closed; bug | 35.292790 | UNJUDGED |
| C_bug | bm25 | 5 | [solvePnPRefineLM/VVS: out-of-bounds read, silent no-op, and exception when rvec/tvec are row vectors](https://github.com/opencv/opencv/issues/29747) | closed; bug, category: calib3d | 33.014968 | UNJUDGED |

## O-E2 — core_development

참고 원문: [opencv/opencv#28525](https://github.com/opencv/opencv/issues/28525). 유형: `error_literal`.

import 시 실제 공유 라이브러리 오류가 핵심 단서. OS는 보고된 배경이며 성공 조건 비교 없음.

### A_ko_symptom

```text
[PROBLEM]
GitHub Actions에서 설치한 OpenCV를 Python으로 불러오면 import 단계에서 실패합니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.893183 | UNJUDGED |
| C_raw | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.892055 | UNJUDGED |
| C_raw | semantic | 3 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.884495 | UNJUDGED |
| C_raw | semantic | 4 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.883041 | UNJUDGED |
| C_raw | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.881962 | UNJUDGED |
| C_raw | hybrid | 1 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.032522 | UNJUDGED |
| C_raw | hybrid | 2 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032018 | UNJUDGED |
| C_raw | hybrid | 3 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 0.029762 | UNJUDGED |
| C_raw | hybrid | 4 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.029287 | UNJUDGED |
| C_raw | hybrid | 5 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.027746 | UNJUDGED |
| C_raw | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 5.801647 | UNJUDGED |
| C_raw | bm25 | 2 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 5.333629 | UNJUDGED |
| C_raw | bm25 | 3 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 5.281531 | UNJUDGED |
| C_raw | bm25 | 4 | [QRCode Decode didn&#x27;t read a specific string](https://github.com/opencv/opencv/issues/29540) | open; bug, category: objdetect | 5.059628 | UNJUDGED |
| C_raw | bm25 | 5 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 5.035592 | UNJUDGED |
| C_bug | semantic | 1 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.893183 | UNJUDGED |
| C_bug | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.892055 | UNJUDGED |
| C_bug | semantic | 3 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.884495 | UNJUDGED |
| C_bug | semantic | 4 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.883041 | UNJUDGED |
| C_bug | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.881962 | UNJUDGED |
| C_bug | hybrid | 1 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.032522 | UNJUDGED |
| C_bug | hybrid | 2 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032018 | UNJUDGED |
| C_bug | hybrid | 3 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.030415 | UNJUDGED |
| C_bug | hybrid | 4 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 0.030159 | UNJUDGED |
| C_bug | hybrid | 5 | [cv2.imshow hangs on 4.13.0.90/92](https://github.com/opencv/opencv/issues/29195) | open; bug, category: highgui-gui, category: 3rdparty | 0.027425 | UNJUDGED |
| C_bug | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 5.779582 | UNJUDGED |
| C_bug | bm25 | 2 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 5.409451 | UNJUDGED |
| C_bug | bm25 | 3 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 5.327960 | UNJUDGED |
| C_bug | bm25 | 4 | [QRCode Decode didn&#x27;t read a specific string](https://github.com/opencv/opencv/issues/29540) | open; bug, category: objdetect | 5.101276 | UNJUDGED |
| C_bug | bm25 | 5 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 5.054230 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
GitHub Actions에서 opencv_contrib_python_rolling을 설치한 Python 프로젝트가 cv2 import 단계에서 실패합니다. 공유 라이브러리를 include 디렉터리에 링크하고 LD_LIBRARY_PATH에도 넣었습니다.

[ERROR]
ImportError: libavcodec.so.58: cannot open shared object file: No such file or directory

[ENVIRONMENT]
ubuntu-latest / Ubuntu 24.04; Python 3.12, 3.13, 3.14
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.928455 | UNJUDGED |
| C_raw | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.911397 | UNJUDGED |
| C_raw | semantic | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.886113 | UNJUDGED |
| C_raw | semantic | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.885559 | UNJUDGED |
| C_raw | semantic | 5 | [compile error &quot;unknown target CPU &#x27;armv8-a&#x27;&quot; on macOS  with KleidiCV](https://github.com/opencv/opencv/issues/28187) | open; bug, category: build/install, platform: ios/osx, platform: arm | 0.883152 | UNJUDGED |
| C_raw | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 146.325633 | UNJUDGED |
| C_raw | bm25 | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 64.799540 | UNJUDGED |
| C_raw | bm25 | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 51.894655 | UNJUDGED |
| C_raw | bm25 | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 47.087800 | UNJUDGED |
| C_raw | bm25 | 5 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 42.078522 | UNJUDGED |
| C_raw | hybrid | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.031746 | UNJUDGED |
| C_raw | hybrid | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.031250 | UNJUDGED |
| C_raw | hybrid | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.029857 | UNJUDGED |
| C_bug | semantic | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.928455 | UNJUDGED |
| C_bug | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.911397 | UNJUDGED |
| C_bug | semantic | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.886113 | UNJUDGED |
| C_bug | semantic | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.885559 | UNJUDGED |
| C_bug | semantic | 5 | [compile error &quot;unknown target CPU &#x27;armv8-a&#x27;&quot; on macOS  with KleidiCV](https://github.com/opencv/opencv/issues/28187) | open; bug, category: build/install, platform: ios/osx, platform: arm | 0.883152 | UNJUDGED |
| C_bug | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 137.960176 | UNJUDGED |
| C_bug | bm25 | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 63.359891 | UNJUDGED |
| C_bug | bm25 | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 49.931358 | UNJUDGED |
| C_bug | bm25 | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 44.433990 | UNJUDGED |
| C_bug | bm25 | 5 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 40.617801 | UNJUDGED |
| C_bug | hybrid | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.031746 | UNJUDGED |
| C_bug | hybrid | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.031250 | UNJUDGED |
| C_bug | hybrid | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.030077 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
A Python project using opencv_contrib_python_rolling fails while importing cv2 in GitHub Actions. Shared libraries were symlinked into an include directory which was also added to LD_LIBRARY_PATH.

[ERROR]
ImportError: libavcodec.so.58: cannot open shared object file: No such file or directory

[ENVIRONMENT]
ubuntu-latest / Ubuntu 24.04; Python 3.12, 3.13, 3.14
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.931989 | UNJUDGED |
| C_raw | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.901207 | UNJUDGED |
| C_raw | semantic | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.897567 | UNJUDGED |
| C_raw | semantic | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.894047 | UNJUDGED |
| C_raw | semantic | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.888317 | UNJUDGED |
| C_raw | hybrid | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.031498 | UNJUDGED |
| C_raw | hybrid | 4 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.031498 | UNJUDGED |
| C_raw | hybrid | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.030769 | UNJUDGED |
| C_raw | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 186.186191 | UNJUDGED |
| C_raw | bm25 | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 73.730136 | UNJUDGED |
| C_raw | bm25 | 3 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 62.510086 | UNJUDGED |
| C_raw | bm25 | 4 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 58.609727 | UNJUDGED |
| C_raw | bm25 | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 56.814282 | UNJUDGED |
| C_bug | semantic | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.931989 | UNJUDGED |
| C_bug | semantic | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.901207 | UNJUDGED |
| C_bug | semantic | 3 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.897567 | UNJUDGED |
| C_bug | semantic | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.894047 | UNJUDGED |
| C_bug | semantic | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.888317 | UNJUDGED |
| C_bug | hybrid | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.031498 | UNJUDGED |
| C_bug | hybrid | 4 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 0.031498 | UNJUDGED |
| C_bug | hybrid | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.030769 | UNJUDGED |
| C_bug | bm25 | 1 | [Ubuntu 24.04 FFmpeg: ImportError: libavcodec.so.58: cannot open shared object file: No such file or ](https://github.com/opencv/opencv/issues/28525) | open; bug, category: build/install, incomplete | 175.267260 | UNJUDGED |
| C_bug | bm25 | 2 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 71.862659 | UNJUDGED |
| C_bug | bm25 | 3 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 60.681781 | UNJUDGED |
| C_bug | bm25 | 4 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 55.480633 | UNJUDGED |
| C_bug | bm25 | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 54.342323 | UNJUDGED |

## O-S1 — core_development

참고 원문: [opencv/opencv#29565](https://github.com/opencv/opencv/issues/29565). 유형: `symptom_without_error`.

핵심 예외 문구 없이 Python API 속성이 없다고 관찰함. 이전 버전 성공은 관찰되지 않음.

### A_ko_symptom

```text
[PROBLEM]
Python OpenCV에서 손과 눈 보정용 calibrateHandEye 함수를 사용할 수 없습니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 14.700679 | UNJUDGED |
| C_raw | bm25 | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 13.299376 | UNJUDGED |
| C_raw | bm25 | 3 | [[Feature] Expose per-instance cv::RNG objects in Python bindings](https://github.com/opencv/opencv/issues/29591) | open; category: python bindings | 2.882387 | UNJUDGED |
| C_raw | bm25 | 4 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 2.853051 | UNJUDGED |
| C_raw | bm25 | 5 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 2.801711 | UNJUDGED |
| C_raw | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 0.030090 | UNJUDGED |
| C_raw | hybrid | 4 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.028612 | UNJUDGED |
| C_raw | hybrid | 5 | [cv2.dnn.blobFromImage fails for 2-D grayscale NumPy input (Python only)](https://github.com/opencv/opencv/issues/28358) | closed;  | 0.028259 | UNJUDGED |
| C_raw | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.912566 | UNJUDGED |
| C_raw | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.886662 | UNJUDGED |
| C_raw | semantic | 3 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.885018 | UNJUDGED |
| C_raw | semantic | 4 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.878429 | UNJUDGED |
| C_raw | semantic | 5 | [k3 parameter and 1x4 distortion input in calibrateCamera](https://github.com/opencv/opencv/issues/29817) | closed; category: documentation, category: calib3d | 0.878170 | UNJUDGED |
| C_bug | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 13.965774 | UNJUDGED |
| C_bug | bm25 | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 12.955145 | UNJUDGED |
| C_bug | bm25 | 3 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 3.109836 | UNJUDGED |
| C_bug | bm25 | 4 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 3.048782 | UNJUDGED |
| C_bug | bm25 | 5 | [Python: reference leak in `pyopencv_to` modules/python/src2/cv2_convert.cpp](https://github.com/opencv/opencv/issues/28046) | closed; bug, category: python bindings | 3.021643 | UNJUDGED |
| C_bug | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 0.030550 | UNJUDGED |
| C_bug | hybrid | 4 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.029710 | UNJUDGED |
| C_bug | hybrid | 5 | [OpenBLAS detection broken on Fedora/RHEL (headers not found &amp; serial library linked)](https://github.com/opencv/opencv/issues/28049) | closed; bug, category: build/install, platform: linux | 0.029040 | UNJUDGED |
| C_bug | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.912566 | UNJUDGED |
| C_bug | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.886662 | UNJUDGED |
| C_bug | semantic | 3 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.885018 | UNJUDGED |
| C_bug | semantic | 4 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.878429 | UNJUDGED |
| C_bug | semantic | 5 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.873716 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Python OpenCV의 calibrateHandEye 함수를 쓰려는데 cv2에 해당 속성이 없습니다. hasattr로 확인해도 False가 나오며 마이그레이션 안내에서는 Python 보정 함수가 바뀌지 않았다고 합니다.

[ENVIRONMENT]
opencv-contrib-python 5.0.0.93; Ubuntu 24 Docker 컨테이너, Arch Linux 호스트
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.030769 | UNJUDGED |
| C_raw | hybrid | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.029287 | UNJUDGED |
| C_raw | hybrid | 4 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.028814 | UNJUDGED |
| C_raw | hybrid | 5 | [MSER::detectRegions() finds 0 regions on OpenCV 5.0.0 where 4.13.0 finds 2, with identical default p](https://github.com/opencv/opencv/issues/29652) | closed;  | 0.028177 | UNJUDGED |
| C_raw | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.930035 | UNJUDGED |
| C_raw | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.891614 | UNJUDGED |
| C_raw | semantic | 3 | [opencv_test_imgproc failed when upgraded to 4.13.0 version](https://github.com/opencv/opencv/issues/28383) | open; bug, category: imgproc | 0.885335 | UNJUDGED |
| C_raw | semantic | 4 | [Imgproc_ConnectedComponents tests fail on Alpine Linux](https://github.com/opencv/opencv/issues/29035) | closed; bug, category: imgproc | 0.885037 | UNJUDGED |
| C_raw | semantic | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.884614 | UNJUDGED |
| C_raw | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 61.089516 | UNJUDGED |
| C_raw | bm25 | 2 | [MSER::detectRegions() finds 0 regions on OpenCV 5.0.0 where 4.13.0 finds 2, with identical default p](https://github.com/opencv/opencv/issues/29652) | closed;  | 32.379183 | UNJUDGED |
| C_raw | bm25 | 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 32.227260 | UNJUDGED |
| C_raw | bm25 | 4 | [[MLAS] Build failure on s390x due to missing SgemmKernelZVECTOR.h and FgemmKernelZVECTOR.h headers](https://github.com/opencv/opencv/issues/29465) | closed; bug, category: build/install, category: dnn, category: 3rdparty | 28.421361 | UNJUDGED |
| C_raw | bm25 | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 28.166189 | UNJUDGED |
| C_bug | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.031010 | UNJUDGED |
| C_bug | hybrid | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.030835 | UNJUDGED |
| C_bug | hybrid | 4 | [ImportError after upgrading from 4.12.0.88 to 4.13.0.90 on linux/aarch64, missing libxcb.so.1](https://github.com/opencv/opencv/issues/28438) | closed; bug, category: python bindings, priority: high, category: build/install | 0.029010 | UNJUDGED |
| C_bug | hybrid | 5 | [cv2.linemod.match causes segmentation fault with Python 3.13](https://github.com/opencv/opencv/issues/29576) | open; bug | 0.028309 | UNJUDGED |
| C_bug | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.930035 | UNJUDGED |
| C_bug | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.891614 | UNJUDGED |
| C_bug | semantic | 3 | [opencv_test_imgproc failed when upgraded to 4.13.0 version](https://github.com/opencv/opencv/issues/28383) | open; bug, category: imgproc | 0.885335 | UNJUDGED |
| C_bug | semantic | 4 | [Imgproc_ConnectedComponents tests fail on Alpine Linux](https://github.com/opencv/opencv/issues/29035) | closed; bug, category: imgproc | 0.885037 | UNJUDGED |
| C_bug | semantic | 5 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 0.884614 | UNJUDGED |
| C_bug | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 58.135330 | UNJUDGED |
| C_bug | bm25 | 2 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 31.505588 | UNJUDGED |
| C_bug | bm25 | 3 | [[MLAS] Build failure on s390x due to missing SgemmKernelZVECTOR.h and FgemmKernelZVECTOR.h headers](https://github.com/opencv/opencv/issues/29465) | closed; bug, category: build/install, category: dnn, category: 3rdparty | 28.261647 | UNJUDGED |
| C_bug | bm25 | 4 | [[MLAS] Build failure on loongarch64 due to missing include directory for ASM](https://github.com/opencv/opencv/issues/29422) | closed; bug, category: 3rdparty, platform: loongson | 27.127629 | UNJUDGED |
| C_bug | bm25 | 5 | [QRCodeDetector: detectAndDecodeMulti throws StsNotImplemented (&quot;mode 13&quot;) on valid Hanzi-mode (GB/T ](https://github.com/opencv/opencv/issues/30110) | open; bug | 20.901879 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
I need calibrateHandEye in Python OpenCV, but cv2 does not have that attribute. Checking with hasattr returns False, although the migration guide says the Python calibration functions have not changed.

[ENVIRONMENT]
opencv-contrib-python 5.0.0.93; Ubuntu 24 Docker container on an Arch Linux host
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [MSER::detectRegions() finds 0 regions on OpenCV 5.0.0 where 4.13.0 finds 2, with identical default p](https://github.com/opencv/opencv/issues/29652) | closed;  | 0.030415 | UNJUDGED |
| C_raw | hybrid | 3 | [Breaking changes in mcc modules API not documented in OpenCV 5.0 migration guide](https://github.com/opencv/opencv/issues/29705) | open;  | 0.030303 | UNJUDGED |
| C_raw | hybrid | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.029116 | UNJUDGED |
| C_raw | hybrid | 5 | [[Bug] Python bindings silently reinterpret HWC arrays above 128 channels in OpenCV 5](https://github.com/opencv/opencv/issues/29586) | closed; category: imgproc | 0.028439 | UNJUDGED |
| C_raw | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.950345 | UNJUDGED |
| C_raw | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.902525 | UNJUDGED |
| C_raw | semantic | 3 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.893017 | UNJUDGED |
| C_raw | semantic | 4 | [resize(): SIGSEGV for CV_8UC3 with INTER_LINEAR on arm64 macOS at scale factors just below 1.0 (work](https://github.com/opencv/opencv/issues/29794) | open; bug, category: imgproc, platform: android, platform: ios/osx, platform: arm, category: 3rdparty | 0.892496 | UNJUDGED |
| C_raw | semantic | 5 | [cv2.omnidir.calibrate Assertion Failure](https://github.com/opencv/opencv/issues/28462) | open; bug | 0.890522 | UNJUDGED |
| C_raw | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 98.208077 | UNJUDGED |
| C_raw | bm25 | 2 | [MSER::detectRegions() finds 0 regions on OpenCV 5.0.0 where 4.13.0 finds 2, with identical default p](https://github.com/opencv/opencv/issues/29652) | closed;  | 45.328964 | UNJUDGED |
| C_raw | bm25 | 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 41.546355 | UNJUDGED |
| C_raw | bm25 | 4 | [[MLAS] Build failure on s390x due to missing SgemmKernelZVECTOR.h and FgemmKernelZVECTOR.h headers](https://github.com/opencv/opencv/issues/29465) | closed; bug, category: build/install, category: dnn, category: 3rdparty | 39.351514 | UNJUDGED |
| C_raw | bm25 | 5 | [[Feature] Expose per-instance cv::RNG objects in Python bindings](https://github.com/opencv/opencv/issues/29591) | open; category: python bindings | 39.328965 | UNJUDGED |
| C_bug | hybrid | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.030835 | UNJUDGED |
| C_bug | hybrid | 3 | [cv2.omnidir.calibrate Assertion Failure](https://github.com/opencv/opencv/issues/28462) | open; bug | 0.028718 | UNJUDGED |
| C_bug | hybrid | 4 | [[MLAS] Build failure on s390x due to missing SgemmKernelZVECTOR.h and FgemmKernelZVECTOR.h headers](https://github.com/opencv/opencv/issues/29465) | closed; bug, category: build/install, category: dnn, category: 3rdparty | 0.028373 | UNJUDGED |
| C_bug | hybrid | 5 | [resize(): SIGSEGV for CV_8UC3 with INTER_LINEAR on arm64 macOS at scale factors just below 1.0 (work](https://github.com/opencv/opencv/issues/29794) | open; bug, category: imgproc, platform: android, platform: ios/osx, platform: arm, category: 3rdparty | 0.027820 | UNJUDGED |
| C_bug | semantic | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 0.950345 | UNJUDGED |
| C_bug | semantic | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.902525 | UNJUDGED |
| C_bug | semantic | 3 | [calibrateCamera function missing \| None on cameraMatrix and distCoeffs in Python type stubs](https://github.com/opencv/opencv/issues/28469) | closed; bug, category: python bindings, category: samples | 0.893017 | UNJUDGED |
| C_bug | semantic | 4 | [resize(): SIGSEGV for CV_8UC3 with INTER_LINEAR on arm64 macOS at scale factors just below 1.0 (work](https://github.com/opencv/opencv/issues/29794) | open; bug, category: imgproc, platform: android, platform: ios/osx, platform: arm, category: 3rdparty | 0.892496 | UNJUDGED |
| C_bug | semantic | 5 | [cv2.omnidir.calibrate Assertion Failure](https://github.com/opencv/opencv/issues/28462) | open; bug | 0.890522 | UNJUDGED |
| C_bug | bm25 | 1 | [calibrateHandEye is missing in python package for version 5.0.0.93](https://github.com/opencv/opencv/issues/29565) | closed; bug, category: python bindings | 95.077389 | UNJUDGED |
| C_bug | bm25 | 2 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 39.849680 | UNJUDGED |
| C_bug | bm25 | 3 | [[MLAS] Build failure on s390x due to missing SgemmKernelZVECTOR.h and FgemmKernelZVECTOR.h headers](https://github.com/opencv/opencv/issues/29465) | closed; bug, category: build/install, category: dnn, category: 3rdparty | 37.676376 | UNJUDGED |
| C_bug | bm25 | 4 | [opencv-python-headless shadows stdlib typing when cv2 package directory is inserted onto sys.path](https://github.com/opencv/opencv/issues/28766) | open; bug, category: python bindings | 32.924704 | UNJUDGED |
| C_bug | bm25 | 5 | [QRCodeDetector: detectAndDecodeMulti throws StsNotImplemented (&quot;mode 13&quot;) on valid Hanzi-mode (GB/T ](https://github.com/opencv/opencv/issues/30110) | open; bug | 32.865934 | UNJUDGED |

## O-S2 — core_development

참고 원문: [opencv/opencv#30090](https://github.com/opencv/opencv/issues/30090). 유형: `symptom_without_error`.

웹 문서 누락 관찰이며 복사할 예외 없음. 코드 버그인지 문서 문제인지 관련성 판정 필요.

### A_ko_symptom

```text
[PROBLEM]
출시된 OpenCV 버전의 온라인 문서를 찾을 수 없고 문서 링크가 이전 버전으로 갑니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 6.770749 | UNJUDGED |
| C_raw | bm25 | 2 | [Warnings in Windows for ARM build in 4.x](https://github.com/opencv/opencv/issues/30095) | open; bug, category: build/install, platform: win32 | 0.132483 | UNJUDGED |
| C_raw | bm25 | 3 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.131964 | UNJUDGED |
| C_raw | bm25 | 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.131619 | UNJUDGED |
| C_raw | bm25 | 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.130945 | UNJUDGED |
| C_raw | hybrid | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.029877 | UNJUDGED |
| C_raw | hybrid | 3 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.029139 | UNJUDGED |
| C_raw | hybrid | 4 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.028475 | UNJUDGED |
| C_raw | hybrid | 5 | [modules/core/src/hal_internal.cpp:540:48: error: expected unqualified-id before &#x27;_Complex&#x27;](https://github.com/opencv/opencv/issues/29452) | closed; bug, category: build/install, platform: other | 0.028259 | UNJUDGED |
| C_raw | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.879974 | UNJUDGED |
| C_raw | semantic | 2 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.866244 | UNJUDGED |
| C_raw | semantic | 3 | [OpenBLAS detection broken on Fedora/RHEL (headers not found &amp; serial library linked)](https://github.com/opencv/opencv/issues/28049) | closed; bug, category: build/install, platform: linux | 0.864578 | UNJUDGED |
| C_raw | semantic | 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.864053 | UNJUDGED |
| C_raw | semantic | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.862448 | UNJUDGED |
| C_bug | bm25 | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 6.482432 | UNJUDGED |
| C_bug | bm25 | 2 | [Warnings in Windows for ARM build in 4.x](https://github.com/opencv/opencv/issues/30095) | open; bug, category: build/install, platform: win32 | 0.005259 | UNJUDGED |
| C_bug | bm25 | 3 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.005247 | UNJUDGED |
| C_bug | bm25 | 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.005237 | UNJUDGED |
| C_bug | bm25 | 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.005217 | UNJUDGED |
| C_bug | hybrid | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.029877 | UNJUDGED |
| C_bug | hybrid | 3 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.029287 | UNJUDGED |
| C_bug | hybrid | 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.029139 | UNJUDGED |
| C_bug | hybrid | 5 | [modules/core/src/hal_internal.cpp:540:48: error: expected unqualified-id before &#x27;_Complex&#x27;](https://github.com/opencv/opencv/issues/29452) | closed; bug, category: build/install, platform: other | 0.028439 | UNJUDGED |
| C_bug | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.879974 | UNJUDGED |
| C_bug | semantic | 2 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.866244 | UNJUDGED |
| C_bug | semantic | 3 | [OpenBLAS detection broken on Fedora/RHEL (headers not found &amp; serial library linked)](https://github.com/opencv/opencv/issues/28049) | closed; bug, category: build/install, platform: linux | 0.864578 | UNJUDGED |
| C_bug | semantic | 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.864053 | UNJUDGED |
| C_bug | semantic | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.862448 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
OpenCV 4.14.0은 출시됐는데 wiki의 4.x 문서 링크는 4.13.0으로 이동합니다. 5.0 문서 페이지의 버전 선택 메뉴에도 4.14.0은 없고 4.13.0만 보입니다.

[ENVIRONMENT]
온라인 wiki 및 docs.opencv.org의 문서 메뉴
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 0.032522 | UNJUDGED |
| C_raw | hybrid | 2 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.027530 | UNJUDGED |
| C_raw | hybrid | 4 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.027418 | UNJUDGED |
| C_raw | hybrid | 5 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.026334 | UNJUDGED |
| C_raw | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.900135 | UNJUDGED |
| C_raw | semantic | 2 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 0.899112 | UNJUDGED |
| C_raw | semantic | 3 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 0.882125 | UNJUDGED |
| C_raw | semantic | 4 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.879817 | UNJUDGED |
| C_raw | semantic | 5 | [OpenCV.Js link is broken](https://github.com/opencv/opencv/issues/29818) | open; category: documentation | 0.876112 | UNJUDGED |
| C_raw | bm25 | 1 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 29.141969 | UNJUDGED |
| C_raw | bm25 | 2 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 22.560340 | UNJUDGED |
| C_raw | bm25 | 3 | [Breaking changes in mcc modules API not documented in OpenCV 5.0 migration guide](https://github.com/opencv/opencv/issues/29705) | open;  | 21.059620 | UNJUDGED |
| C_raw | bm25 | 4 | [Python: HoughLinesP return shape changed from (N, 1, 4) to (N, 4) in OpenCV 5.0](https://github.com/opencv/opencv/issues/29637) | closed; category: documentation | 20.846237 | UNJUDGED |
| C_raw | bm25 | 5 | [cv::boundingRect called with cv::Mat_&lt;bool&gt; throws exception in 5.0.0, works in 4.x](https://github.com/opencv/opencv/issues/29578) | closed; bug, category: geometry | 17.423479 | UNJUDGED |
| C_bug | hybrid | 1 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 0.030090 | UNJUDGED |
| C_bug | hybrid | 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.029116 | UNJUDGED |
| C_bug | hybrid | 3 | [ctest(opencv_test_imgproc ..............***Failed)](https://github.com/opencv/opencv/issues/28382) | closed; bug | 0.027598 | UNJUDGED |
| C_bug | hybrid | 4 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 0.027390 | UNJUDGED |
| C_bug | hybrid | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.025125 | UNJUDGED |
| C_bug | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.900135 | UNJUDGED |
| C_bug | semantic | 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.879817 | UNJUDGED |
| C_bug | semantic | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.873691 | UNJUDGED |
| C_bug | semantic | 4 | [&#x27;warpAffine&#x27; different translation with version 4.12 and 4.13](https://github.com/opencv/opencv/issues/28554) | closed; bug, category: imgproc | 0.872356 | UNJUDGED |
| C_bug | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.872166 | UNJUDGED |
| C_bug | bm25 | 1 | [cv::boundingRect called with cv::Mat_&lt;bool&gt; throws exception in 5.0.0, works in 4.x](https://github.com/opencv/opencv/issues/29578) | closed; bug, category: geometry | 14.131060 | UNJUDGED |
| C_bug | bm25 | 2 | [cv::connectedComponentsWithStats asserts on input mask of type CV_Bool](https://github.com/opencv/opencv/issues/29593) | closed; bug, category: geometry | 13.866276 | UNJUDGED |
| C_bug | bm25 | 3 | [cv::distanceTransform throws exception on input mask of type CV_Bool](https://github.com/opencv/opencv/issues/29596) | closed; bug, category: imgproc | 13.645468 | UNJUDGED |
| C_bug | bm25 | 4 | [Some OpenCL tests fail on Ubuntu 26.04 LTS](https://github.com/opencv/opencv/issues/28919) | closed; bug, category: ocl, platform: linux | 11.670674 | UNJUDGED |
| C_bug | bm25 | 5 | [[MSVC] Test_ONNX_layers.RandomNormalLike_basic/0 and Test_ONNX_layers.RandomNormalLike_complex/0 fai](https://github.com/opencv/opencv/issues/29072) | closed; bug, category: dnn (onnx) | 11.425111 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
OpenCV 4.14.0 has been released, but the wiki link for the 4.x documentation redirects to 4.13.0. The version menu on the 5.0 documentation page also shows 4.13.0 and does not list 4.14.0.

[ENVIRONMENT]
Online wiki and the documentation version menu at docs.opencv.org
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 0.935513 | UNJUDGED |
| C_raw | semantic | 2 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 0.909192 | UNJUDGED |
| C_raw | semantic | 3 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens)](https://github.com/opencv/opencv/issues/28549) | open; bug | 0.902176 | UNJUDGED |
| C_raw | semantic | 4 | [DNN: ONNX Conv import fails when kernel_shape is omitted (spec-compliant models)](https://github.com/opencv/opencv/issues/28321) | closed; bug, category: dnn | 0.900679 | UNJUDGED |
| C_raw | semantic | 5 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.900294 | UNJUDGED |
| C_raw | hybrid | 1 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.029851 | UNJUDGED |
| C_raw | hybrid | 4 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens)](https://github.com/opencv/opencv/issues/28549) | open; bug | 0.029572 | UNJUDGED |
| C_raw | hybrid | 5 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.028665 | UNJUDGED |
| C_raw | bm25 | 1 | [OpenCV 4.14.0 documentation is not available.](https://github.com/opencv/opencv/issues/30090) | open; category: documentation | 102.755139 | UNJUDGED |
| C_raw | bm25 | 2 | [doc: Broken links for nightly and portal documentation on Wiki](https://github.com/opencv/opencv/issues/29263) | closed; category: documentation | 48.991635 | UNJUDGED |
| C_raw | bm25 | 3 | [Python: HoughLinesP return shape changed from (N, 1, 4) to (N, 4) in OpenCV 5.0](https://github.com/opencv/opencv/issues/29637) | closed; category: documentation | 39.358845 | UNJUDGED |
| C_raw | bm25 | 4 | [computeECC mishandles unsigned input: 3-channel values saturate and self-correlation can exceed 1 🤖🤖](https://github.com/opencv/opencv/issues/30046) | open; bug, category: video | 38.652755 | UNJUDGED |
| C_raw | bm25 | 5 | [Breaking changes in mcc modules API not documented in OpenCV 5.0 migration guide](https://github.com/opencv/opencv/issues/29705) | open;  | 38.512588 | UNJUDGED |
| C_bug | semantic | 1 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens)](https://github.com/opencv/opencv/issues/28549) | open; bug | 0.902176 | UNJUDGED |
| C_bug | semantic | 2 | [DNN: ONNX Conv import fails when kernel_shape is omitted (spec-compliant models)](https://github.com/opencv/opencv/issues/28321) | closed; bug, category: dnn | 0.900679 | UNJUDGED |
| C_bug | semantic | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.900294 | UNJUDGED |
| C_bug | semantic | 4 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.899996 | UNJUDGED |
| C_bug | semantic | 5 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.895780 | UNJUDGED |
| C_bug | hybrid | 1 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens)](https://github.com/opencv/opencv/issues/28549) | open; bug | 0.032266 | UNJUDGED |
| C_bug | hybrid | 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 0.031514 | UNJUDGED |
| C_bug | hybrid | 3 | [IPP HAL warpAffine INTER_NEAREST is not bit-exact with the native implementation (CV_16S vs CV_16U g](https://github.com/opencv/opencv/issues/29279) | closed; bug, category: imgproc, category: 3rdparty | 0.028283 | UNJUDGED |
| C_bug | hybrid | 4 | [Face Landmark Detector with LBF fails on 5.0.0 but works on 4.14.0](https://github.com/opencv/opencv/issues/29703) | open; bug | 0.026496 | UNJUDGED |
| C_bug | hybrid | 5 | [Cannot link OpenCV 5 statically to native code on Android](https://github.com/opencv/opencv/issues/29342) | closed; bug, category: build/install, platform: android, platform: ios/osx | 0.026042 | UNJUDGED |
| C_bug | bm25 | 1 | [computeECC mishandles unsigned input: 3-channel values saturate and self-correlation can exceed 1 🤖🤖](https://github.com/opencv/opencv/issues/30046) | open; bug, category: video | 32.682901 | UNJUDGED |
| C_bug | bm25 | 2 | [4.14.0: build failure in modules/core/src/lut.dispatch.cpp](https://github.com/opencv/opencv/issues/29694) | closed; bug, category: core, category: build/install | 32.364825 | UNJUDGED |
| C_bug | bm25 | 3 | [[bug] : Hamburger menu icon is invisible on white backgrounds (small screens)](https://github.com/opencv/opencv/issues/28549) | open; bug | 29.478991 | UNJUDGED |
| C_bug | bm25 | 4 | [IPP HAL warpAffine INTER_NEAREST is not bit-exact with the native implementation (CV_16S vs CV_16U g](https://github.com/opencv/opencv/issues/29279) | closed; bug, category: imgproc, category: 3rdparty | 27.894857 | UNJUDGED |
| C_bug | bm25 | 5 | [Face Landmark Detector with LBF fails on 5.0.0 but works on 4.14.0](https://github.com/opencv/opencv/issues/29703) | open; bug | 27.206388 | UNJUDGED |

## O-C1 — core_development

참고 원문: [opencv/opencv#28207](https://github.com/opencv/opencv/issues/28207). 유형: `condition_sensitive`.

FFmpeg 직접 실행과 Java VideoCapture 실행의 하드웨어 디코더 차이가 보고됨.

### A_ko_symptom

```text
[PROBLEM]
OpenCV Java로 영상을 읽을 때 NVIDIA 하드웨어 디코더가 사용되지 않습니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.883988 | UNJUDGED |
| C_raw | semantic | 2 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.881487 | UNJUDGED |
| C_raw | semantic | 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.879351 | UNJUDGED |
| C_raw | semantic | 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.873572 | UNJUDGED |
| C_raw | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.873469 | UNJUDGED |
| C_raw | bm25 | 1 | [cv::cuda::resize failed with Continuous GpuMat](https://github.com/opencv/opencv/issues/28407) | closed; bug, category: gpu/cuda (contrib) | 7.156555 | UNJUDGED |
| C_raw | bm25 | 2 | [Dynamic CUDA support](https://github.com/opencv/opencv/issues/29318) | open; feature | 5.691663 | UNJUDGED |
| C_raw | bm25 | 3 | [[Windows] RTX 5070 Ti (Blackwell sm_120) - setup and deployment notes](https://github.com/opencv/opencv/issues/28924) | open;  | 5.642361 | UNJUDGED |
| C_raw | bm25 | 4 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 5.477977 | UNJUDGED |
| C_raw | bm25 | 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 5.291336 | UNJUDGED |
| C_raw | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.031754 | UNJUDGED |
| C_raw | hybrid | 2 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.031010 | UNJUDGED |
| C_raw | hybrid | 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.028485 | UNJUDGED |
| C_raw | hybrid | 4 | [[bug] Incorrect result from the `cv::createHanningWindow()` function](https://github.com/opencv/opencv/issues/29634) | closed; category: imgproc | 0.027746 | UNJUDGED |
| C_raw | hybrid | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.027313 | UNJUDGED |
| C_bug | semantic | 1 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.883988 | UNJUDGED |
| C_bug | semantic | 2 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.881487 | UNJUDGED |
| C_bug | semantic | 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.879351 | UNJUDGED |
| C_bug | semantic | 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.873572 | UNJUDGED |
| C_bug | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.873469 | UNJUDGED |
| C_bug | bm25 | 1 | [cv::cuda::resize failed with Continuous GpuMat](https://github.com/opencv/opencv/issues/28407) | closed; bug, category: gpu/cuda (contrib) | 7.345363 | UNJUDGED |
| C_bug | bm25 | 2 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 5.838979 | UNJUDGED |
| C_bug | bm25 | 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 5.701666 | UNJUDGED |
| C_bug | bm25 | 4 | [5.x: cv::addWeighted segfaults (null kernel pointer) for 8U/8S/16U/16S/16F/16BF/32F inputs with dtyp](https://github.com/opencv/opencv/issues/29880) | closed; bug, category: core, priority: high, confirmed | 3.169513 | UNJUDGED |
| C_bug | bm25 | 5 | [Some OpenCL tests fail on Ubuntu 26.04 LTS](https://github.com/opencv/opencv/issues/28919) | closed; bug, category: ocl, platform: linux | 2.146417 | UNJUDGED |
| C_bug | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.032258 | UNJUDGED |
| C_bug | hybrid | 2 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.031498 | UNJUDGED |
| C_bug | hybrid | 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.029437 | UNJUDGED |
| C_bug | hybrid | 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.028405 | UNJUDGED |
| C_bug | hybrid | 5 | [Unable to build with CUDA](https://github.com/opencv/opencv/issues/28952) | closed; bug, category: build/install, category: gpu/cuda (contrib) | 0.028083 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
FFmpeg에서 h264_cuvid로 같은 영상을 직접 디코딩하면 GPU 디코더가 동작하지만, OpenCV Java VideoCapture에서는 동작하지 않습니다. CAP_FFMPEG와 VIDEO_ACCELERATION_ANY를 선택했고 OPENCV_FFMPEG_CAPTURE_OPTIONS로 video_codec=h264_cuvid를 지정했습니다.

[ENVIRONMENT]
Ubuntu 24.04; FFmpeg 6.1; OpenCV 4.12.0; NVIDIA RTX 5060
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 111.703468 | UNJUDGED |
| C_raw | bm25 | 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 41.586168 | UNJUDGED |
| C_raw | bm25 | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 39.128427 | UNJUDGED |
| C_raw | bm25 | 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 34.520835 | UNJUDGED |
| C_raw | bm25 | 5 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read](https://github.com/opencv/opencv/issues/29722) | open; category: videoio, category: 3rdparty | 31.081876 | UNJUDGED |
| C_raw | semantic | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.915780 | UNJUDGED |
| C_raw | semantic | 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.897023 | UNJUDGED |
| C_raw | semantic | 3 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.891112 | UNJUDGED |
| C_raw | semantic | 4 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.890339 | UNJUDGED |
| C_raw | semantic | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.888856 | UNJUDGED |
| C_raw | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read](https://github.com/opencv/opencv/issues/29722) | open; category: videoio, category: 3rdparty | 0.030310 | UNJUDGED |
| C_raw | hybrid | 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 0.030118 | UNJUDGED |
| C_raw | hybrid | 5 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.028043 | UNJUDGED |
| C_bug | bm25 | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 114.562391 | UNJUDGED |
| C_bug | bm25 | 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 38.208145 | UNJUDGED |
| C_bug | bm25 | 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 34.284697 | UNJUDGED |
| C_bug | bm25 | 4 | [cv::cuda::resize failed with Continuous GpuMat](https://github.com/opencv/opencv/issues/28407) | closed; bug, category: gpu/cuda (contrib) | 30.575601 | UNJUDGED |
| C_bug | bm25 | 5 | [[iOS] VideoWriter::release() causes NSInvalidArgumentException on OpenCV 4.12.0 (works in 4.8.0)](https://github.com/opencv/opencv/issues/28165) | closed; bug, category: videoio, platform: ios/osx | 26.848863 | UNJUDGED |
| C_bug | semantic | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.915780 | UNJUDGED |
| C_bug | semantic | 2 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.891112 | UNJUDGED |
| C_bug | semantic | 3 | [4.13.0 build error both on Windows and Linux when using cuda13.2](https://github.com/opencv/opencv/issues/28784) | closed; bug, duplicate, category: build/install, category: gpu/cuda (contrib) | 0.890339 | UNJUDGED |
| C_bug | semantic | 4 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.888856 | UNJUDGED |
| C_bug | semantic | 5 | [Last IPP HAL refactoring introduced invalid memory access issue on Windows](https://github.com/opencv/opencv/issues/29166) | closed; bug, priority: high, platform: win32, category: 3rdparty | 0.888091 | UNJUDGED |
| C_bug | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 0.030798 | UNJUDGED |
| C_bug | hybrid | 3 | [OpenCV 5 cannot link to zlib](https://github.com/opencv/opencv/issues/29325) | open; bug, category: build/install | 0.029710 | UNJUDGED |
| C_bug | hybrid | 4 | [Compilation Errors during build](https://github.com/opencv/opencv/issues/28629) | open; bug, category: build/install | 0.029437 | UNJUDGED |
| C_bug | hybrid | 5 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 0.028665 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
Decoding the same video directly with FFmpeg and h264_cuvid uses the GPU decoder, but OpenCV Java VideoCapture does not. I selected CAP_FFMPEG and VIDEO_ACCELERATION_ANY, and set OPENCV_FFMPEG_CAPTURE_OPTIONS to video_codec=h264_cuvid.

[ENVIRONMENT]
Ubuntu 24.04; FFmpeg 6.1; OpenCV 4.12.0; NVIDIA RTX 5060
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 189.047224 | UNJUDGED |
| C_raw | bm25 | 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 77.643431 | UNJUDGED |
| C_raw | bm25 | 3 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 66.159685 | UNJUDGED |
| C_raw | bm25 | 4 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 66.151032 | UNJUDGED |
| C_raw | bm25 | 5 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read](https://github.com/opencv/opencv/issues/29722) | open; category: videoio, category: 3rdparty | 64.248005 | UNJUDGED |
| C_raw | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read](https://github.com/opencv/opencv/issues/29722) | open; category: videoio, category: 3rdparty | 0.031514 | UNJUDGED |
| C_raw | hybrid | 4 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 0.031258 | UNJUDGED |
| C_raw | hybrid | 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 0.029631 | UNJUDGED |
| C_raw | semantic | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.933715 | UNJUDGED |
| C_raw | semantic | 2 | [VideoCapture reports a frame count it cannot deliver when the decoder fails on first read](https://github.com/opencv/opencv/issues/29722) | open; category: videoio, category: 3rdparty | 0.913273 | UNJUDGED |
| C_raw | semantic | 3 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 0.909716 | UNJUDGED |
| C_raw | semantic | 4 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.907172 | UNJUDGED |
| C_raw | semantic | 5 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 0.905209 | UNJUDGED |
| C_bug | bm25 | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 189.180100 | UNJUDGED |
| C_bug | bm25 | 2 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 66.369102 | UNJUDGED |
| C_bug | bm25 | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 64.547012 | UNJUDGED |
| C_bug | bm25 | 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 61.034850 | UNJUDGED |
| C_bug | bm25 | 5 | [AVFoundation seeking drifts for non-integer frame rates](https://github.com/opencv/opencv/issues/28831) | closed; bug | 44.800843 | UNJUDGED |
| C_bug | hybrid | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 0.030777 | UNJUDGED |
| C_bug | hybrid | 4 | [AVFoundation seeking drifts for non-integer frame rates](https://github.com/opencv/opencv/issues/28831) | closed; bug | 0.030090 | UNJUDGED |
| C_bug | hybrid | 5 | [Windows11+Opencv4.13-build-issue](https://github.com/opencv/opencv/issues/28608) | open; bug, category: build/install, platform: win32 | 0.029211 | UNJUDGED |
| C_bug | semantic | 1 | [can&#x27;t using h264_cuvid decoder when using java api](https://github.com/opencv/opencv/issues/28207) | open; bug, category: videoio | 0.933715 | UNJUDGED |
| C_bug | semantic | 2 | [Compilation error: drawing_text.cpp: in function `cv::FontRenderEngine::~FontRenderEngine()&#x27;:](https://github.com/opencv/opencv/issues/29458) | open; bug, category: imgproc, category: build/install | 0.907172 | UNJUDGED |
| C_bug | semantic | 3 | [Persistent VideoCapture RTSP connections produce corrupted frames after 15-30 second](https://github.com/opencv/opencv/issues/28638) | open; bug, category: videoio | 0.905209 | UNJUDGED |
| C_bug | semantic | 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | open; bug, category: imgproc | 0.902879 | UNJUDGED |
| C_bug | semantic | 5 | [Last IPP HAL refactoring introduced invalid memory access issue on Windows](https://github.com/opencv/opencv/issues/29166) | closed; bug, priority: high, platform: win32, category: 3rdparty | 0.902536 | UNJUDGED |

## O-C2 — core_development

참고 원문: [opencv/opencv#29636](https://github.com/opencv/opencv/issues/29636). 유형: `condition_sensitive`.

동일 파라미터에서도 보드 생성 경로에 따라 코너 검출 결과가 다름. 첨부 이미지는 읽지 않음.

### A_ko_symptom

```text
[PROBLEM]
ChArUco 보드에서 마커는 검출되는데 체스보드 코너는 검출되지 않습니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032522 | UNJUDGED |
| C_raw | hybrid | 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.030415 | UNJUDGED |
| C_raw | hybrid | 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 0.029387 | UNJUDGED |
| C_raw | hybrid | 4 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.016393 | UNJUDGED |
| C_raw | hybrid | 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.015873 | UNJUDGED |
| C_raw | semantic | 1 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.866477 | UNJUDGED |
| C_raw | semantic | 2 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.857889 | UNJUDGED |
| C_raw | semantic | 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.849423 | UNJUDGED |
| C_raw | semantic | 4 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.847421 | UNJUDGED |
| C_raw | semantic | 5 | [Protobuf 6 support](https://github.com/opencv/opencv/issues/28325) | open; feature | 0.845630 | UNJUDGED |
| C_raw | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 10.598812 | UNJUDGED |
| C_raw | bm25 | 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 8.002478 | UNJUDGED |
| C_raw | bm25 | 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 6.264772 | UNJUDGED |
| C_raw | bm25 | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 2.667201 | UNJUDGED |
| C_bug | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032522 | UNJUDGED |
| C_bug | hybrid | 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.030622 | UNJUDGED |
| C_bug | hybrid | 3 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.016393 | UNJUDGED |
| C_bug | hybrid | 4 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.015873 | UNJUDGED |
| C_bug | hybrid | 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.015873 | UNJUDGED |
| C_bug | semantic | 1 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.866477 | UNJUDGED |
| C_bug | semantic | 2 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.857889 | UNJUDGED |
| C_bug | semantic | 3 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.849423 | UNJUDGED |
| C_bug | semantic | 4 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.847421 | UNJUDGED |
| C_bug | semantic | 5 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 0.845483 | UNJUDGED |
| C_bug | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 10.059997 | UNJUDGED |
| C_bug | bm25 | 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 7.764285 | UNJUDGED |
| C_bug | bm25 | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 2.897320 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
동일 파라미터의 8x6 ChArUco 보드 중 OpenCV로 생성한 보드에서는 마커와 코너가 모두 검출됩니다. calib.io로 생성한 보드에서는 마커만 검출되고 코너가 나오지 않습니다. CharucoDetector.detectBoard를 사용합니다.

[ENVIRONMENT]
opencv-python 4.14.0.94; macOS ARM; DICT_4X4_50, square length 35 mm, marker length 24 mm
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 0.031514 | UNJUDGED |
| C_raw | hybrid | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.031498 | UNJUDGED |
| C_raw | hybrid | 4 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.030798 | UNJUDGED |
| C_raw | hybrid | 5 | [Fails to build](https://github.com/opencv/opencv/issues/29435) | closed; bug, category: imgcodecs, platform: ios/osx | 0.025987 | UNJUDGED |
| C_raw | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 92.343862 | UNJUDGED |
| C_raw | bm25 | 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 40.271475 | UNJUDGED |
| C_raw | bm25 | 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 27.835291 | UNJUDGED |
| C_raw | bm25 | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 26.392846 | UNJUDGED |
| C_raw | bm25 | 5 | [AVFOUNDATION backend issue on iOSSimulator](https://github.com/opencv/opencv/issues/28666) | open; bug, category: videoio, platform: ios/osx | 25.578591 | UNJUDGED |
| C_raw | semantic | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.912270 | UNJUDGED |
| C_raw | semantic | 2 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.892932 | UNJUDGED |
| C_raw | semantic | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.887311 | UNJUDGED |
| C_raw | semantic | 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.886981 | UNJUDGED |
| C_raw | semantic | 5 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 0.886401 | UNJUDGED |
| C_bug | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.031025 | UNJUDGED |
| C_bug | hybrid | 4 | [Fails to build](https://github.com/opencv/opencv/issues/29435) | closed; bug, category: imgcodecs, platform: ios/osx | 0.027347 | UNJUDGED |
| C_bug | hybrid | 5 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.026861 | UNJUDGED |
| C_bug | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 94.016526 | UNJUDGED |
| C_bug | bm25 | 2 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 27.249513 | UNJUDGED |
| C_bug | bm25 | 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 26.881783 | UNJUDGED |
| C_bug | bm25 | 4 | [AVFOUNDATION backend issue on iOSSimulator](https://github.com/opencv/opencv/issues/28666) | open; bug, category: videoio, platform: ios/osx | 24.653814 | UNJUDGED |
| C_bug | bm25 | 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 23.752345 | UNJUDGED |
| C_bug | semantic | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.912270 | UNJUDGED |
| C_bug | semantic | 2 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.892932 | UNJUDGED |
| C_bug | semantic | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.887311 | UNJUDGED |
| C_bug | semantic | 4 | [OpenCV CharucoBoard.testWrongSizeDetection/* tests contains stack-use-after-scope errors](https://github.com/opencv/opencv/issues/28241) | closed; bug, category: objdetect | 0.886981 | UNJUDGED |
| C_bug | semantic | 5 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.880656 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
For 8x6 ChArUco boards with the same parameters, the OpenCV-generated board produces both markers and corners. A board generated with calib.io produces markers but no corners. I use CharucoDetector.detectBoard.

[ENVIRONMENT]
opencv-python 4.14.0.94; macOS ARM; DICT_4X4_50, square length 35 mm, marker length 24 mm
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 177.501715 | UNJUDGED |
| C_raw | bm25 | 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 105.615749 | UNJUDGED |
| C_raw | bm25 | 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 60.233945 | UNJUDGED |
| C_raw | bm25 | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 34.629688 | UNJUDGED |
| C_raw | bm25 | 5 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 33.067425 | UNJUDGED |
| C_raw | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 0.031054 | UNJUDGED |
| C_raw | hybrid | 4 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.031025 | UNJUDGED |
| C_raw | hybrid | 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.031010 | UNJUDGED |
| C_raw | semantic | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.927269 | UNJUDGED |
| C_raw | semantic | 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 0.905800 | UNJUDGED |
| C_raw | semantic | 3 | [[RFC] Overhaul of ArUco module for OpenCV 5.0 (ArUco 2.0)](https://github.com/opencv/opencv/issues/28953) | open; feature, category: objdetect | 0.905438 | UNJUDGED |
| C_raw | semantic | 4 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.905183 | UNJUDGED |
| C_raw | semantic | 5 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.899744 | UNJUDGED |
| C_bug | bm25 | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 177.868354 | UNJUDGED |
| C_bug | bm25 | 2 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 57.185462 | UNJUDGED |
| C_bug | bm25 | 3 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 35.522288 | UNJUDGED |
| C_bug | bm25 | 4 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 29.528264 | UNJUDGED |
| C_bug | bm25 | 5 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 28.980090 | UNJUDGED |
| C_bug | hybrid | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 0.031754 | UNJUDGED |
| C_bug | hybrid | 3 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.031514 | UNJUDGED |
| C_bug | hybrid | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.031498 | UNJUDGED |
| C_bug | hybrid | 5 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.028373 | UNJUDGED |
| C_bug | semantic | 1 | [Charuco corner detection fails, while markers are detected.](https://github.com/opencv/opencv/issues/29636) | closed; bug | 0.927269 | UNJUDGED |
| C_bug | semantic | 2 | [findChessboardCorners returns false after upgrading from 4.8 to 4.12](https://github.com/opencv/opencv/issues/28028) | open; bug, category: calib3d, confirmed | 0.905800 | UNJUDGED |
| C_bug | semantic | 3 | [`cv2.aruco.CharucoBoard` missing `getNearestMarkerIdx` and `getNearestMarkerCorners` Python bindings](https://github.com/opencv/opencv/issues/28512) | closed; bug, category: python bindings, category: objdetect | 0.905183 | UNJUDGED |
| C_bug | semantic | 4 | [cv2.fisheye.calibrate() fails with (N, 1, C) point arrays in OpenCV 5.0.0](https://github.com/opencv/opencv/issues/29692) | open; bug, category: calib3d | 0.899744 | UNJUDGED |
| C_bug | semantic | 5 | [cv::aruco::CharucoDetector::detectDiamonds() does not detect correctly when pass pre detected Aruco ](https://github.com/opencv/opencv/issues/28783) | closed; bug, category: calib3d | 0.894647 | UNJUDGED |

## T-E1 — core_development

참고 원문: [huggingface/transformers#47879](https://github.com/huggingface/transformers/issues/47879). 유형: `error_literal`.

영상 처리 중 보고된 tuple AttributeError. 수정 제안은 질의에서 제외.

### A_ko_symptom

```text
[PROBLEM]
Gemma4로 영상을 처리하면 실행 중 속성 오류가 나서 중단됩니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | — | no_lexical_match | — | — | UNJUDGED |
| C_raw | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.851840 | UNJUDGED |
| C_raw | semantic | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.849891 | UNJUDGED |
| C_raw | semantic | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.848716 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-07-13](https://github.com/huggingface/transformers/issues/47309) | closed;  | 0.848186 | UNJUDGED |
| C_raw | semantic | 5 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314)](https://github.com/huggingface/transformers/issues/48736) | open;  | 0.847213 | UNJUDGED |
| C_raw | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.016393 | UNJUDGED |
| C_raw | hybrid | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.016129 | UNJUDGED |
| C_raw | hybrid | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.015873 | UNJUDGED |
| C_raw | hybrid | 4 | [[serge] integration failure triage - 2026-07-13](https://github.com/huggingface/transformers/issues/47309) | closed;  | 0.015625 | UNJUDGED |
| C_raw | hybrid | 5 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314)](https://github.com/huggingface/transformers/issues/48736) | open;  | 0.015385 | UNJUDGED |
| C_bug | bm25 | — | no_lexical_match | — | — | UNJUDGED |
| C_bug | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.851840 | UNJUDGED |
| C_bug | semantic | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.849891 | UNJUDGED |
| C_bug | semantic | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.848716 | UNJUDGED |
| C_bug | semantic | 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.842576 | UNJUDGED |
| C_bug | semantic | 5 | [Nemotron3Diarization streaming: the last chunk drops the final valid frame when len(audio) % 160 &lt; 9](https://github.com/huggingface/transformers/issues/49113) | closed; bug | 0.839137 | UNJUDGED |
| C_bug | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.016393 | UNJUDGED |
| C_bug | hybrid | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.016129 | UNJUDGED |
| C_bug | hybrid | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.015873 | UNJUDGED |
| C_bug | hybrid | 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.015625 | UNJUDGED |
| C_bug | hybrid | 5 | [Nemotron3Diarization streaming: the last chunk drops the final valid frame when len(audio) % 160 &lt; 9](https://github.com/huggingface/transformers/issues/49113) | closed; bug | 0.015385 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Gemma4-E2B-IT의 영상 처리 중 forward에서 속성 오류로 중단됩니다.

[ERROR]
AttributeError: 'tuple' object has no attribute 'to'

[ENVIRONMENT]
Transformers 5.15.0.dev0; WSL2 Linux; Python 3.13.14; PyTorch 2.13.0+cu132; NVIDIA RTX 4080 Laptop
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.917255 | UNJUDGED |
| C_raw | semantic | 2 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.892198 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-09-15](https://github.com/huggingface/transformers/issues/48837) | closed;  | 0.888017 | UNJUDGED |
| C_raw | semantic | 4 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314)](https://github.com/huggingface/transformers/issues/48736) | open;  | 0.887546 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-08-24](https://github.com/huggingface/transformers/issues/48263) | closed;  | 0.887008 | UNJUDGED |
| C_raw | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.031054 | UNJUDGED |
| C_raw | hybrid | 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.029644 | UNJUDGED |
| C_raw | hybrid | 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.025914 | UNJUDGED |
| C_raw | hybrid | 5 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27;](https://github.com/huggingface/transformers/issues/48556) | closed;  | 0.023559 | UNJUDGED |
| C_raw | bm25 | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 104.231155 | UNJUDGED |
| C_raw | bm25 | 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 28.315793 | UNJUDGED |
| C_raw | bm25 | 3 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | closed; bug | 26.301104 | UNJUDGED |
| C_raw | bm25 | 4 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 26.167571 | UNJUDGED |
| C_raw | bm25 | 5 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 26.106429 | UNJUDGED |
| C_bug | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.917255 | UNJUDGED |
| C_bug | semantic | 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.886348 | UNJUDGED |
| C_bug | semantic | 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.886166 | UNJUDGED |
| C_bug | semantic | 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.885796 | UNJUDGED |
| C_bug | semantic | 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.881454 | UNJUDGED |
| C_bug | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.031498 | UNJUDGED |
| C_bug | hybrid | 4 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.029236 | UNJUDGED |
| C_bug | hybrid | 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.029139 | UNJUDGED |
| C_bug | bm25 | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 82.783730 | UNJUDGED |
| C_bug | bm25 | 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 20.097480 | UNJUDGED |
| C_bug | bm25 | 3 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 20.049728 | UNJUDGED |
| C_bug | bm25 | 4 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 19.999919 | UNJUDGED |
| C_bug | bm25 | 5 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | closed; bug | 19.021072 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
Video processing with Gemma4-E2B-IT stops with an attribute error during forward.

[ERROR]
AttributeError: 'tuple' object has no attribute 'to'

[ENVIRONMENT]
Transformers 5.15.0.dev0; WSL2 Linux; Python 3.13.14; PyTorch 2.13.0+cu132; NVIDIA RTX 4080 Laptop
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 129.387527 | UNJUDGED |
| C_raw | bm25 | 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27;](https://github.com/huggingface/transformers/issues/48556) | closed;  | 38.336762 | UNJUDGED |
| C_raw | bm25 | 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 33.049953 | UNJUDGED |
| C_raw | bm25 | 4 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 32.738665 | UNJUDGED |
| C_raw | bm25 | 5 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | closed; bug | 31.877627 | UNJUDGED |
| C_raw | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.923892 | UNJUDGED |
| C_raw | semantic | 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27;](https://github.com/huggingface/transformers/issues/48556) | closed;  | 0.903613 | UNJUDGED |
| C_raw | semantic | 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.902696 | UNJUDGED |
| C_raw | semantic | 4 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors](https://github.com/huggingface/transformers/issues/49007) | closed; bug | 0.897149 | UNJUDGED |
| C_raw | semantic | 5 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.895226 | UNJUDGED |
| C_raw | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27;](https://github.com/huggingface/transformers/issues/48556) | closed;  | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.030310 | UNJUDGED |
| C_raw | hybrid | 4 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors](https://github.com/huggingface/transformers/issues/49007) | closed; bug | 0.029324 | UNJUDGED |
| C_raw | hybrid | 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.027526 | UNJUDGED |
| C_bug | bm25 | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 105.537680 | UNJUDGED |
| C_bug | bm25 | 2 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 26.798817 | UNJUDGED |
| C_bug | bm25 | 3 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 25.732625 | UNJUDGED |
| C_bug | bm25 | 4 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | closed; bug | 23.684011 | UNJUDGED |
| C_bug | bm25 | 5 | [Loading `RTDetrModel` from a detection checkpoint (or `SEWDForCTC` from a SEW-D checkpoint) gives a ](https://github.com/huggingface/transformers/issues/48722) | closed; bug | 21.559566 | UNJUDGED |
| C_bug | semantic | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.923892 | UNJUDGED |
| C_bug | semantic | 2 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.902696 | UNJUDGED |
| C_bug | semantic | 3 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors](https://github.com/huggingface/transformers/issues/49007) | closed; bug | 0.897149 | UNJUDGED |
| C_bug | semantic | 4 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.895226 | UNJUDGED |
| C_bug | semantic | 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.893375 | UNJUDGED |
| C_bug | hybrid | 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors](https://github.com/huggingface/transformers/issues/49007) | closed; bug | 0.031025 | UNJUDGED |
| C_bug | hybrid | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.030550 | UNJUDGED |
| C_bug | hybrid | 4 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.030415 | UNJUDGED |
| C_bug | hybrid | 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | closed; bug | 0.029274 | UNJUDGED |

## T-E2 — core_development

참고 원문: [huggingface/transformers#48346](https://github.com/huggingface/transformers/issues/48346). 유형: `error_literal`.

실제 NoneType 예외가 주요 검색 단서. override 부재는 입력 상황이며 유형 중복 여부는 사람 검토 필요.

### A_ko_symptom

```text
[PROBLEM]
일반 FP8 설정으로 모델을 준비하다가 속성 오류가 납니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.030769 | UNJUDGED |
| C_raw | hybrid | 2 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 0.029514 | UNJUDGED |
| C_raw | hybrid | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 0.025974 | UNJUDGED |
| C_raw | hybrid | 4 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization](https://github.com/huggingface/transformers/issues/48350) | closed;  | 0.016393 | UNJUDGED |
| C_raw | hybrid | 5 | [[serge] integration failure triage - 2026-09-15](https://github.com/huggingface/transformers/issues/48837) | closed;  | 0.016393 | UNJUDGED |
| C_raw | bm25 | 1 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization](https://github.com/huggingface/transformers/issues/48350) | closed;  | 7.930313 | UNJUDGED |
| C_raw | bm25 | 2 | [FineGrainedFP8: modules_to_not_convert never matches on text-only loads of multimodal checkpoints (s](https://github.com/huggingface/transformers/issues/48349) | closed;  | 7.804559 | UNJUDGED |
| C_raw | bm25 | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 7.631248 | UNJUDGED |
| C_raw | bm25 | 4 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 7.211241 | UNJUDGED |
| C_raw | bm25 | 5 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 7.017466 | UNJUDGED |
| C_raw | semantic | 1 | [[serge] integration failure triage - 2026-09-15](https://github.com/huggingface/transformers/issues/48837) | closed;  | 0.858023 | UNJUDGED |
| C_raw | semantic | 2 | [[serge] integration failure triage - 2026-08-23](https://github.com/huggingface/transformers/issues/48240) | closed;  | 0.858009 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.852766 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-09-10](https://github.com/huggingface/transformers/issues/48695) | closed;  | 0.852537 | UNJUDGED |
| C_raw | semantic | 5 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.852461 | UNJUDGED |
| C_bug | hybrid | 1 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model.](https://github.com/huggingface/transformers/issues/48400) | closed; bug | 0.016393 | UNJUDGED |
| C_bug | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.016129 | UNJUDGED |
| C_bug | hybrid | 3 | [The kernel&#x27;s version doesn&#x27;t properly check.](https://github.com/huggingface/transformers/issues/47455) | closed; bug | 0.015873 | UNJUDGED |
| C_bug | hybrid | 4 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally](https://github.com/huggingface/transformers/issues/47917) | closed; bug | 0.015625 | UNJUDGED |
| C_bug | hybrid | 5 | [CLIPSeg, TimesFM, PP-OCR detector and VideoPrism base/head loads still give every weight randomly in](https://github.com/huggingface/transformers/issues/48862) | open; bug | 0.015385 | UNJUDGED |
| C_bug | bm25 | — | no_lexical_match | — | — | UNJUDGED |
| C_bug | semantic | 1 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model.](https://github.com/huggingface/transformers/issues/48400) | closed; bug | 0.841239 | UNJUDGED |
| C_bug | semantic | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.840482 | UNJUDGED |
| C_bug | semantic | 3 | [The kernel&#x27;s version doesn&#x27;t properly check.](https://github.com/huggingface/transformers/issues/47455) | closed; bug | 0.840276 | UNJUDGED |
| C_bug | semantic | 4 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally](https://github.com/huggingface/transformers/issues/47917) | closed; bug | 0.839374 | UNJUDGED |
| C_bug | semantic | 5 | [CLIPSeg, TimesFM, PP-OCR detector and VideoPrism base/head loads still give every weight randomly in](https://github.com/huggingface/transformers/issues/48862) | open; bug | 0.838836 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
FineGrainedFP8Config로 만든 양자화 객체에서 update_tp_plan을 호출하면 속성 오류가 납니다. 설정에는 base_model_tp_plan이 있고 별도의 _experts_implementation은 지정하지 않았습니다. 일반 Qwen FP8 모델 로딩에서도 문제가 보고됩니다.

[ERROR]
AttributeError: 'NoneType' object has no attribute 'get'

[ENVIRONMENT]
Transformers 5.16.0 및 main; Python 3.12.13; PyTorch 2.13.0+cu130; Linux
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.032002 | UNJUDGED |
| C_raw | hybrid | 4 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward](https://github.com/huggingface/transformers/issues/48307) | open;  | 0.026879 | UNJUDGED |
| C_raw | hybrid | 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 0.025849 | UNJUDGED |
| C_raw | bm25 | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 96.663374 | UNJUDGED |
| C_raw | bm25 | 2 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 51.557836 | UNJUDGED |
| C_raw | bm25 | 3 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 43.937237 | UNJUDGED |
| C_raw | bm25 | 4 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank)](https://github.com/huggingface/transformers/issues/48308) | open;  | 41.744557 | UNJUDGED |
| C_raw | bm25 | 5 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward](https://github.com/huggingface/transformers/issues/48307) | open;  | 36.271017 | UNJUDGED |
| C_raw | semantic | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 0.921902 | UNJUDGED |
| C_raw | semantic | 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.902838 | UNJUDGED |
| C_raw | semantic | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 0.897691 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-08-23](https://github.com/huggingface/transformers/issues/48240) | closed;  | 0.892557 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-09-17](https://github.com/huggingface/transformers/issues/48914) | closed;  | 0.890518 | UNJUDGED |
| C_bug | hybrid | 1 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 0.031514 | UNJUDGED |
| C_bug | hybrid | 2 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 0.031054 | UNJUDGED |
| C_bug | hybrid | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.030579 | UNJUDGED |
| C_bug | hybrid | 4 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.028778 | UNJUDGED |
| C_bug | hybrid | 5 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors](https://github.com/huggingface/transformers/issues/49190) | open; bug | 0.028442 | UNJUDGED |
| C_bug | bm25 | 1 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 25.054713 | UNJUDGED |
| C_bug | bm25 | 2 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 22.349403 | UNJUDGED |
| C_bug | bm25 | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 21.365518 | UNJUDGED |
| C_bug | bm25 | 4 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | closed; bug | 20.779072 | UNJUDGED |
| C_bug | bm25 | 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 20.411330 | UNJUDGED |
| C_bug | semantic | 1 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors](https://github.com/huggingface/transformers/issues/49190) | open; bug | 0.884187 | UNJUDGED |
| C_bug | semantic | 2 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 0.883548 | UNJUDGED |
| C_bug | semantic | 3 | [Module-level getattr breaks unittest functionality](https://github.com/huggingface/transformers/issues/48966) | open; bug | 0.881631 | UNJUDGED |
| C_bug | semantic | 4 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B`](https://github.com/huggingface/transformers/issues/47333) | closed; bug | 0.880873 | UNJUDGED |
| C_bug | semantic | 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 0.880092 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
Calling update_tp_plan on a quantizer created with FineGrainedFP8Config raises an attribute error. The configuration has base_model_tp_plan and no separately specified _experts_implementation. The same problem is reported when loading normal Qwen FP8 models.

[ERROR]
AttributeError: 'NoneType' object has no attribute 'get'

[ENVIRONMENT]
Transformers 5.16.0 and main; Python 3.12.13; PyTorch 2.13.0+cu130; Linux
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 166.244967 | UNJUDGED |
| C_raw | bm25 | 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 96.643250 | UNJUDGED |
| C_raw | bm25 | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 85.423342 | UNJUDGED |
| C_raw | bm25 | 4 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank)](https://github.com/huggingface/transformers/issues/48308) | open;  | 68.003502 | UNJUDGED |
| C_raw | bm25 | 5 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward](https://github.com/huggingface/transformers/issues/48307) | open;  | 58.669432 | UNJUDGED |
| C_raw | semantic | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 0.951323 | UNJUDGED |
| C_raw | semantic | 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.924134 | UNJUDGED |
| C_raw | semantic | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 0.922738 | UNJUDGED |
| C_raw | semantic | 4 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 0.898617 | UNJUDGED |
| C_raw | semantic | 5 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally](https://github.com/huggingface/transformers/issues/47917) | closed; bug | 0.894636 | UNJUDGED |
| C_raw | hybrid | 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent](https://github.com/huggingface/transformers/issues/48346) | closed;  | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan](https://github.com/huggingface/transformers/issues/48351) | closed;  | 0.031746 | UNJUDGED |
| C_raw | hybrid | 4 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27;](https://github.com/huggingface/transformers/issues/48556) | closed;  | 0.028405 | UNJUDGED |
| C_raw | hybrid | 5 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank)](https://github.com/huggingface/transformers/issues/48308) | open;  | 0.027673 | UNJUDGED |
| C_bug | bm25 | 1 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 34.845696 | UNJUDGED |
| C_bug | bm25 | 2 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | open; bug | 34.735412 | UNJUDGED |
| C_bug | bm25 | 3 | [Loading `RTDetrModel` from a detection checkpoint (or `SEWDForCTC` from a SEW-D checkpoint) gives a ](https://github.com/huggingface/transformers/issues/48722) | closed; bug | 34.316416 | UNJUDGED |
| C_bug | bm25 | 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 32.205144 | UNJUDGED |
| C_bug | bm25 | 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 31.940743 | UNJUDGED |
| C_bug | semantic | 1 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 0.898617 | UNJUDGED |
| C_bug | semantic | 2 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally](https://github.com/huggingface/transformers/issues/47917) | closed; bug | 0.894636 | UNJUDGED |
| C_bug | semantic | 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 0.891151 | UNJUDGED |
| C_bug | semantic | 4 | [NameError: name &#x27;nn&#x27; is not defined when resolving OutputRecorder type hints](https://github.com/huggingface/transformers/issues/47766) | closed; bug | 0.888508 | UNJUDGED |
| C_bug | semantic | 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 0.887044 | UNJUDGED |
| C_bug | hybrid | 1 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 0.032266 | UNJUDGED |
| C_bug | hybrid | 2 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27;](https://github.com/huggingface/transformers/issues/47436) | closed; bug | 0.030769 | UNJUDGED |
| C_bug | hybrid | 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | closed; bug | 0.030077 | UNJUDGED |
| C_bug | hybrid | 4 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 0.029907 | UNJUDGED |
| C_bug | hybrid | 5 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.028612 | UNJUDGED |

## T-S1 — core_development

참고 원문: [huggingface/transformers#47752](https://github.com/huggingface/transformers/issues/47752). 유형: `symptom_without_error`.

설정 값 불일치가 증상. 예외 traceback 없이 assert 재현만 있음; 실행 조건 겹침은 검토 필요.

### A_ko_symptom

```text
[PROBLEM]
모델에서 설정한 생성 길이가 text-generation 파이프라인에 반영되지 않습니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.031545 | UNJUDGED |
| C_raw | hybrid | 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings)](https://github.com/huggingface/transformers/issues/47981) | closed;  | 0.031010 | UNJUDGED |
| C_raw | hybrid | 3 | [[serge] integration failure triage - 2026-08-23](https://github.com/huggingface/transformers/issues/48240) | closed;  | 0.030835 | UNJUDGED |
| C_raw | hybrid | 4 | [[serge] integration failure triage - 2026-08-24](https://github.com/huggingface/transformers/issues/48263) | closed;  | 0.029437 | UNJUDGED |
| C_raw | hybrid | 5 | [[serge] integration failure triage - 2026-08-25](https://github.com/huggingface/transformers/issues/48321) | closed;  | 0.026320 | UNJUDGED |
| C_raw | semantic | 1 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP](https://github.com/huggingface/transformers/issues/48757) | open;  | 0.866996 | UNJUDGED |
| C_raw | semantic | 2 | [[serge] integration failure triage - 2026-08-23](https://github.com/huggingface/transformers/issues/48240) | closed;  | 0.862661 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-09-22](https://github.com/huggingface/transformers/issues/49026) | closed;  | 0.859122 | UNJUDGED |
| C_raw | semantic | 4 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings)](https://github.com/huggingface/transformers/issues/47981) | closed;  | 0.859077 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.858141 | UNJUDGED |
| C_raw | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 12.642330 | UNJUDGED |
| C_raw | bm25 | 2 | [Continuous batching crashes on every VLM: config attributes read from the top-level config](https://github.com/huggingface/transformers/issues/48298) | closed;  | 5.045750 | UNJUDGED |
| C_raw | bm25 | 3 | [Add native support for OpenBMB VoxCPM2](https://github.com/huggingface/transformers/issues/47695) | open; New model | 4.714354 | UNJUDGED |
| C_raw | bm25 | 4 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 4.359857 | UNJUDGED |
| C_raw | bm25 | 5 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings)](https://github.com/huggingface/transformers/issues/47981) | closed;  | 4.268360 | UNJUDGED |
| C_bug | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.029710 | UNJUDGED |
| C_bug | hybrid | 3 | [MusicGen: forward(labels=...) raises &quot;set the decoder_start_token_id&quot; on every released checkpoint, ](https://github.com/huggingface/transformers/issues/49095) | open; bug | 0.029437 | UNJUDGED |
| C_bug | hybrid | 4 | [gemma 4 can not load audio file and produce  Audio features and audio tokens do not match, tokens: 3](https://github.com/huggingface/transformers/issues/48887) | closed; bug | 0.029387 | UNJUDGED |
| C_bug | hybrid | 5 | [## Flaky test: `IndexError` — bbox coordinate values out of 0-1000 range](https://github.com/huggingface/transformers/issues/47337) | closed; bug | 0.028595 | UNJUDGED |
| C_bug | semantic | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.858076 | UNJUDGED |
| C_bug | semantic | 2 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot;](https://github.com/huggingface/transformers/issues/47553) | closed; bug | 0.857887 | UNJUDGED |
| C_bug | semantic | 3 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model.](https://github.com/huggingface/transformers/issues/48400) | closed; bug | 0.854886 | UNJUDGED |
| C_bug | semantic | 4 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.854681 | UNJUDGED |
| C_bug | semantic | 5 | [AMD quark class not updated](https://github.com/huggingface/transformers/issues/47321) | closed; bug | 0.850054 | UNJUDGED |
| C_bug | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 11.585368 | UNJUDGED |
| C_bug | bm25 | 2 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 4.743748 | UNJUDGED |
| C_bug | bm25 | 3 | [gemma 4 can not load audio file and produce  Audio features and audio tokens do not match, tokens: 3](https://github.com/huggingface/transformers/issues/48887) | closed; bug | 4.691615 | UNJUDGED |
| C_bug | bm25 | 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 4.315738 | UNJUDGED |
| C_bug | bm25 | 5 | [Special tokens aren&#x27;t escaped in template generation](https://github.com/huggingface/transformers/issues/47822) | closed; bug | 4.181645 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Phi-3 모델의 generation_config에서 max_new_tokens를 500으로 설정하고 do_sample=False로 둔 뒤 모델과 토크나이저를 text-generation pipeline에 넘깁니다. pipeline의 generation_config.max_new_tokens가 500이 아니며 모델 설정이 유지되기를 기대합니다.

[ENVIRONMENT]
microsoft/Phi-3-mini-4k-instruct; Transformers 5.14.1; macOS ARM; Python 3.12.13; PyTorch 2.13.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.031498 | UNJUDGED |
| C_raw | hybrid | 4 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 0.030769 | UNJUDGED |
| C_raw | hybrid | 5 | [Mamba2-family `cuda_kernels_forward` decode step is broken since #47452: missing seq-dim squeeze](https://github.com/huggingface/transformers/issues/47532) | closed;  | 0.029031 | UNJUDGED |
| C_raw | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 114.983370 | UNJUDGED |
| C_raw | bm25 | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 60.410180 | UNJUDGED |
| C_raw | bm25 | 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 49.729567 | UNJUDGED |
| C_raw | bm25 | 4 | [[serge] integration failure triage - 2026-08-15](https://github.com/huggingface/transformers/issues/47993) | closed;  | 41.435172 | UNJUDGED |
| C_raw | bm25 | 5 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 40.082181 | UNJUDGED |
| C_raw | semantic | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.915152 | UNJUDGED |
| C_raw | semantic | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.894323 | UNJUDGED |
| C_raw | semantic | 3 | [Mamba2-family `cuda_kernels_forward` decode step is broken since #47452: missing seq-dim squeeze](https://github.com/huggingface/transformers/issues/47532) | closed;  | 0.889717 | UNJUDGED |
| C_raw | semantic | 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.889432 | UNJUDGED |
| C_raw | semantic | 5 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 0.887499 | UNJUDGED |
| C_bug | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 0.030579 | UNJUDGED |
| C_bug | hybrid | 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 0.029958 | UNJUDGED |
| C_bug | hybrid | 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 0.029274 | UNJUDGED |
| C_bug | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 96.401199 | UNJUDGED |
| C_bug | bm25 | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 51.239942 | UNJUDGED |
| C_bug | bm25 | 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 30.723401 | UNJUDGED |
| C_bug | bm25 | 4 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 29.256803 | UNJUDGED |
| C_bug | bm25 | 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 26.947558 | UNJUDGED |
| C_bug | semantic | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.915152 | UNJUDGED |
| C_bug | semantic | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.894323 | UNJUDGED |
| C_bug | semantic | 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 0.885325 | UNJUDGED |
| C_bug | semantic | 4 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to f](https://github.com/huggingface/transformers/issues/49093) | closed; bug | 0.881847 | UNJUDGED |
| C_bug | semantic | 5 | [Incorrect model predictions (because of incorrect tokenization output) after the 5.0 update](https://github.com/huggingface/transformers/issues/48967) | closed; bug | 0.880639 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
I set max_new_tokens=500 and do_sample=False in a Phi-3 model generation_config, then pass the model and tokenizer to a text-generation pipeline. The pipeline generation_config.max_new_tokens is not 500; I expect it to preserve the model setting.

[ENVIRONMENT]
microsoft/Phi-3-mini-4k-instruct; Transformers 5.14.1; macOS ARM; Python 3.12.13; PyTorch 2.13.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.923045 | UNJUDGED |
| C_raw | semantic | 2 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 0.911589 | UNJUDGED |
| C_raw | semantic | 3 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.909233 | UNJUDGED |
| C_raw | semantic | 4 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to f](https://github.com/huggingface/transformers/issues/49093) | closed; bug | 0.906767 | UNJUDGED |
| C_raw | semantic | 5 | [Version-gated tokenizer file selection (fast_tokenizer_files) hands different vocabularies to differ](https://github.com/huggingface/transformers/issues/48836) | closed; Code agent slop | 0.904520 | UNJUDGED |
| C_raw | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 167.425234 | UNJUDGED |
| C_raw | bm25 | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 73.726190 | UNJUDGED |
| C_raw | bm25 | 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 70.241029 | UNJUDGED |
| C_raw | bm25 | 4 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 63.058151 | UNJUDGED |
| C_raw | bm25 | 5 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 58.034237 | UNJUDGED |
| C_raw | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant](https://github.com/huggingface/transformers/issues/48039) | closed;  | 0.031754 | UNJUDGED |
| C_raw | hybrid | 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.030159 | UNJUDGED |
| C_raw | hybrid | 5 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 0.029631 | UNJUDGED |
| C_bug | semantic | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.923045 | UNJUDGED |
| C_bug | semantic | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.909233 | UNJUDGED |
| C_bug | semantic | 3 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to f](https://github.com/huggingface/transformers/issues/49093) | closed; bug | 0.906767 | UNJUDGED |
| C_bug | semantic | 4 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 0.903025 | UNJUDGED |
| C_bug | semantic | 5 | [Incorrect model predictions (because of incorrect tokenization output) after the 5.0 update](https://github.com/huggingface/transformers/issues/48967) | closed; bug | 0.902462 | UNJUDGED |
| C_bug | bm25 | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 142.860403 | UNJUDGED |
| C_bug | bm25 | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 64.427423 | UNJUDGED |
| C_bug | bm25 | 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 50.884251 | UNJUDGED |
| C_bug | bm25 | 4 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 44.916572 | UNJUDGED |
| C_bug | bm25 | 5 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 42.932380 | UNJUDGED |
| C_bug | hybrid | 1 | [incorrect precedence of generation_config values](https://github.com/huggingface/transformers/issues/47752) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` sc](https://github.com/huggingface/transformers/issues/48748) | closed; bug | 0.031250 | UNJUDGED |
| C_bug | hybrid | 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 0.027921 | UNJUDGED |
| C_bug | hybrid | 5 | [ESMFold throws error when explicitly cast to fp16](https://github.com/huggingface/transformers/issues/47470) | closed; bug | 0.027826 | UNJUDGED |

## T-S2 — core_development

참고 원문: [huggingface/transformers#48826](https://github.com/huggingface/transformers/issues/48826). 유형: `symptom_without_error`.

indexer 학습 불가가 보고됨. 원인으로 지목된 연산과 해결 제안은 질의에 넣지 않음.

### A_ko_symptom

```text
[PROBLEM]
Qwen의 QSA indexer 파라미터를 학습하려는데 업데이트되지 않습니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 20.870035 | UNJUDGED |
| C_raw | bm25 | 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41)](https://github.com/huggingface/transformers/issues/48755) | open;  | 9.680246 | UNJUDGED |
| C_raw | bm25 | 3 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures](https://github.com/huggingface/transformers/issues/48913) | open;  | 5.648850 | UNJUDGED |
| C_raw | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41)](https://github.com/huggingface/transformers/issues/48755) | open;  | 0.016129 | UNJUDGED |
| C_raw | hybrid | 3 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.016129 | UNJUDGED |
| C_raw | hybrid | 4 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures](https://github.com/huggingface/transformers/issues/48913) | open;  | 0.015873 | UNJUDGED |
| C_raw | hybrid | 5 | [[serge] integration failure triage - 2026-09-21](https://github.com/huggingface/transformers/issues/49000) | closed;  | 0.015873 | UNJUDGED |
| C_raw | semantic | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.869992 | UNJUDGED |
| C_raw | semantic | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.867107 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-09-21](https://github.com/huggingface/transformers/issues/49000) | closed;  | 0.862534 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-09-29](https://github.com/huggingface/transformers/issues/49175) | closed;  | 0.861561 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.857563 | UNJUDGED |
| C_bug | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 17.616901 | UNJUDGED |
| C_bug | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.016129 | UNJUDGED |
| C_bug | hybrid | 3 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors](https://github.com/huggingface/transformers/issues/49190) | open; bug | 0.015873 | UNJUDGED |
| C_bug | hybrid | 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot;](https://github.com/huggingface/transformers/issues/47553) | closed; bug | 0.015625 | UNJUDGED |
| C_bug | hybrid | 5 | [BarthezTokenizer cannot load moussaKam/barthez: v4.57 → v5 regression, BPE vocab into a hardcoded Un](https://github.com/huggingface/transformers/issues/48567) | closed; bug | 0.015385 | UNJUDGED |
| C_bug | semantic | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.869992 | UNJUDGED |
| C_bug | semantic | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.867107 | UNJUDGED |
| C_bug | semantic | 3 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors](https://github.com/huggingface/transformers/issues/49190) | open; bug | 0.856506 | UNJUDGED |
| C_bug | semantic | 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot;](https://github.com/huggingface/transformers/issues/47553) | closed; bug | 0.851359 | UNJUDGED |
| C_bug | semantic | 5 | [BarthezTokenizer cannot load moussaKam/barthez: v4.57 → v5 regression, BPE vocab into a hardcoded Un](https://github.com/huggingface/transformers/issues/48567) | closed; bug | 0.850741 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Qwen3.8-flash-next의 QSA indexer 파라미터를 학습하려고 합니다. 기술 보고서는 KL loss로 학습할 수 있다고 하는데 현재 코드에서 파라미터가 학습되지 않습니다.

[ENVIRONMENT]
버전과 실행 환경은 원문에 제공되지 않음
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032522 | UNJUDGED |
| C_raw | hybrid | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.031319 | UNJUDGED |
| C_raw | hybrid | 3 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization](https://github.com/huggingface/transformers/issues/48350) | closed;  | 0.029211 | UNJUDGED |
| C_raw | hybrid | 4 | [[serge] integration failure triage - 2026-09-29](https://github.com/huggingface/transformers/issues/49175) | closed;  | 0.027032 | UNJUDGED |
| C_raw | hybrid | 5 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.026133 | UNJUDGED |
| C_raw | semantic | 1 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.887116 | UNJUDGED |
| C_raw | semantic | 2 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.886868 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-08-18](https://github.com/huggingface/transformers/issues/48050) | closed;  | 0.882216 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-09-28](https://github.com/huggingface/transformers/issues/49169) | closed;  | 0.881454 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-09-12](https://github.com/huggingface/transformers/issues/48749) | closed;  | 0.878500 | UNJUDGED |
| C_raw | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 36.592071 | UNJUDGED |
| C_raw | bm25 | 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41)](https://github.com/huggingface/transformers/issues/48755) | open;  | 15.042218 | UNJUDGED |
| C_raw | bm25 | 3 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures](https://github.com/huggingface/transformers/issues/48913) | open;  | 9.197127 | UNJUDGED |
| C_raw | bm25 | 4 | [FineGrainedFP8: modules_to_not_convert never matches on text-only loads of multimodal checkpoints (s](https://github.com/huggingface/transformers/issues/48349) | closed;  | 9.015581 | UNJUDGED |
| C_raw | bm25 | 5 | [Qwen3.5-9B fine-tuning with run_clm.py on 8x B200 ran the gated DeltaNet layers on the fp32 torch ch](https://github.com/huggingface/transformers/issues/48718) | open;  | 8.996552 | UNJUDGED |
| C_bug | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032522 | UNJUDGED |
| C_bug | hybrid | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.032522 | UNJUDGED |
| C_bug | hybrid | 3 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.031258 | UNJUDGED |
| C_bug | hybrid | 4 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors](https://github.com/huggingface/transformers/issues/49190) | open; bug | 0.029211 | UNJUDGED |
| C_bug | hybrid | 5 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.028694 | UNJUDGED |
| C_bug | semantic | 1 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.887116 | UNJUDGED |
| C_bug | semantic | 2 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.886868 | UNJUDGED |
| C_bug | semantic | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.874595 | UNJUDGED |
| C_bug | semantic | 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot;](https://github.com/huggingface/transformers/issues/47553) | closed; bug | 0.874356 | UNJUDGED |
| C_bug | semantic | 5 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.873136 | UNJUDGED |
| C_bug | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 32.461828 | UNJUDGED |
| C_bug | bm25 | 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 9.373549 | UNJUDGED |
| C_bug | bm25 | 3 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 8.156084 | UNJUDGED |
| C_bug | bm25 | 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert)](https://github.com/huggingface/transformers/issues/48312) | closed;  | 7.626278 | UNJUDGED |
| C_bug | bm25 | 5 | [Transformers 5.13 CPU memory growth loading Qwen3-235B-A22B with DeepSpeed ZeRO-3; 4.51.0 remains bo](https://github.com/huggingface/transformers/issues/47514) | closed; bug | 7.057966 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
I want to train the QSA indexer parameters in Qwen3.8-flash-next. The technical report says they can be trained with KL loss, but the parameters cannot be trained in the current code.

[ENVIRONMENT]
The source report does not provide a version or runtime environment
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 102.473000 | UNJUDGED |
| C_raw | bm25 | 2 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field](https://github.com/huggingface/transformers/issues/48241) | closed;  | 30.124117 | UNJUDGED |
| C_raw | bm25 | 3 | [MusicGen: hub configs set decoder dropout=0.1 but the checkpoints were trained with 0 — train() doub](https://github.com/huggingface/transformers/issues/49094) | open; bug | 29.928458 | UNJUDGED |
| C_raw | bm25 | 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 29.836751 | UNJUDGED |
| C_raw | bm25 | 5 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare](https://github.com/huggingface/transformers/issues/48841) | open;  | 28.965862 | UNJUDGED |
| C_raw | semantic | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.912735 | UNJUDGED |
| C_raw | semantic | 2 | [CompressedTensorsConfig(run_compressed=False) silently random-initializes unmapped fused-MoE expert ](https://github.com/huggingface/transformers/issues/47407) | closed;  | 0.901575 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-08-18](https://github.com/huggingface/transformers/issues/48050) | closed;  | 0.896658 | UNJUDGED |
| C_raw | semantic | 4 | [Qwen3.5-9B fine-tuning with run_clm.py on 8x B200 ran the gated DeltaNet layers on the fp32 torch ch](https://github.com/huggingface/transformers/issues/48718) | open;  | 0.895864 | UNJUDGED |
| C_raw | semantic | 5 | [Llama 4 declares `output_router_logits` and `router_aux_loss_coef` but never reads them](https://github.com/huggingface/transformers/issues/48889) | open;  | 0.893816 | UNJUDGED |
| C_raw | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.029911 | UNJUDGED |
| C_raw | hybrid | 3 | [Heads that declare **kwargs but drop num_items_in_batch train with an inflated loss under gradient a](https://github.com/huggingface/transformers/issues/47688) | closed;  | 0.029851 | UNJUDGED |
| C_raw | hybrid | 4 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare](https://github.com/huggingface/transformers/issues/48841) | open;  | 0.028372 | UNJUDGED |
| C_raw | hybrid | 5 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.027984 | UNJUDGED |
| C_bug | bm25 | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 92.760097 | UNJUDGED |
| C_bug | bm25 | 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 29.390883 | UNJUDGED |
| C_bug | bm25 | 3 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 27.516787 | UNJUDGED |
| C_bug | bm25 | 4 | [MusicGen: hub configs set decoder dropout=0.1 but the checkpoints were trained with 0 — train() doub](https://github.com/huggingface/transformers/issues/49094) | open; bug | 25.723290 | UNJUDGED |
| C_bug | bm25 | 5 | [`Qwen3_5GatedDeltaNet` / `Qwen3_5MoeGatedDeltaNet` initialize `A_log` to `-inf` on some heads (bf16 ](https://github.com/huggingface/transformers/issues/47831) | closed; bug | 24.660842 | UNJUDGED |
| C_bug | semantic | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.912735 | UNJUDGED |
| C_bug | semantic | 2 | [Qwen3-VL and Gemma3 (VLM) ignore `shift_labels`](https://github.com/huggingface/transformers/issues/48491) | closed; bug | 0.893778 | UNJUDGED |
| C_bug | semantic | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.891449 | UNJUDGED |
| C_bug | semantic | 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.890694 | UNJUDGED |
| C_bug | semantic | 5 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.889962 | UNJUDGED |
| C_bug | hybrid | 1 | [[Qwen3.8-flash-next] QSAIndexer can not train](https://github.com/huggingface/transformers/issues/48826) | open; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [Installed nested optional kernels silently fall back to the Torch implementation](https://github.com/huggingface/transformers/issues/48148) | closed; bug | 0.031258 | UNJUDGED |
| C_bug | hybrid | 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.030777 | UNJUDGED |
| C_bug | hybrid | 5 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.029857 | UNJUDGED |

## T-C1 — core_development

참고 원문: [huggingface/transformers#48501](https://github.com/huggingface/transformers/issues/48501). 유형: `condition_sensitive`.

static cache와 chunked prefill의 조합 및 layer별 head_dim이 핵심 조건. 원인/수정은 제외.

### A_ko_symptom

```text
[PROBLEM]
Gemma4에서 generate를 실행하면 예외가 발생합니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.869015 | UNJUDGED |
| C_raw | semantic | 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings)](https://github.com/huggingface/transformers/issues/47981) | closed;  | 0.864526 | UNJUDGED |
| C_raw | semantic | 3 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.860098 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-09-29](https://github.com/huggingface/transformers/issues/49175) | closed;  | 0.855934 | UNJUDGED |
| C_raw | semantic | 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.854509 | UNJUDGED |
| C_raw | bm25 | — | no_lexical_match | — | — | UNJUDGED |
| C_raw | hybrid | 1 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.016393 | UNJUDGED |
| C_raw | hybrid | 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings)](https://github.com/huggingface/transformers/issues/47981) | closed;  | 0.016129 | UNJUDGED |
| C_raw | hybrid | 3 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.015873 | UNJUDGED |
| C_raw | hybrid | 4 | [[serge] integration failure triage - 2026-09-29](https://github.com/huggingface/transformers/issues/49175) | closed;  | 0.015625 | UNJUDGED |
| C_raw | hybrid | 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.015385 | UNJUDGED |
| C_bug | semantic | 1 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.869015 | UNJUDGED |
| C_bug | semantic | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.860098 | UNJUDGED |
| C_bug | semantic | 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.854509 | UNJUDGED |
| C_bug | semantic | 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.853267 | UNJUDGED |
| C_bug | semantic | 5 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.852938 | UNJUDGED |
| C_bug | bm25 | — | no_lexical_match | — | — | UNJUDGED |
| C_bug | hybrid | 1 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.016393 | UNJUDGED |
| C_bug | hybrid | 2 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.016129 | UNJUDGED |
| C_bug | hybrid | 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.015873 | UNJUDGED |
| C_bug | hybrid | 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.015625 | UNJUDGED |
| C_bug | hybrid | 5 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logi](https://github.com/huggingface/transformers/issues/47530) | closed; bug | 0.015385 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Gemma4 generate에서 cache_implementation="static"과 prefill_chunk_size=2를 함께 사용하면 예외가 납니다. sliding_attention과 full_attention 층이 섞여 있고 층마다 head_dim이 다르게 설정된 모델입니다. CPU에서도 재현됩니다.

[ERROR]
AmbiguousGlobalPerLayerAttributeError: 'head_dim' is a per-layer attribute and may vary across layers.

[ENVIRONMENT]
Transformers 5.16.0.dev0; Linux; Python 3.12; torch 2.9.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.951555 | UNJUDGED |
| C_raw | semantic | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.913461 | UNJUDGED |
| C_raw | semantic | 3 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mapping](https://github.com/huggingface/transformers/issues/47534) | closed;  | 0.904154 | UNJUDGED |
| C_raw | semantic | 4 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8)](https://github.com/huggingface/transformers/issues/48305) | open;  | 0.898004 | UNJUDGED |
| C_raw | semantic | 5 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.897306 | UNJUDGED |
| C_raw | hybrid | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys](https://github.com/huggingface/transformers/issues/48392) | closed;  | 0.031025 | UNJUDGED |
| C_raw | hybrid | 4 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mapping](https://github.com/huggingface/transformers/issues/47534) | closed;  | 0.030366 | UNJUDGED |
| C_raw | hybrid | 5 | [[BUG] Odd head_dim is accepted but RoPE crashes during forward](https://github.com/huggingface/transformers/issues/48101) | closed;  | 0.030077 | UNJUDGED |
| C_raw | bm25 | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 150.798298 | UNJUDGED |
| C_raw | bm25 | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 86.047042 | UNJUDGED |
| C_raw | bm25 | 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys](https://github.com/huggingface/transformers/issues/48392) | closed;  | 52.648988 | UNJUDGED |
| C_raw | bm25 | 4 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field](https://github.com/huggingface/transformers/issues/48241) | closed;  | 48.114277 | UNJUDGED |
| C_raw | bm25 | 5 | [Add Kimi Linear (Kimi Delta Attention) native support](https://github.com/huggingface/transformers/issues/47875) | closed;  | 47.264531 | UNJUDGED |
| C_bug | semantic | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.951555 | UNJUDGED |
| C_bug | semantic | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.913461 | UNJUDGED |
| C_bug | semantic | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.897306 | UNJUDGED |
| C_bug | semantic | 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.890842 | UNJUDGED |
| C_bug | semantic | 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 0.890020 | UNJUDGED |
| C_bug | hybrid | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix](https://github.com/huggingface/transformers/issues/47246) | closed; bug | 0.031025 | UNJUDGED |
| C_bug | hybrid | 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 0.028612 | UNJUDGED |
| C_bug | hybrid | 5 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache](https://github.com/huggingface/transformers/issues/48693) | open; bug | 0.028309 | UNJUDGED |
| C_bug | bm25 | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 141.033990 | UNJUDGED |
| C_bug | bm25 | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 82.396104 | UNJUDGED |
| C_bug | bm25 | 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix](https://github.com/huggingface/transformers/issues/47246) | closed; bug | 30.462793 | UNJUDGED |
| C_bug | bm25 | 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 29.128311 | UNJUDGED |
| C_bug | bm25 | 5 | [`use_gqa_in_sdpa` doesn&#x27;t check GPU architecture: up to 28% slower decode on pre-sm80 GPUs](https://github.com/huggingface/transformers/issues/48633) | closed; bug | 28.686372 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
Gemma4 generate raises when cache_implementation="static" is combined with prefill_chunk_size=2. The model mixes sliding_attention and full_attention layers with different head_dim settings per layer. It also reproduces on CPU.

[ERROR]
AmbiguousGlobalPerLayerAttributeError: 'head_dim' is a per-layer attribute and may vary across layers.

[ENVIRONMENT]
Transformers 5.16.0.dev0; Linux; Python 3.12; torch 2.9.0
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.966008 | UNJUDGED |
| C_raw | semantic | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.930611 | UNJUDGED |
| C_raw | semantic | 3 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mapping](https://github.com/huggingface/transformers/issues/47534) | closed;  | 0.912893 | UNJUDGED |
| C_raw | semantic | 4 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8)](https://github.com/huggingface/transformers/issues/48305) | open;  | 0.907399 | UNJUDGED |
| C_raw | semantic | 5 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys](https://github.com/huggingface/transformers/issues/48392) | closed;  | 0.904942 | UNJUDGED |
| C_raw | hybrid | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.032258 | UNJUDGED |
| C_raw | hybrid | 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys](https://github.com/huggingface/transformers/issues/48392) | closed;  | 0.031258 | UNJUDGED |
| C_raw | hybrid | 4 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mapping](https://github.com/huggingface/transformers/issues/47534) | closed;  | 0.029958 | UNJUDGED |
| C_raw | hybrid | 5 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8)](https://github.com/huggingface/transformers/issues/48305) | open;  | 0.028958 | UNJUDGED |
| C_raw | bm25 | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 197.647331 | UNJUDGED |
| C_raw | bm25 | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 124.699802 | UNJUDGED |
| C_raw | bm25 | 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys](https://github.com/huggingface/transformers/issues/48392) | closed;  | 79.453651 | UNJUDGED |
| C_raw | bm25 | 4 | [Add Kimi Linear (Kimi Delta Attention) native support](https://github.com/huggingface/transformers/issues/47875) | closed;  | 67.248836 | UNJUDGED |
| C_raw | bm25 | 5 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field](https://github.com/huggingface/transformers/issues/48241) | closed;  | 66.548644 | UNJUDGED |
| C_bug | semantic | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.966008 | UNJUDGED |
| C_bug | semantic | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.930611 | UNJUDGED |
| C_bug | semantic | 3 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | closed; bug | 0.904933 | UNJUDGED |
| C_bug | semantic | 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 remov](https://github.com/huggingface/transformers/issues/49051) | closed; bug | 0.902369 | UNJUDGED |
| C_bug | semantic | 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 0.899118 | UNJUDGED |
| C_bug | hybrid | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix](https://github.com/huggingface/transformers/issues/47246) | closed; bug | 0.030536 | UNJUDGED |
| C_bug | hybrid | 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 0.029206 | UNJUDGED |
| C_bug | hybrid | 5 | [[BLT, Byte-Latent Transformer] Entropy patcher is missing BLT&#x27;s 512-token sliding-window attention —](https://github.com/huggingface/transformers/issues/49185) | open; bug | 0.028624 | UNJUDGED |
| C_bug | bm25 | 1 | [Exception raised for Gemma4 with static cache and chunked prefill](https://github.com/huggingface/transformers/issues/48501) | closed; bug | 187.734694 | UNJUDGED |
| C_bug | bm25 | 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_head](https://github.com/huggingface/transformers/issues/47721) | closed; bug | 122.206336 | UNJUDGED |
| C_bug | bm25 | 3 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 46.189392 | UNJUDGED |
| C_bug | bm25 | 4 | [`use_gqa_in_sdpa` doesn&#x27;t check GPU architecture: up to 28% slower decode on pre-sm80 GPUs](https://github.com/huggingface/transformers/issues/48633) | closed; bug | 46.094426 | UNJUDGED |
| C_bug | bm25 | 5 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix](https://github.com/huggingface/transformers/issues/47246) | closed; bug | 41.662392 | UNJUDGED |

## T-C2 — core_development

참고 원문: [huggingface/transformers#48315](https://github.com/huggingface/transformers/issues/48315). 유형: `condition_sensitive`.

이동한 체크포인트·없는 best 경로·새 best 부재·save_total_limit=1 조합이 중요.

### A_ko_symptom

```text
[PROBLEM]
체크포인트에서 재개한 Trainer 학습이 끝까지 진행된 뒤 마지막에 파일 오류로 실패합니다.
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | semantic | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.872970 | UNJUDGED |
| C_raw | semantic | 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.865739 | UNJUDGED |
| C_raw | semantic | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.859925 | UNJUDGED |
| C_raw | semantic | 4 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.856185 | UNJUDGED |
| C_raw | semantic | 5 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discov](https://github.com/huggingface/transformers/issues/47375) | closed;  | 0.854831 | UNJUDGED |
| C_raw | hybrid | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.032018 | UNJUDGED |
| C_raw | hybrid | 2 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discov](https://github.com/huggingface/transformers/issues/47375) | closed;  | 0.031778 | UNJUDGED |
| C_raw | hybrid | 3 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.031281 | UNJUDGED |
| C_raw | hybrid | 4 | [Nothing destroys the process group, so every distributed Trainer run warns at exit](https://github.com/huggingface/transformers/issues/48874) | closed;  | 0.031025 | UNJUDGED |
| C_raw | hybrid | 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.030798 | UNJUDGED |
| C_raw | bm25 | 1 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discov](https://github.com/huggingface/transformers/issues/47375) | closed;  | 6.184072 | UNJUDGED |
| C_raw | bm25 | 2 | [Should Trainer support models FSDP2-sharded at load time (DistributedConfig(fsdp_size=N))?](https://github.com/huggingface/transformers/issues/48210) | closed;  | 6.146981 | UNJUDGED |
| C_raw | bm25 | 3 | [Nothing destroys the process group, so every distributed Trainer run warns at exit](https://github.com/huggingface/transformers/issues/48874) | closed;  | 5.931824 | UNJUDGED |
| C_raw | bm25 | 4 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 5.929963 | UNJUDGED |
| C_raw | bm25 | 5 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare](https://github.com/huggingface/transformers/issues/48841) | open;  | 5.903999 | UNJUDGED |
| C_bug | semantic | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.865739 | UNJUDGED |
| C_bug | semantic | 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.859925 | UNJUDGED |
| C_bug | semantic | 3 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.856185 | UNJUDGED |
| C_bug | semantic | 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.852312 | UNJUDGED |
| C_bug | semantic | 5 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.851905 | UNJUDGED |
| C_bug | hybrid | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.032258 | UNJUDGED |
| C_bug | hybrid | 3 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.031498 | UNJUDGED |
| C_bug | hybrid | 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.031010 | UNJUDGED |
| C_bug | hybrid | 5 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.030366 | UNJUDGED |
| C_bug | bm25 | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 5.995781 | UNJUDGED |
| C_bug | bm25 | 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 5.992928 | UNJUDGED |
| C_bug | bm25 | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 5.705326 | UNJUDGED |
| C_bug | bm25 | 4 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 5.688558 | UNJUDGED |
| C_bug | bm25 | 5 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 5.404516 | UNJUDGED |

### B_ko_context

```text
[PROBLEM]
Trainer 체크포인트를 다른 위치로 옮긴 뒤 재개했습니다. trainer_state.json의 best_model_checkpoint는 존재하지 않는 이전 경로를 가리킵니다. 새 best가 생기지 않았고 save_total_limit=1, load_best_model_at_end=True입니다. 학습은 끝났지만 마지막 정리에서 실패합니다.

[ERROR]
FileNotFoundError: [WinError 2] The system cannot find the file specified

[ENVIRONMENT]
Transformers 5.16.0.dev0; torch 2.11.0+cu128; Python 3.12.6; Windows 11
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | bm25 | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 133.161770 | UNJUDGED |
| C_raw | bm25 | 2 | [XPU: `from_pretrained(device_map=...)` fails under WSL2 because `caching_allocator_warmup` does not ](https://github.com/huggingface/transformers/issues/48127) | closed;  | 42.004308 | UNJUDGED |
| C_raw | bm25 | 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 37.600505 | UNJUDGED |
| C_raw | bm25 | 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 37.143272 | UNJUDGED |
| C_raw | bm25 | 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-o](https://github.com/huggingface/transformers/issues/48285) | closed; bug | 36.829554 | UNJUDGED |
| C_raw | semantic | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.916085 | UNJUDGED |
| C_raw | semantic | 2 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.887187 | UNJUDGED |
| C_raw | semantic | 3 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B`](https://github.com/huggingface/transformers/issues/47333) | closed; bug | 0.886227 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.883250 | UNJUDGED |
| C_raw | semantic | 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.881578 | UNJUDGED |
| C_raw | hybrid | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.029911 | UNJUDGED |
| C_raw | hybrid | 3 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.029287 | UNJUDGED |
| C_raw | hybrid | 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.029236 | UNJUDGED |
| C_raw | hybrid | 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.029083 | UNJUDGED |
| C_bug | bm25 | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 31.146240 | UNJUDGED |
| C_bug | bm25 | 2 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 30.439230 | UNJUDGED |
| C_bug | bm25 | 3 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-o](https://github.com/huggingface/transformers/issues/48285) | closed; bug | 30.341069 | UNJUDGED |
| C_bug | bm25 | 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 27.695244 | UNJUDGED |
| C_bug | bm25 | 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with ](https://github.com/huggingface/transformers/issues/47914) | closed; bug | 26.607115 | UNJUDGED |
| C_bug | semantic | 1 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.887187 | UNJUDGED |
| C_bug | semantic | 2 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B`](https://github.com/huggingface/transformers/issues/47333) | closed; bug | 0.886227 | UNJUDGED |
| C_bug | semantic | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.881578 | UNJUDGED |
| C_bug | semantic | 4 | [[Offloading] Cannot save disk-offloaded `Qwen3-VL-32B-Instruct`](https://github.com/huggingface/transformers/issues/47332) | closed; bug | 0.879877 | UNJUDGED |
| C_bug | semantic | 5 | [AMD quark class not updated](https://github.com/huggingface/transformers/issues/47321) | closed; bug | 0.879359 | UNJUDGED |
| C_bug | hybrid | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.031545 | UNJUDGED |
| C_bug | hybrid | 2 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.031319 | UNJUDGED |
| C_bug | hybrid | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.031025 | UNJUDGED |
| C_bug | hybrid | 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.030622 | UNJUDGED |
| C_bug | hybrid | 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-o](https://github.com/huggingface/transformers/issues/48285) | closed; bug | 0.030579 | UNJUDGED |

### C_en_context

```text
[PROBLEM]
I resumed Trainer after moving the checkpoint to a different location. The best_model_checkpoint in trainer_state.json points to an old path that no longer exists. No new best was set, with save_total_limit=1 and load_best_model_at_end=True. Training completes but final cleanup fails.

[ERROR]
FileNotFoundError: [WinError 2] The system cannot find the file specified

[ENVIRONMENT]
Transformers 5.16.0.dev0; torch 2.11.0+cu128; Python 3.12.6; Windows 11
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.031498 | UNJUDGED |
| C_raw | hybrid | 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.030310 | UNJUDGED |
| C_raw | hybrid | 5 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.029877 | UNJUDGED |
| C_raw | semantic | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 0.951691 | UNJUDGED |
| C_raw | semantic | 2 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.913406 | UNJUDGED |
| C_raw | semantic | 3 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.906569 | UNJUDGED |
| C_raw | semantic | 4 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.898581 | UNJUDGED |
| C_raw | semantic | 5 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | closed;  | 0.897998 | UNJUDGED |
| C_raw | bm25 | 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at ](https://github.com/huggingface/transformers/issues/48315) | closed;  | 224.584587 | UNJUDGED |
| C_raw | bm25 | 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 75.662592 | UNJUDGED |
| C_raw | bm25 | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 60.163050 | UNJUDGED |
| C_raw | bm25 | 4 | [XPU: `from_pretrained(device_map=...)` fails under WSL2 because `caching_allocator_warmup` does not ](https://github.com/huggingface/transformers/issues/48127) | closed;  | 60.157969 | UNJUDGED |
| C_raw | bm25 | 5 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 58.202330 | UNJUDGED |
| C_bug | hybrid | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.032522 | UNJUDGED |
| C_bug | hybrid | 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.031498 | UNJUDGED |
| C_bug | hybrid | 4 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.030679 | UNJUDGED |
| C_bug | hybrid | 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-o](https://github.com/huggingface/transformers/issues/48285) | closed; bug | 0.030090 | UNJUDGED |
| C_bug | semantic | 1 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | open; bug | 0.913406 | UNJUDGED |
| C_bug | semantic | 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 0.906569 | UNJUDGED |
| C_bug | semantic | 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 0.898581 | UNJUDGED |
| C_bug | semantic | 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 0.896198 | UNJUDGED |
| C_bug | semantic | 5 | [Silent conversion skip on model_type mismatch: loading a converted checkpoint via the wrong Auto cla](https://github.com/huggingface/transformers/issues/47405) | closed; bug | 0.895047 | UNJUDGED |
| C_bug | bm25 | 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | open; bug | 65.792543 | UNJUDGED |
| C_bug | bm25 | 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | closed; bug | 50.076430 | UNJUDGED |
| C_bug | bm25 | 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | closed; bug | 49.754540 | UNJUDGED |
| C_bug | bm25 | 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 49.285171 | UNJUDGED |
| C_bug | bm25 | 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-o](https://github.com/huggingface/transformers/issues/48285) | closed; bug | 47.411031 | UNJUDGED |

## H-O — historical_probe

참고 원문: [opencv/opencv#17687](https://github.com/opencv/opencv/issues/17687). 유형: `historical`.

이미 노출된 역사 사례, 핵심 표본 평균에서 제외.

### B_ko_context

```text
[PROBLEM]
OpenCV에서 Windows 웹캠을 CAP_MSMF 또는 CAP_ANY로 열면 오래 걸리지만 CAP_DSHOW로 열 때는 다르게 동작합니다.

[ENVIRONMENT]
Windows 웹캠; CAP_MSMF, CAP_ANY, CAP_DSHOW 비교
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 0.032787 | UNJUDGED |
| C_raw | hybrid | 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.032002 | UNJUDGED |
| C_raw | hybrid | 3 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like so](https://github.com/opencv/opencv/issues/29724) | closed; question (invalid tracker) | 0.031250 | UNJUDGED |
| C_raw | hybrid | 4 | [AVFoundation seeking drifts for non-integer frame rates](https://github.com/opencv/opencv/issues/28831) | closed; bug | 0.027783 | UNJUDGED |
| C_raw | hybrid | 5 | [Heap Buffer Overflow in MJPEG Encoder mjpeg_buffer::put_bits via Small Frame (1×1)](https://github.com/opencv/opencv/issues/29112) | closed; bug, category: videoio | 0.027651 | UNJUDGED |
| C_raw | semantic | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 0.882545 | UNJUDGED |
| C_raw | semantic | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.879736 | UNJUDGED |
| C_raw | semantic | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.876583 | UNJUDGED |
| C_raw | semantic | 4 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like so](https://github.com/opencv/opencv/issues/29724) | closed; question (invalid tracker) | 0.869413 | UNJUDGED |
| C_raw | semantic | 5 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.868735 | UNJUDGED |
| C_raw | bm25 | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 74.811462 | UNJUDGED |
| C_raw | bm25 | 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 67.371843 | UNJUDGED |
| C_raw | bm25 | 3 | [5.x: intermittent opencv-python crash on process exit after VideoCapture fails to find a decoder (re](https://github.com/opencv/opencv/issues/30017) | open;  | 56.320538 | UNJUDGED |
| C_raw | bm25 | 4 | [CAP_ANY aborts instead of falling through when CAP_IMAGES&#x27;s pattern check rejects a long/URL-like so](https://github.com/opencv/opencv/issues/29724) | closed; question (invalid tracker) | 53.362488 | UNJUDGED |
| C_raw | bm25 | 5 | [Potential license issue with cap_msmf.cpp](https://github.com/opencv/opencv/issues/28594) | open;  | 51.940191 | UNJUDGED |
| C_bug | hybrid | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 0.032787 | UNJUDGED |
| C_bug | hybrid | 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.032002 | UNJUDGED |
| C_bug | hybrid | 3 | [AVFoundation seeking drifts for non-integer frame rates](https://github.com/opencv/opencv/issues/28831) | closed; bug | 0.029670 | UNJUDGED |
| C_bug | hybrid | 4 | [Heap Buffer Overflow in MJPEG Encoder mjpeg_buffer::put_bits via Small Frame (1×1)](https://github.com/opencv/opencv/issues/29112) | closed; bug, category: videoio | 0.029412 | UNJUDGED |
| C_bug | hybrid | 5 | [Performance regression: cv::compare on Windows ~4× slower in OpenCV 4.12 vs 4.11](https://github.com/opencv/opencv/issues/28251) | closed; bug, optimization, category: core | 0.028485 | UNJUDGED |
| C_bug | semantic | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 0.882545 | UNJUDGED |
| C_bug | semantic | 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | closed; bug, category: build/install, platform: win32 | 0.879736 | UNJUDGED |
| C_bug | semantic | 3 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 0.876583 | UNJUDGED |
| C_bug | semantic | 4 | [Division-by-Zero in OpenCV SGBM 3-Way Mode](https://github.com/opencv/opencv/issues/29761) | closed; bug, category: calib3d | 0.868735 | UNJUDGED |
| C_bug | semantic | 5 | [opencv 5.0.0 build failed: identifier &quot;ulong&quot; is undefined](https://github.com/opencv/opencv/issues/29265) | open; bug, category: build/install, platform: win32 | 0.868395 | UNJUDGED |
| C_bug | bm25 | 1 | [videoio(MSMF): SourceReaderCB leaks an Event handle 🤖🤖🤖](https://github.com/opencv/opencv/issues/29562) | closed; bug, category: videoio, platform: win32 | 75.711055 | UNJUDGED |
| C_bug | bm25 | 2 | [Open CV cannot open Microsoft&#x27;s demo camera named ball -](https://github.com/opencv/opencv/issues/28904) | open; bug, category: videoio, platform: win32 | 69.322151 | UNJUDGED |
| C_bug | bm25 | 3 | [videoio: unnecessary use of get&lt;double&gt;() for integer parameters in several backends](https://github.com/opencv/opencv/issues/28498) | closed; bug, category: videoio | 52.290815 | UNJUDGED |
| C_bug | bm25 | 4 | [VideoCapture FFMPEG backend: crash (Windows/Linux) or silent frame corruption (macOS) when pixel for](https://github.com/opencv/opencv/issues/29699) | closed; bug, category: videoio | 41.446574 | UNJUDGED |
| C_bug | bm25 | 5 | [AVFoundation seeking drifts for non-integer frame rates](https://github.com/opencv/opencv/issues/28831) | closed; bug | 38.661242 | UNJUDGED |

## H-T — historical_probe

참고 원문: [huggingface/transformers#24694](https://github.com/huggingface/transformers/issues/24694). 유형: `historical`.

이미 노출된 역사 사례, 핵심 표본 평균에서 제외.

### B_ko_context

```text
[PROBLEM]
GPT-Neo에서 입력에 왼쪽 패딩을 넣으면 생성 결과가 반복적이고 부자연스러워집니다.

[ENVIRONMENT]
GPT-Neo; left padding
```

| 범위 | 방법 | 순위 | 결과 | 상태·레이블 | 점수 | 사람 판정 |
|---|---|---:|---|---|---:|---|
| C_raw | hybrid | 1 | [[serge] integration failure triage - 2026-08-22](https://github.com/huggingface/transformers/issues/48222) | closed;  | 0.029727 | UNJUDGED |
| C_raw | hybrid | 2 | [Right-padded prefill produces a corrupted cache in Mamba-family models (zero conv state, decayed SSM](https://github.com/huggingface/transformers/issues/48256) | open;  | 0.028191 | UNJUDGED |
| C_raw | hybrid | 3 | [[serge] integration failure triage - 2026-08-18](https://github.com/huggingface/transformers/issues/48050) | closed;  | 0.025942 | UNJUDGED |
| C_raw | hybrid | 4 | [Major Bug in parallel generation / left padding.](https://github.com/huggingface/transformers/issues/47651) | closed; bug | 0.025859 | UNJUDGED |
| C_raw | hybrid | 5 | [[serge] integration failure triage - 2026-08-21](https://github.com/huggingface/transformers/issues/48202) | closed;  | 0.025694 | UNJUDGED |
| C_raw | bm25 | 1 | [[serge] integration failure triage - 2026-08-22](https://github.com/huggingface/transformers/issues/48222) | closed;  | 14.135213 | UNJUDGED |
| C_raw | bm25 | 2 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache](https://github.com/huggingface/transformers/issues/48693) | open; bug | 13.775892 | UNJUDGED |
| C_raw | bm25 | 3 | [Several slow tokenizers read all_special_tokens or all_special_ids once per token in decode loops](https://github.com/huggingface/transformers/issues/47424) | closed;  | 13.217502 | UNJUDGED |
| C_raw | bm25 | 4 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution](https://github.com/huggingface/transformers/issues/48459) | closed; bug | 12.148652 | UNJUDGED |
| C_raw | bm25 | 5 | [[serge] integration failure triage - 2026-08-21](https://github.com/huggingface/transformers/issues/48202) | closed;  | 11.906290 | UNJUDGED |
| C_raw | semantic | 1 | [[serge] integration failure triage - 2026-09-29](https://github.com/huggingface/transformers/issues/49175) | closed;  | 0.870345 | UNJUDGED |
| C_raw | semantic | 2 | [GenerationConfig should validate that pad_token_id is not in eos_token_id list](https://github.com/huggingface/transformers/issues/48016) | closed;  | 0.867767 | UNJUDGED |
| C_raw | semantic | 3 | [[serge] integration failure triage - 2026-08-31](https://github.com/huggingface/transformers/issues/48423) | closed;  | 0.866371 | UNJUDGED |
| C_raw | semantic | 4 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | closed;  | 0.866227 | UNJUDGED |
| C_raw | semantic | 5 | [[serge] integration failure triage - 2026-09-21](https://github.com/huggingface/transformers/issues/49000) | closed;  | 0.865032 | UNJUDGED |
| C_bug | hybrid | 1 | [Major Bug in parallel generation / left padding.](https://github.com/huggingface/transformers/issues/47651) | closed; bug | 0.031545 | UNJUDGED |
| C_bug | hybrid | 2 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 0.030579 | UNJUDGED |
| C_bug | hybrid | 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.029710 | UNJUDGED |
| C_bug | hybrid | 4 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution](https://github.com/huggingface/transformers/issues/48459) | closed; bug | 0.029462 | UNJUDGED |
| C_bug | hybrid | 5 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache](https://github.com/huggingface/transformers/issues/48693) | open; bug | 0.029380 | UNJUDGED |
| C_bug | bm25 | 1 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache](https://github.com/huggingface/transformers/issues/48693) | open; bug | 13.244871 | UNJUDGED |
| C_bug | bm25 | 2 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution](https://github.com/huggingface/transformers/issues/48459) | closed; bug | 10.777045 | UNJUDGED |
| C_bug | bm25 | 3 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor`](https://github.com/huggingface/transformers/issues/48630) | closed; bug | 9.678648 | UNJUDGED |
| C_bug | bm25 | 4 | [Incompatible with kernels 0.16](https://github.com/huggingface/transformers/issues/47312) | closed; bug | 7.905911 | UNJUDGED |
| C_bug | bm25 | 5 | [Transformers 5.13 CPU memory growth loading Qwen3-235B-A22B with DeepSpeed ZeRO-3; 4.51.0 remains bo](https://github.com/huggingface/transformers/issues/47514) | closed; bug | 7.656581 | UNJUDGED |
| C_bug | semantic | 1 | [Major Bug in parallel generation / left padding.](https://github.com/huggingface/transformers/issues/47651) | closed; bug | 0.859584 | UNJUDGED |
| C_bug | semantic | 2 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0)](https://github.com/huggingface/transformers/issues/48057) | closed; bug | 0.859529 | UNJUDGED |
| C_bug | semantic | 3 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3](https://github.com/huggingface/transformers/issues/49066) | closed; bug | 0.857486 | UNJUDGED |
| C_bug | semantic | 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | open; bug | 0.855535 | UNJUDGED |
| C_bug | semantic | 5 | [CSM codebook embedding tying is ignored when `tie_word_embeddings=False`](https://github.com/huggingface/transformers/issues/49196) | open; bug | 0.855466 | UNJUDGED |
