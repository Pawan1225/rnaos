# RNAOS

## Quantum-Inspired Optimization for mRNA Secondary Structure Prediction

### WISER Global Quantum+AI Program 2026

### WISER <> Moderna Challenge

---

# Project Overview

RNAOS (RNA Optimization System) is a quantum-inspired hybrid optimization framework developed to investigate mRNA secondary structure prediction.

The project explores how optimization-based approaches can be used to search for low-energy RNA secondary structures while benchmarking against classical Minimum Free Energy (MFE) folding methods.

RNAOS combines:

- RNA structural constraints
- thermodynamic energy evaluation
- optimization-based candidate selection
- quantum resource estimation

The objective is not to claim quantum advantage, but to investigate how quantum-inspired optimization concepts can support future RNA folding research.

---

# Challenge Problem

mRNA secondary structure influences important biological properties including:

- molecular stability
- translation efficiency
- manufacturability

However, RNA folding is computationally challenging because a single RNA sequence can produce many possible secondary structures.

Classical tools such as ViennaRNA use dynamic programming and thermodynamic models to identify Minimum Free Energy structures.

The WISER <> Moderna challenge explores whether quantum or quantum-inspired optimization methods can help investigate this complex search problem.

---

# RNAOS Approach

RNAOS formulates RNA secondary structure prediction as a constrained optimization problem.

The workflow:

~~~text
RNA Sequence

      |

Candidate Structure Generation

      |

Biological Constraint Validation

      |

Energy Evaluation

      |

Energy-Aware Optimization

      |

Benchmark Comparison
~~~

The framework:

- generates candidate structures
- validates biological constraints
- evaluates thermodynamic energy
- compares against ViennaRNA references
- analyzes scaling behavior

---

# Methods Used

RNAOS investigated multiple approaches.

## Classical Methods

ViennaRNA was used for:

- MFE reference generation
- energy evaluation
- benchmark comparison

---

## AI Methods

AI approaches were considered for:

- learned structure representations
- candidate generation
- future optimization guidance

---

## Quantum and Quantum-Inspired Methods

Potential future formulations include:

- QAOA
- Variational Quantum Algorithms
- Quantum Annealing
- Tensor-network-inspired optimization

The final implementation uses a quantum-inspired optimization framework that can run on classical resources while remaining compatible with future quantum implementations.

---

# Experimental Validation

RNAOS was evaluated using:

~~~text
400 synthetic RNA benchmark sequences
~~~

Sequence lengths:

- 20 nucleotides
- 40 nucleotides
- 60 nucleotides
- 80 nucleotides

Evaluation metrics:

- structure accuracy
- F1 similarity score
- energy gap
- runtime scaling
- estimated quantum resources

---

# Key Results

## Structure Accuracy

Average accuracy:

~~~text
1.0
~~~

---

## Structural Similarity

Average F1 score:

~~~text
0.9725
~~~

---

## Energy Agreement

Average energy gap:

~~~text
0.0
~~~

---

## Quantum Resource Analysis

Maximum estimated qubit requirement:

~~~text
160 qubits
~~~

for 80 nucleotide RNA sequences.

These values represent resource estimation for future quantum implementations.

---

# Repository Structure

~~~text
wiser_submission/

├── benchmark_results/
│
├── scientific_analysis/
│
├── figures/
│
└── documentation/
~~~

---

# Documentation

Detailed project documentation:

- [Documentation Index](documentation/DOCUMENTATION_INDEX.md)
- [Problem Statement](documentation/01_problem_statement.md)
- [Background Review](documentation/02_background_review.md)
- [Solution Approach](documentation/03_solution_approach.md)
- [Methods and Tools](documentation/04_methods_and_tools.md)
- [Results and Findings](documentation/05_results_and_findings.md)
- [Limitations and Future Work](documentation/06_limitations_and_future_work.md)
- [Team Contribution](documentation/07_team_contribution.md)

---

# Evidence Package

## Benchmark Results

Contains:

- experiment results
- benchmark statistics
- execution metadata

Location:

~~~text
benchmark_results/
~~~

---

## Scientific Analysis

Contains:

- accuracy analysis
- energy gap analysis
- runtime scaling
- quantum resource analysis
- scientific report

Location:

~~~text
scientific_analysis/
~~~

---

## Figures

Contains:

- accuracy scaling
- energy distribution
- runtime scaling
- quantum resource scaling visualizations

Location:

~~~text
figures/
~~~

---

# Reproducibility

The complete benchmark pipeline can be reproduced using:

~~~text
python services/validation/scripts/run_large_campaign.py

python services/validation/scripts/generate_scientific_evidence.py

python services/validation/scripts/generate_benchmark_statistics.py

python services/validation/scripts/generate_publication_figures.py
~~~

---

# Limitations

Current limitations:

- synthetic benchmark sequences
- no execution on real quantum hardware
- pseudoknot structures not included
- resource estimates represent theoretical requirements

---

# Future Work

Future development directions:

- QAOA-based RNA optimization
- VQE formulations
- pseudoknot-aware structures
- AI-assisted candidate generation
- noisy quantum simulation
- real quantum hardware evaluation

---

# Team

## J. K. Pawan Kumar

Role:

~~~text
Project Lead and Sole Developer
~~~

Contributions:

- research and problem formulation
- RNAOS architecture design
- implementation
- benchmark development
- scientific validation
- documentation preparation

---

# Project Status

RNAOS Benchmark V1

A reproducible quantum-inspired framework for RNA secondary structure optimization.
