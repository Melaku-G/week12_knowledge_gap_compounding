# Question

## Final Sharpened Question (Week 12 — Agent & Tool-Use Internals)

In a tau2-bench-style multi-tool agent workflow, how does the model transition from continued reasoning to tool invocation at the token level, and which guardrails — schema constraints vs stop conditions — most effectively reduce tool hallucination and invalid tool calls without introducing unacceptable latency?

---

## Why This Question Matters

Previous evaluation work measured:

* task success,
* and total latency.

However, it did not explain:

* *why* agents make incorrect tool decisions,
* or *where* latency actually accumulates.

This question targets the core mechanism:

* the decision boundary between reasoning and acting,
* and how system-level constraints reshape that behavior.

---

## Linked Artifacts

* Week 11 tau2-bench evaluation (`eval/baseline.md`)
* Agent loop implementation used in benchmarking
* Experimental setup comparing schema constraints and stop conditions

---

## Gap Identified

The agent was previously treated as a black box:

* no visibility into reasoning vs tool steps,
* no measurement of tool hallucination,
* no decomposition of loop behavior.

This question addresses that gap by:

* focusing on token-level decision dynamics,
* and connecting them to measurable system outcomes.

---

## Expected Outcome

Answering this question should enable:

* mechanism-level understanding of agent behavior,
* improved reliability through constraint design,
* and better latency optimization through loop control.
