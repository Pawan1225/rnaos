"""
RNAOS solver execution batch model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.solver_execution import (
    SolverExecution,
)


@dataclass(
    slots=True,
    frozen=True,
)
class ExecutionBatch:
    """
    Immutable solver execution batch.
    """

    batch_id: int

    executions: tuple[SolverExecution, ...]

    problem_id: str

    status: str
