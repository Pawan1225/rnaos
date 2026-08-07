"""
RNAOS energy visualization module.
"""

from __future__ import annotations

from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)
from dl.models.benchmark.plot_configuration import (
    PlotConfiguration,
)


class EnergyVisualizer:
    """
    Creates energy visualization definitions.
    """

    def create_energy_plot(
        self,
        metrics: tuple[
            EnergyMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create energy comparison plot.
        """

        return PlotConfiguration(
            plot_id="ENERGY_COMPARISON",
            title="Energy Comparison",
            metric="predicted_energy",
            chart_type="bar",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=energy",),
        )

    def create_energy_gap_plot(
        self,
        metrics: tuple[
            EnergyMetrics,
            ...,
        ],
    ) -> PlotConfiguration:
        """
        Create energy gap visualization.
        """

        return PlotConfiguration(
            plot_id="ENERGY_GAP_COMPARISON",
            title="Energy Gap Comparison",
            metric="energy_gap",
            chart_type="bar",
            formats=(
                "PNG",
                "PDF",
            ),
            width=12.0,
            height=8.0,
            dpi=300,
            metadata=("type=energy_difference",),
        )
