# Week 12 — Pair Day Cycle: Agent & Tool-Use Internals

## Overview

This repository contains my Week 12 pair-day submission focused on **agent and tool-use internals**, specifically investigating how large language models decide between continued reasoning and tool invocation in multi-step workflows.

The central goal was to move from **black-box evaluation** to **mechanism-level understanding** of agent behavior.

---

## Core Question

> In a tau2-bench-style multi-tool agent workflow, how does the model transition from continued reasoning to tool invocation at the token level, and which guardrails — schema constraints vs stop conditions — most effectively reduce tool hallucination and invalid tool calls without introducing unacceptable latency?

---

## Key Insight

Agents do not explicitly “decide” to call tools.

Instead, tool invocation emerges from a **token-level probability competition** between:

* natural language reasoning, and
* structured tool-call outputs.

Failures such as hallucinated tool calls are not purely reasoning errors — they are **generation-space failures** caused by insufficient constraints.

---

## What This Work Demonstrates

### 1. Agent Decision Boundary

* The transition from reasoning → tool call is a **probabilistic token-generation outcome**, not a discrete control step.

### 2. Guardrail Effects

* **Schema constraints** reduce invalid tool calls by restricting output space.
* **Stop conditions** reduce latency by limiting unnecessary loop iterations.

### 3. Reliability–Latency Tradeoff

* Weak constraints → flexible but error-prone and slow
* Strong constraints + stopping → most stable and efficient configuration

---

## Repository Structure

```text
DAYN/
├── question.md               # Final sharpened question
├── explainer.md              # Deep mechanism-level explanation
├── thread.md                 # Compressed 4–6 tweet version
├── morningcallsummary.md     # Question refinement summary
├── eveningcallsummary.md     # Feedback + revision summary
├── groundingcommit.md        # Changes applied to Week 10/11 artifacts
├── sources.md                # Canonical + practical references
├── agent_experiment.py       # Runnable experiment code
```

---

## Experiment Summary

A controlled experiment was conducted across four configurations:

| Schema | Stop Condition | Outcome                           |
| ------ | -------------- | --------------------------------- |
| Weak   | None           | High hallucination, long loops    |
| Strong | None           | Fewer errors, inefficient runtime |
| Weak   | Yes            | Faster but still error-prone      |
| Strong | Yes            | Best reliability–latency balance  |

### Metrics Collected

* Tool hallucination rate
* Valid tool call rate
* Steps per task
* Total latency

---

## Grounding Change (Week 11 → Week 12)

The original tau2-bench evaluation:

* measured only final success and latency,
* treated the agent loop as a black box.

This work adds:

* step-level logging (reasoning vs tool calls),
* tool-call validity tracking,
* latency decomposition by step,
* guardrail-based evaluation framework.

This transforms evaluation from:

> outcome measurement

to:

> mechanism-aware analysis

---

## How to Run the Experiment

```bash
python agent_experiment.py
```

Toggle configurations inside the script:

```python
USE_STRONG_SCHEMA = True / False
USE_STOP_CONDITION = True / False
```

Run all four combinations and compare metrics.

---

## Related Write-up

The full explainer expands on:

* token-level decision mechanics,
* generation-space constraints,
* and agent reliability design.

(If published externally, link here)

---

## Takeaway

Reliable agents are not achieved by better reasoning alone.

They emerge when:

* the output space is constrained,
* the execution loop is controlled,
* and decisions are made observable.

---

## Author

Week 12 Pair-Day Submission
Focus: Agent Systems, Inference Mechanics, Evaluation Design
