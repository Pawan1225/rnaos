"""
RNAOS continuous learning profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ContinuousLearningProfile:
    """
    Immutable learning system state.
    """

    total_experiments: int

    best_solver: str

    recommended_solver: str

    confidence: float

    success_rate: float

    knowledge_items: int
