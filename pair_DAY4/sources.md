# Sources

## Canonical Papers

1. Hu et al. (2021) — LoRA: Low-Rank Adaptation of Large Language Models
https://arxiv.org/abs/2106.09685

2. Aghajanyan et al. (2020) — Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning
https://arxiv.org/abs/2012.13255

3. Dettmers et al. (2023) — QLoRA: Efficient Finetuning of Quantized LLMs
https://arxiv.org/abs/2305.14314

4. Dao et al. (2022) — FlashAttention
https://arxiv.org/abs/2205.14135

---

## Transformer & Representation References

5. Vaswani et al. (2017) — Attention Is All You Need
https://arxiv.org/abs/1706.03762

6. Anthropic — Transformer Circuits
https://transformer-circuits.pub/

---

## Practical Documentation

7. Hugging Face PEFT Documentation
https://huggingface.co/docs/peft

8. Unsloth Documentation
https://docs.unsloth.ai/

---

## Concepts Investigated

- Low-rank adaptation
- Representational subspaces
- Decision boundary sensitivity
- Attention projection layers
- Behavioral calibration
- Benchmark masking effects

---

## Experimental Grounding

This analysis was grounded in:
- Week 11 Qwen2.5-0.5B-Instruct LoRA experiments
- rank=16 adapter configuration
- q_proj + v_proj targeting
- benchmark evaluation traces
- confidence-boundary failure analysis
