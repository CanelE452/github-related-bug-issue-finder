# T-C2 · huggingface/transformers

cohort: `core_development`. 이 사례는 기존 원문에서 재구성한 개발 사례입니다. 독립 신규 과제/사람 정확도 검증이 아닙니다.

참고 원문: [huggingface/transformers#48315](https://github.com/huggingface/transformers/issues/48315)

질의 작성 사전 노출: Agent read current title/body before drafting. Not blind; no retrieved ranks or comments used.

## A_ko_symptom

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
체크포인트에서 재개한 Trainer 학습이 끝까지 진행된 뒤 마지막에 파일 오류로 실패합니다.</pre>

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | cosine_similarity / 0.87297034 | UNJUDGED | unreviewed [] |

| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | cosine_similarity / 0.86573899 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.85992455 | UNJUDGED | unreviewed [] |

| 4 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.85618550 | UNJUDGED | unreviewed [] |

| 5 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discover branch, and wrong eval loss/perplexity on partial batches · #47375](https://github.com/huggingface/transformers/issues/47375) | cosine_similarity / 0.85483050 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | rrf / 0.03201844 | UNJUDGED | unreviewed [] |

| 2 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discover branch, and wrong eval loss/perplexity on partial batches · #47375](https://github.com/huggingface/transformers/issues/47375) | rrf / 0.03177806 | UNJUDGED | unreviewed [] |

| 3 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03128055 | UNJUDGED | unreviewed [] |

| 4 | [Nothing destroys the process group, so every distributed Trainer run warns at exit · #48874](https://github.com/huggingface/transformers/issues/48874) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.03079839 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `4` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Two systematic bugs in examples/pytorch/*_no_trainer.py: broken --resume_from_checkpoint auto-discover branch, and wrong eval loss/perplexity on partial batches · #47375](https://github.com/huggingface/transformers/issues/47375) | bm25 / 6.18407179 | UNJUDGED | unreviewed [] |

| 2 | [Should Trainer support models FSDP2-sharded at load time (DistributedConfig(fsdp_size=N))? · #48210](https://github.com/huggingface/transformers/issues/48210) | bm25 / 6.14698067 | UNJUDGED | unreviewed [] |

| 3 | [Nothing destroys the process group, so every distributed Trainer run warns at exit · #48874](https://github.com/huggingface/transformers/issues/48874) | bm25 / 5.93182399 | UNJUDGED | unreviewed [] |

| 4 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | bm25 / 5.92996285 | UNJUDGED | unreviewed [] |

| 5 | [FSDP2: evaluate/predict on a fresh Trainer raises in Accelerator.prepare · #48841](https://github.com/huggingface/transformers/issues/48841) | bm25 / 5.90399911 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | cosine_similarity / 0.86573899 | UNJUDGED | unreviewed [] |

| 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.85992455 | UNJUDGED | unreviewed [] |

| 3 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.85618550 | UNJUDGED | unreviewed [] |

| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | cosine_similarity / 0.85231245 | UNJUDGED | unreviewed [] |

| 5 | [Qwen2Tokenizer overwrites pre_tokenizer from tokenizer.json. Wrong token IDs for all Qwen3.6 / Qwen3.8 models (v4→v5 regression) · #49066](https://github.com/huggingface/transformers/issues/49066) | cosine_similarity / 0.85190463 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.03225806 | UNJUDGED | unreviewed [] |

| 3 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | rrf / 0.03100962 | UNJUDGED | unreviewed [] |

| 5 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | rrf / 0.03036577 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | bm25 / 5.99578059 | UNJUDGED | unreviewed [] |

| 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | bm25 / 5.99292781 | UNJUDGED | unreviewed [] |

| 3 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 5.70532607 | UNJUDGED | unreviewed [] |

| 4 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | bm25 / 5.68855803 | UNJUDGED | unreviewed [] |

| 5 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | bm25 / 5.40451647 | UNJUDGED | unreviewed [] |

## B_ko_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
Trainer 체크포인트를 다른 위치로 옮긴 뒤 재개했습니다. trainer_state.json의 best_model_checkpoint는 존재하지 않는 이전 경로를 가리킵니다. 새 best가 생기지 않았고 save_total_limit=1, load_best_model_at_end=True입니다. 학습은 끝났지만 마지막 정리에서 실패합니다.

[ERROR]
FileNotFoundError: [WinError 2] The system cannot find the file specified

[ENVIRONMENT]
Transformers 5.16.0.dev0; torch 2.11.0+cu128; Python 3.12.6; Windows 11</pre>

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | bm25 / 133.16176994 | UNJUDGED | unreviewed [] |

| 2 | [XPU: `from_pretrained(device_map=...)` fails under WSL2 because `caching_allocator_warmup` does not guard `mem_get_info` · #48127](https://github.com/huggingface/transformers/issues/48127) | bm25 / 42.00430824 | UNJUDGED | unreviewed [] |

| 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | bm25 / 37.60050520 | UNJUDGED | unreviewed [] |

| 4 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | bm25 / 37.14327240 | UNJUDGED | unreviewed [] |

| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory) · #48285](https://github.com/huggingface/transformers/issues/48285) | bm25 / 36.82955396 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | cosine_similarity / 0.91608524 | UNJUDGED | unreviewed [] |

| 2 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.88718742 | UNJUDGED | unreviewed [] |

| 3 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B` · #47333](https://github.com/huggingface/transformers/issues/47333) | cosine_similarity / 0.88622737 | UNJUDGED | unreviewed [] |

| 4 | [[serge] integration failure triage - 2026-08-30 · #48422](https://github.com/huggingface/transformers/issues/48422) | cosine_similarity / 0.88325000 | UNJUDGED | unreviewed [] |

| 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.88157773 | UNJUDGED | unreviewed [] |

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.02991071 | UNJUDGED | unreviewed [] |

| 3 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | rrf / 0.02928693 | UNJUDGED | unreviewed [] |

| 4 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | rrf / 0.02923602 | UNJUDGED | unreviewed [] |

| 5 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.02908325 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | bm25 / 31.14623997 | UNJUDGED | unreviewed [] |

| 2 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | bm25 / 30.43923019 | UNJUDGED | unreviewed [] |

| 3 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory) · #48285](https://github.com/huggingface/transformers/issues/48285) | bm25 / 30.34106899 | UNJUDGED | unreviewed [] |

| 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 27.69524427 | UNJUDGED | unreviewed [] |

| 5 | [caching_allocator_warmup crashes with AttributeError when loading bitsandbytes-quantized model with PEFT adapter · #47914](https://github.com/huggingface/transformers/issues/47914) | bm25 / 26.60711496 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.88718742 | UNJUDGED | unreviewed [] |

| 2 | [[Offloading] Cannot save disk-offloaded `Qwen/Qwen3-30B-A3B` · #47333](https://github.com/huggingface/transformers/issues/47333) | cosine_similarity / 0.88622737 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.88157773 | UNJUDGED | unreviewed [] |

| 4 | [[Offloading] Cannot save disk-offloaded `Qwen3-VL-32B-Instruct` · #47332](https://github.com/huggingface/transformers/issues/47332) | cosine_similarity / 0.87987685 | UNJUDGED | unreviewed [] |

| 5 | [AMD quark class not updated · #47321](https://github.com/huggingface/transformers/issues/47321) | cosine_similarity / 0.87935865 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03154496 | UNJUDGED | unreviewed [] |

| 2 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | rrf / 0.03131882 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.03102453 | UNJUDGED | unreviewed [] |

| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | rrf / 0.03062179 | UNJUDGED | unreviewed [] |

| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory) · #48285](https://github.com/huggingface/transformers/issues/48285) | rrf / 0.03057890 | UNJUDGED | unreviewed [] |

## C_en_context

승인: `False` · query_unreviewed · 실제 검토 노출: []

<pre>[PROBLEM]
I resumed Trainer after moving the checkpoint to a different location. The best_model_checkpoint in trainer_state.json points to an old path that no longer exists. No new best was set, with save_total_limit=1 and load_best_model_at_end=True. Training completes but final cleanup fails.

[ERROR]
FileNotFoundError: [WinError 2] The system cannot find the file specified

[ENVIRONMENT]
Transformers 5.16.0.dev0; torch 2.11.0+cu128; Python 3.12.6; Windows 11</pre>

### C_raw · hybrid

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | rrf / 0.03278689 | UNJUDGED | unreviewed [] |

| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | rrf / 0.03030999 | UNJUDGED | unreviewed [] |

| 5 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | rrf / 0.02987737 | UNJUDGED | unreviewed [] |

### C_raw · semantic

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | cosine_similarity / 0.95169061 | UNJUDGED | unreviewed [] |

| 2 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.91340619 | UNJUDGED | unreviewed [] |

| 3 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | cosine_similarity / 0.90656912 | UNJUDGED | unreviewed [] |

| 4 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.89858091 | UNJUDGED | unreviewed [] |

| 5 | [`Trainer` deletes `config.bos_token_id` when the tokenizer declares no BOS, and persists it · #48592](https://github.com/huggingface/transformers/issues/48592) | cosine_similarity / 0.89799833 | UNJUDGED | unreviewed [] |

### C_raw · bm25

실행 상태: `ok` · 참고 원문 순위: `1` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer crashes at the end of a resumed run when trainer_state.json points best_model_checkpoint at a missing directory · #48315](https://github.com/huggingface/transformers/issues/48315) | bm25 / 224.58458743 | UNJUDGED | unreviewed [] |

| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | bm25 / 75.66259161 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | bm25 / 60.16305019 | UNJUDGED | unreviewed [] |

| 4 | [XPU: `from_pretrained(device_map=...)` fails under WSL2 because `caching_allocator_warmup` does not guard `mem_get_info` · #48127](https://github.com/huggingface/transformers/issues/48127) | bm25 / 60.15796884 | UNJUDGED | unreviewed [] |

| 5 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | bm25 / 58.20232979 | UNJUDGED | unreviewed [] |

### C_bug · hybrid

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | rrf / 0.03252247 | UNJUDGED | unreviewed [] |

| 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | rrf / 0.03200205 | UNJUDGED | unreviewed [] |

| 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | rrf / 0.03149802 | UNJUDGED | unreviewed [] |

| 4 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | rrf / 0.03067916 | UNJUDGED | unreviewed [] |

| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory) · #48285](https://github.com/huggingface/transformers/issues/48285) | rrf / 0.03009050 | UNJUDGED | unreviewed [] |

### C_bug · semantic

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Only on saving a checkpoint are weight conversions used · #48805](https://github.com/huggingface/transformers/issues/48805) | cosine_similarity / 0.91340619 | UNJUDGED | unreviewed [] |

| 2 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | cosine_similarity / 0.90656912 | UNJUDGED | unreviewed [] |

| 3 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | cosine_similarity / 0.89858091 | UNJUDGED | unreviewed [] |

| 4 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | cosine_similarity / 0.89619797 | UNJUDGED | unreviewed [] |

| 5 | [Silent conversion skip on model_type mismatch: loading a converted checkpoint via the wrong Auto class yields randomly-initialized weights that generate fluently · #47405](https://github.com/huggingface/transformers/issues/47405) | cosine_similarity / 0.89504677 | UNJUDGED | unreviewed [] |

### C_bug · bm25

실행 상태: `ok` · 참고 원문 순위: `None` (관련성 정답이라는 뜻 아님)

| 순위 | 문서 | 점수 종류 / 점수 | 사람 판정 | 근거 / 이유 |

|---|---|---|---|---|

| 1 | [Trainer reports incorrect final loss and throughput after resuming from a full checkpoint · #49193](https://github.com/huggingface/transformers/issues/49193) | bm25 / 65.79254330 | UNJUDGED | unreviewed [] |

| 2 | [Trainer fails to resume from a checkpoint on CPU with two or more processes · #49121](https://github.com/huggingface/transformers/issues/49121) | bm25 / 50.07642952 | UNJUDGED | unreviewed [] |

| 3 | [`CheckpointError` with PEFT + DeepSpeed ZeRO-3 + gradient checkpointing · #47254](https://github.com/huggingface/transformers/issues/47254) | bm25 / 49.75454036 | UNJUDGED | unreviewed [] |

| 4 | [[Bug] Qwen3-MoE router auxiliary loss is multiplied by the DDP world size in Trainer · #48690](https://github.com/huggingface/transformers/issues/48690) | bm25 / 49.28517099 | UNJUDGED | unreviewed [] |

| 5 | [`from_pretrained` with safetensors mmap crashes on Windows for large multi-shard checkpoints (copy-on-write commit charge exhausts memory) · #48285](https://github.com/huggingface/transformers/issues/48285) | bm25 / 47.41103058 | UNJUDGED | unreviewed [] |

## 판단과 다음 단계

범위·토큰·RRF·구간 관찰은 별도 원자료에 연결됩니다. 관련성에 따른 성공/실패·개선/무차이/악화는 사람 판정과 같은 공통 풀이 갖춰질 때만 결정합니다. 참고 원문의 포함이나 순위만으로 해결 가능성을 확정하지 않습니다.
