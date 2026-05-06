Q1. In my ablation, FastLanguageModel.for_inference() produces a 2.41× speedup even though LoRA weights are merged and the parameter count is unchanged — what operations are actually fused or optimized, and at which phase (prefill vs decode) does the speedup concentrate?
Q2. My tau2-bench p95 latency is 347s for a 15-step agent loop. If I decompose that wall-clock time into prefill cost, decode cost, API RTT, and tool execution, which component dominates — and how does that change the right optimization target?

Q3. At seq_len=1024 on a T4 (16 GB), what is the actual KV cache memory footprint for Qwen2.5-1.5B — and how does that constrain the batch size available during inference, vs during training?

Q4. I set max_new_tokens=300 but cannot decompose 2.98s into prefill vs decode phases. How does the prefill/decode cost ratio change with input length — and what does that imply for the cost of running the adapter at inference time on longer enrichment briefs?