"""
Tests for solver runtime.
"""

from __future__ import annotations

from dl.models.optimization.solver_execution import (
    SolverExecution,
)
from dl.models.optimization.solver_result import (
    SolverResult,
)
from dl.optimization.runtime.solver_runtime import (
    SolverRuntime,
)


def test_solver_runtime() -> None:
    """
    Runtime executes a solver request.
    """

    execution = SolverExecution(
        execution_id=1,
        solver_name="ising",
        problem_id="rna_001",
        parameters=("iterations=100",),
        status="pending",
    )

    runtime = SolverRuntime()

    result = runtime.execute(execution)

    assert isinstance(
        result,
        SolverResult,
    )

    assert result.solver_name == "ising"

    assert result.solution == ()

    assert result.energy == 0.0

    assert result.iterations == 0

    assert result.converged is False
