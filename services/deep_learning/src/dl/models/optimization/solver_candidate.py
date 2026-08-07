"""
RNAOS solver candidate model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverCandidate:
    """
    Immutable optimization candidate.
    """

    candidate_id: int

    source_solver: str

    structure: tuple[str, ...]

    energy: float

    score: float
