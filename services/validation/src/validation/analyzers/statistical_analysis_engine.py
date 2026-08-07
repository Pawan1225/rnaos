"""
RNAOS statistical analysis engine.
"""

from __future__ import annotations

import math

from validation.models.statistical_summary import (
    StatisticalSummary,
)


class StatisticalAnalysisEngine:
    """
    Performs benchmark statistics.
    """

    def analyze(
        self,
        values: tuple[float, ...],
        metric_name: str,
    ) -> StatisticalSummary:
        """
        Analyze metric distribution.
        """

        if not values:
            raise ValueError("No values provided")

        mean = sum(values) / len(values)

        variance = sum((value - mean) ** 2 for value in values) / len(values)

        standard_deviation = math.sqrt(variance)

        stability_score = 1.0 / (1.0 + standard_deviation)

        return StatisticalSummary(
            metric_name=metric_name,
            sample_count=len(values),
            mean=mean,
            minimum=min(values),
            maximum=max(values),
            standard_deviation=standard_deviation,
            stability_score=stability_score,
            version="1.0.0",
        )
