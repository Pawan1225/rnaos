"""
Solver Recommendation Engine.
"""

from __future__ import annotations

from optimization.models.optimization_problem import QUBOProblem

from solver.base.base_solver import BaseSolver


class SolverRecommender:
    """Recommend an appropriate solver for a problem."""

    def recommend(
        self,
        problem: QUBOProblem,
        solvers: list[BaseSolver],
    ) -> BaseSolver:
        """Recommend the most suitable compatible solver."""

        compatible = [solver for solver in solvers if solver.supports(problem)]

        if not compatible:
            raise ValueError("No compatible solvers available.")

        #
        # Prefer deterministic (exact) solvers
        # when they support the problem.
        #

        deterministic = [solver for solver in compatible if solver.capabilities.deterministic]

        if deterministic:
            return deterministic[0]

        #
        # Otherwise choose the solver capable of
        # handling the largest problem size.
        #

        compatible.sort(
            key=lambda solver: (
                -solver.capabilities.max_problem_size,
                solver.name,
            ),
        )

        return compatible[0]
