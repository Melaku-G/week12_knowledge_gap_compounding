In my Week 11 ablation (`bench/ablations/ablation_results.json`), the LoRA-adapted Qwen2.5-1.5B model achieves a 2.41× inference speedup (2.98s vs 7.17s) after `FastLanguageModel.for_inference(model)` is applied, even though the LoRA weights are merged and the final parameter count is unchanged from the base model.

What inference-time mechanisms actually produce this speedup, and how can the gain be experimentally decomposed across prefill vs decode phases, fused attention kernels, quantization behavior, KV-cache usage, and memory-bandwidth effects?

Understanding this would let me revise the “Pareto dominance” claim in my final report from an empirical observation into a mechanism-defended systems explanation.
