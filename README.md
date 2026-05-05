# Week 12 — Knowledge Gap Formulation for Compounding

This repository contains my Week 12 pair-cycle work focused on inference-time mechanics, LoRA deployment behavior, and transformer inference optimization.

The goal of Week 12 was not only to answer technical questions, but to:

* identify genuine gaps in understanding,
* sharpen them collaboratively,
* investigate them experimentally,
* and ground the resulting understanding back into prior portfolio work.

---

# Repository Structure

```text
week12_knowledge_gap_compounding/
│
├── README.md
│
├── pair_DAY1/
│   ├── question.md
│   ├── morning_call_summary.md
│   ├── explainer.md
│   ├── thread.md
│   ├── evening_call_summary.md
│   ├── signoff.md
│   ├── grounding_commit.md
│   ├── sources.md
│   │
│   ├── code/
│   │   └── profile_lora_merge.py
│   │
│   └── assets/
│
└── ...
```

---

# Day 1 Theme — Inference-Time Mechanics

## My Sharpened Question

> How can a LoRA-adapted Qwen2.5-1.5B model achieve a 2.41× inference speedup despite identical merged parameter counts — and how can I experimentally decompose that gain across prefill, decode, quantization, kernel fusion, and KV-cache behavior?

This question emerged from reviewing Week 11 inference benchmarks and discovering that the observed speedup could not be defended purely through parameter-count arguments.

---

# Public Artifacts

## Blog Post

(To be added after publishing)

* Medium:

  [Insert Medium URL here]

---

## Thread

(To be added after publishing)

* X / Twitter / LinkedIn:

  [Insert thread URL here]

---

# Experimental Work

The repository includes:

* merged vs. unmerged LoRA inference benchmarking,
* latency and throughput measurement,
* inference-phase decomposition methodology,
* profiling-oriented benchmark scripts.

Core benchmark:

* `pair_DAY1/code/profile_lora_merge.py`

Observed benchmark result:

| Variant       | Latency | Tokens/sec |
| ------------- | ------- | ---------- |
| Base Model    | 39.386s | 3.25 tok/s |
| Unmerged LoRA | 42.590s | 3.01 tok/s |
| Merged LoRA   | 39.670s | 3.23 tok/s |

Key finding:

* LoRA merging alone restored baseline inference efficiency but explained only a fraction of the original 2.41× end-to-end speedup.
* The remaining gain likely came from optimized inference-stack behaviors such as Flash Attention, fused kernels, quantized execution paths, and graph-level runtime optimizations.

---

# Canonical Sources

Primary references used during the investigation:

1. Hu et al. — LoRA: Low-Rank Adaptation of Large Language Models
2. Dao et al. — FlashAttention
3. Hugging Face PEFT Documentation
4. Unsloth Documentation

Full citations are available in:

* `pair_DAY1/sources.md`

---

# Grounding Commit

The Week 12 investigation resulted in updates to prior Week 11 portfolio artifacts, specifically:

* revised inference-performance explanations,
* corrected mechanism attribution,
* improved latency decomposition reasoning.

See:

* `pair_DAY1/grounding_commit.md`

---

# Key Learning Outcome

The most important insight from this cycle was:

> inference performance is determined not only by parameter count, but by runtime execution structure.

Merged and unmerged LoRA models may contain equivalent learned behavior while exhibiting different latency profiles due to:

* dynamic adapter application,
* memory-access patterns,
* kernel fusion compatibility,
* quantized execution efficiency,
* and decode-phase overhead accumulation.
