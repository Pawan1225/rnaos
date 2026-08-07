"""
Tests for parallel tempering solver.
"""

from __future__ import annotations

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)
from dl.solvers.parallel_tempering import (
    ParallelTemperingSolver,
)


def test_solver_name() -> None:
    """
    Solver reports correct name.
    """

    solver = ParallelTemperingSolver()

    assert solver.name() == ("parallel_tempering")


def test_parallel_tempering_execution() -> None:
    """
    Solver produces deterministic result.
    """

    solver = ParallelTemperingSolver(
        seed=42,
        replicas=3,
        iterations=100,
    )

    problem = OptimizationProblem(
        name="rna_test",
        variables=(
            OptimizationVariable(
                variable_id="x0",
                index=0,
            ),
        ),
        constraints=(),
        objective="energy",
    )

    result = solver.solve(
        problem,
    )

    assert (
        len(
            result.solution,
        )
        == 1
    )

    assert result.converged is True
