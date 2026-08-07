"""
Tests for solver execution state model.
"""

from __future__ import annotations

from dl.models.optimization.solver_execution_state import (
    SolverExecutionState,
)


def test_solver_execution_state_creation() -> None:
    """
    Solver execution state can be created.
    """

    state = SolverExecutionState(
        execution_id=1,
        status="running",
        current_solver="ising",
        completed_stages=1,
    )

    assert state.execution_id == 1

    assert state.status == "running"

    assert state.current_solver == "ising"

    assert state.completed_stages == 1
