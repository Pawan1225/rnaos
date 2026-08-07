"""
RNAOS learning analytics model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LearningAnalytics:
    """
    Immutable learning analytics result.
    """

    total_experiments: int

    success_rate: float

    average_runtime: float

    average_accuracy: float

    average_energy: float

    best_solver: str
