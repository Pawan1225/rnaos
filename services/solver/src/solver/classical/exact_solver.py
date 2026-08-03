"""
Exact QUBO Solver.
"""

from __future__ import annotations

import itertools
import time

from optimization.models.optimization_problem import QUBOProblem

from solver.base.base_solver import BaseSolver
from solver.evaluation import QUBOEvaluator
from solver.models import (
    SolverCapabilities,
    SolverFamily,
    SolverResult,
)


class ExactSolver(BaseSolver):
    """Brute-force exact QUBO solver."""

    @property
    def name(self) -> str:
        """Return the solver name."""

        return "Exact Solver"

    @property
    def capabilities(self) -> SolverCapabilities:
        """Return the solver capabilities."""

        return SolverCapabilities(
            solver_family=SolverFamily.MATHEMATICAL,
            supports_sparse_qubo=True,
            supports_dense_qubo=True,
            supports_binary_variables=True,
            supports_continuous_variables=False,
            deterministic=True,
            parallel=False,
            gpu_accelerated=False,
            quantum=False,
            hybrid=False,
            max_problem_size=25,
        )

    def solve(
        self,
        problem: QUBOProblem,
    ) -> SolverResult:
        """Solve a QUBO problem exactly using exhaustive search."""

        start_time = time.perf_counter()

        best_solution: list[int] | None = None
        best_objective = float("inf")

        evaluations = 0

        for assignment in itertools.product(
            (0, 1),
            repeat=problem.size,
        ):
            solution = list(assignment)

            objective = QUBOEvaluator.evaluate(
                problem,
                solution,
            )

            evaluations += 1

            if objective < best_objective:
                best_objective = objective
                best_solution = solution

        runtime = time.perf_counter() - start_time

        assert best_solution is not None

        return SolverResult(
            solver_name=self.name,
            objective_value=best_objective,
            solution=best_solution,
            runtime_seconds=runtime,
            iterations=evaluations,
            metadata={
                "evaluations": evaluations,
            },
        )
