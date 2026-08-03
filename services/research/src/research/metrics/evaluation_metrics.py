"""
Research evaluation metrics.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class EvaluationMetrics:
    """
    Standardized evaluation metrics for benchmark experiments.
    """

    benchmark_id: str

    solver_name: str

    objective_value: float

    runtime_seconds: float

    reference_objective: float | None = None

    solved: bool = True

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def absolute_error(self) -> float:
        """Absolute error from the reference objective."""
        if self.reference_objective is None:
            return 0.0

        return abs(self.objective_value - self.reference_objective)

    @property
    def relative_error(self) -> float:
        """Relative error from the reference objective."""
        if self.reference_objective is None:
            return 0.0

        denominator = max(abs(self.reference_objective), 1.0)
        return self.absolute_error / denominator

    @property
    def accuracy(self) -> float:
        """Normalized accuracy score."""
        return max(0.0, 1.0 - self.relative_error)


class MetricsFactory:
    """Factory for creating evaluation metrics."""

    @staticmethod
    def build(
        *,
        benchmark_id: str,
        solver_name: str,
        objective_value: float,
        runtime_seconds: float,
        reference_objective: float | None = None,
        solved: bool = True,
        metadata: dict[str, Any] | None = None,
    ) -> EvaluationMetrics:
        return EvaluationMetrics(
            benchmark_id=benchmark_id,
            solver_name=solver_name,
            objective_value=objective_value,
            runtime_seconds=runtime_seconds,
            reference_objective=reference_objective,
            solved=solved,
            metadata=metadata or {},
        )
