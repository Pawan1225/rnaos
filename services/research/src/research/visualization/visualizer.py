"""
Research visualization utilities.
"""

from __future__ import annotations

from research.analysis.statistical_summary import StatisticalSummary


class Visualizer:
    """
    Generate lightweight visualization data structures.

    These outputs are intentionally plotting-library agnostic so they
    can later be consumed by matplotlib, Plotly, Altair, or web dashboards.
    """

    def runtime_chart(
        self,
        summary: StatisticalSummary,
    ) -> dict[str, float]:
        """Runtime statistics."""

        return {
            "mean_runtime": summary.mean_runtime,
            "median_runtime": summary.median_runtime,
            "fastest_runtime": summary.fastest_runtime,
            "slowest_runtime": summary.slowest_runtime,
            "std_runtime": summary.std_runtime,
        }

    def accuracy_chart(
        self,
        summary: StatisticalSummary,
    ) -> dict[str, float]:
        """Accuracy statistics."""

        return {
            "mean_accuracy": summary.mean_accuracy,
            "mean_relative_error": summary.mean_relative_error,
        }

    def error_chart(
        self,
        summary: StatisticalSummary,
    ) -> dict[str, float]:
        """Energy error statistics."""

        return {
            "mean_absolute_error": summary.mean_absolute_error,
            "median_absolute_error": summary.median_absolute_error,
            "std_absolute_error": summary.std_absolute_error,
        }

    def dashboard(
        self,
        summary: StatisticalSummary,
    ) -> dict[str, dict[str, float]]:
        """
        Complete visualization payload for dashboards.
        """

        return {
            "runtime": self.runtime_chart(summary),
            "accuracy": self.accuracy_chart(summary),
            "error": self.error_chart(summary),
        }
