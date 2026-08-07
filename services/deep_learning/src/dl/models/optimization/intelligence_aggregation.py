"""
RNAOS intelligence aggregation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceAggregation:
    """
    Immutable optimization intelligence aggregation.
    """

    total_features: int

    average_capability: float

    learning_confidence: float

    meta_confidence: float

    unified_score: float
