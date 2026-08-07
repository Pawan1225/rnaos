"""
RNAOS learning feedback model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LearningFeedback:
    """
    Immutable learning feedback signal.
    """

    solver_name: str

    reward: float

    quality_score: float

    efficiency_score: float
