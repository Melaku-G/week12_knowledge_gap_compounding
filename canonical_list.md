# Canonical Reading & Tool List

This document summarizes the papers, tools, frameworks, and engineering patterns that proved most valuable throughout the Pair Day investigations.

---

# Inference & Runtime Mechanics

## FlashAttention
Paper:
- Dao et al. (2022)
- https://arxiv.org/abs/2205.14135

Why it matters:
- Reduces memory bandwidth bottlenecks in transformer attention.
- Critical for understanding modern inference optimization stacks.

---

## FlashAttention-2
Paper:
- Dao (2023)
- https://arxiv.org/abs/2307.08691

Why it matters:
- Improved GPU parallelism and inference throughput.
- Important for prefill/decode analysis.

---

## Hugging Face PEFT
Documentation:
- https://huggingface.co/docs/peft/index

Why it matters:
- Canonical implementation of LoRA adapters and merge workflows.

---

## Unsloth
Documentation:
- https://docs.unsloth.ai/

Why it matters:
- Demonstrates how runtime optimization stacks combine:
  - kernel fusion,
  - quantization,
  - and inference graph optimizations.

---

# Agent Systems & Tool Use

## ReAct
Paper:
- Yao et al. (2022)
- https://arxiv.org/abs/2210.03629

Why it matters:
- Foundational reasoning + acting framework for tool-using agents.

---

## Toolformer
Paper:
- Schick et al. (2023)
- https://arxiv.org/abs/2302.04761

Why it matters:
- Shows how models learn API/tool invocation behavior.

---

## LangGraph
Framework:
- https://www.langchain.com/langgraph

Why it matters:
- Strong abstraction for stateful multi-step agent execution.

---

## Guardrails AI
Framework:
- https://www.guardrailsai.com/

Why it matters:
- Useful for schema validation and tool-call reliability.

---

# LoRA & Post-Training Mechanics

## LoRA
Paper:
- Hu et al. (2021)
- https://arxiv.org/abs/2106.09685

Why it matters:
- Foundational PEFT method used throughout the Week 11 work.

---

## QLoRA
Paper:
- Dettmers et al. (2023)
- https://arxiv.org/abs/2305.14314

Why it matters:
- Combines quantization and low-rank adaptation efficiently.

---

## Intrinsic Dimensionality
Paper:
- Aghajanyan et al. (2020)
- https://arxiv.org/abs/2012.13255

Why it matters:
- Explains why low-rank adaptation works despite massive model size.

---

# Evaluation & Statistics

## Bootstrap Methods
Book:
- Efron & Tibshirani (1993)

Why it matters:
- Canonical reference for bootstrap confidence intervals and resampling.

---

## Statistical Significance in NLP
Paper:
- Dror et al. (2018)
- https://aclanthology.org/P18-1128/

Why it matters:
- Clarifies significance testing pitfalls in ML evaluation.

---

## CheckList
Paper:
- Ribeiro et al. (2020)
- https://aclanthology.org/2020.acl-main.442/

Why it matters:
- Demonstrates behavioral testing beyond aggregate metrics.

---

## Benchmark Critique
Paper:
- Bowman & Dahl (2021)
- https://aclanthology.org/2021.naacl-main.190/

Why it matters:
- Shows why benchmark scores alone can be misleading.

---

# Most Valuable Engineering Patterns

## Prefill vs Decode Decomposition
Why it matters:
- Essential for understanding inference bottlenecks.

---

## Paired Bootstrap Evaluation
Why it matters:
- Reduces variance when comparing models on identical tasks.

---

## Schema-Constrained Tool Calling
Why it matters:
- Significantly improves agent reliability.

---

## Boundary-Focused Evaluation
Why it matters:
- Reveals failures hidden by aggregate benchmarks.

---

# Most Valuable Tools Used

- Claude Code
- Hugging Face PEFT
- PyTorch Profiler
- bitsandbytes
- Unsloth
- LangChain
- LangGraph
- tau2-bench evaluation workflows

These tools collectively strengthened:
- systems understanding,
- evaluation rigor,
- and deployment-oriented reasoning.
