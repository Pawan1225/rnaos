"""
Tests for population annealing solver.
"""

from __future__ import annotations

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)
from dl.solvers.population_annealing import (
    PopulationAnnealingSolver,
)


def test_solver_name() -> None:
    """
    Solver reports correct name.
    """

    solver = PopulationAnnealingSolver()

    assert solver.name() == ("population_annealing")


def test_population_execution() -> None:
    """
    Population solver produces result.
    """

    solver = PopulationAnnealingSolver(
        seed=42,
        population_size=5,
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
