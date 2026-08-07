"""
RNAOS solver execution model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverExecution:
    """
    Immutable solver execution request.
    """

    execution_id: int

    solver_name: str

    problem_id: str

    parameters: tuple[str, ...]

    status: str
