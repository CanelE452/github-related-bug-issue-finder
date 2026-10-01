# T-E2 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#48346](https://github.com/huggingface/transformers/issues/48346)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
일반 FP8 설정으로 모델을 준비하다가 속성 오류가 납니다.</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | rrf / 0.03076923 | UNJUDGED | unreviewed [] |

| 2 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | rrf / 0.02951389 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | rrf / 0.02597403 | UNJUDGED | unreviewed [] |

| 4 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization · #48350](https://github.com/huggingface/transformers/issues/48350) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-09-15 · #48837](https://github.com/huggingface/transformers/issues/48837) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `4` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization · #48350](https://github.com/huggingface/transformers/issues/48350) | bm25 / 7.93031254 | UNJUDGED | unreviewed [] |

| 2 | [FineGrainedFP8: modules_to_not_convert never matches on text-only loads of multimodal checkpoints (silent quality corruption) · #48349](https://github.com/huggingface/transformers/issues/48349) | bm25 / 7.80455860 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | bm25 / 7.63124792 | UNJUDGED | unreviewed [] |

| 4 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | bm25 / 7.21124057 | UNJUDGED | unreviewed [] |

| 5 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | bm25 / 7.01746634 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `12` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[serge] integration failure triage - 2026-09-15 · #48837](https://github.com/huggingface/transformers/issues/48837) | cosine_similarity / 0.85802341 | UNJUDGED | unreviewed [] |

| 2 | [[serge] integration failure triage - 2026-08-23 · #48240](https://github.com/huggingface/transformers/issues/48240) | cosine_similarity / 0.85800874 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.85276598 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-10 · #48695](https://github.com/huggingface/transformers/issues/48695) | cosine_similarity / 0.85253698 | UNJUDGED | unreviewed [] |

| 5 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | cosine_similarity / 0.85246134 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model. · #48400](https://github.com/huggingface/transformers/issues/48400) | rrf / 0.01639344 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [The kernel&#x27;s version doesn&#x27;t properly check. · #47455](https://github.com/huggingface/transformers/issues/47455) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally · #47917](https://github.com/huggingface/transformers/issues/47917) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [CLIPSeg, TimesFM, PP-OCR detector and VideoPrism base/head loads still give every weight randomly initialized (#48722 follow-up) · #48862](https://github.com/huggingface/transformers/issues/48862) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `no_lexical_match` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Bug about transformers==5.16.1 while loading &#x27;nvidia/audio-flamingo-next-hf&#x27; model. · #48400](https://github.com/huggingface/transformers/issues/48400) | cosine_similarity / 0.84123909 | UNJUDGED | unreviewed [] |

| 2 | [Phi3/Phimoe: prepare_inputs_for_generation forwards logits_to_keep=None into forward() -&gt; 4-dim logits -&gt; torch.multinomial crash · #47530](https://github.com/huggingface/transformers/issues/47530) | cosine_similarity / 0.84048247 | UNJUDGED | unreviewed [] |

| 3 | [The kernel&#x27;s version doesn&#x27;t properly check. · #47455](https://github.com/huggingface/transformers/issues/47455) | cosine_similarity / 0.84027600 | UNJUDGED | unreviewed [] |

| 4 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally · #47917](https://github.com/huggingface/transformers/issues/47917) | cosine_similarity / 0.83937395 | UNJUDGED | unreviewed [] |

| 5 | [CLIPSeg, TimesFM, PP-OCR detector and VideoPrism base/head loads still give every weight randomly initialized (#48722 follow-up) · #48862](https://github.com/huggingface/transformers/issues/48862) | cosine_similarity / 0.83883572 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
FineGrainedFP8Config로 만든 양자화 객체에서 update_tp_plan을 호출하면 속성 오류가 납니다. 설정에는 base_model_tp_plan이 있고 별도의 _experts_implementation은 지정하지 않았습니다. 일반 Qwen FP8 모델 로딩에서도 문제가 보고됩니다.

[ERROR]
AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;get&#x27;

[ENVIRONMENT]
Transformers 5.16.0 및 main; Python 3.12.13; PyTorch 2.13.0+cu130; Linux</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 4 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward · #48307](https://github.com/huggingface/transformers/issues/48307) | rrf / 0.02687887 | UNJUDGED | unreviewed [] |

| 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | rrf / 0.02584921 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | bm25 / 96.66337444 | UNJUDGED | unreviewed [] |

| 2 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | bm25 / 51.55783599 | UNJUDGED | unreviewed [] |

| 3 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | bm25 / 43.93723718 | UNJUDGED | unreviewed [] |

| 4 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank) · #48308](https://github.com/huggingface/transformers/issues/48308) | bm25 / 41.74455694 | UNJUDGED | unreviewed [] |

| 5 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward · #48307](https://github.com/huggingface/transformers/issues/48307) | bm25 / 36.27101718 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | cosine_similarity / 0.92190194 | UNJUDGED | unreviewed [] |

| 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | cosine_similarity / 0.90283769 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | cosine_similarity / 0.89769089 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-08-23 · #48240](https://github.com/huggingface/transformers/issues/48240) | cosine_similarity / 0.89255732 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-09-17 · #48914](https://github.com/huggingface/transformers/issues/48914) | cosine_similarity / 0.89051849 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | rrf / 0.03151365 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | rrf / 0.03105441 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.03057890 | UNJUDGED | unreviewed [] |

| 4 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | rrf / 0.02877847 | UNJUDGED | unreviewed [] |

| 5 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors · #49190](https://github.com/huggingface/transformers/issues/49190) | rrf / 0.02844164 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 25.05471341 | UNJUDGED | unreviewed [] |

| 2 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 22.34940268 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 21.36551752 | UNJUDGED | unreviewed [] |

| 4 | [Issue doing PEFT on Embedding Gemma w/ new classifier head · #48964](https://github.com/huggingface/transformers/issues/48964) | bm25 / 20.77907155 | UNJUDGED | unreviewed [] |

| 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | bm25 / 20.41133039 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors · #49190](https://github.com/huggingface/transformers/issues/49190) | cosine_similarity / 0.88418734 | UNJUDGED | unreviewed [] |

| 2 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | cosine_similarity / 0.88354844 | UNJUDGED | unreviewed [] |

| 3 | [Module-level getattr breaks unittest functionality · #48966](https://github.com/huggingface/transformers/issues/48966) | cosine_similarity / 0.88163066 | UNJUDGED | unreviewed [] |

| 4 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B` · #47333](https://github.com/huggingface/transformers/issues/47333) | cosine_similarity / 0.88087296 | UNJUDGED | unreviewed [] |

| 5 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | cosine_similarity / 0.88009185 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Calling update_tp_plan on a quantizer created with FineGrainedFP8Config raises an attribute error. The configuration has base_model_tp_plan and no separately specified _experts_implementation. The same problem is reported when loading normal Qwen FP8 models.

[ERROR]
AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;get&#x27;

[ENVIRONMENT]
Transformers 5.16.0 and main; Python 3.12.13; PyTorch 2.13.0+cu130; Linux</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | bm25 / 166.24496744 | UNJUDGED | unreviewed [] |

| 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | bm25 / 96.64325010 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | bm25 / 85.42334205 | UNJUDGED | unreviewed [] |

| 4 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank) · #48308](https://github.com/huggingface/transformers/issues/48308) | bm25 / 68.00350193 | UNJUDGED | unreviewed [] |

| 5 | [Native TP has no KV-head replication: tp_size &gt; num_key_value_heads fails mid-forward · #48307](https://github.com/huggingface/transformers/issues/48307) | bm25 / 58.66943228 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | cosine_similarity / 0.95132256 | UNJUDGED | unreviewed [] |

| 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | cosine_similarity / 0.92413402 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | cosine_similarity / 0.92273790 | UNJUDGED | unreviewed [] |

| 4 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | cosine_similarity / 0.89861697 | UNJUDGED | unreviewed [] |

| 5 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally · #47917](https://github.com/huggingface/transformers/issues/47917) | cosine_similarity / 0.89463615 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Regression] FineGrainedFP8HfQuantizer crashes when expert TP overrides are absent · #48346](https://github.com/huggingface/transformers/issues/48346) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [FP8 quantizer: update_tp_plan misses composite configs, expert scales stay replicated under EP · #48757](https://github.com/huggingface/transformers/issues/48757) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [FineGrainedFP8HfQuantizer.update_tp_plan crashes when the model has no tp_plan · #48351](https://github.com/huggingface/transformers/issues/48351) | rrf / 0.03174603 | UNJUDGED | unreviewed [] |

| 4 | [AutoProcessor.from_pretrained raises AttributeError: &#x27;NoneType&#x27; object has no attribute &#x27;__module__&#x27; when torchvision is missing · #48556](https://github.com/huggingface/transformers/issues/48556) | rrf / 0.02840451 | UNJUDGED | unreviewed [] |

| 5 | [Native TP does not shard qwen3_vl_moe experts (weights fully replicated per rank) · #48308](https://github.com/huggingface/transformers/issues/48308) | rrf / 0.02767319 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 34.84569578 | UNJUDGED | unreviewed [] |

| 2 | [MIGRATION_GUIDE_V5.md missing Dynamic - Cache API removals (key_cache, from_legacy_cache) · #48479](https://github.com/huggingface/transformers/issues/48479) | bm25 / 34.73541177 | UNJUDGED | unreviewed [] |

| 3 | [Loading `RTDetrModel` from a detection checkpoint (or `SEWDForCTC` from a SEW-D checkpoint) gives a model with every weight randomly initialized · #48722](https://github.com/huggingface/transformers/issues/48722) | bm25 / 34.31641631 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | bm25 / 32.20514416 | UNJUDGED | unreviewed [] |

| 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | bm25 / 31.94074269 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | cosine_similarity / 0.89861697 | UNJUDGED | unreviewed [] |

| 2 | [TimmWrapperPreTrainedModel: SDPA dispatch fails even though timm uses SDPA internally · #47917](https://github.com/huggingface/transformers/issues/47917) | cosine_similarity / 0.89463615 | UNJUDGED | unreviewed [] |

| 3 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | cosine_similarity / 0.89115065 | UNJUDGED | unreviewed [] |

| 4 | [NameError: name &#x27;nn&#x27; is not defined when resolving OutputRecorder type hints · #47766](https://github.com/huggingface/transformers/issues/47766) | cosine_similarity / 0.88850808 | UNJUDGED | unreviewed [] |

| 5 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | cosine_similarity / 0.88704431 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | rrf / 0.03226646 | UNJUDGED | unreviewed [] |

| 2 | [AttributeError: &#x27;Qwen2_5OmniConfig&#x27; object has no attribute &#x27;max_position_embeddings&#x27; · #47436](https://github.com/huggingface/transformers/issues/47436) | rrf / 0.03076923 | UNJUDGED | unreviewed [] |

| 3 | [gemma4 12B arch is not recognized! · #47448](https://github.com/huggingface/transformers/issues/47448) | rrf / 0.03007689 | UNJUDGED | unreviewed [] |

| 4 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | rrf / 0.02990696 | UNJUDGED | unreviewed [] |

| 5 | [Continuous batching (generate_batch) fails on models with heterogeneous per-layer num_key_value_heads/head_dim (e.g. Gemma4) · #47721](https://github.com/huggingface/transformers/issues/47721) | rrf / 0.02861201 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
