"""
Solver Orchestrator.
"""

from __future__ import annotations

from optimization.models.optimization_problem import QUBOProblem

from solver.base.base_solver import BaseSolver
from solver.models import SolverResult
from solver.recommender.solver_recommender import SolverRecommender


class SolverOrchestrator:
    """Coordinate execution of multiple solvers."""

    def __init__(
        self,
        solvers: list[BaseSolver],
    ) -> None:
        """Initialize the orchestrator."""

        self._solvers = solvers
        self._recommender = SolverRecommender()

    @property
    def solvers(self) -> list[BaseSolver]:
        """Return the registered solvers."""

        return self._solvers

    @property
    def recommender(self) -> SolverRecommender:
        """Return the solver recommender."""

        return self._recommender

    def recommend(
        self,
        problem: QUBOProblem,
    ) -> BaseSolver:
        """Recommend the best solver for the given problem."""

        return self.recommender.recommend(
            problem,
            self.solvers,
        )

    def solve(
        self,
        problem: QUBOProblem,
    ) -> list[SolverResult]:
        """Execute all compatible solvers and rank the results."""

        results: list[SolverResult] = []

        for solver in self.solvers:
            if not solver.supports(problem):
                continue

            results.append(
                solver.solve(problem),
            )

        results.sort(
            key=lambda result: result.objective_value,
        )

        return results

    def best_solver(
        self,
        problem: QUBOProblem,
    ) -> SolverResult:
        """Return the best solver result."""

        results = self.solve(problem)

        if not results:
            raise ValueError("No compatible solvers available.")

        return results[0]
