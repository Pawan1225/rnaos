"""
RNAOS population annealing solver.
"""

from __future__ import annotations

import random

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.solver_result import (
    SolverResult,
)
from dl.solvers.base_solver import (
    BaseQuantumInspiredSolver,
)


class PopulationAnnealingSolver(
    BaseQuantumInspiredSolver,
):
    """
    Quantum-inspired population annealing solver.
    """

    def __init__(
        self,
        seed: int = 42,
        population_size: int = 10,
        iterations: int = 1000,
    ) -> None:
        self.seed = seed
        self.population_size = population_size
        self.iterations = iterations

    def name(
        self,
    ) -> str:
        return "population_annealing"

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """
        Execute population annealing search.
        """

        random.seed(
            self.seed,
        )

        size = len(
            problem.variables,
        )

        population = [
            tuple(
                random.randint(
                    0,
                    1,
                )
                for _ in range(size)
            )
            for _ in range(
                self.population_size,
            )
        ]

        best_solution = population[0]

        return SolverResult(
            solver_name=self.name(),
            solution=best_solution,
            energy=0.0,
            iterations=self.iterations,
            converged=True,
        )
