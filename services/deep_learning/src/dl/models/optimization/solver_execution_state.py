"""
RNAOS solver execution state model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverExecutionState:
    """
    Immutable solver execution state.
    """

    execution_id: int

    status: str

    current_solver: str

    completed_stages: int
