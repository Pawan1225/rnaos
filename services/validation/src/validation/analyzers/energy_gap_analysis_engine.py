"""
RNAOS energy gap analysis engine.
"""

from __future__ import annotations

from validation.models.energy_gap_analysis import (
    EnergyGapAnalysis,
)


class EnergyGapAnalysisEngine:
    """
    Analyzes RNAOS energy differences.
    """

    def analyze(
        self,
        values: tuple[float, ...],
    ) -> EnergyGapAnalysis:
        """
        Calculate energy gap statistics.
        """

        if not values:
            raise ValueError("No energy gap values provided")

        average_gap = round(
            sum(values) / len(values),
            10,
        )

        stability_score = round(
            1.0 / (1.0 + average_gap),
            10,
        )

        return EnergyGapAnalysis(
            analysis_id="ENERGY_GAP_ANALYSIS_001",
            sample_count=len(values),
            average_gap=average_gap,
            minimum_gap=min(values),
            maximum_gap=max(values),
            stability_score=stability_score,
            benchmark_version="1.0.0",
        )
