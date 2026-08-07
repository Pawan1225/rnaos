"""
Tests for simulated annealing solver.
"""

from __future__ import annotations

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)
from dl.solvers.simulated_annealing import (
    SimulatedAnnealingSolver,
)


def test_solver_name() -> None:
    """
    Solver reports correct name.
    """

    solver = SimulatedAnnealingSolver()

    assert solver.name() == ("simulated_annealing")


def test_solver_execution() -> None:
    """
    Solver produces result.
    """

    solver = SimulatedAnnealingSolver(
        seed=42,
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

    assert result.solution == (0,)

    assert result.converged is True
