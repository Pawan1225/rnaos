# RNAOS Experiment Protocol

Version: 1.0

Status: Locked

---

# Purpose

This document defines how every experiment in RNAOS is designed, executed, recorded, evaluated, and reproduced.

All experiments must follow this protocol to ensure scientific rigor and reproducibility.

---

# Experiment Lifecycle

Research Question

↓

Hypothesis

↓

Experiment Design

↓

Execution

↓

Evaluation

↓

Reflection

↓

Knowledge Repository

↓

Next Experiment

---

# Experiment Identification

Every experiment receives a unique identifier.

Format

EXP-YYYY-XXXX

Example

EXP-2026-0001

---

# Required Metadata

Every experiment must record:

- Experiment ID
- Timestamp
- Research objective
- Research question
- Hypothesis
- RNA sequence
- RNA length
- Feature profile
- Optimization formulation
- Solver
- Quantum backend
- Hyperparameters
- Random seed
- Software version
- Git commit hash
- Environment
- Runtime
- Memory usage

---

# Execution Rules

Every experiment must:

- Use version-controlled code
- Store configuration
- Log execution
- Record failures
- Preserve outputs
- Generate a summary report

---

# Evaluation Metrics

Scientific

- Minimum Free Energy
- Energy Gap
- Structural Accuracy

Engineering

- Runtime
- Memory Usage
- Scalability

AI

- Solver Selection Accuracy
- Confidence Score

Quantum

- Circuit Depth
- Qubit Count
- Execution Time

---

# Reflection

After every experiment record:

- What worked?
- What failed?
- Why?
- Improvements
- Confidence
- Recommendations

---

# Experiment Storage

experiments/

EXP-YYYY-XXXX/

config/

logs/

results/

reflection/

analytics/

report/

---

# Reproducibility

Every experiment must be reproducible from:

- Source code
- Configuration
- Random seed
- Input data
- Software versions
- Git commit
- Experiment metadata

---

# Benchmarking

Every optimization experiment should be compared against:

- ViennaRNA
- Classical baseline
- Previous best experiment

---

# Reporting

Each experiment automatically generates:

- Summary
- Metrics
- Plots
- Reflection
- Recommendations

---

# Completion Criteria

An experiment is complete only when:

- Execution finished
- Metrics recorded
- Reflection completed
- Results stored
- Report generated
- Reproducibility verified
