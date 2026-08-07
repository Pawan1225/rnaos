"""
RNAOS execution result collection model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.solver_result import (
    SolverResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class ExecutionResultCollection:
    """
    Immutable collection of solver results.
    """

    collection_id: int

    results: tuple[SolverResult, ...]

    problem_id: str

    status: str
