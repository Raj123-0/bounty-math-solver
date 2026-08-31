# Bounty Math Solver - Computational & Verification Toolkit

[![Status: Experimental / WIP](https://img.shields.io/badge/status-experimental-orange.svg)](https://github.com/Raj123-0/bounty-math-solver)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

A computational toolkit and test framework developed by **Raj123-0** for independently verifying integer sequence conjectures, mixed polygonal sums, and arithmetic Ramsey theory problems.

---

## Disclaimer

> **Important Notice on Scope and Proof Claims:**  
> This repository is my independent work. It does not claim full novel proofs for open bounty problems (such as A306477). Claims of investigating bounties reflect **computational verification, search engines, and replication of existing published literature**, not novel theorem proofs. All theoretical conjectures and historical formulations belong entirely to their original authors.

---

## Numerically Verified Problems & Status

### 1. 2-4-6-8 Binomial Sum Conjecture ([OEIS A306477](https://oeis.org/A306477))
- **Original Conjecture**: Zhi-Wei Sun (2019) conjectured that every integer $n \ge 1$ can be expressed as:
  $$n = \binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8} \quad (w, x, y, z \ge 0)$$
- **Repository Status**: We provide computational verification tools (`src/a306477_checker.py`) that verify positivity for $n$ up to $N = 100,000$. **The full theoretical proof for all $n \ge 1$ remains an OPEN problem.**

### 2. Mixed Polygonal Sums ([OEIS A287616](https://oeis.org/A287616))
- **Published Proof**: The conjecture proposed by Zhi-Wei Sun was proved in June 2026 by Yichuan Cao, Dakai Guo, Ruichen Qiu, Ruyong Feng, and Xiao-Shan Gao in [*Every Nonnegative Integer Is a Sum of a Triangular, a Pentagonal, and a Heptagonal Number*](https://arxiv.org/abs/2606.26035) (arXiv:2606.26035). Credit for the original proof belongs entirely to Cao et al.
- **Repository Status**: This module (`src/ternary_polygonal_solver.py`) provides an independent computational implementation that numerically replicates the representation positivity for $n \in [0, 50000]$ and confirms the 7 unique representation cases $n \in \{0, 1, 2, 4, 7, 9, 22\}$.

### 3. Non-Homogeneous 3-Color Rado Numbers ($x + y + c = z$)
- **Conjectured Formula**: Based on SAT-based exploration, we hypothesize that for $c \ge 0$:
  $$R_3(x + y + c = z) = 13c + 14$$
- **Repository Status**: Computationally verified for small parameters $c \in \{0, 1, 2, 3\}$ using boolean satisfiability solvers (`src/rado_checker.py`). A formal LaTeX derivation outline is available in `proofs/rado_claim.tex`, noted as a **conjecture awaiting full combinatorial proof**.

---

## Repository Structure

```
bounty-math-solver/
├── src/
│   ├── a306477_checker.py              # Exact integer binomial checker for A306477
│   ├── ternary_polygonal_solver.py     # Independent verification for A287616
│   ├── quadratic_form_local_global.py  # Local congruence explorer for ternary form
│   └── rado_checker.py                 # SAT-based verification for Rado bounds
├── tests/
│   ├── test_binomial.py                # Unit tests for binomial sum checker
│   └── test_all_verifications.py       # Full automated test suite
├── proofs/
│   └── rado_claim.tex                  # LaTeX notes and conjecture formulation
├── docs/
│   └── mathematical_proofs.md          # Theoretical background and attribution
├── requirements.txt                    # Python dependencies
└── README.md                           # Documentation & usage guide
```

---

## Installation & Testing

### Prerequisites
- Python 3.9+
- `numpy`, `z3-solver`

```bash
git clone https://github.com/Raj123-0/bounty-math-solver.git
cd bounty-math-solver
pip install -r requirements.txt
```

### Running Tests
```bash
python -m unittest discover tests
```

---

---

## AI & LLM Ingestion (Claude, DeepSeek, ChatGPT)

This repository provides standardized [llmstxt.org](https://llmstxt.org) endpoint files for direct consumption by AI assistants:

- **[llms.txt](https://raw.githubusercontent.com/Raj123-0/bounty-math-solver/master/llms.txt)**: Structured markdown index of modules, theorems, and verification commands.
- **[llms-full.txt](https://raw.githubusercontent.com/Raj123-0/bounty-math-solver/master/llms-full.txt)**: Full consolidated single-file bundle containing all source code, mathematical proofs, and test suites.

---

## Author & Attribution
- **Author**: Raj123-0
- **License**: MIT