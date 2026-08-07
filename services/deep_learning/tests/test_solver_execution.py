"""
Tests for solver execution model.
"""

from __future__ import annotations

from dl.models.optimization.solver_execution import (
    SolverExecution,
)


def test_solver_execution() -> None:
    """
    Solver execution can be created.
    """

    execution = SolverExecution(
        execution_id=1,
        solver_name="ising",
        problem_id="rna_001",
        parameters=("iterations=100",),
        status="pending",
    )

    assert execution.execution_id == 1

    assert execution.solver_name == "ising"

    assert execution.problem_id == "rna_001"

    assert execution.parameters == ("iterations=100",)

    assert execution.status == "pending"
