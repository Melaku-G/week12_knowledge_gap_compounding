# Week 12 — Pair Day 3: Training & Post-Training Mechanics

## Overview

This repository contains my Pair Day 3 investigation into:
- LoRA representational limits,
- target-module selection,
- and hidden behavioral failures during post-training.

The work was motivated by a Week 11 observation where a LoRA adapter improved aggregate benchmark performance while still failing consistently near a confidence boundary between phrasing tiers.

The investigation explores whether those failures emerged not from optimization instability, but from representational constraints imposed by:
- low-rank adaptation,
- and restricted module targeting.

---

# Core Question

> How do LoRA rank and target-module selection constrain which behavioral corrections are representable during fine-tuning, and why can low-rank adapters maintain benchmark performance while still failing near ambiguous decision boundaries?

---

# Key Insight

Strong benchmark performance does not guarantee:
- uniform behavioral competence,
- or complete representational flexibility.

Low-rank adapters can improve global behavior while remaining structurally incapable of expressing certain localized corrections.

---

# Main Findings

- LoRA rank constrains behavioral expressivity into a limited subspace
- q_proj and v_proj targeting modifies attention routing but not full representation transformation
- Boundary-sensitive behaviors require finer representational calibration than average benchmark cases
- Aggregate metrics can mask systematic localized failures

---

# Repository Structure

```text
DAYN/
├── question.md
├── explainer.md
├── morning_call_summary.md
├── evening_call_summary.md
├── signedoff.md
├── sources.md
└── README.md
