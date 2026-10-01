# T-E1 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#47879](https://github.com/huggingface/transformers/issues/47879)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Gemma4로 영상을 처리하면 실행 중 속성 오류가 나서 중단됩니다.</pre>

### C_raw · bm25

실행 상태: `no_lexical_match` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.85183996 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.84989136 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.84871560 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-07-13 · #47309](https://github.com/huggingface/transformers/issues/47309) | cosine_similarity / 0.84818637 | UNJUDGED | unreviewed [] |

| 5 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314) · #48736](https://github.com/huggingface/transformers/issues/48736) | cosine_similarity / 0.84721261 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-07-13 · #47309](https://github.com/huggingface/transformers/issues/47309) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314) · #48736](https://github.com/huggingface/transformers/issues/48736) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `no_lexical_match` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.85183996 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.84989136 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.84871560 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.84257638 | UNJUDGED | unreviewed [] |

| 5 | [Nemotron3Diarization streaming: the last chunk drops the final valid frame when len(audio) % 160 &lt; 96 · #49113](https://github.com/huggingface/transformers/issues/49113) | cosine_similarity / 0.83913696 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [Nemotron3Diarization streaming: the last chunk drops the final valid frame when len(audio) % 160 &lt; 96 · #49113](https://github.com/huggingface/transformers/issues/49113) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Gemma4-E2B-IT의 영상 처리 중 forward에서 속성 오류로 중단됩니다.

[ERROR]
AttributeError: &#x27;tuple&#x27; object has no attribute &#x27;to&#x27;

[ENVIRONMENT]
Transformers 5.15.0.dev0; WSL2 Linux; Python 3.13.14; PyTorch 2.13.0+cu132; NVIDIA RTX 4080 Laptop</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.91725528 | UNJUDGED | unreviewed [] |

| 2 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.89219809 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-09-15 · #48837](https://github.com/huggingface/transformers/issues/48837) | cosine_similarity / 0.88801706 | UNJUDGED | unreviewed [] |

| 4 | [Follow-up: clean up video_duration handling in hyperclovax_vision_v2 (#44314) · #48736](https://github.com/huggingface/transformers/issues/48736) | cosine_similarity / 0.88754594 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-24 · #48263](https://github.com/huggingface/transformers/issues/48263) | cosine_similarity / 0.88700771 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.03105441 | UNJUDGED | unreviewed [] |

| 3 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | rrf / 0.02964427 | UNJUDGED | unreviewed [] |

| 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | rrf / 0.02591362 | UNJUDGED | unreviewed [] |

| 5 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27; when torchvision is missing · #48556](https://github.com/huggingface/transformers/issues/48556) | rrf / 0.02355876 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | bm25 / 104.23115469 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | bm25 / 28.31579290 | UNJUDGED | unreviewed [] |

| 3 | [Issue doing PEFT on Embedding Gemma w/ new classifier head · #48964](https://github.com/huggingface/transformers/issues/48964) | bm25 / 26.30110426 | UNJUDGED | unreviewed [] |

| 4 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 26.16757138 | UNJUDGED | unreviewed [] |

| 5 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | bm25 / 26.10642871 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.91725528 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.88634789 | UNJUDGED | unreviewed [] |

| 3 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | cosine_similarity / 0.88616621 | UNJUDGED | unreviewed [] |

| 4 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | cosine_similarity / 0.88579553 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.88145405 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | rrf / 0.02923602 | UNJUDGED | unreviewed [] |

| 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | rrf / 0.02913851 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | bm25 / 82.78373019 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | bm25 / 20.09748005 | UNJUDGED | unreviewed [] |

| 3 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 20.04972752 | UNJUDGED | unreviewed [] |

| 4 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | bm25 / 19.99991894 | UNJUDGED | unreviewed [] |

| 5 | [Issue doing PEFT on Embedding Gemma w/ new classifier head · #48964](https://github.com/huggingface/transformers/issues/48964) | bm25 / 19.02107151 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Video processing with Gemma4-E2B-IT stops with an attribute error during forward.

[ERROR]
AttributeError: &#x27;tuple&#x27; object has no attribute &#x27;to&#x27;

[ENVIRONMENT]
Transformers 5.15.0.dev0; WSL2 Linux; Python 3.13.14; PyTorch 2.13.0+cu132; NVIDIA RTX 4080 Laptop</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | bm25 / 129.38752685 | UNJUDGED | unreviewed [] |

| 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27; when torchvision is missing · #48556](https://github.com/huggingface/transformers/issues/48556) | bm25 / 38.33676227 | UNJUDGED | unreviewed [] |

| 3 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | bm25 / 33.04995337 | UNJUDGED | unreviewed [] |

| 4 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 32.73866463 | UNJUDGED | unreviewed [] |

| 5 | [Issue doing PEFT on Embedding Gemma w/ new classifier head · #48964](https://github.com/huggingface/transformers/issues/48964) | bm25 / 31.87762727 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.92389166 | UNJUDGED | unreviewed [] |

| 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27; when torchvision is missing · #48556](https://github.com/huggingface/transformers/issues/48556) | cosine_similarity / 0.90361297 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.90269637 | UNJUDGED | unreviewed [] |

| 4 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors · #49007](https://github.com/huggingface/transformers/issues/49007) | cosine_similarity / 0.89714891 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.89522564 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27; when torchvision is missing · #48556](https://github.com/huggingface/transformers/issues/48556) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.03030999 | UNJUDGED | unreviewed [] |

| 4 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors · #49007](https://github.com/huggingface/transformers/issues/49007) | rrf / 0.02932363 | UNJUDGED | unreviewed [] |

| 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | rrf / 0.02752640 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | bm25 / 105.53767958 | UNJUDGED | unreviewed [] |

| 2 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | bm25 / 26.79881719 | UNJUDGED | unreviewed [] |

| 3 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 25.73262519 | UNJUDGED | unreviewed [] |

| 4 | [Issue doing PEFT on Embedding Gemma w/ new classifier head · #48964](https://github.com/huggingface/transformers/issues/48964) | bm25 / 23.68401116 | UNJUDGED | unreviewed [] |

| 5 | [Loading `RTDetrModel` from a detection checkpoint (or `SEWDForCTC` from a SEW-D checkpoint) gives a model with every weight randomly initialized · #48722](https://github.com/huggingface/transformers/issues/48722) | bm25 / 21.55956640 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | cosine_similarity / 0.92389166 | UNJUDGED | unreviewed [] |

| 2 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.90269637 | UNJUDGED | unreviewed [] |

| 3 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors · #49007](https://github.com/huggingface/transformers/issues/49007) | cosine_similarity / 0.89714891 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.89522564 | UNJUDGED | unreviewed [] |

| 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | cosine_similarity / 0.89337456 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Error during video handling with Gemma4 (E2B-Instruct) · #47879](https://github.com/huggingface/transformers/issues/47879) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [[BUG] Passing only min_pixels or only max_pixels raises ValueError in image and video processors · #49007](https://github.com/huggingface/transformers/issues/49007) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.03055037 | UNJUDGED | unreviewed [] |

| 4 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | rrf / 0.03041475 | UNJUDGED | unreviewed [] |

| 5 | [AutoImageProcessor and the *ImageProcessorPil classes require torchvision from a docstring mention · #48607](https://github.com/huggingface/transformers/issues/48607) | rrf / 0.02927350 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
