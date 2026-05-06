# Grounding Commit

## Updated Artifact

Week 11 — tau2-bench evaluation (`eval/baseline.md` and final report sections on agent performance)

---

## What Was Missing Before

The original Week 11 evaluation measured:

* total latency across multi-step agent workflows
* task success rates

However, it treated the agent loop as a black box. Specifically:

* Tool calls were not distinguished from reasoning steps
* No tracking existed for invalid or hallucinated tool invocations
* Latency was reported only as aggregate wall-clock time
* No explanation was provided for why agents made incorrect tool decisions

As a result, the evaluation described *what happened*, but not *why it happened*.

---

## What Was Added

Based on the Week 12 investigation into agent and tool-use internals, I introduced the following changes:

### 1. Step-Level Logging

Each agent step is now recorded with:

* step type (reasoning vs tool call)
* tool name (if invoked)
* validity (correct / incorrect / malformed)
* per-step latency

This enables direct observation of the agent’s internal control flow.

---

### 2. Tool Call Quality Metrics

Added new evaluation metrics:

* tool hallucination rate (% invalid tool calls)
* valid tool call rate
* tool calls per task

This shifts evaluation from output-only correctness to **decision quality**.

---

### 3. Latency Decomposition

Latency is now broken into:

* number of steps per task
* number of tool calls
* average step latency

This reveals whether slow runs are caused by:

* excessive reasoning,
* unnecessary tool calls,
* or loop inefficiencies.

---

### 4. Guardrail Evaluation Framework

Introduced controlled comparison of:

* schema constraints (weak vs strict JSON)
* stop conditions (none vs bounded / early stop)

This allows measuring how constraints affect:

* hallucination rate
* task success
* total latency

---

## Why This Matters

This grounding change converts the agent evaluation from:

```text
black-box benchmarking
```

to:

```text
mechanism-aware analysis
```

Instead of asking:

> Did the agent succeed?

the evaluation now asks:

> How did the agent decide, and where did it fail?

---

## Resulting Insight

The updated evaluation shows that:

* Many failures originate at the **reason → tool decision boundary**
* Weak schemas increase invalid tool calls
* Missing stop conditions inflate latency through unnecessary loops

This directly informs how to design more reliable and efficient agent systems.

---

## Linked Changes

* Updated evaluation logic in tau2-bench workflow
* Added step-level logging to agent loop
* Added metrics computation for tool-call quality
* Integrated guardrail configurations into experiment pipeline

---

## Summary

Week 12 transformed the evaluation from measuring outcomes to understanding mechanisms. The agent is no longer treated as a black box — its internal decisions are now observable, measurable, and optimizable.
