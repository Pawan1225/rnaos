"""
Tests for energy visualization.
"""

from __future__ import annotations

from dl.benchmark.visualization.energy_visualizer import (
    EnergyVisualizer,
)
from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)


def test_energy_visualization() -> None:
    """
    Energy plot configuration is created.
    """

    visualizer = EnergyVisualizer()

    metrics = (
        EnergyMetrics(
            reference_energy=-32.5,
            predicted_energy=-35.0,
            energy_gap=2.5,
            relative_error=0.07,
            improvement=0.07,
        ),
    )

    plot = visualizer.create_energy_plot(
        metrics,
    )

    assert plot.metric == ("predicted_energy")

    assert plot.chart_type == ("bar")


def test_energy_gap_visualization() -> None:
    """
    Energy gap plot configuration is created.
    """

    visualizer = EnergyVisualizer()

    plot = visualizer.create_energy_gap_plot(
        (),
    )

    assert plot.metric == ("energy_gap")
