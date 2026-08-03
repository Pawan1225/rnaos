"""
Base Solver Interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from optimization.models.optimization_problem import QUBOProblem

from solver.models import SolverCapabilities, SolverResult


class BaseSolver(ABC):
    """Abstract base class for all optimization solvers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable solver name."""

    @property
    @abstractmethod
    def capabilities(self) -> SolverCapabilities:
        """Static capabilities advertised by the solver."""

    @abstractmethod
    def solve(
        self,
        problem: QUBOProblem,
    ) -> SolverResult:
        """Solve a QUBO optimization problem."""

    def supports(
        self,
        problem: QUBOProblem,
    ) -> bool:
        """
        Return whether this solver can solve the given problem.

        Subclasses may override this method to perform additional
        compatibility checks.
        """

        return problem.size <= self.capabilities.max_problem_size
