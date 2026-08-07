# RNAOS Benchmark Accuracy and Energy Gap Analysis

## Purpose

This document analyzes the observed benchmark results from RNAOS Benchmark V1.

Observed results:

- Average Accuracy: 1.0
- Average F1 Score: 0.9725
- Average Energy Gap: 0.0

The purpose of this analysis is to understand why these results occurred and identify improvements for future RNAOS versions.

---

# Observed Benchmark Behavior

The benchmark results show:

400 experiments completed

Accuracy:

1.0

Energy Gap:

0.0

Initial inspection of experiment outputs shows examples where:

RNAOS structure matches the reference structure.

Example:

RNAOS structure:

...(((...)))........

Reference structure:

...(((...)))........

RNAOS energy:

-3.0

Reference energy:

-3.0

This indicates that RNAOS predictions exactly match the classical reference MFE structures for these benchmark cases.

---

# Why Accuracy Is 1.0

The accuracy metric measures structural agreement between:

RNAOS predicted structure

and

ViennaRNA reference MFE structure.

When:

RNAOS structure == Reference structure

the calculated accuracy becomes:

Accuracy = 1.0

Therefore, the perfect accuracy indicates successful reproduction of the reference benchmark structures.

---

# Why Energy Gap Is 0.0

Energy gap is calculated as:

Energy Gap = RNAOS Energy - Reference Energy

Example:

RNAOS Energy:

-3.0

Reference Energy:

-3.0

Calculation:

Energy Gap = -3.0 - (-3.0)

Energy Gap = 0.0

The zero energy gap occurs because the selected RNAOS structures have identical energies to the ViennaRNA MFE reference structures.

---

# Interpretation

The current benchmark demonstrates:

- RNAOS can reproduce classical MFE structures.
- The validation pipeline correctly compares structures and energies.
- The framework can generate reproducible benchmark evidence.

However, the benchmark does not yet measure:

- independent discovery of structures
- optimization improvement from initial candidates
- convergence behavior
- search efficiency compared with classical baselines

---

# Current Benchmark Limitation

The current benchmark is primarily a structure recovery benchmark.

Current workflow:

RNA Sequence

↓

Reference MFE Structure

↓

RNAOS Candidate Evaluation

↓

Comparison

Because the reference structure is already known, the benchmark can produce perfect agreement.

---

# Future Benchmark Design

Future RNAOS benchmarks should introduce independent optimization evaluation.

Improved workflow:

RNA Sequence

↓

Initial Candidate Structures

↓

RNAOS Optimization Engine

↓

Energy Evaluation

↓

Comparison Against ViennaRNA MFE

Future metrics:

- initial candidate energy
- optimized candidate energy
- final energy gap
- convergence rate
- runtime efficiency
- search quality

---

# Research Conclusion

RNAOS Benchmark V1 successfully validates the reproducibility of the RNAOS evaluation framework.

The observed:

Accuracy = 1.0

Energy Gap = 0.0

results are explained by exact agreement between RNAOS outputs and classical MFE reference structures.

Future RNAOS versions should extend validation toward independent optimization experiments to evaluate search capability rather than only structure recovery.
