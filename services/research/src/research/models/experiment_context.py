"""
Experiment context model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from research.metrics.evaluation_metrics import EvaluationMetrics
from research.models.benchmark_case import BenchmarkCase


@dataclass(slots=True)
class ExperimentContext:
    """
    Mutable state shared across the experiment pipeline.
    """

    benchmark_case: BenchmarkCase

    rna_profile: Any | None = None

    ai_profile: Any | None = None

    folding_result: Any | None = None

    optimization_problem: Any | None = None

    qubo: Any | None = None

    solver_result: Any | None = None

    metrics: EvaluationMetrics | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def benchmark_id(self) -> str:
        """Return benchmark identifier."""
        return self.benchmark_case.sequence_id

    @property
    def sequence(self) -> str:
        """Return RNA sequence."""
        return self.benchmark_case.sequence

    @property
    def completed(self) -> bool:
        """Whether evaluation metrics have been produced."""
        return self.metrics is not None
