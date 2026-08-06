"""
RNAOS machine learning benchmark report.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class BenchmarkReport:
    """
    Immutable report comparing ML models.

    Stores model performance results from
    benchmarking experiments.
    """

    benchmark_id: str

    model_scores: tuple[tuple[str, float], ...]

    metric_name: str

    created_at: str

    @property
    def model_count(
        self,
    ) -> int:
        """
        Number of benchmarked models.
        """

        return len(
            self.model_scores,
        )

    @property
    def best_model(
        self,
    ) -> str | None:
        """
        Return highest scoring model.
        """

        if not self.model_scores:
            return None

        return max(
            self.model_scores,
            key=lambda item: item[1],
        )[0]
