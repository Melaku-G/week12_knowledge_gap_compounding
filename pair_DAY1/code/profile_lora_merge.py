# code/profile_lora_merge.py

import gc
import json
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
# --------------------------------------------------
# CONFIG
# --------------------------------------------------

LORA_PATH = os.path.abspath("lora_adapter")

# CPU-friendly base model.
# Do not use the adapter's recorded Unsloth 4-bit base on CPU,
# because it requires bitsandbytes.
BASE_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"

PROMPT = """
You are an enrichment operations assistant.
Summarize the following CRM enrichment workflow
and propose improvements for latency reduction.
"""

MAX_NEW_TOKENS = 128
WARMUP_RUNS = 1
BENCHMARK_RUNS = 3

DEVICE = "cpu"
DTYPE = torch.float32
DEVICE_MAP = None


# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def synchronize():
    if DEVICE == "cuda":
        torch.cuda.synchronize()


def reset_memory_stats():
    if DEVICE == "cuda":
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
    gc.collect()


def benchmark_generation(model, tokenizer, label):
    reset_memory_stats()

    inputs = tokenizer(PROMPT, return_tensors="pt").to(DEVICE)

    # Warmup
    for _ in range(WARMUP_RUNS):
        with torch.inference_mode():
            _ = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )

    synchronize()

    latencies = []
    tokens_generated = []

    for _ in range(BENCHMARK_RUNS):
        start = time.perf_counter()

        with torch.inference_mode():
            outputs = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )

        synchronize()

        end = time.perf_counter()

        generated_tokens = outputs.shape[1] - inputs["input_ids"].shape[1]

        latencies.append(end - start)
        tokens_generated.append(generated_tokens)

    avg_latency = sum(latencies) / len(latencies)
    avg_tokens = sum(tokens_generated) / len(tokens_generated)
    tokens_per_second = avg_tokens / avg_latency

    print("\n" + "=" * 60)
    print(label)
    print("=" * 60)
    print(f"Average latency: {avg_latency:.3f}s")
    print(f"Average generated tokens: {avg_tokens:.1f}")
    print(f"Tokens/sec: {tokens_per_second:.2f}")

    if DEVICE == "cuda":
        memory_mb = torch.cuda.max_memory_allocated() / 1024**2
        print(f"Peak GPU memory: {memory_mb:.2f} MB")

    return {
        "label": label,
        "avg_latency": avg_latency,
        "tokens_per_second": tokens_per_second,
    }


# --------------------------------------------------
# LOAD TOKENIZER
# --------------------------------------------------

print(f"Using base model: {BASE_MODEL}")
print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# --------------------------------------------------
# LOAD BASE MODEL ONCE
# --------------------------------------------------

print("\nLoading base model once...")

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    dtype=DTYPE,
    device_map=DEVICE_MAP,
)

base_model.eval()

# --------------------------------------------------
# 1. BASE MODEL
# --------------------------------------------------

base_results = benchmark_generation(
    base_model,
    tokenizer,
    "BASE MODEL",
)

# --------------------------------------------------
# 2. UNMERGED LORA
# --------------------------------------------------

print("\nAttaching LoRA adapter to existing base model...")

lora_model = PeftModel.from_pretrained(
    base_model,
    LORA_PATH,
)

lora_model.eval()

unmerged_results = benchmark_generation(
    lora_model,
    tokenizer,
    "UNMERGED LORA",
)

# --------------------------------------------------
# 3. MERGED LORA
# --------------------------------------------------

print("\nMerging adapter weights into existing model...")

merged_model = lora_model.merge_and_unload()
merged_model.eval()

merged_results = benchmark_generation(
    merged_model,
    tokenizer,
    "MERGED LORA",
)

# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------

print("\n" + "#" * 60)
print("FINAL COMPARISON")
print("#" * 60)

all_results = [
    base_results,
    unmerged_results,
    merged_results,
]

for r in all_results:
    print(
        f"{r['label']:20s} | "
        f"{r['avg_latency']:.3f}s | "
        f"{r['tokens_per_second']:.2f} tok/s"
    )

print("\nDone.")
