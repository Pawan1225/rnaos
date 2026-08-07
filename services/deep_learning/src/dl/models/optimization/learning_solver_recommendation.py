"""
RNAOS learning solver recommendation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LearningSolverRecommendation:
    """
    Immutable learning-based solver recommendation.
    """

    problem_type: str

    recommended_solver: str

    confidence: float
