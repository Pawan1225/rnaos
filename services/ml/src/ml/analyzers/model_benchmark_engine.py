"""
RNAOS machine learning model benchmark engine.
"""

from __future__ import annotations

from datetime import UTC, datetime

from ml.models.benchmark_report import (
    BenchmarkReport,
)
from ml.models.trained_model import (
    TrainedModel,
)


class ModelBenchmarkEngine:
    """
    Compare trained machine learning models.

    Generates immutable benchmark reports.
    """

    def benchmark(
        self,
        models: tuple[TrainedModel, ...],
        metric_name: str = "r2",
    ) -> BenchmarkReport:
        """
        Benchmark trained models.
        """

        if not models:
            raise ValueError(
                "At least one model is required.",
            )

        scores = tuple(
            (
                model.model_name,
                model.metric_value,
            )
            for model in models
        )

        return BenchmarkReport(
            benchmark_id=self._benchmark_id(),
            model_scores=scores,
            metric_name=metric_name,
            created_at=datetime.now(
                UTC,
            ).isoformat(),
        )

    def _benchmark_id(
        self,
    ) -> str:
        """
        Generate deterministic benchmark identifier.
        """

        return "benchmark_" + datetime.now(
            UTC,
        ).strftime(
            "%Y%m%d%H%M%S",
        )
