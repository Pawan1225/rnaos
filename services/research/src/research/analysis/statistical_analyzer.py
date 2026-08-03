"""
Statistical analysis for RNAOS experiments.
"""

from __future__ import annotations

from statistics import mean, median, stdev

from research.analysis.statistical_summary import StatisticalSummary
from research.metrics.evaluation_metrics import EvaluationMetrics


class StatisticalAnalyzer:
    """
    Compute aggregate statistics from experiment metrics.
    """

    def summarize(
        self,
        metrics: list[EvaluationMetrics],
    ) -> StatisticalSummary:
        """
        Generate a statistical summary for a collection of experiment metrics.
        """
        if not metrics:
            raise ValueError("Cannot summarize an empty metrics collection.")

        runtimes = [m.runtime_seconds for m in metrics]
        absolute_errors = [m.absolute_error for m in metrics]
        relative_errors = [m.relative_error for m in metrics]
        accuracies = [m.accuracy for m in metrics]

        return StatisticalSummary(
            sample_size=len(metrics),
            mean_runtime=mean(runtimes),
            median_runtime=median(runtimes),
            std_runtime=stdev(runtimes) if len(runtimes) > 1 else 0.0,
            fastest_runtime=min(runtimes),
            slowest_runtime=max(runtimes),
            mean_absolute_error=mean(absolute_errors),
            median_absolute_error=median(absolute_errors),
            std_absolute_error=(stdev(absolute_errors) if len(absolute_errors) > 1 else 0.0),
            mean_relative_error=mean(relative_errors),
            mean_accuracy=mean(accuracies),
        )
