"""
RNAOS population candidate model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PopulationCandidate:
    """
    Immutable optimization candidate.
    """

    candidate_id: int

    state: tuple[int, ...]

    energy: float

    fitness: float
