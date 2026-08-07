"""
RNAOS parallel execution task model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ParallelExecutionTask:
    """
    Immutable parallel execution task.
    """

    task_id: int

    solver_name: str

    priority: int

    status: str
