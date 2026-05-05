# Grounding Commit

Updated artifact:
`Week11/final_report.docx`

Section updated:
Inference Performance / Ablation Discussion

Changes made:

* Added explanation of why unmerged LoRA adapters increase inference latency despite relatively small parameter overhead.
* Clarified that the slowdown comes from runtime low-rank adapter application during transformer forward passes rather than from model-size increase alone.
* Added note that merging adapters with `merge_and_unload()` restores near-baseline throughput by removing dynamic adapter computations and recovering optimized inference execution paths.

Reason for change:
The original Week 11 report described inference latency differences empirically but did not explain the systems mechanism responsible for the slowdown. After researching and benchmarking merged versus unmerged LoRA inference, I can now defend the latency behavior in terms of transformer execution structure, memory access, and runtime adapter application overhead.
