"""
RNAOS embedding evaluation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class EmbeddingEvaluationReport:
    """
    Immutable embedding evaluation result.
    """

    embedding_dimension: int

    embedding_norm: float

    sparsity_score: float

    quality_score: float

    evaluation_version: str
