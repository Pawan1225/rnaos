"""
RNAOS learning optimization profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LearningProfile:
    """
    Immutable learning intelligence profile.
    """

    total_experiences: int

    best_solver: str

    average_reward: float

    confidence: float
