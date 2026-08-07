"""
RNAOS refinement result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RefinementResult:
    """
    Immutable refinement result.
    """

    candidate_id: int

    original_energy: float

    improved_energy: float

    improvement_score: float

    status: str
