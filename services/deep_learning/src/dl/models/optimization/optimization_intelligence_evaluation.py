"""
RNAOS optimization intelligence evaluation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationIntelligenceEvaluation:
    """
    Immutable optimization intelligence evaluation.
    """

    overall_score: float

    optimization_score: float

    learning_score: float

    evolution_score: float
