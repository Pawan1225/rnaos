"""
RNAOS solver intelligence registry.
"""

from __future__ import annotations

from dl.models.optimization.solver_entry import (
    SolverEntry,
)
from dl.models.optimization.solver_registry import (
    SolverRegistry,
)


class SolverIntelligenceRegistry:
    """
    Provides access to registered solver intelligence.
    """

    def __init__(
        self,
        registry: SolverRegistry,
    ) -> None:
        self._registry = registry

    @classmethod
    def build(
        cls,
        solvers: tuple[
            SolverEntry,
            ...,
        ],
    ) -> SolverIntelligenceRegistry:
        """
        Build a registry from solver entries.
        """

        registry = SolverRegistry(
            solvers=solvers,
            total_solvers=len(solvers),
        )

        return cls(registry)

    def get_solver(
        self,
        name: str,
    ) -> SolverEntry:
        """
        Retrieve a solver by name.
        """

        for solver in self._registry.solvers:
            if solver.solver_name == name:
                return solver

        raise ValueError("Solver not found")

    def best_solver(
        self,
    ) -> SolverEntry:
        """
        Return the highest capability solver.
        """

        return max(
            self._registry.solvers,
            key=lambda solver: solver.capability_score,
        )
