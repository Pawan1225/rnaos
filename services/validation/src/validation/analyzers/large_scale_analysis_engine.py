"""
RNAOS large scale analysis engine.
"""

from __future__ import annotations

from validation.models.large_scale_analysis import (
    LargeScaleAnalysis,
)


class LargeScaleAnalysisEngine:
    """
    Performs final benchmark analysis.
    """

    def analyze(
        self,
        accuracies: tuple[float, ...],
        energy_gaps: tuple[float, ...],
        runtimes: tuple[float, ...],
    ) -> LargeScaleAnalysis:
        """
        Calculate campaign statistics.
        """

        if not accuracies:
            raise ValueError("No benchmark data")

        return LargeScaleAnalysis(
            analysis_id=("LARGE_SCALE_ANALYSIS_V1"),
            total_experiments=len(accuracies),
            average_accuracy=round(
                sum(accuracies) / len(accuracies),
                2,
            ),
            average_energy_gap=round(
                sum(energy_gaps) / len(energy_gaps),
                2,
            ),
            average_runtime=round(
                sum(runtimes) / len(runtimes),
                2,
            ),
            benchmark_version="1.0.0",
        )
