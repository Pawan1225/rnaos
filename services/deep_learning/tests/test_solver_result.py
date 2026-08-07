"""
Tests for solver result model.
"""

from __future__ import annotations

from dl.models.optimization.solver_result import (
    SolverResult,
)


def test_solver_result_creation() -> None:
    """
    Solver result is created.
    """

    result = SolverResult(
        solver_name="simulated_annealing",
        solution=(
            1,
            0,
            1,
        ),
        energy=-5.0,
        iterations=100,
        converged=True,
    )

    assert result.solver_name == ("simulated_annealing")

    assert result.energy == -5.0

    assert result.converged is True


def test_solution_storage() -> None:
    """
    Solution vector is preserved.
    """

    result = SolverResult(
        solver_name="test_solver",
        solution=(
            1,
            1,
        ),
        energy=-2.0,
        iterations=10,
        converged=False,
    )

    assert result.solution == (
        1,
        1,
    )
