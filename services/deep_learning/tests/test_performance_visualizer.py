"""
Tests for performance visualization.
"""

from __future__ import annotations

from dl.benchmark.visualization.performance_visualizer import (
    PerformanceVisualizer,
)
from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)


def test_runtime_visualization() -> None:
    """
    Runtime plot configuration is created.
    """

    visualizer = PerformanceVisualizer()

    metrics = (
        PerformanceMetrics(
            runtime=2.0,
            memory_usage=512.0,
            cpu_usage=80.0,
            iterations=100,
            solver_calls=2,
            scalability_score=0.9,
        ),
    )

    plot = visualizer.create_runtime_plot(
        metrics,
    )

    assert plot.metric == ("runtime")

    assert plot.chart_type == ("bar")


def test_scalability_visualization() -> None:
    """
    Scalability plot configuration is created.
    """

    visualizer = PerformanceVisualizer()

    plot = visualizer.create_scalability_plot(
        (),
    )

    assert plot.metric == ("scalability_score")

    assert plot.chart_type == ("line")
