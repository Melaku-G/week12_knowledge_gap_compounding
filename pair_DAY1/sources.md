# Sources

## Canonical Papers

### 1. LoRA: Low-Rank Adaptation of Large Language Models

Hu et al. (2021)

https://arxiv.org/abs/2106.09685

Used for:

* LoRA formulation
* low-rank decomposition mechanics
* inference-time adapter application explanation

---

### 2. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Dao et al. (2022)

https://arxiv.org/abs/2205.14135

Used for:

* fused attention kernels
* memory-bandwidth bottlenecks
* optimized transformer inference paths

---

## Documentation / Engineering References

### 3. Hugging Face PEFT Documentation

https://huggingface.co/docs/peft/index

Used for:

* `merge_and_unload()`
* merged vs unmerged adapter workflows

---

### 4. Unsloth Documentation

https://docs.unsloth.ai/

Used for:

* optimized inference path discussion
* LoRA inference optimization references

---

## Tooling / Demonstration

### Planned experiments

* merged vs unmerged LoRA benchmarking
* tokens/sec measurements
* latency decomposition
* CUDA timing
* PyTorch profiler

### Planned scripts

* `profile_lora_merge.py`
* `benchmark_prefill_decode.py`
