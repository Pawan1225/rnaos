"""
RNAOS solver execution pool model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.parallel_execution_task import (
    ParallelExecutionTask,
)


@dataclass(
    slots=True,
    frozen=True,
)
class SolverExecutionPool:
    """
    Immutable solver execution pool.
    """

    tasks: tuple[
        ParallelExecutionTask,
        ...,
    ]

    capacity: int
