# T-S2 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#48826](https://github.com/huggingface/transformers/issues/48826)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Qwen의 QSA indexer 파라미터를 학습하려는데 업데이트되지 않습니다.</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 20.87003491 | UNJUDGED | unreviewed [] |

| 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41) · #48755](https://github.com/huggingface/transformers/issues/48755) | bm25 / 9.68024566 | UNJUDGED | unreviewed [] |

| 3 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures · #48913](https://github.com/huggingface/transformers/issues/48913) | bm25 / 5.64884985 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41) · #48755](https://github.com/huggingface/transformers/issues/48755) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 4 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures · #48913](https://github.com/huggingface/transformers/issues/48913) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-09-21 · #49000](https://github.com/huggingface/transformers/issues/49000) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.86999249 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.86710733 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-09-21 · #49000](https://github.com/huggingface/transformers/issues/49000) | cosine_similarity / 0.86253405 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-29 · #49175](https://github.com/huggingface/transformers/issues/49175) | cosine_similarity / 0.86156100 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.85756278 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 17.61690079 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | rrf / 0.01612903 | UNJUDGED | unreviewed [] |

| 3 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors · #49190](https://github.com/huggingface/transformers/issues/49190) | rrf / 0.01587302 | UNJUDGED | unreviewed [] |

| 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot; · #47553](https://github.com/huggingface/transformers/issues/47553) | rrf / 0.01562500 | UNJUDGED | unreviewed [] |

| 5 | [BarthezTokenizer cannot load moussaKam/barthez: v4.57 → v5 regression, BPE vocab into a hardcoded Unigram · #48567](https://github.com/huggingface/transformers/issues/48567) | rrf / 0.01538462 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.86999249 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.86710733 | UNJUDGED | unreviewed [] |

| 3 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors · #49190](https://github.com/huggingface/transformers/issues/49190) | cosine_similarity / 0.85650551 | UNJUDGED | unreviewed [] |

| 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot; · #47553](https://github.com/huggingface/transformers/issues/47553) | cosine_similarity / 0.85135937 | UNJUDGED | unreviewed [] |

| 5 | [BarthezTokenizer cannot load moussaKam/barthez: v4.57 → v5 regression, BPE vocab into a hardcoded Unigram · #48567](https://github.com/huggingface/transformers/issues/48567) | cosine_similarity / 0.85074139 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Qwen3.8-flash-next의 QSA indexer 파라미터를 학습하려고 합니다. 기술 보고서는 KL loss로 학습할 수 있다고 하는데 현재 코드에서 파라미터가 학습되지 않습니다.

[ENVIRONMENT]
버전과 실행 환경은 원문에 제공되지 않음</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | rrf / 0.03131882 | UNJUDGED | unreviewed [] |

| 3 | [qwen4_exp: fp8-quantized n-gram (PLE) embedding rows are gathered without dequantization · #48350](https://github.com/huggingface/transformers/issues/48350) | rrf / 0.02921109 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-29 · #49175](https://github.com/huggingface/transformers/issues/49175) | rrf / 0.02703196 | UNJUDGED | unreviewed [] |

| 5 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | rrf / 0.02613270 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.88711631 | UNJUDGED | unreviewed [] |

| 2 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.88686824 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-18 · #48050](https://github.com/huggingface/transformers/issues/48050) | cosine_similarity / 0.88221562 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-09-28 · #49169](https://github.com/huggingface/transformers/issues/49169) | cosine_similarity / 0.88145405 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-09-12 · #48749](https://github.com/huggingface/transformers/issues/48749) | cosine_similarity / 0.87850034 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 36.59207131 | UNJUDGED | unreviewed [] |

| 2 | [Add DeepSeek-V4.1-Flash (deepseek_v41) · #48755](https://github.com/huggingface/transformers/issues/48755) | bm25 / 15.04221804 | UNJUDGED | unreviewed [] |

| 3 | [MtpModel/MtpLayer topology is too rigid to represent non-uniform MTP architectures · #48913](https://github.com/huggingface/transformers/issues/48913) | bm25 / 9.19712715 | UNJUDGED | unreviewed [] |

| 4 | [FineGrainedFP8: modules_to_not_convert never matches on text-only loads of multimodal checkpoints (silent quality corruption) · #48349](https://github.com/huggingface/transformers/issues/48349) | bm25 / 9.01558101 | UNJUDGED | unreviewed [] |

| 5 | [Qwen3.5-9B fine-tuning with run_clm.py on 8x B200 ran the gated DeltaNet layers on the fp32 torch chunk loop because flash-linear-attention was not installed · #48718](https://github.com/huggingface/transformers/issues/48718) | bm25 / 8.99655219 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 3 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | rrf / 0.03125763 | UNJUDGED | unreviewed [] |

| 4 | [[eager MOE] Selected expert IDs should probably not be treated as 0-d GPU tensors · #49190](https://github.com/huggingface/transformers/issues/49190) | rrf / 0.02921109 | UNJUDGED | unreviewed [] |

| 5 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.02869353 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `2` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.88711631 | UNJUDGED | unreviewed [] |

| 2 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.88686824 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | cosine_similarity / 0.87459475 | UNJUDGED | unreviewed [] |

| 4 | [&quot;ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported&quot; · #47553](https://github.com/huggingface/transformers/issues/47553) | cosine_similarity / 0.87435633 | UNJUDGED | unreviewed [] |

| 5 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | cosine_similarity / 0.87313563 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 32.46182796 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | bm25 / 9.37354922 | UNJUDGED | unreviewed [] |

| 3 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | bm25 / 8.15608384 | UNJUDGED | unreviewed [] |

| 4 | [Continuous batching CUDA-graph capture crashes under distributed runs (allocator internal assert) · #48312](https://github.com/huggingface/transformers/issues/48312) | bm25 / 7.62627811 | UNJUDGED | unreviewed [] |

| 5 | [Transformers 5.13 CPU memory growth loading Qwen3-235B-A22B with DeepSpeed ZeRO-3; 4.51.0 remains bounded · #47514](https://github.com/huggingface/transformers/issues/47514) | bm25 / 7.05796615 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
I want to train the QSA indexer parameters in Qwen3.8-flash-next. The technical report says they can be trained with KL loss, but the parameters cannot be trained in the current code.

[ENVIRONMENT]
The source report does not provide a version or runtime environment</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 102.47300016 | UNJUDGED | unreviewed [] |

| 2 | [MiniMaxM2 silently applies full-head RoPE: config drops the checkpoints&#x27; legacy `rotary_dim` field · #48241](https://github.com/huggingface/transformers/issues/48241) | bm25 / 30.12411656 | UNJUDGED | unreviewed [] |

| 3 | [MusicGen: hub configs set decoder dropout=0.1 but the checkpoints were trained with 0 — train() doubles the loss and silently breaks fine-tuning · #49094](https://github.com/huggingface/transformers/issues/49094) | bm25 / 29.92845783 | UNJUDGED | unreviewed [] |

| 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 29.83675090 | UNJUDGED | unreviewed [] |

| 5 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare · #48841](https://github.com/huggingface/transformers/issues/48841) | bm25 / 28.96586157 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.91273475 | UNJUDGED | unreviewed [] |

| 2 | [CompressedTensorsConfig(run_compressed=False) silently random-initializes unmapped fused-MoE expert weights on 5.10.x (works on 5.13.1) — request hard error for unmapped packed tensors · #47407](https://github.com/huggingface/transformers/issues/47407) | cosine_similarity / 0.90157485 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-18 · #48050](https://github.com/huggingface/transformers/issues/48050) | cosine_similarity / 0.89665842 | UNJUDGED | unreviewed [] |

| 4 | [Qwen3.5-9B fine-tuning with run_clm.py on 8x B200 ran the gated DeltaNet layers on the fp32 torch chunk loop because flash-linear-attention was not installed · #48718](https://github.com/huggingface/transformers/issues/48718) | cosine_similarity / 0.89586419 | UNJUDGED | unreviewed [] |

| 5 | [Llama 4 declares `output_router_logits` and `router_aux_loss_coef` but never reads them · #48889](https://github.com/huggingface/transformers/issues/48889) | cosine_similarity / 0.89381599 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.02991071 | UNJUDGED | unreviewed [] |

| 3 | [Heads that declare **kwargs but drop num_items_in_batch train with an inflated loss under gradient accumulation · #47688](https://github.com/huggingface/transformers/issues/47688) | rrf / 0.02985075 | UNJUDGED | unreviewed [] |

| 4 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare · #48841](https://github.com/huggingface/transformers/issues/48841) | rrf / 0.02837163 | UNJUDGED | unreviewed [] |

| 5 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | rrf / 0.02798434 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | bm25 / 92.76009715 | UNJUDGED | unreviewed [] |

| 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 29.39088320 | UNJUDGED | unreviewed [] |

| 3 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | bm25 / 27.51678672 | UNJUDGED | unreviewed [] |

| 4 | [MusicGen: hub configs set decoder dropout=0.1 but the checkpoints were trained with 0 — train() doubles the loss and silently breaks fine-tuning · #49094](https://github.com/huggingface/transformers/issues/49094) | bm25 / 25.72329038 | UNJUDGED | unreviewed [] |

| 5 | [`Qwen3_5GatedDeltaNet` / `Qwen3_5MoeGatedDeltaNet` initialize `A_log` to `-inf` on some heads (bf16 models) · #47831](https://github.com/huggingface/transformers/issues/47831) | bm25 / 24.66084247 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | cosine_similarity / 0.91273475 | UNJUDGED | unreviewed [] |

| 2 | [Qwen3-VL and Gemma3 (VLM) ignore `shift_labels` · #48491](https://github.com/huggingface/transformers/issues/48491) | cosine_similarity / 0.89377832 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | cosine_similarity / 0.89144909 | UNJUDGED | unreviewed [] |

| 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | cosine_similarity / 0.89069450 | UNJUDGED | unreviewed [] |

| 5 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | cosine_similarity / 0.88996208 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[Qwen3.8-flash-next] QSAIndexer can not train · #48826](https://github.com/huggingface/transformers/issues/48826) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [Installed nested optional kernels silently fall back to the Torch implementation · #48148](https://github.com/huggingface/transformers/issues/48148) | rrf / 0.03125763 | UNJUDGED | unreviewed [] |

| 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03077652 | UNJUDGED | unreviewed [] |

| 5 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | rrf / 0.02985740 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
