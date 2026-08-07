"""
RNAOS quantum-inspired solver interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)


class BaseQuantumInspiredSolver(ABC):
    """
    Base interface for all
    quantum-inspired solvers.
    """

    @abstractmethod
    def solve(
        self,
        problem: OptimizationProblem,
    ) -> tuple[int, ...]:
        """
        Solve optimization problem.
        """

        raise NotImplementedError

    @abstractmethod
    def name(
        self,
    ) -> str:
        """
        Return solver name.
        """

        raise NotImplementedError
