"""
Greedy Solver

Reference implementation of the BaseSolver interface.
"""

from __future__ import annotations

from optimization.models.optimization_problem import (
    OptimizationProblem,
)

from solver_portfolio.base.base_solver import (
    BaseSolver,
    SolverResult,
)


class GreedySolver(BaseSolver):
    """Simple deterministic greedy solver."""

    name = "greedy"

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """Solve an optimization problem using a greedy heuristic."""

        def _solve() -> SolverResult:
            solution = {variable.name: 1.0 for variable in problem.variables}

            objective_value = float(sum(solution.values()))

            return SolverResult(
                solver_name=self.name,
                objective_value=objective_value,
                solution=solution,
                runtime_seconds=0.0,
                success=True,
                metadata={
                    "strategy": "greedy_baseline",
                },
            )

        result, runtime = self.measure_runtime(_solve)

        result.runtime_seconds = runtime

        return result
