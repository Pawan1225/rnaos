"""
RNAOS result aggregation engine.
"""

from __future__ import annotations

from validation.models.benchmark_summary import (
    BenchmarkSummary,
)
from validation.models.comparison_result import (
    ComparisonResult,
)


class ResultAggregationEngine:
    """
    Aggregates benchmark comparison results.
    """

    def aggregate(
        self,
        results: tuple[ComparisonResult, ...],
    ) -> BenchmarkSummary:
        """
        Generate benchmark statistics.
        """

        if not results:
            raise ValueError("No results provided")

        energy_gaps = [result.energy_gap for result in results]

        accuracies = [result.structure_accuracy for result in results]

        runtimes = [result.runtime_difference for result in results]

        scores = [result.overall_score for result in results]

        return BenchmarkSummary(
            benchmark_id=("BENCHMARK_SUMMARY_001"),
            total_experiments=len(results),
            average_energy_gap=(sum(energy_gaps) / len(energy_gaps)),
            average_accuracy=(sum(accuracies) / len(accuracies)),
            average_runtime=(sum(runtimes) / len(runtimes)),
            best_score=max(scores),
            version="1.0.0",
        )
