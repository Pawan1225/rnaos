"""
RNAOS adaptive solver selection models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AdaptiveSolverSelection:
    """
    Immutable adaptive solver selection.
    """

    primary_solver: str

    solver_weights: tuple[tuple[str, float], ...]

    reasoning: str
