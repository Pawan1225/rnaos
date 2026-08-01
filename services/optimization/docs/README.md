# Optimization Generator

## Overview

The Optimization Generator converts AI-generated RNA analysis into
solver-independent optimization problems.

It serves as the bridge between AI Intelligence and the Solver Portfolio.

---

## Components

### OptimizationProblem

Canonical optimization representation.

Contains:

- Decision variables
- Objective
- Constraints
- Metadata

---

### ObjectiveFunctionGenerator

Creates optimization objectives.

---

### ConstraintGenerator

Creates solver-independent constraints.

---

### OptimizationProblemValidator

Validates generated optimization problems.

---

### QUBOGenerator

Converts OptimizationProblem into a QUBO representation.

---

### OptimizationProfiler

Coordinates the complete optimization pipeline.

---

## Pipeline

```text
AIProfile
      │
      ▼
Objective Generator
      │
      ▼
Constraint Generator
      │
      ▼
OptimizationProblem
      │
      ▼
Validator
      │
      ▼
QUBO Generator
      │
      ▼
OptimizationProfile
```

---

## Public API

```python
from optimization import OptimizationProfiler
```

---

## Future Work

- Ising Translator
- MILP Translator
- CP-SAT Translator
- Multi-objective optimization
- Automatic penalty tuning
- Constraint simplification
- Warm-start generation
- Quantum resource estimation
