# Question

## Final Sharpened Question (Week 12 — Training & Post-Training Mechanics)

In Week 11 I fine-tuned Qwen2.5-0.5B-Instruct using LoRA (rank=16, targeting only q_proj and v_proj). The adapter improved overall benchmark performance but consistently failed near the confidence≈0.50 boundary between phrasing tiers — a failure case the aggregate benchmark never exposed.

How do LoRA rank and target-module selection constrain which behavioral corrections are actually representable during fine-tuning, and why can those constraints produce failures near ambiguous decision boundaries while overall scores still appear strong?

---

## Why This Question Matters

The original evaluation focused on aggregate benchmark improvement and treated the adapter as successful because overall metrics increased.

However, closer inspection revealed systematic failures concentrated near ambiguous confidence thresholds. This exposed a gap between:
- benchmark-level improvement,
- and representational capability.

The question investigates whether the limitation is not data quality or optimization instability, but the representational constraints imposed by:
- low-rank adaptation,
- and selective module targeting.

---

## Linked Artifacts

- Week 11 LoRA fine-tuning pipeline
- Qwen2.5-0.5B-Instruct adapter configuration
- Benchmark evaluation outputs
- Confidence-tier classification behavior
- tau2-bench evaluation traces

---

## Gap Identified

The system previously measured:
- overall accuracy,
- latency,
- and benchmark success.

But it did not explain:
- why certain boundary cases systematically failed,
- or whether the adapter architecture itself limited what could be learned.

This question addresses that representational gap directly.

---

## Expected Outcome

Answering this question should clarify:
- how LoRA rank limits behavioral expressivity,
- why module targeting matters,
- and why aggregate benchmark gains can hide localized capability failures near ambiguous decision boundaries.
