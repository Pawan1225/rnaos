"""
RNAOS solver result models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverResult:
    """
    Immutable optimization solver result.
    """

    solver_name: str

    solution: tuple[int, ...]

    energy: float

    iterations: int

    converged: bool
