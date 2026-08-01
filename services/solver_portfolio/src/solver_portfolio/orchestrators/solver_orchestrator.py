"""
Solver Orchestrator.

Coordinates solver selection and execution.
"""

from __future__ import annotations

from optimization.models.optimization_problem import (
    OptimizationProfile,
)

from solver_portfolio.annealing.simulated_annealing_solver import (
    SimulatedAnnealingSolver,
)
from solver_portfolio.base.base_solver import (
    SolverResult,
)
from solver_portfolio.genetic.genetic_solver import (
    GeneticSolver,
)
from solver_portfolio.greedy.greedy_solver import (
    GreedySolver,
)
from solver_portfolio.registry.solver_registry import (
    SolverRegistry,
)


class SolverOrchestrator:
    """Coordinates optimization solver execution."""

    def __init__(
        self,
    ) -> None:
        self.registry = SolverRegistry()

        self.registry.register(
            GreedySolver(),
        )

        self.registry.register(
            SimulatedAnnealingSolver(),
        )

        self.registry.register(
            GeneticSolver(),
        )

    def solve(
        self,
        profile: OptimizationProfile,
    ) -> SolverResult:
        """Execute the recommended solver."""

        solver_name = profile.problem.metadata.solver_hint

        if not self.registry.exists(
            solver_name,
        ):
            solver_name = "greedy"

        solver = self.registry.get(
            solver_name,
        )

        return solver.solve(
            profile.problem,
        )
