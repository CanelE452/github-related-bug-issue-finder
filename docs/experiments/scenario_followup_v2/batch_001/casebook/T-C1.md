# T-C1 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#48501](https://github.com/huggingface/transformers/issues/48501)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Gemma4에서 generate를 실행하면 예외가 발생합니다.</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `3` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.86901540 | UNJUDGED | unreviewed [] |

| 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings) · #47981](https://github.com/huggingface/transformers/issues/47981) | cosine_similarity / 0.86452591 | UNJUDGED | unreviewed [] |

| 3 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.86009771 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-29 · #49175](https://github.com/huggingface/transformers/issues/49175) | cosine_similarity / 0.85593385 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.85450888 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `no_lexical_match` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `3` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 2 | [CI single GPU regressions: 08/13 vs 08/14 diff (42 findings) · #47981](https://github.com/huggingface/transformers/issues/47981) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-29 · #49175](https://github.com/huggingface/transformers/issues/49175) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.86901540 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.86009771 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.85450888 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | cosine_similarity / 0.85326684 | UNJUDGED | unreviewed [] |

| 5 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.85293770 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `no_lexical_match` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 2 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Gemma4 generate에서 cache_implementation=&quot;static&quot;과 prefill_chunk_size=2를 함께 사용하면 예외가 납니다. sliding_attention과 full_attention 층이 섞여 있고 층마다 head_dim이 다르게 설정된 모델입니다. CPU에서도 재현됩니다.

[ERROR]
AmbiguousGlobalPerLayerAttributeError: &#x27;head_dim&#x27; is a per-layer attribute and may vary across layers.

[ENVIRONMENT]
Transformers 5.16.0.dev0; Linux; Python 3.12; torch 2.9.0</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.95155513 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | cosine_similarity / 0.91346055 | UNJUDGED | unreviewed [] |

| 3 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mappings · #47534](https://github.com/huggingface/transformers/issues/47534) | cosine_similarity / 0.90415382 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8) · #48305](https://github.com/huggingface/transformers/issues/48305) | cosine_similarity / 0.89800370 | UNJUDGED | unreviewed [] |

| 5 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.89730644 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys · #48392](https://github.com/huggingface/transformers/issues/48392) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 4 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mappings · #47534](https://github.com/huggingface/transformers/issues/47534) | rrf / 0.03036577 | UNJUDGED | unreviewed [] |

| 5 | [[BUG] Odd head_dim is accepted but RoPE crashes during forward · #48101](https://github.com/huggingface/transformers/issues/48101) | rrf / 0.03007689 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | bm25 / 150.79829779 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 86.04704225 | UNJUDGED | unreviewed [] |

| 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys · #48392](https://github.com/huggingface/transformers/issues/48392) | bm25 / 52.64898763 | UNJUDGED | unreviewed [] |

| 4 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field · #48241](https://github.com/huggingface/transformers/issues/48241) | bm25 / 48.11427719 | UNJUDGED | unreviewed [] |

| 5 | [Add Kimi Linear (Kimi Delta Attention) native support · #47875](https://github.com/huggingface/transformers/issues/47875) | bm25 / 47.26453115 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.95155513 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | cosine_similarity / 0.91346055 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.89730644 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.89084196 | UNJUDGED | unreviewed [] |

| 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | cosine_similarity / 0.89002049 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix from #35154 was never propagated to `nemotron_h` · #47246](https://github.com/huggingface/transformers/issues/47246) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | rrf / 0.02861201 | UNJUDGED | unreviewed [] |

| 5 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache · #48693](https://github.com/huggingface/transformers/issues/48693) | rrf / 0.02830941 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | bm25 / 141.03398992 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 82.39610404 | UNJUDGED | unreviewed [] |

| 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix from #35154 was never propagated to `nemotron_h` · #47246](https://github.com/huggingface/transformers/issues/47246) | bm25 / 30.46279267 | UNJUDGED | unreviewed [] |

| 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | bm25 / 29.12831103 | UNJUDGED | unreviewed [] |

| 5 | [`use_gqa_in_sdpa` doesn&#x27;t check GPU architecture: up to 28% slower decode on pre-sm80 GPUs · #48633](https://github.com/huggingface/transformers/issues/48633) | bm25 / 28.68637189 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Gemma4 generate raises when cache_implementation=&quot;static&quot; is combined with prefill_chunk_size=2. The model mixes sliding_attention and full_attention layers with different head_dim settings per layer. It also reproduces on CPU.

[ERROR]
AmbiguousGlobalPerLayerAttributeError: &#x27;head_dim&#x27; is a per-layer attribute and may vary across layers.

[ENVIRONMENT]
Transformers 5.16.0.dev0; Linux; Python 3.12; torch 2.9.0</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.96600759 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | cosine_similarity / 0.93061095 | UNJUDGED | unreviewed [] |

| 3 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mappings · #47534](https://github.com/huggingface/transformers/issues/47534) | cosine_similarity / 0.91289330 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8) · #48305](https://github.com/huggingface/transformers/issues/48305) | cosine_similarity / 0.90739942 | UNJUDGED | unreviewed [] |

| 5 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys · #48392](https://github.com/huggingface/transformers/issues/48392) | cosine_similarity / 0.90494215 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys · #48392](https://github.com/huggingface/transformers/issues/48392) | rrf / 0.03125763 | UNJUDGED | unreviewed [] |

| 4 | [`KeyError: &#x27;mlp&#x27;` when building a cache for Nemotron-H — `&quot;mlp&quot;` missing from the layer-type mappings · #47534](https://github.com/huggingface/transformers/issues/47534) | rrf / 0.02995752 | UNJUDGED | unreviewed [] |

| 5 | [Continuous batching does not support hybrid linear-attention models (all Qwen3.5/3.6/3.8) · #48305](https://github.com/huggingface/transformers/issues/48305) | rrf / 0.02895833 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | bm25 / 197.64733144 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 124.69980207 | UNJUDGED | unreviewed [] |

| 3 | [Nested per-layer `rope_parameters` is misparsed when `layer_types` omits one of its keys · #48392](https://github.com/huggingface/transformers/issues/48392) | bm25 / 79.45365056 | UNJUDGED | unreviewed [] |

| 4 | [Add Kimi Linear (Kimi Delta Attention) native support · #47875](https://github.com/huggingface/transformers/issues/47875) | bm25 / 67.24883610 | UNJUDGED | unreviewed [] |

| 5 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field · #48241](https://github.com/huggingface/transformers/issues/48241) | bm25 / 66.54864355 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | cosine_similarity / 0.96600759 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | cosine_similarity / 0.93061095 | UNJUDGED | unreviewed [] |

| 3 | [Gemma 4 assistant uses first-token hidden state after prefill · #48703](https://github.com/huggingface/transformers/issues/48703) | cosine_similarity / 0.90493304 | UNJUDGED | unreviewed [] |

| 4 | [Gemma 1 checkpoints silently use exact GELU instead of gelu_pytorch_tanh since v4.48.0 (#35235 removed the hidden_activation guard) · #49051](https://github.com/huggingface/transformers/issues/49051) | cosine_similarity / 0.90236932 | UNJUDGED | unreviewed [] |

| 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | cosine_similarity / 0.89911819 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix from #35154 was never propagated to `nemotron_h` · #47246](https://github.com/huggingface/transformers/issues/47246) | rrf / 0.03053613 | UNJUDGED | unreviewed [] |

| 4 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | rrf / 0.02920635 | UNJUDGED | unreviewed [] |

| 5 | [[BLT, Byte-Latent Transformer] Entropy patcher is missing BLT&#x27;s 512-token sliding-window attention — patch rate collapses on inputs longer than 512 bytes · #49185](https://github.com/huggingface/transformers/issues/49185) | rrf / 0.02862400 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Exception raised for Gemma4 with static cache and chunked prefill · #48501](https://github.com/huggingface/transformers/issues/48501) | bm25 / 187.73469423 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 122.20633559 | UNJUDGED | unreviewed [] |

| 3 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | bm25 / 46.18939200 | UNJUDGED | unreviewed [] |

| 4 | [`use_gqa_in_sdpa` doesn&#x27;t check GPU architecture: up to 28% slower decode on pre-sm80 GPUs · #48633](https://github.com/huggingface/transformers/issues/48633) | bm25 / 46.09442603 | UNJUDGED | unreviewed [] |

| 5 | [Incorrect inter-chunk recurrence in `NemotronHMamba2Mixer.torch_forward` (slow path). the Mamba2 fix from #35154 was never propagated to `nemotron_h` · #47246](https://github.com/huggingface/transformers/issues/47246) | bm25 / 41.66239232 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
