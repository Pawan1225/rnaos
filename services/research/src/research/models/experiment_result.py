"""
Experiment result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from research.metrics.evaluation_metrics import EvaluationMetrics


@dataclass(frozen=True, slots=True)
class ExperimentResult:
    """
    Result of a single benchmark experiment.
    """

    benchmark_id: str

    metrics: EvaluationMetrics

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        """Whether the experiment completed successfully."""
        return self.metrics.solved
