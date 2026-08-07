"""
RNAOS solver recommendation models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverRecommendation:
    """
    Immutable solver recommendation.
    """

    solver: str

    confidence: float

    reasoning: str
