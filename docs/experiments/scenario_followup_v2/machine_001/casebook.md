# AI 예비 검토 사례집

사람 판정이 아닙니다. 고정된 3개 개발 사례의 B 질의와 공통 후보만 검토했습니다.

## O-E1
```text
[PROBLEM]
CMake로 OpenCV 빌드 파일을 만든 뒤 mingw32-make로 컴파일하면 두 곳에서 같은 선언 누락 오류로 빌드가 멈춥니다. 추가 빌드 설정은 하지 않았습니다.

[ERROR]
error: 'posix_memalign' was not declared in this scope

[ENVIRONMENT]
OpenCV 5.0.0, Windows 11, MinGW GCC 16.1.0
```

### C_raw / bm25
AI Hit@5=1; AI pooled nDCG@5=0.921824; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
| 3 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing <cstdint> in ADE)](https://github.com/opencv/opencv/issues/29564) | 1 |
| 4 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | 1 |
| 5 | [solvePnPRefineLM/VVS: out-of-bounds read, silent no-op, and exception when rvec/tvec are row vectors (Size(3,1))](https://github.com/opencv/opencv/issues/29747) | 0 |
### C_raw / semantic
AI Hit@5=1; AI pooled nDCG@5=0.811926; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | 1 |
| 3 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | 0 |
| 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | 0 |
| 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
### C_raw / hybrid
AI Hit@5=1; AI pooled nDCG@5=0.834791; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
| 3 | [CMake: opencv_world with core and imgproc fails with "Unknown CMake command ocv_imgcodecs_configure_target"](https://github.com/opencv/opencv/issues/29778) | 1 |
| 4 | [allocation/write-width mismatch in AKAZE generateDescriptorSubsample when descriptor_channels < 3](https://github.com/opencv/opencv/issues/29613) | 0 |
| 5 | [oob read in Domain_Filter::compute_NCfilter when cv::stylization is given a single-column image](https://github.com/opencv/opencv/issues/29614) | 0 |
### C_bug / bm25
AI Hit@5=1; AI pooled nDCG@5=0.912968; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
| 3 | [OpenCV 4.6.0 fails to build with GCC 16.1.0 (missing <cstdint> in ADE)](https://github.com/opencv/opencv/issues/29564) | 1 |
| 4 | [solvePnPRefineLM/VVS: out-of-bounds read, silent no-op, and exception when rvec/tvec are row vectors (Size(3,1))](https://github.com/opencv/opencv/issues/29747) | 0 |
| 5 | [opencv 5.0.0 compile error in modul dnn](https://github.com/opencv/opencv/issues/29308) | 1 |
### C_bug / semantic
AI Hit@5=1; AI pooled nDCG@5=0.811926; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | 1 |
| 3 | [OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch](https://github.com/opencv/opencv/issues/28580) | 0 |
| 4 | [OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value](https://github.com/opencv/opencv/issues/28598) | 0 |
| 5 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
### C_bug / hybrid
AI Hit@5=1; AI pooled nDCG@5=0.811926; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [posix_memalign related issue emerged twice in MinGW32 compilation](https://github.com/opencv/opencv/issues/29350) | 2 |
| 2 | [opengl_testdata_generator.cpp fails to build in 5.0](https://github.com/opencv/opencv/issues/29292) | 1 |
| 3 | [allocation/write-width mismatch in AKAZE generateDescriptorSubsample when descriptor_channels < 3](https://github.com/opencv/opencv/issues/29613) | 0 |
| 4 | [oob read in Domain_Filter::compute_NCfilter when cv::stylization is given a single-column image](https://github.com/opencv/opencv/issues/29614) | 0 |
| 5 | [Build failure on Windows (MSVC) with WITH_ONNXRUNTIME=ON due to C2664 in net_impl_backend.cpp](https://github.com/opencv/opencv/issues/29278) | 1 |

### 공통 후보 전체의 AI 판정 근거
| 문서 | 등급 | 실제 인용 | 판정 이유 |
|---|---:|---|---|
| [opencv/opencv#29292](https://github.com/opencv/opencv/issues/29292) | 1 | Try to compile 5.0.0 with `BUILD_EXAMPLES=ON` | OpenCV 5 빌드·선언 누락은 유사하지만 Linux 예제의 loadMesh/열거형 오류이고 MinGW posix_memalign 오류가 아니다. |
| [opencv/opencv#29278](https://github.com/opencv/opencv/issues/29278) | 1 | opts.EnableProfiling(ort_profile_path_prefix.c_str()); | Windows OpenCV 5 빌드 문제지만 MSVC·ONNX wchar_t 변환 오류로 원인과 컴파일러가 다르다. |
| [opencv/opencv#29747](https://github.com/opencv/opencv/issues/29747) | 0 | solvePnPRefineLM/VVS: out-of-bounds read | posix_memalign은 실행 중 ASan 할당 스택에 나오며 실제 문제는 PnP 행벡터 접근이다. 컴파일 선언 누락과 다르다. |
| [opencv/opencv#29614](https://github.com/opencv/opencv/issues/29614) | 0 | oob read in Domain_Filter::compute_NCfilter | 사진 stylization 실행 중 단일 열 이미지 범위 밖 읽기이다. 빌드 실패 문제와 다르다. |
| [opencv/opencv#29308](https://github.com/opencv/opencv/issues/29308) | 1 | cannot convert 'const char*' to 'const wchar_t*' | Windows GCC·mingw32-make 빌드까지 유사하지만 DNN ONNX 문자열 타입 변환 문제여서 직접 근거가 아니다. |
| [opencv/opencv#29350](https://github.com/opencv/opencv/issues/29350) | 2 | error: 'posix_memalign' was not declared in this scope | OpenCV 5·Windows 11·MinGW GCC 16.1.0과 두 곳의 같은 선언 누락 오류가 모두 일치한다. 해결됐다는 주장은 하지 않는다. |
| [opencv/opencv#28580](https://github.com/opencv/opencv/issues/28580) | 0 | OpenCV UBSan Bug: countNonZero32f Function Pointer Type Mismatch | countNonZero 실행 중 함수 포인터 타입 불일치이며 MinGW 컴파일 선언 문제와 다르다. |
| [opencv/opencv#29778](https://github.com/opencv/opencv/issues/29778) | 1 | Unknown CMake command "ocv_imgcodecs_configure_target". | OpenCV 5 CMake 빌드는 관련되지만 최소 world 구성 단계에서 중단되어 이미 생성된 파일의 MinGW 컴파일 실패와 다르다. |
| [opencv/opencv#29564](https://github.com/opencv/opencv/issues/29564) | 1 | error: 'uintptr_t' in namespace 'std' does not name a type | Windows GCC 16 빌드·헤더 누락은 유사하지만 OpenCV 4.6 ADE uintptr_t 오류이다. posix_memalign의 근거가 아니다. |
| [opencv/opencv#28598](https://github.com/opencv/opencv/issues/28598) | 0 | OpenCV UBSan Bug: FillConvexPoly Left Shift of Negative Value | 그리기 함수 실행 중 음수 시프트 문제이며 검색 질의의 빌드 오류와 다르다. |
| [opencv/opencv#29613](https://github.com/opencv/opencv/issues/29613) | 0 | allocation/write-width mismatch in AKAZE generateDescriptorSubsample | AKAZE 실행 중 채널 수와 할당 크기 불일치이다. 컴파일 posix_memalign 선언 문제와 다르다. |

## T-E1
```text
[PROBLEM]
Gemma4-E2B-IT의 영상 처리 중 forward에서 속성 오류로 중단됩니다.

[ERROR]
AttributeError: 'tuple' object has no attribute 'to'

[ENVIRONMENT]
Transformers 5.15.0.dev0; WSL2 Linux; Python 3.13.14; PyTorch 2.13.0+cu132; NVIDIA RTX 4080 Laptop
```

### C_raw / bm25
AI Hit@5=1; AI pooled nDCG@5=0.606249; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | 0 |
| 3 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | 0 |
| 4 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | 0 |
| 5 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 0 |
### C_raw / semantic
AI Hit@5=1; AI pooled nDCG@5=0.693282; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | 0 |
| 3 | [[serge] integration failure triage - 2026-09-15](https://github.com/huggingface/transformers/issues/48837) | 0 |
| 4 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314)](https://github.com/huggingface/transformers/issues/48736) | 1 |
| 5 | [[serge] integration failure triage - 2026-08-24](https://github.com/huggingface/transformers/issues/48263) | 0 |
### C_raw / hybrid
AI Hit@5=1; AI pooled nDCG@5=0.872500; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | 0 |
| 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | 1 |
| 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | 1 |
| 5 | [AutoProcessor.from_pretrained raises AttributeError: 'NoneType' object has no attribute '__module__' when torchvision is missing](https://github.com/huggingface/transformers/issues/48556) | 1 |
### C_bug / bm25
AI Hit@5=1; AI pooled nDCG@5=0.693282; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | 0 |
| 3 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache)](https://github.com/huggingface/transformers/issues/48479) | 0 |
| 4 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | 1 |
| 5 | [Issue doing PEFT on Embedding Gemma w/ new classifier head](https://github.com/huggingface/transformers/issues/48964) | 0 |
### C_bug / semantic
AI Hit@5=1; AI pooled nDCG@5=0.794323; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | 0 |
| 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | 1 |
| 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | 1 |
| 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard)](https://github.com/huggingface/transformers/issues/49051) | 0 |
### C_bug / hybrid
AI Hit@5=1; AI pooled nDCG@5=0.785467; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Error during video handling with Gemma4 (E2B-Instruct)](https://github.com/huggingface/transformers/issues/47879) | 2 |
| 2 | [Gemma 4 assistant uses first-token hidden state after prefill](https://github.com/huggingface/transformers/issues/48703) | 0 |
| 3 | [gemma4 12B arch is not recognized!](https://github.com/huggingface/transformers/issues/47448) | 1 |
| 4 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 0 |
| 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention](https://github.com/huggingface/transformers/issues/48607) | 1 |

### 공통 후보 전체의 AI 판정 근거
| 문서 | 등급 | 실제 인용 | 판정 이유 |
|---|---:|---|---|
| [huggingface/transformers#48479](https://github.com/huggingface/transformers/issues/48479) | 0 | AttributeError: 'DynamicCache' object has no attribute 'key_cache' | KV cache API 삭제와 마이그레이션 문서 문제이다. tuple.to 영상 forward 오류와 객체·기능이 다르다. |
| [huggingface/transformers#48422](https://github.com/huggingface/transformers/issues/48422) | 0 | [serge] integration failure triage - 2026-08-30 | 여러 모델의 CI 실패 묶음이며 본문에 Gemma4 영상 tuple.to 오류의 직접 재현이 없다. |
| [huggingface/transformers#47448](https://github.com/huggingface/transformers/issues/47448) | 1 | KeyError: 'gemma4_unified' | Gemma4 멀티모달 지원·버전 확인에는 참고할 수 있지만 12B 모델 로드 단계의 아키텍처 미지원으로 E2B 영상 forward 오류와 다르다. |
| [huggingface/transformers#48703](https://github.com/huggingface/transformers/issues/48703) | 0 | Gemma 4 assistant uses first-token hidden state after prefill | Gemma4 계열이 같아도 assistant 생성의 hidden-state 선택 문제이다. 영상 tuple.to 예외와 경로·증상이 다르다. |
| [huggingface/transformers#48805](https://github.com/huggingface/transformers/issues/48805) | 0 | Only on saving a checkpoint are weight conversions used | Trainer 체크포인트 저장·로드 가중치 이름 문제이다. 영상 추론과 관련 없는 학습 저장 경로이다. |
| [huggingface/transformers#48837](https://github.com/huggingface/transformers/issues/48837) | 0 | [serge] integration failure triage - 2026-09-15 | 다른 모델 CI 실패와 재현되지 않은 generation 테스트를 묶은 문서로 해당 Gemma4 오류 근거가 없다. |
| [huggingface/transformers#48556](https://github.com/huggingface/transformers/issues/48556) | 1 | AttributeError: 'NoneType' object has no attribute '__module__' | 영상 processor·AttributeError는 부분 관련되지만 torchvision 누락·다른 모델 로드 단계이다. 실제 tuple.to 원인은 아니다. |
| [huggingface/transformers#48607](https://github.com/huggingface/transformers/issues/48607) | 1 | AutoImageProcessor requires the Torchvision library | 시각 입력 전처리 의존성 문제로 참고 범위만 겹친다. ImportError와 PIL backend 문제라 영상 forward tuple.to와 다르다. |
| [huggingface/transformers#48736](https://github.com/huggingface/transformers/issues/48736) | 1 | Follow-up: clean up video_duration handling in hyperclovax_vision_v2 | 영상 metadata 처리라는 하위 주제는 관련되지만 HyperCLOVAX processor와 템플릿 정리로 모델·실패 지점이 다르다. |
| [huggingface/transformers#48964](https://github.com/huggingface/transformers/issues/48964) | 0 | AttributeError: 'Gemma3TextForSequenceClassification' object has no attribute 'peft_config' | Gemma 이름·AttributeError만 겹친다. EmbeddingGemma 분류기 LoRA 어댑터 추가 오류로 영상 모델과 다르다. |
| [huggingface/transformers#48263](https://github.com/huggingface/transformers/issues/48263) | 0 | [serge] integration failure triage - 2026-08-24 | Gemma4 언급은 텍스트 export의 OOM 항목이다. 영상 tuple.to 예외를 설명하지 않는다. |
| [huggingface/transformers#47879](https://github.com/huggingface/transformers/issues/47879) | 2 | AttributeError: 'tuple' object has no attribute 'to' | Gemma4-E2B 영상 forward·동일 오류·WSL2 및 버전 조건이 일치한다. 본문은 video_features[0] 사용을 제안하지만 이 작업에서 해결 코드를 실행 검증한 것은 아니다. |
| [huggingface/transformers#49051](https://github.com/huggingface/transformers/issues/49051) | 0 | Gemma 1 checkpoints silently use exact GELU | Gemma1 활성화 함수 수치 문제이다. Gemma4 영상 tuple 객체 예외와 모델 세대·경로·증상이 다르다. |

## T-C2
```text
[PROBLEM]
Trainer 체크포인트를 다른 위치로 옮긴 뒤 재개했습니다. trainer_state.json의 best_model_checkpoint는 존재하지 않는 이전 경로를 가리킵니다. 새 best가 생기지 않았고 save_total_limit=1, load_best_model_at_end=True입니다. 학습은 끝났지만 마지막 정리에서 실패합니다.

[ERROR]
FileNotFoundError: [WinError 2] The system cannot find the file specified

[ENVIRONMENT]
Transformers 5.16.0.dev0; torch 2.11.0+cu128; Python 3.12.6; Windows 11
```

### C_raw / bm25
AI Hit@5=1; AI pooled nDCG@5=0.693282; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory](https://github.com/huggingface/transformers/issues/48315) | 2 |
| 2 | [XPU: `from_pretrained(device_map=...)` fails under WSL2 because `caching_allocator_warmup` does not guard `mem_get_info`](https://github.com/huggingface/transformers/issues/48127) | 0 |
| 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | 0 |
| 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | 1 |
| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory)](https://github.com/huggingface/transformers/issues/48285) | 0 |
### C_raw / semantic
AI Hit@5=1; AI pooled nDCG@5=0.912968; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory](https://github.com/huggingface/transformers/issues/48315) | 2 |
| 2 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 1 |
| 3 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B`](https://github.com/huggingface/transformers/issues/47333) | 1 |
| 4 | [[serge] integration failure triage - 2026-08-30](https://github.com/huggingface/transformers/issues/48422) | 0 |
| 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | 1 |
### C_raw / hybrid
AI Hit@5=1; AI pooled nDCG@5=0.912968; 직접 관련 문서 범위 포함=True
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory](https://github.com/huggingface/transformers/issues/48315) | 2 |
| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | 1 |
| 3 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 1 |
| 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it](https://github.com/huggingface/transformers/issues/48592) | 0 |
| 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | 1 |
### C_bug / bm25
AI Hit@5=0; AI pooled nDCG@5=0.202083; 직접 관련 문서 범위 포함=False
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | 1 |
| 2 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | 0 |
| 3 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory)](https://github.com/huggingface/transformers/issues/48285) | 0 |
| 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer](https://github.com/huggingface/transformers/issues/48690) | 0 |
| 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter](https://github.com/huggingface/transformers/issues/47914) | 0 |
### C_bug / semantic
AI Hit@5=0; AI pooled nDCG@5=0.517657; 직접 관련 문서 범위 포함=False
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 1 |
| 2 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B`](https://github.com/huggingface/transformers/issues/47333) | 1 |
| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | 1 |
| 4 | [[Offloading] Cannot save disk-offloaded `Qwen3-VL-32B-Instruct`](https://github.com/huggingface/transformers/issues/47332) | 1 |
| 5 | [AMD quark class not updated](https://github.com/huggingface/transformers/issues/47321) | 0 |
### C_bug / hybrid
AI Hit@5=0; AI pooled nDCG@5=0.430625; 직접 관련 문서 범위 포함=False
| 순위 | 원문 | AI 예비 등급 |
|---:|---|---:|
| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint](https://github.com/huggingface/transformers/issues/49193) | 1 |
| 2 | [Only on saving a checkpoint are weight conversions used](https://github.com/huggingface/transformers/issues/48805) | 1 |
| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes](https://github.com/huggingface/transformers/issues/49121) | 1 |
| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing](https://github.com/huggingface/transformers/issues/47254) | 0 |
| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory)](https://github.com/huggingface/transformers/issues/48285) | 0 |

### 공통 후보 전체의 AI 판정 근거
| 문서 | 등급 | 실제 인용 | 판정 이유 |
|---|---:|---|---|
| [huggingface/transformers#47321](https://github.com/huggingface/transformers/issues/47321) | 0 | AMD quark class not updated | AMD 양자화 설정의 클래스 import 경로 변경이다. Trainer 체크포인트 경로 정리와 다르다. |
| [huggingface/transformers#48127](https://github.com/huggingface/transformers/issues/48127) | 0 | XPU: `from_pretrained(device_map=...)` fails under WSL2 | XPU 메모리 조회로 초기 모델 로드가 실패한다. 완료한 Trainer 재개 실행의 디렉터리 정리 오류와 다르다. |
| [huggingface/transformers#47333](https://github.com/huggingface/transformers/issues/47333) | 1 | NotImplementedError: Cannot copy out of meta tensor; no data! | 저장된 모델 파일 관리라는 하위 주제만 관련된다. disk offload 모델 저장의 meta tensor 오류로 Trainer 종료 정리와 다르다. |
| [huggingface/transformers#47254](https://github.com/huggingface/transformers/issues/47254) | 0 | `CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing | 여기 checkpointing은 역전파 메모리 재계산이다. 디스크 체크포인트 재개·정리와 다른 기능이므로 단어 일치만으로 관련 판정하지 않는다. |
| [huggingface/transformers#48285](https://github.com/huggingface/transformers/issues/48285) | 0 | copy-on-write commit charge exhausts memory | Windows 대형 모델 초기 mmap 메모리 고갈이다. 파일이 없어진 경로를 비교하는 Trainer 종료 오류와 다르다. |
| [huggingface/transformers#48422](https://github.com/huggingface/transformers/issues/48422) | 0 | [serge] integration failure triage - 2026-08-30 | 다른 모델의 CI 자동 실패 묶음이며 Trainer best_model_checkpoint의 죽은 경로 증상 근거가 없다. |
| [huggingface/transformers#48805](https://github.com/huggingface/transformers/issues/48805) | 1 | Only on saving a checkpoint are weight conversions used | Trainer 체크포인트 재개는 동일 하위 기능이다. 가중치 이름 변환의 불일치라 best 경로·종료 정리 원인은 다르다. |
| [huggingface/transformers#48592](https://github.com/huggingface/transformers/issues/48592) | 0 | `Trainer` deletes `config.bos_token_id` | Trainer의 BOS 토큰 설정 보존 문제이다. 체크포인트 디렉터리 정리·FileNotFoundError를 설명하지 않는다. |
| [huggingface/transformers#49121](https://github.com/huggingface/transformers/issues/49121) | 1 | Trainer fails to resume from a checkpoint on CPU with two or more processes | Trainer 재개 실패라는 기능은 같지만 CPU 분산 optimizer 로드 시작 단계의 cpu:0 오류로 종료 정리와 다르다. |
| [huggingface/transformers#49193](https://github.com/huggingface/transformers/issues/49193) | 1 | Trainer reports incorrect final loss and throughput after resuming | Trainer 재개 후 finalize라는 경로는 관련된다. 평균·처리량 오계산이며 파일 경로 예외는 아니다. |
| [huggingface/transformers#47914](https://github.com/huggingface/transformers/issues/47914) | 0 | caching_allocator_warmup crashes with AttributeError | 양자화 PEFT adapter의 초기 모델 로드 문제이다. Trainer 상태 파일의 이전 best 경로와 다르다. |
| [huggingface/transformers#48690](https://github.com/huggingface/transformers/issues/48690) | 0 | router auxiliary loss is multiplied by the DDP world size | Trainer 분산 손실 스케일링 문제이다. 디스크 체크포인트의 경로 누락과 원인이 다르다. |
| [huggingface/transformers#48315](https://github.com/huggingface/transformers/issues/48315) | 2 | FileNotFoundError: [WinError 2] The system cannot find the file specified | 이동한 체크포인트·best_model_checkpoint 죽은 경로·새 best 없음·save_total_limit=1·종료 samefile 실패가 일치한다. |
| [huggingface/transformers#47332](https://github.com/huggingface/transformers/issues/47332) | 1 | NotImplementedError: Cannot copy out of meta tensor; no data! | disk offload 모델 저장은 지속 체크포인트 파일 관리에 부분 관련되지만 meta tensor 저장 문제이며 Trainer의 dead path 정리와 다르다. |
