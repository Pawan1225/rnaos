"""
RNAOS hybrid quantum-inspired solver.
"""

from __future__ import annotations

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.solver_result import (
    SolverResult,
)
from dl.solvers.base_solver import (
    BaseQuantumInspiredSolver,
)


class HybridSearchSolver(
    BaseQuantumInspiredSolver,
):
    """
    Combines multiple optimization strategies.
    """

    def __init__(
        self,
        solvers: tuple[
            BaseQuantumInspiredSolver,
            ...,
        ],
    ) -> None:
        self.solvers = solvers

    def name(
        self,
    ) -> str:
        return "hybrid_search"

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """
        Execute multiple solvers
        and select best result.
        """

        results = tuple(
            solver.solve(
                problem,
            )
            for solver in self.solvers
        )

        best = min(
            results,
            key=lambda result: result.energy,
        )

        return SolverResult(
            solver_name=self.name(),
            solution=best.solution,
            energy=best.energy,
            iterations=sum(result.iterations for result in results),
            converged=all(result.converged for result in results),
        )
