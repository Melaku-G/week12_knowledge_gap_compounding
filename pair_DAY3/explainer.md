# When Benchmarks Lie: LoRA Rank, Target Modules, and Hidden Behavioral Failures

## Overview

A LoRA adapter can improve benchmark scores while still failing in highly specific behavioral regions.

In Week 11, a Qwen2.5-0.5B-Instruct model fine-tuned with:
- rank = 16
- targeting only q_proj and v_proj

showed strong aggregate improvement, yet repeatedly failed near the confidence≈0.50 boundary separating phrasing tiers.

This exposed a deeper question:

> Can a low-rank adapter actually represent all the behavioral corrections required by the task?

This explainer argues that the failure is not simply a training issue, but a representational constraint imposed by:
- LoRA rank,
- and selective module targeting.

---

# 1. What LoRA Actually Learns

LoRA does not modify the full transformer weight matrix directly.

Instead, it learns a low-rank update:

\[
\Delta W = BA
\]

where:
- \(A \in \mathbb{R}^{r \times d}\)
- \(B \in \mathbb{R}^{d \times r}\)
- \(r\) = LoRA rank

The effective weight becomes:

\[
W' = W + BA
\]

This means the model is not free to learn arbitrary corrections.

It can only learn corrections expressible within a rank-\(r\) subspace.

---

# 2. Why Rank Matters

Rank controls the dimensionality of behavioral change.

A higher rank:
- allows more independent behavioral directions,
- increases expressive flexibility,
- and approximates full fine-tuning more closely.

A low rank compresses all corrections into a small subspace.

This works surprisingly well because:
- transformer representations are highly redundant,
- and many downstream tasks require only small directional adjustments.

However, not all behaviors are equally compressible.

---

# 3. Boundary Failures Are Harder Than Average Cases

The observed failures occurred near confidence≈0.50 boundaries.

These are difficult because:
- examples are semantically ambiguous,
- small representation shifts change classification outcome,
- and decision surfaces become highly sensitive.

Most benchmark examples lie far from the boundary:
- easy positives,
- easy negatives.

These require only coarse behavioral adjustment.

Boundary cases require:
- fine-grained representation reshaping,
- and higher local precision.

A low-rank adapter may improve global behavior while lacking the expressive capacity needed for these localized corrections.

---

# 4. Why q_proj and v_proj Matter

The adapter targeted only:
- q_proj
- v_proj

inside attention layers.

This constrains *where* behavioral change can occur.

---

## q_proj

Controls:
- query representations,
- attention selection patterns,
- token relevance routing.

Updating q_proj changes:
> what the model attends to.

---

## v_proj

Controls:
- value representations passed through attention.

Updating v_proj changes:
> what information is transmitted.

---

## What Was Not Updated

The adapter did not modify:
- k_proj,
- o_proj,
- MLP layers,
- layer norms.

This matters because:
- some behavioral corrections require modifying representation transformation,
- not just attention routing.

Boundary calibration may require coordinated changes across:
- attention,
- feature synthesis,
- and output geometry.

Restricting updates to q_proj and v_proj may leave the model unable to fully reshape those decision surfaces.

---

# 5. Why Aggregate Benchmarks Hide This

Benchmarks average performance across all examples.

This creates a masking effect:
- large improvements on easy cases dominate,
- localized failures contribute little to aggregate score.

As a result:

\[
\text{Strong average performance} \neq \text{uniform behavioral competence}
\]

The model can:
- appear improved overall,
- while remaining systematically weak in narrow behavioral regions.

---

# 6. Representational Failure vs Optimization Failure

This distinction is critical.

An optimization failure means:
> the model could learn the behavior but training failed.

A representational failure means:
> the architecture cannot express the correction efficiently within its constraints.

The evidence suggests the observed boundary issue is closer to representational failure because:
- the failure remained consistent,
- aggregate learning succeeded,
- and the problematic region was highly localized.

---

# 7. The Real Tradeoff of LoRA

LoRA succeeds because:
- most downstream adaptation lies in a low-dimensional subspace.

But the tradeoff is:

> efficiency is purchased by restricting representational freedom.

Low-rank adapters are extremely parameter-efficient, but:
- fine-grained behavioral calibration,
- compositional reasoning,
- and boundary-sensitive decisions

may require updates outside the accessible subspace.

---

# Conclusion

The Week 11 benchmark initially suggested the adapter was fully successful.

Closer inspection revealed something more important:
- the adapter improved average behavior,
- but failed precisely where nuanced calibration mattered most.

This failure was not necessarily caused by poor optimization or insufficient data.

Instead, it likely emerged from the interaction between:
- low-rank representational limits,
- and restricted target-module coverage.

The key lesson is:

> Benchmark improvement does not prove behavioral completeness.

A model can score well globally while remaining structurally incapable of expressing certain local corrections.

Understanding that distinction is essential for evaluating post-training systems honestly.

# sources
Hu et al. (2021) — LoRA: Low-Rank Adaptation of Large Language Models https://arxiv.org/abs/2106.09685

Aghajanyan et al. (2020) — Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning https://arxiv.org/abs/2012.13255

Dettmers et al. (2023) — QLoRA: Efficient Finetuning of Quantized LLMs https://arxiv.org/abs/2305.14314

Dao et al. (2022) — FlashAttention https://arxiv.org/abs/2205.14135

Vaswani et al. (2017) — Attention Is All You Need https://arxiv.org/abs/1706.03762

Anthropic — Transformer Circuits https://transformer-circuits.pub/
