import pytest
from research.analysis.statistical_analyzer import StatisticalAnalyzer
from research.metrics.evaluation_metrics import MetricsFactory


def build_metrics(
    runtime: float,
    reference: float,
    objective: float,
):
    return MetricsFactory.build(
        benchmark_id="toy001",
        solver_name="SA",
        objective_value=objective,
        runtime_seconds=runtime,
        reference_objective=reference,
    )


def test_summary():
    metrics = [
        build_metrics(0.10, -7.0, -6.8),
        build_metrics(0.20, -8.0, -7.9),
        build_metrics(0.30, -9.0, -8.7),
    ]

    summary = StatisticalAnalyzer().summarize(metrics)

    assert summary.sample_size == 3
    assert summary.mean_runtime > 0
    assert summary.fastest_runtime == 0.10
    assert summary.slowest_runtime == 0.30
    assert summary.mean_absolute_error >= 0
    assert summary.mean_relative_error >= 0
    assert 0.0 <= summary.mean_accuracy <= 1.0


def test_single_sample():
    metrics = [
        build_metrics(0.25, -5.0, -4.8),
    ]

    summary = StatisticalAnalyzer().summarize(metrics)

    assert summary.std_runtime == 0.0
    assert summary.std_absolute_error == 0.0


def test_empty_metrics():
    analyzer = StatisticalAnalyzer()

    with pytest.raises(ValueError):
        analyzer.summarize([])
