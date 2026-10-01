# T-S1 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#47752](https://github.com/huggingface/transformers/issues/47752)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
모델에서 설정한 생성 길이가 text-generation 파이프라인에 반영되지 않습니다.</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03154496 | UNJUDGED | unreviewed [] |

| 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings) · #47981](https://github.com/huggingface/transformers/issues/47981) | rrf / 0.03100962 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-23 · #48240](https://github.com/huggingface/transformers/issues/48240) | rrf / 0.03083491 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-08-24 · #48263](https://github.com/huggingface/transformers/issues/48263) | rrf / 0.02943723 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-25 · #48321](https://github.com/huggingface/transformers/issues/48321) | rrf / 0.02632035 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `6` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | cosine_similarity / 0.86699599 | UNJUDGED | unreviewed [] |

| 2 | [[serge] integration failure triage - 2026-08-23 · #48240](https://github.com/huggingface/transformers/issues/48240) | cosine_similarity / 0.86266065 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-09-22 · #49026](https://github.com/huggingface/transformers/issues/49026) | cosine_similarity / 0.85912204 | UNJUDGED | unreviewed [] |

| 4 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings) · #47981](https://github.com/huggingface/transformers/issues/47981) | cosine_similarity / 0.85907674 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.85814059 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 12.64233033 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching crashes on every VLM: config attributes read from the top-level config · #48298](https://github.com/huggingface/transformers/issues/48298) | bm25 / 5.04574981 | UNJUDGED | unreviewed [] |

| 3 | [Add native support for OpenBMB VoxCPM2 · #47695](https://github.com/huggingface/transformers/issues/47695) | bm25 / 4.71435358 | UNJUDGED | unreviewed [] |

| 4 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | bm25 / 4.35985727 | UNJUDGED | unreviewed [] |

| 5 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings) · #47981](https://github.com/huggingface/transformers/issues/47981) | bm25 / 4.26835991 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.02970951 | UNJUDGED | unreviewed [] |

| 3 | [MusicGen: forward(labels=...) raises &quot;set the decoder_start_token_id&quot; on every released checkpoint, while generate() and prepare_decoder_input_ids_from_labels() find the token fine · #49095](https://github.com/huggingface/transformers/issues/49095) | rrf / 0.02943723 | UNJUDGED | unreviewed [] |

| 4 | [gemma 4 can not load audio file and produce  Audio features and audio tokens do not match, tokens: 31, features: 468480 · #48887](https://github.com/huggingface/transformers/issues/48887) | rrf / 0.02938653 | UNJUDGED | unreviewed [] |

| 5 | [## Flaky test: `IndexError` — bbox coordinate values out of 0-1000 range · #47337](https://github.com/huggingface/transformers/issues/47337) | rrf / 0.02859477 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | cosine_similarity / 0.85807592 | UNJUDGED | unreviewed [] |

| 2 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot; · #47553](https://github.com/huggingface/transformers/issues/47553) | cosine_similarity / 0.85788721 | UNJUDGED | unreviewed [] |

| 3 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model. · #48400](https://github.com/huggingface/transformers/issues/48400) | cosine_similarity / 0.85488582 | UNJUDGED | unreviewed [] |

| 4 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.85468149 | UNJUDGED | unreviewed [] |

| 5 | [AMD quark class not updated · #47321](https://github.com/huggingface/transformers/issues/47321) | cosine_similarity / 0.85005397 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 11.58536841 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | bm25 / 4.74374771 | UNJUDGED | unreviewed [] |

| 3 | [gemma 4 can not load audio file and produce  Audio features and audio tokens do not match, tokens: 31, features: 468480 · #48887](https://github.com/huggingface/transformers/issues/48887) | bm25 / 4.69161455 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 4.31573815 | UNJUDGED | unreviewed [] |

| 5 | [Special tokens aren&#x27;t escaped in template generation · #47822](https://github.com/huggingface/transformers/issues/47822) | bm25 / 4.18164536 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Phi-3 모델의 generation_config에서 max_new_tokens를 500으로 설정하고 do_sample=False로 둔 뒤 모델과 토크나이저를 text-generation pipeline에 넘깁니다. pipeline의 generation_config.max_new_tokens가 500이 아니며 모델 설정이 유지되기를 기대합니다.

[ENVIRONMENT]
microsoft/Phi-3-mini-4k-instruct; Transformers 5.14.1; macOS ARM; Python 3.12.13; PyTorch 2.13.0</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | rrf / 0.03076923 | UNJUDGED | unreviewed [] |

| 5 | [Mamba2-family `cuda_kernels_forward` decode step is broken since #47452: missing seq-dim squeeze · #47532](https://github.com/huggingface/transformers/issues/47532) | rrf / 0.02903091 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 114.98336963 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | bm25 / 60.41018050 | UNJUDGED | unreviewed [] |

| 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | bm25 / 49.72956710 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-08-15 · #47993](https://github.com/huggingface/transformers/issues/47993) | bm25 / 41.43517163 | UNJUDGED | unreviewed [] |

| 5 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | bm25 / 40.08218089 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | cosine_similarity / 0.91515160 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.89432323 | UNJUDGED | unreviewed [] |

| 3 | [Mamba2-family `cuda_kernels_forward` decode step is broken since #47452: missing seq-dim squeeze · #47532](https://github.com/huggingface/transformers/issues/47532) | cosine_similarity / 0.88971722 | UNJUDGED | unreviewed [] |

| 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | cosine_similarity / 0.88943189 | UNJUDGED | unreviewed [] |

| 5 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | cosine_similarity / 0.88749874 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | rrf / 0.03057890 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | rrf / 0.02995752 | UNJUDGED | unreviewed [] |

| 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | rrf / 0.02927350 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 96.40119914 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | bm25 / 51.23994240 | UNJUDGED | unreviewed [] |

| 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 30.72340119 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | bm25 / 29.25680303 | UNJUDGED | unreviewed [] |

| 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | bm25 / 26.94755816 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | cosine_similarity / 0.91515160 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.89432323 | UNJUDGED | unreviewed [] |

| 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | cosine_similarity / 0.88532531 | UNJUDGED | unreviewed [] |

| 4 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to full context skipped) · #49093](https://github.com/huggingface/transformers/issues/49093) | cosine_similarity / 0.88184714 | UNJUDGED | unreviewed [] |

| 5 | [Incorrect model predictions (because of incorrect tokenization output) after the 5.0 update · #48967](https://github.com/huggingface/transformers/issues/48967) | cosine_similarity / 0.88063943 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
I set max_new_tokens=500 and do_sample=False in a Phi-3 model generation_config, then pass the model and tokenizer to a text-generation pipeline. The pipeline generation_config.max_new_tokens is not 500; I expect it to preserve the model setting.

[ENVIRONMENT]
microsoft/Phi-3-mini-4k-instruct; Transformers 5.14.1; macOS ARM; Python 3.12.13; PyTorch 2.13.0</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | cosine_similarity / 0.92304540 | UNJUDGED | unreviewed [] |

| 2 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | cosine_similarity / 0.91158921 | UNJUDGED | unreviewed [] |

| 3 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.90923256 | UNJUDGED | unreviewed [] |

| 4 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to full context skipped) · #49093](https://github.com/huggingface/transformers/issues/49093) | cosine_similarity / 0.90676713 | UNJUDGED | unreviewed [] |

| 5 | [Version-gated tokenizer file selection (fast_tokenizer_files) hands different vocabularies to different consumers of the same repo · #48836](https://github.com/huggingface/transformers/issues/48836) | cosine_similarity / 0.90451968 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 167.42523410 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | bm25 / 73.72619039 | UNJUDGED | unreviewed [] |

| 3 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | bm25 / 70.24102914 | UNJUDGED | unreviewed [] |

| 4 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | bm25 / 63.05815091 | UNJUDGED | unreviewed [] |

| 5 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 58.03423745 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [Assisted/speculative decoding ignores `stop_strings` completed mid-block, and raises with `assistant_model` · #48039](https://github.com/huggingface/transformers/issues/48039) | rrf / 0.03175403 | UNJUDGED | unreviewed [] |

| 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | rrf / 0.03015873 | UNJUDGED | unreviewed [] |

| 5 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | rrf / 0.02963126 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | cosine_similarity / 0.92304540 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.90923256 | UNJUDGED | unreviewed [] |

| 3 | [`SequenceBiasLogitsProcessor`: two edge cases (token id 0 rejected in list format; prefix equal to full context skipped) · #49093](https://github.com/huggingface/transformers/issues/49093) | cosine_similarity / 0.90676713 | UNJUDGED | unreviewed [] |

| 4 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | cosine_similarity / 0.90302491 | UNJUDGED | unreviewed [] |

| 5 | [Incorrect model predictions (because of incorrect tokenization output) after the 5.0 update · #48967](https://github.com/huggingface/transformers/issues/48967) | cosine_similarity / 0.90246165 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | bm25 / 142.86040273 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | bm25 / 64.42742254 | UNJUDGED | unreviewed [] |

| 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 50.88425057 | UNJUDGED | unreviewed [] |

| 4 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | bm25 / 44.91657213 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | bm25 / 42.93237958 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [incorrect precedence of generation_config values · #47752](https://github.com/huggingface/transformers/issues/47752) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [`DogeForCausalLM` attends to future tokens with the default `sdpa` backend — `SmallDoge/Doge-20M` scores ppl 5 instead of 16, and cached and uncached `generate()` disagree · #48748](https://github.com/huggingface/transformers/issues/48748) | rrf / 0.03125000 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | rrf / 0.02792121 | UNJUDGED | unreviewed [] |

| 5 | [ESMFold throws error when explicitly cast to fp16 · #47470](https://github.com/huggingface/transformers/issues/47470) | rrf / 0.02782609 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
