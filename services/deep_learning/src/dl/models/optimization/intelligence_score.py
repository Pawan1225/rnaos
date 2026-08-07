"""
RNAOS intelligence score model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceScore:
    """
    Immutable intelligence score.
    """

    overall_score: float

    solver_strength: float

    learning_strength: float

    evolution_strength: float
