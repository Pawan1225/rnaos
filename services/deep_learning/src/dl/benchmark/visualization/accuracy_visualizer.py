"""
RNAOS accuracy visualization module.
"""

from __future__ import annotations

from dl.models.benchmark.plot_configuration import (
    PlotConfiguration,
)
from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


class AccuracyVisualizer:
    """
    Creates structural accuracy visualization definitions.
    """

    def create_accuracy_plot(
        self,
        metrics: tuple[
            StructuralMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create accuracy comparison plot.
        """

        return PlotConfiguration(
            plot_id="ACCURACY_COMPARISON",
            title="Structural Accuracy Comparison",
            metric="base_pair_accuracy",
            chart_type="bar",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=accuracy",),
        )

    def create_f1_plot(
        self,
        metrics: tuple[
            StructuralMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create F1 score comparison plot.
        """

        return PlotConfiguration(
            plot_id="F1_SCORE_COMPARISON",
            title="F1 Score Comparison",
            metric="f1_score",
            chart_type="bar",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=structural_quality",),
        )
