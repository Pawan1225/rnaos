"""
RNAOS accuracy analysis engine.
"""

from __future__ import annotations

from validation.models.accuracy_analysis import (
    AccuracyAnalysis,
)


class AccuracyAnalysisEngine:
    """
    Analyzes RNAOS structure accuracy.
    """

    def analyze(
        self,
        values: tuple[float, ...],
    ) -> AccuracyAnalysis:
        """
        Calculate accuracy statistics.
        """

        if not values:
            raise ValueError("No accuracy values provided")

        return AccuracyAnalysis(
            analysis_id="ACCURACY_ANALYSIS_001",
            sample_count=len(values),
            average_accuracy=round(
                sum(values) / len(values),
                10,
            ),
            minimum_accuracy=min(values),
            maximum_accuracy=max(values),
            benchmark_version="1.0.0",
        )
