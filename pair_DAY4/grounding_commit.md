# Grounding Commit

## Concrete Portfolio Update

This investigation produced a concrete revision to the Week 11 evaluation interpretation inside the benchmarking and ablation analysis workflow.

Previously, the evaluation pipeline treated:
- statistically significant benchmark gains,
- bootstrap confidence intervals,
- and paired bootstrap p-values

as primary evidence of judge improvement.

After the Pair Day 4 investigation, the evaluation interpretation was updated to explicitly distinguish:

- benchmark-level statistical stability,
from:
- deployment-level behavioral reliability.

The portfolio documentation was revised to clarify that:
- paired bootstrap p-values estimate uncertainty only under repeated resampling of the observed benchmark distribution,
- and statistically significant improvements do not guarantee robustness under deployment distribution shift.

---

## New Understanding Added

The investigation changed the interpretation of:

> “p=0.0127 proves the trained judge is reliably better”

into:

> “p=0.0127 shows the observed improvement is statistically stable under the benchmark sampling process, but does not establish deployment robustness or behavioral completeness.”

The updated understanding now explicitly acknowledges:
- benchmark sampling assumptions,
- hidden subgroup failures,
- deployment distribution mismatch,
- and the limitations of aggregate statistical evaluation.

---

## Related Artifacts

Artifacts examined during the investigation:

- `run_real_ablation.py`
- paired bootstrap evaluation outputs
- held-out 50-task benchmark comparisons
- judge accuracy difference calculations
- bootstrap confidence interval generation
- paired bootstrap p-value estimation logic

---

## Conceptual Revision Added to the Portfolio

The evaluation section now distinguishes between:

| Evaluation Property | What It Measures |
|---|---|
| Bootstrap p-value | Stability of metric difference under benchmark resampling |
| Confidence interval | Estimated sampling uncertainty |
| Benchmark accuracy | Average performance on sampled tasks |
| Deployment reliability | Robustness under real-world distribution shift |

This revision prevents statistical significance from being incorrectly interpreted as proof of deployment safety.
