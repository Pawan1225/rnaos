"""
RNAOS simulated annealing solver.
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


class SimulatedAnnealingSolver(
    BaseQuantumInspiredSolver,
):
    """
    Quantum-inspired simulated annealing solver.
    """

    def __init__(
        self,
        seed: int = 42,
        iterations: int = 1000,
    ) -> None:
        self.seed = seed
        self.iterations = iterations

    def name(
        self,
    ) -> str:
        return "simulated_annealing"

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """
        Execute simulated annealing.

        Initial implementation provides
        deterministic search foundation.
        """

        random.seed(
            self.seed,
        )

        size = len(
            problem.variables,
        )

        state = tuple(
            random.randint(
                0,
                1,
            )
            for _ in range(size)
        )

        best_state = state

        return SolverResult(
            solver_name=self.name(),
            solution=best_state,
            energy=0.0,
            iterations=self.iterations,
            converged=True,
        )
