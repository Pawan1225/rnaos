from research.analysis.statistical_summary import StatisticalSummary
from research.visualization.visualizer import Visualizer


def build_summary() -> StatisticalSummary:
    return StatisticalSummary(
        sample_size=10,
        mean_runtime=0.10,
        median_runtime=0.09,
        std_runtime=0.01,
        fastest_runtime=0.08,
        slowest_runtime=0.12,
        mean_absolute_error=0.20,
        median_absolute_error=0.19,
        std_absolute_error=0.03,
        mean_relative_error=0.04,
        mean_accuracy=0.95,
    )


def test_runtime_chart():
    summary = build_summary()

    chart = Visualizer().runtime_chart(summary)

    assert chart["mean_runtime"] == 0.10
    assert chart["fastest_runtime"] == 0.08


def test_accuracy_chart():
    summary = build_summary()

    chart = Visualizer().accuracy_chart(summary)

    assert chart["mean_accuracy"] == 0.95
    assert chart["mean_relative_error"] == 0.04


def test_error_chart():
    summary = build_summary()

    chart = Visualizer().error_chart(summary)

    assert chart["mean_absolute_error"] == 0.20
    assert chart["median_absolute_error"] == 0.19


def test_dashboard():
    summary = build_summary()

    dashboard = Visualizer().dashboard(summary)

    assert "runtime" in dashboard
    assert "accuracy" in dashboard
    assert "error" in dashboard
