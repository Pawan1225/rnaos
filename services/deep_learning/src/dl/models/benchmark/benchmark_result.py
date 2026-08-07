"""
RNAOS benchmark result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)
from dl.models.benchmark.evaluation_metrics import (
    EvaluationMetrics,
)


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkResult:
    """
    Immutable benchmark execution result.
    """

    case_id: str

    method_name: str

    adapter_result: BenchmarkAdapterResult

    evaluation_metrics: EvaluationMetrics

    success: bool

    metadata: tuple[str, ...]
