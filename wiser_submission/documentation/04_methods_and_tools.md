# Methods and Tools

## Implementation Environment

RNAOS was implemented as a modular Python-based research framework.

The development environment included:

~~~text
Programming Language:
Python 3.11

Operating System:
macOS development environment

Project Structure:
Modular service-based architecture
~~~

The framework was designed to support reproducible experiments, automated validation, and future extension toward quantum optimization workflows.

---

# Software Tools

## ViennaRNA

ViennaRNA was used as the classical RNA folding reference framework.

RNAOS uses ViennaRNA for:

- generating Minimum Free Energy (MFE) reference structures
- evaluating candidate structure energies
- calculating energy differences between predictions

ViennaRNA provides the classical benchmark required for evaluating optimization approaches.

---

## Python Libraries

Core libraries used include:

~~~text
RNA folding:
- ViennaRNA Python package

Data processing:
- Python standard libraries

Visualization:
- Matplotlib

Testing:
- Pytest

Code quality:
- Ruff
~~~

---

# Benchmark Generation Methodology

RNAOS was evaluated using synthetic RNA sequences.

Benchmark dataset:

~~~text
Total sequences:
400

Sequence lengths:
20 nucleotides
40 nucleotides
60 nucleotides
80 nucleotides
~~~

For each sequence, RNAOS generated a prediction and compared it against the ViennaRNA reference MFE structure.

---

# Evaluation Metrics

RNAOS predictions were evaluated using multiple metrics.

## Structural Metrics

The following structural measurements were calculated:

- exact structure accuracy
- base-pair precision
- base-pair recall
- F1 similarity score
- base-pair distance

These metrics measure how closely RNAOS structures match classical reference structures.

---

## Energy Metrics

Thermodynamic evaluation included:

- RNAOS predicted energy
- ViennaRNA reference energy
- energy gap

The energy gap is defined as:

~~~text
Energy Gap = |RNAOS Energy - Reference Energy|
~~~

A smaller energy gap indicates closer agreement with the classical MFE reference.

---

## Scaling Metrics

RNAOS also evaluated computational scaling through:

- runtime measurement
- estimated quantum variables
- estimated qubit requirements
- resource growth with sequence length

---

# Validation Pipeline

The complete validation workflow:

~~~text
Generate RNA Dataset

        |

        v

Run RNAOS Optimization

        |

        v

Evaluate Structures

        |

        v

Compare With ViennaRNA

        |

        v

Generate Scientific Evidence

        |

        v

Create Reports and Figures
~~~

---

# Testing Strategy

RNAOS components were validated using automated tests.

Testing covered:

- candidate generation
- structure validation
- energy evaluation
- optimization logic
- benchmark evaluation
- result generation

Code quality checks were performed using:

~~~text
ruff check services/validation --fix
~~~

Automated tests were executed using:

~~~text
pytest services/validation/tests/
~~~

---

# Evidence Generation

After validation, RNAOS generated reproducible evidence artifacts:

~~~text
benchmark_results/

    experiment_results.json
    benchmark_summary.json
    benchmark_statistics.json


scientific_analysis/

    accuracy_analysis.json
    energy_gap_analysis.json
    runtime_scaling.json
    quantum_resource_scaling.json
    scientific_report.json


figures/

    accuracy_vs_length.png
    energy_gap_distribution.png
    runtime_scaling.png
    quantum_resource_scaling.png
~~~

These artifacts provide transparent evidence of benchmark performance and scaling behavior.
