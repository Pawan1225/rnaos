"""
RNAOS optimization candidate model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationCandidate:
    """
    Immutable optimization candidate.
    """

    candidate_id: int

    solver_name: str

    fitness: float

    quality: float
