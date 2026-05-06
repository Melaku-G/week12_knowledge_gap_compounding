# Sources

This explainer is based on a combination of canonical research papers, official documentation, and experimental validation.

---

## Canonical Papers

### 1. LoRA: Low-Rank Adaptation of Large Language Models

https://arxiv.org/abs/2106.09685

* Introduces LoRA as a parameter-efficient fine-tuning method
* Provides the mathematical foundation for low-rank updates
* Relevant for understanding how adapter-based systems interact with inference behavior

---

### 2. FlashAttention: Fast and Memory-Efficient Exact Attention

https://arxiv.org/abs/2205.14135

* Explains memory-bound vs compute-bound phases in transformer inference
* Helps contextualize latency tradeoffs in agent loops

---

### 3. ReAct: Synergizing Reasoning and Acting in Language Models

https://arxiv.org/abs/2210.03629

* Introduces the reasoning + acting loop used in modern agents
* Directly relevant to understanding the decision boundary between reasoning and tool use

---

## Documentation & Systems References

### 4. LangChain Documentation

https://python.langchain.com/

* Provides abstractions for agent loops and tool calling
* Used for implementing the experimental setup

---

### 5. Hugging Face PEFT Documentation

https://huggingface.co/docs/peft

* Describes adapter merging and inference behavior
* Relevant background for understanding structured outputs and tool schemas

---

### 6. OpenAI Function Calling / Tool Use Docs

https://platform.openai.com/docs

* Explains structured tool invocation formats
* Informs schema constraint design and JSON tool-call enforcement

---

## Supporting Concepts

### 7. Prefill vs Decode

* Prefill: full prompt processing (compute-bound)
* Decode: token-by-token generation (memory-bound)
* Important for understanding latency accumulation in agent loops

---

### 8. KV Cache

* Stores intermediate attention states across tokens
* Relevant for understanding repeated reasoning steps in agent loops

---

## Experimental Methodology

In addition to literature, the following were used:

* Custom agent loop implementation (Python + LangChain)
* Controlled experiments across:

  * schema constraints (weak vs strict)
  * stop conditions (none vs bounded)
* Metrics:

  * hallucination rate
  * tool-call validity
  * latency and step count

This combination of:

* canonical theory
* system documentation
* and direct experimentation

ensures that conclusions are grounded in both research and observed behavior.

---

## Summary

The explanation of agent tool-use internals is not derived from a single source, but from the intersection of:

* reasoning-acting frameworks (ReAct),
* structured output systems (function calling),
* and empirical observation of agent execution loops.

This multi-source grounding is necessary to move from surface-level behavior to mechanism-level understanding.
