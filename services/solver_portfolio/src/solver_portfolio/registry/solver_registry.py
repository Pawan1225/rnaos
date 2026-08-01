"""
Solver Registry.

Central registry for all optimization solvers.
"""

from __future__ import annotations

from solver_portfolio.base.base_solver import BaseSolver


class SolverRegistry:
    """Registry for optimization solvers."""

    def __init__(self) -> None:
        self._solvers: dict[str, BaseSolver] = {}

    def register(
        self,
        solver: BaseSolver,
    ) -> None:
        """Register a solver instance."""

        self._solvers[solver.name] = solver

    def get(
        self,
        name: str,
    ) -> BaseSolver:
        """Retrieve a registered solver."""

        if name not in self._solvers:
            raise KeyError(f"Unknown solver: {name}")

        return self._solvers[name]

    def names(
        self,
    ) -> list[str]:
        """Return registered solver names."""

        return sorted(self._solvers.keys())

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return True if a solver is registered."""

        return name in self._solvers
