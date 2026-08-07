"""
RNAOS optimization intelligence request models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationIntelligenceRequest:
    """
    Immutable optimization request.
    """

    sequence_id: str

    sequence_length: int

    complexity_score: float

    predicted_energy: float

    folding_difficulty: float

    solver_hint: str
