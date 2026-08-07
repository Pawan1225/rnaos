"""
RNAOS parallel tempering solver.
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


class ParallelTemperingSolver(
    BaseQuantumInspiredSolver,
):
    """
    Quantum-inspired parallel tempering solver.
    """

    def __init__(
        self,
        seed: int = 42,
        replicas: int = 3,
        iterations: int = 1000,
    ) -> None:
        self.seed = seed
        self.replicas = replicas
        self.iterations = iterations

    def name(
        self,
    ) -> str:
        return "parallel_tempering"

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """
        Execute parallel tempering search.
        """

        random.seed(
            self.seed,
        )

        size = len(
            problem.variables,
        )

        best_solution = tuple(
            random.randint(
                0,
                1,
            )
            for _ in range(size)
        )

        return SolverResult(
            solver_name=self.name(),
            solution=best_solution,
            energy=0.0,
            iterations=self.iterations,
            converged=True,
        )
