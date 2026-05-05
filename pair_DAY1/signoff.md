# Sign-Off

Status: CLOSED

Before this explainer, I understood empirically that LoRA-adapted models could run slower during inference, but I could not explain the mechanism responsible for the slowdown or why merging restored performance. I treated the effect as a tooling artifact rather than a transformer execution issue.

The explainer clarified that the key distinction is between dynamically applying low-rank adapter updates during every forward pass versus folding those updates directly into the transformer weights before inference. I now understand how unmerged adapters introduce additional matrix operations, memory reads, and reduced kernel-fusion opportunities during autoregressive decoding.

The benchmark comparing base, unmerged, and merged LoRA inference made the mechanism concrete and connected the explanation directly to measurable runtime behavior rather than abstract claims.


# Sign-Off

Status: CLOSED WITH REVISIONS

The explainer successfully clarified the core inference-time mechanisms behind LoRA-related latency changes, especially the distinction between prefill and decode phases, the role of runtime adapter application, and why merged adapters restore near-baseline inference behavior.

The strongest improvement was the systems-level decomposition across quantization, kernel fusion, KV-cache behavior, and decode-time overhead. Before this explainer, I treated the observed speedup primarily as a tooling artifact and could not connect it to transformer execution structure.

However, after independently benchmarking merged versus unmerged LoRA inference, I observed only an ~8% throughput difference between the two configurations. This suggests that LoRA merge overhead alone likely does not explain the full 2.41× speedup originally observed in the Week 11 ablation.

I therefore think the explainer would be stronger if it more clearly separated:

* LoRA adapter overhead removal,
* optimized inference kernels,
* quantized execution paths,
* and other runtime optimizations inside `FastLanguageModel.for_inference()`.

Overall, the conceptual gap was substantially closed, but the attribution of the full speedup mechanism still requires more careful experimental isolation.
