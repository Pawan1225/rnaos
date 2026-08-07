# RNAOS

## Quantum-Inspired Optimization for mRNA Secondary Structure Prediction

### WISER Global Quantum+AI Program 2026

### WISER <> Moderna Challenge

---

# Project Overview

RNAOS (RNA Optimization System) is a quantum-inspired hybrid optimization framework developed for exploring mRNA secondary structure prediction.

The project investigates how optimization methods can be applied to RNA folding while benchmarking against classical Minimum Free Energy (MFE) structures generated using ViennaRNA.

RNAOS focuses on:

- RNA structure candidate generation
- biological constraint validation
- thermodynamic energy evaluation
- energy-aware optimization
- quantum resource estimation

---

# Challenge Background

mRNA secondary structure plays an important role in RNA-based medicines.

RNA structure can influence:

- molecular stability
- translation efficiency
- manufacturability

However, RNA folding is computationally challenging because a single RNA sequence can form many possible secondary structures.

The WISER <> Moderna challenge explores whether quantum or quantum-inspired optimization methods can help investigate RNA folding landscapes.

---

# RNAOS Solution Approach

RNAOS implements a hybrid optimization pipeline:

~~~text
RNA Sequence

      |
      v

Candidate Structure Generation

      |
      v

RNA Constraint Validation

      |
      v

Energy Evaluation

      |
      v

Energy-Aware Optimization

      |
      v

Benchmark Comparison
~~~

The system generates valid RNA structures, evaluates their thermodynamic energy, and compares predictions against ViennaRNA reference MFE structures.

---

# Methods and Tools

## Classical Methods

ViennaRNA is used for:

- Minimum Free Energy reference generation
- structure energy evaluation
- benchmark comparison

---

## Optimization Methods

RNAOS uses:

~~~text
Candidate Generation

        +

Biological Constraints

        +

Energy Optimization

        +

Structure Validation
~~~

---

## Quantum-Inspired Analysis

RNAOS includes:

- optimization formulation
- estimated variables
- qubit resource analysis
- scaling evaluation

The project does not claim quantum advantage but provides a framework compatible with future quantum optimization methods.

---

# Experimental Validation

RNAOS was evaluated using:

~~~text
400 synthetic RNA sequences
~~~

Sequence lengths:

~~~text
20 nucleotides

40 nucleotides

60 nucleotides

80 nucleotides
~~~

Evaluation metrics:

- structure accuracy
- F1 similarity score
- energy gap
- runtime scaling
- quantum resource estimation

---

# Results

## Structure Accuracy

~~~text
Average Accuracy:

1.0
~~~

---

## Structural Similarity

~~~text
Average F1 Score:

0.9725
~~~

---

## Energy Evaluation

~~~text
Average Energy Gap:

0.0
~~~

---

## Quantum Resource Scaling

~~~text
Maximum Estimated Qubits:

160
~~~

The resource estimation represents theoretical requirements for future quantum implementations.

---

# Repository Structure

~~~text
wiser_submission/

├── benchmark_results/

│   └── Experimental benchmark outputs


├── scientific_analysis/

│   └── Scientific evaluation reports


├── figures/

│   └── Generated benchmark visualizations


├── documentation/

│   └── Complete technical documentation

└── submission_manifest.json
~~~

---

# Evidence Package

The submission contains:

## Benchmark Results

Includes:

- experiment results
- benchmark statistics
- benchmark summary
- execution manifest

Location:

~~~text
benchmark_results/
~~~

---

## Scientific Analysis

Includes:

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

## Visualizations

Generated figures include:

- accuracy versus sequence length
- energy gap distribution
- runtime scaling
- quantum resource scaling

Location:

~~~text
figures/
~~~

---

# Reproducibility

The complete validation workflow can be reproduced using:

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
- no real quantum hardware execution
- pseudoknot structures are not included
- resource estimates represent theoretical scaling

---

# Future Work

Future development directions:

- QAOA-based RNA optimization
- variational quantum approaches
- AI-assisted candidate generation
- larger RNA datasets
- pseudoknot-aware modeling
- quantum hardware experiments

---

# Team Contribution

## J. K. Pawan Kumar

Role:

~~~text
Project Lead

Researcher

Software Developer
~~~

Contributions:

- RNAOS architecture design
- optimization framework implementation
- benchmark development
- validation pipeline
- scientific analysis
- documentation preparation

---

# Detailed Documentation

Additional technical details are available in:

~~~text
documentation/
~~~

---

# Project Status

RNAOS Benchmark V1

A reproducible quantum-inspired framework for RNA secondary structure optimization.
