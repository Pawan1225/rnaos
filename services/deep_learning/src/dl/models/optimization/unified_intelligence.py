"""
RNAOS unified intelligence model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class UnifiedIntelligence:
    """
    Immutable unified optimization intelligence.
    """

    quantum_score: float

    optimization_score: float

    learning_score: float

    meta_score: float

    orchestration_score: float
