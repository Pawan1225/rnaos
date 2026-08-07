"""
Tests for hybrid search solver.
"""

from __future__ import annotations

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)
from dl.solvers.hybrid_search import (
    HybridSearchSolver,
)


class DummySolver:
    """
    Dummy solver for testing.
    """

    def __init__(
        self,
        energy: float,
    ) -> None:
        self.energy = energy

    def solve(
        self,
        problem,
    ):
        from dl.models.optimization.solver_result import (
            SolverResult,
        )

        return SolverResult(
            solver_name="dummy",
            solution=(1,),
            energy=self.energy,
            iterations=10,
            converged=True,
        )

    def name(
        self,
    ) -> str:
        return "dummy"


def test_hybrid_solver_name() -> None:
    """
    Hybrid solver reports name.
    """

    solver = HybridSearchSolver(
        solvers=(),
    )

    assert solver.name() == ("hybrid_search")


def test_best_solution_selected() -> None:
    """
    Hybrid solver selects lowest energy.
    """

    solver = HybridSearchSolver(
        solvers=(
            DummySolver(-5.0),
            DummySolver(-10.0),
        ),
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

    assert result.energy == -10.0
