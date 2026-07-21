# AI Intelligence

## Overview

The AI Intelligence module transforms validated RNA profiles into AI-ready representations and optimization recommendations.

It consumes the output of the RNA Intelligence module and produces an `AIProfile` used by downstream optimization services.

---

## Components

### FeatureEngineeringEngine

Converts biological features into standardized numerical feature vectors.

---

### RNAEmbeddingEngine

Generates fixed-length embedding vectors for machine learning.

Current implementation:

- Feature Embedding V1

Future support:

- RNA-FM
- Nucleotide Transformer
- Graph Neural Networks
- Quantum Embeddings

---

### ComplexityEstimator

Estimates optimization complexity using interpretable heuristics.

Outputs:

- Complexity score
- Category
- Explanation

---

### SolverSuitabilityPredictor

Recommends the most appropriate optimization strategy.

Current recommendations:

- Classical
- Hybrid
- Quantum

---

### AIProfiler

Coordinates the complete AI pipeline.

Returns:

- AIProfile

---

## Public Pipeline

```text
RNAProfile
      │
      ▼
Feature Engineering
      │
      ▼
Feature Vector
      │
      ├────────────┐
      ▼            ▼
Embedding     Complexity
      │            │
      └──────┬─────┘
             ▼
Solver Predictor
             │
             ▼
AIProfile
```

---

## Public Objects

- FeatureVector
- RNAEmbedding
- ComplexityEstimate
- SolverRecommendation
- AIProfile

---

## Planned Improvements

- Learned embeddings
- Neural complexity prediction
- Solver ranking
- Reinforcement learning
- AutoML
- Quantum ML integration
