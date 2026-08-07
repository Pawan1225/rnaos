"""
RNAOS large benchmark result analyzer.
"""

from __future__ import annotations

from validation.models.benchmark_summary import (
    BenchmarkSummary,
)


class LargeBenchmarkResultAnalyzer:
    """
    Extracts scientific benchmark metrics.
    """

    def analyze(
        self,
        accuracies: tuple[float, ...],
        energy_gaps: tuple[float, ...],
        runtimes: tuple[float, ...],
    ) -> BenchmarkSummary:
        """
        Calculate benchmark statistics.
        """

        if not accuracies:
            raise ValueError("No benchmark results")

        return BenchmarkSummary(
            benchmark_id=("RNAOS_LARGE_BENCHMARK_V1"),
            total_experiments=len(accuracies),
            average_energy_gap=(sum(energy_gaps) / len(energy_gaps)),
            average_accuracy=(sum(accuracies) / len(accuracies)),
            average_runtime=(sum(runtimes) / len(runtimes)),
            best_score=max(accuracies),
            version="1.0.0",
        )
