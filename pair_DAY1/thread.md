1/6

Why can a LoRA fine-tuned model run slower at inference time even when generation settings are identical?

I benchmarked:

* base model
* unmerged LoRA adapter
* merged LoRA adapter

…and found the slowdown comes from runtime execution overhead, not parameter count alone.

2/6

LoRA doesn’t replace the original transformer weights.

It learns a low-rank update:

ΔW = BA

During inference with an *unmerged* adapter, the model effectively computes:

W'x = Wx + BAx

for every forward pass through adapted layers.

That extra work happens at runtime.

3/6

Benchmark results from Qwen2.5-1.5B:

| Variant       | Latency | Tokens/sec |
| ------------- | ------- | ---------- |
| Base          | 39.386s | 3.25       |
| Unmerged LoRA | 42.590s | 3.01       |
| Merged LoRA   | 39.670s | 3.23       |

Unmerged adapters reduced throughput by ~8%.

4/6

Why does this happen?

Unmerged LoRA introduces:

* extra matrix multiplications
* extra memory reads
* reduced kernel fusion opportunities

Transformer inference is often memory-bandwidth-bound, so even small runtime overhead compounds during autoregressive decoding.

5/6

The standard fix is:

`merge_and_unload()`

This folds the learned LoRA update directly into the transformer weights before inference begins.

After merging:

* runtime adapter application disappears
* optimized kernels are restored
* throughput returns near baseline

6/6

Key insight:

Inference latency is not determined only by parameter count.

Runtime execution structure matters just as much:

* fused kernels
* memory movement
* decode loops
* KV-cache behavior

That was the actual mechanism hidden behind the slowdown.

Week 12 inference-time mechanics exploration.
