# Sources

## Canonical Sources

1. Efron, B. & Tibshirani, R. (1993)
Bootstrap Methods and Their Application
https://www.cambridge.org/core/books/bootstrap-methods-and-their-application

Why it mattered:
- Canonical explanation of bootstrap resampling and confidence estimation.

---

2. Dror et al. (2018)
The Hitchhiker’s Guide to Testing Statistical Significance in NLP
https://aclanthology.org/P18-1128/

Why it mattered:
- Clarifies significance testing pitfalls in machine learning evaluation.

---

3. Ribeiro et al. (2020)
CheckList: Beyond Accuracy Behavioral Testing of NLP Models
https://aclanthology.org/2020.acl-main.442/

Why it mattered:
- Demonstrates why aggregate benchmark scores fail to capture behavioral reliability.

---

4. Bowman & Dahl (2021)
What Will it Take to Fix Benchmarking in Natural Language Understanding?
https://aclanthology.org/2021.naacl-main.190/

Why it mattered:
- Explains benchmark blind spots and distribution limitations.

---

## Tools Used

- Claude Code
- Bootstrap evaluation scripts
- tau2-bench evaluation workflow
- Python statistical resampling utilities

---

## Grounding Artifacts

The explainer was grounded against:
- `run_real_ablation.py`
- paired bootstrap evaluation outputs
- held-out benchmark comparisons between:
  - rule-based,
  - prompt-only,
  - and LoRA-trained judges.
