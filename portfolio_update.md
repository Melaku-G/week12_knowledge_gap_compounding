# Portfolio Update — Weeks 10 & 11

## Overview

Across Weeks 10 and 11, I worked on two connected systems:

- a tau2-bench-style conversion engine evaluation workflow,
- and a domain-specific adaptation workflow built around LoRA fine-tuning and agent evaluation.

Initially, my portfolio focused primarily on:
- benchmark outcomes,
- ablation metrics,
- and implementation completion.

The Pair Day investigations significantly deepened the technical rigor behind those artifacts by exposing hidden assumptions inside:
- inference systems,
- agent execution,
- post-training adaptation,
- and evaluation methodology.

The result is a substantially stronger portfolio grounded not only in implementation, but also in systems-level reasoning and evaluation integrity.

---

# Pair Day 1 — Inference-Time Mechanics

The first investigation focused on a major inference claim inside the Week 11 benchmark artifacts:

> how could a LoRA-adapted model achieve large inference speedups despite identical merged parameter counts?

The original benchmark observed:
- substantial latency differences,
- but did not explain the underlying mechanism.

The investigation decomposed inference into:
- prefill,
- decode,
- KV-cache behavior,
- kernel fusion,
- and quantization effects.

A controlled benchmark comparing:
- base,
- unmerged LoRA,
- and merged LoRA

demonstrated that:
- unmerged adapters introduce per-token runtime overhead,
- while merging primarily restores baseline execution efficiency rather than creating “free” speedups.

This strengthened the portfolio by:
- grounding benchmark claims experimentally,
- improving latency interpretation,
- and separating architectural mechanisms from framework-level optimizations.

---

# Pair Day 2 — Agent and Tool-Use Internals

The second investigation examined how multi-tool agents transition from:
- reasoning,
- to tool invocation,
- to loop termination.

The original system relied heavily on prompt-level orchestration but lacked a mechanistic explanation for:
- tool hallucination,
- invalid tool calls,
- and reliability tradeoffs.

The investigation analyzed:
- schema constraints,
- stop conditions,
- validation layers,
- and guardrail design.

This produced a clearer understanding that:
- reliability in agent systems depends less on raw model intelligence,
- and more on execution constraints and state-management structure.

The portfolio improved by:
- reframing agent reliability as a systems-design problem,
- clarifying tool orchestration mechanics,
- and introducing stronger evaluation reasoning for multi-step workflows.

---

# Pair Day 3 — Training & Post-Training Mechanics

The third investigation focused on LoRA representational limits.

The central question emerged from a Week 11 observation:
- the adapter improved aggregate benchmark performance,
- yet consistently failed on confidence-boundary cases.

The investigation analyzed:
- LoRA rank,
- target-module selection,
- representational subspaces,
- and boundary-sensitive behavior.

The major insight was that:
- low-rank adapters can achieve strong global benchmark performance,
- while remaining structurally incapable of expressing certain localized behavioral corrections.

This distinction between:
- optimization failure,
and:
- representational failure

substantially improved the interpretability of the original benchmark results.

The portfolio was strengthened by:
- adding architectural reasoning behind observed failures,
- improving understanding of post-training constraints,
- and explicitly acknowledging benchmark blind spots.

---

# Pair Day 4 — Evaluation & Statistical Interpretation

The fourth investigation focused on bootstrap significance testing inside the evaluation pipeline.

The original benchmark used:
- paired bootstrap confidence intervals,
- and paired bootstrap p-values

to compare:
- rule-based,
- prompt-only,
- and LoRA-trained judges.

The investigation clarified:
- what the paired bootstrap physically computes,
- what statistical significance actually establishes,
- and why statistically significant improvements do not guarantee deployment reliability.

The major insight was:

> statistical significance measures stability under the benchmark sampling process — not universal behavioral correctness.

This investigation fundamentally improved the evaluation rigor of the portfolio by:
- separating benchmark stability from deployment robustness,
- exposing hidden distribution assumptions,
- and reframing p-values as measurement tools rather than reliability guarantees.

---

# Collective Impact Across the Portfolio

Together, the five grounding commits transformed the Weeks 10 and 11 portfolio from:
- implementation-focused benchmarking,

into:
- mechanism-aware systems analysis.

The portfolio now demonstrates stronger capability in:
- inference optimization reasoning,
- agent reliability engineering,
- post-training representational analysis,
- and statistical evaluation interpretation.

Most importantly, the investigations reinforced a core engineering lesson:

> benchmark success alone is insufficient without understanding the systems assumptions underneath the benchmark.

The revised portfolio therefore reflects not only the ability to build AI systems, but also the ability to:
- interrogate their assumptions,
- identify hidden failure modes,
- and evaluate them rigorously under deployment-oriented thinking.

That shift significantly improved the technical maturity and defensibility of the Weeks 10 and 11 work.
