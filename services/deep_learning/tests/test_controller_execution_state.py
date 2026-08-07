"""
Tests for controller execution state.
"""

from __future__ import annotations

from dl.models.optimization.controller_execution_state import (
    ControllerExecutionState,
)


def test_controller_execution_state() -> None:
    """
    Controller execution state can be created.
    """

    state = ControllerExecutionState(
        execution_id=1,
        status="analyzing",
        selected_solver="ising",
        completed_stages=1,
    )

    assert state.execution_id == 1

    assert state.status == "analyzing"

    assert state.selected_solver == "ising"

    assert state.completed_stages == 1
