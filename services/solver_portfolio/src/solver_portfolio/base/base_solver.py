"""
Base Solver Interface

Defines the abstract interface implemented by all optimization solvers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from time import perf_counter
from typing import Any

from optimization.models.optimization_problem import (
    OptimizationProblem,
)


@dataclass(slots=True)
class SolverResult:
    """Represents the result returned by an optimization solver."""

    solver_name: str
    objective_value: float
    solution: dict[str, float]
    runtime_seconds: float
    success: bool
    metadata: dict[str, Any] = field(default_factory=dict)


class BaseSolver(ABC):
    """Abstract base class for all optimization solvers."""

    name: str = "base"

    def __call__(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """Convenience wrapper around solve()."""
        return self.solve(problem)

    @abstractmethod
    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """Solve an optimization problem."""
        raise NotImplementedError

    def measure_runtime(
        self,
        fn,
        *args,
        **kwargs,
    ):
        """Execute a function while measuring runtime."""

        start = perf_counter()
        result = fn(*args, **kwargs)
        elapsed = perf_counter() - start

        return result, elapsed
