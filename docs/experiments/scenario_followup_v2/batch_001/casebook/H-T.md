# H-T · huggingface/transformers

cohort: `historical_probe`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#24694](https://github.com/huggingface/transformers/issues/24694)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
GPT-Neo에서 입력에 왼쪽 패딩을 넣으면 생성 결과가 반복적이고 부자연스러워집니다.

[ENVIRONMENT]
GPT-Neo; left padding</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[serge] integration failure triage - 2026-08-22 · #48222](https://github.com/huggingface/transformers/issues/48222) | rrf / 0.02972678 | UNJUDGED | unreviewed [] |

| 2 | [Right-padded prefill produces a corrupted cache in Mamba-family models (zero conv state, decayed SSM state) · #48256](https://github.com/huggingface/transformers/issues/48256) | rrf / 0.02819138 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-18 · #48050](https://github.com/huggingface/transformers/issues/48050) | rrf / 0.02594184 | UNJUDGED | unreviewed [] |

| 4 | [Major Bug in parallel generation / left padding. · #47651](https://github.com/huggingface/transformers/issues/47651) | rrf / 0.02585919 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-21 · #48202](https://github.com/huggingface/transformers/issues/48202) | rrf / 0.02569389 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[serge] integration failure triage - 2026-08-22 · #48222](https://github.com/huggingface/transformers/issues/48222) | bm25 / 14.13521311 | UNJUDGED | unreviewed [] |

| 2 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache · #48693](https://github.com/huggingface/transformers/issues/48693) | bm25 / 13.77589240 | UNJUDGED | unreviewed [] |

| 3 | [Several slow tokenizers read all_special_tokens or all_special_ids once per token in decode loops · #47424](https://github.com/huggingface/transformers/issues/47424) | bm25 / 13.21750192 | UNJUDGED | unreviewed [] |

| 4 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution · #48459](https://github.com/huggingface/transformers/issues/48459) | bm25 / 12.14865201 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-08-21 · #48202](https://github.com/huggingface/transformers/issues/48202) | bm25 / 11.90628997 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[serge] integration failure triage - 2026-09-29 · #49175](https://github.com/huggingface/transformers/issues/49175) | cosine_similarity / 0.87034452 | UNJUDGED | unreviewed [] |

| 2 | [GenerationConfig should validate that pad_token_id is not in eos_token_id list · #48016](https://github.com/huggingface/transformers/issues/48016) | cosine_similarity / 0.86776704 | UNJUDGED | unreviewed [] |

| 3 | [[serge] integration failure triage - 2026-08-31 · #48423](https://github.com/huggingface/transformers/issues/48423) | cosine_similarity / 0.86637104 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.86622715 | UNJUDGED | unreviewed [] |

| 5 | [[serge] integration failure triage - 2026-09-21 · #49000](https://github.com/huggingface/transformers/issues/49000) | cosine_similarity / 0.86503220 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Major Bug in parallel generation / left padding. · #47651](https://github.com/huggingface/transformers/issues/47651) | rrf / 0.03154496 | UNJUDGED | unreviewed [] |

| 2 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | rrf / 0.03057890 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.02970951 | UNJUDGED | unreviewed [] |

| 4 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution · #48459](https://github.com/huggingface/transformers/issues/48459) | rrf / 0.02946237 | UNJUDGED | unreviewed [] |

| 5 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache · #48693](https://github.com/huggingface/transformers/issues/48693) | rrf / 0.02938046 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [[ImageGPT] Cross-attention crashes, ignores encoder_attention_mask, and doubles its cache · #48693](https://github.com/huggingface/transformers/issues/48693) | bm25 / 13.24487078 | UNJUDGED | unreviewed [] |

| 2 | [GPT-NeoX: hardcoded float32 softmax silently caps float64 inference at float32 resolution · #48459](https://github.com/huggingface/transformers/issues/48459) | bm25 / 10.77704524 | UNJUDGED | unreviewed [] |

| 3 | [GPTNeoXJapanese crashes for any `rotary_pct != 1.0`: RoPE ignores `partial_rotary_factor` · #48630](https://github.com/huggingface/transformers/issues/48630) | bm25 / 9.67864849 | UNJUDGED | unreviewed [] |

| 4 | [Incompatible with kernels 0.16 · #47312](https://github.com/huggingface/transformers/issues/47312) | bm25 / 7.90591122 | UNJUDGED | unreviewed [] |

| 5 | [Transformers 5.13 CPU memory growth loading Qwen3-235B-A22B with DeepSpeed ZeRO-3; 4.51.0 remains bounded · #47514](https://github.com/huggingface/transformers/issues/47514) | bm25 / 7.65658120 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Major Bug in parallel generation / left padding. · #47651](https://github.com/huggingface/transformers/issues/47651) | cosine_similarity / 0.85958421 | UNJUDGED | unreviewed [] |

| 2 | [Qwen2-VL get_rope_index shape mismatch even with batch_size=1 (transformers 5.15.0) · #48057](https://github.com/huggingface/transformers/issues/48057) | cosine_similarity / 0.85952890 | UNJUDGED | unreviewed [] |

| 3 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.85748589 | UNJUDGED | unreviewed [] |

| 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | cosine_similarity / 0.85553533 | UNJUDGED | unreviewed [] |

| 5 | [CSM codebook embedding tying is ignored when `tie_word_embeddings=False` · #49196](https://github.com/huggingface/transformers/issues/49196) | cosine_similarity / 0.85546637 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
