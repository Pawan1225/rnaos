"""
Tests for accuracy visualization.
"""

from __future__ import annotations

from dl.benchmark.visualization.accuracy_visualizer import (
    AccuracyVisualizer,
)
from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


def test_accuracy_visualization() -> None:
    """
    Accuracy plot configuration is created.
    """

    visualizer = AccuracyVisualizer()

    metrics = (
        StructuralMetrics(
            base_pair_accuracy=0.95,
            sensitivity=0.94,
            specificity=0.96,
            precision=0.93,
            recall=0.94,
            f1_score=0.935,
        ),
    )

    plot = visualizer.create_accuracy_plot(
        metrics,
    )

    assert plot.metric == ("base_pair_accuracy")

    assert plot.chart_type == ("bar")


def test_f1_visualization() -> None:
    """
    F1 plot configuration is created.
    """

    visualizer = AccuracyVisualizer()

    plot = visualizer.create_f1_plot(
        (),
    )

    assert plot.metric == ("f1_score")
