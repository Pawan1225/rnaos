"""
Tests for plot configuration.
"""

from __future__ import annotations

from dl.models.benchmark.plot_configuration import (
    PlotConfiguration,
)


def test_plot_configuration() -> None:
    """
    Plot configuration can be created.
    """

    config = PlotConfiguration(
        plot_id="PLOT_001",
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
        metadata=("style=scientific",),
    )

    assert config.plot_id == ("PLOT_001")

    assert config.metric == ("runtime")

    assert config.chart_type == ("bar")

    assert config.dpi == 300
