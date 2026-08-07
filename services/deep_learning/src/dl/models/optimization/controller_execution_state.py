"""
RNAOS controller execution state model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ControllerExecutionState:
    """
    Immutable controller execution state.
    """

    execution_id: int

    status: str

    selected_solver: str

    completed_stages: int
