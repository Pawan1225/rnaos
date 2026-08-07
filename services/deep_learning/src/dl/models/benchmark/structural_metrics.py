"""
RNAOS structural evaluation metrics model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class StructuralMetrics:
    """
    Immutable RNA structural evaluation metrics.
    """

    base_pair_accuracy: float

    sensitivity: float

    specificity: float

    precision: float

    recall: float

    f1_score: float
