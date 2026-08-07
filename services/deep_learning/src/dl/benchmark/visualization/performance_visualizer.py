"""
RNAOS performance visualization module.
"""

from __future__ import annotations

from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)
from dl.models.benchmark.plot_configuration import (
    PlotConfiguration,
)


class PerformanceVisualizer:
    """
    Creates performance visualization definitions.
    """

    def create_runtime_plot(
        self,
        metrics: tuple[
            PerformanceMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create runtime comparison plot.
        """

        return PlotConfiguration(
            plot_id="RUNTIME_COMPARISON",
            title="Runtime Comparison",
            metric="runtime",
            chart_type="bar",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=performance",),
        )

    def create_scalability_plot(
        self,
        metrics: tuple[
            PerformanceMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create scalability plot.
        """

        return PlotConfiguration(
            plot_id="SCALABILITY_COMPARISON",
            title="Scalability Comparison",
            metric="scalability_score",
            chart_type="line",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=scaling",),
        )
