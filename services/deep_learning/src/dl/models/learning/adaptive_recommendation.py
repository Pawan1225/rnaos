"""
RNAOS adaptive recommendation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AdaptiveRecommendation:
    """
    Immutable optimization recommendation.
    """

    recommended_solver: str

    optimization_strategy: str

    expected_accuracy: float

    expected_runtime: float

    confidence: float

    reasoning: tuple[str, ...]
