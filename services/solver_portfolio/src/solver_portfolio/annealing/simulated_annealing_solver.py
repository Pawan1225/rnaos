"""
Simulated Annealing Solver.

Reference implementation of the BaseSolver interface using
a basic simulated annealing optimization strategy.
"""

from __future__ import annotations

import math
import random

from optimization.models.optimization_problem import (
    OptimizationProblem,
)

from solver_portfolio.base.base_solver import (
    BaseSolver,
    SolverResult,
)


class SimulatedAnnealingSolver(BaseSolver):
    """Basic simulated annealing solver."""

    name = "simulated_annealing"

    def __init__(
        self,
        initial_temperature: float = 10.0,
        cooling_rate: float = 0.95,
        iterations: int = 100,
    ) -> None:
        """Initialize the solver."""

        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.iterations = iterations

    def _objective(
        self,
        solution: list[int],
    ) -> float:
        """Dummy objective for Version 1."""

        return float(sum(solution))

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """Solve an optimization problem."""

        def _solve() -> SolverResult:
            n = problem.variable_count

            current = [random.randint(0, 1) for _ in range(n)]

            current_score = self._objective(current)

            best = current.copy()
            best_score = current_score

            temperature = self.initial_temperature

            for _ in range(self.iterations):
                candidate = current.copy()

                idx = random.randrange(n)

                candidate[idx] ^= 1

                candidate_score = self._objective(candidate)

                delta = candidate_score - current_score

                if delta >= 0 or random.random() < math.exp(delta / temperature):
                    current = candidate
                    current_score = candidate_score

                if current_score > best_score:
                    best = current.copy()
                    best_score = current_score

                temperature *= self.cooling_rate

            solution = {
                variable.name: float(best[i]) for i, variable in enumerate(problem.variables)
            }

            return SolverResult(
                solver_name=self.name,
                objective_value=best_score,
                solution=solution,
                runtime_seconds=0.0,
                success=True,
                metadata={
                    "temperature": self.initial_temperature,
                    "iterations": self.iterations,
                },
            )

        result, runtime = self.measure_runtime(_solve)

        result.runtime_seconds = runtime

        return result
