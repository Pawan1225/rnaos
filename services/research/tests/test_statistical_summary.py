from research.analysis.statistical_summary import StatisticalSummary


def test_has_samples():
    summary = StatisticalSummary(
        sample_size=5,
        mean_runtime=0.2,
        median_runtime=0.2,
        std_runtime=0.01,
        fastest_runtime=0.1,
        slowest_runtime=0.3,
        mean_absolute_error=0.5,
        median_absolute_error=0.5,
        std_absolute_error=0.1,
        mean_relative_error=0.05,
        mean_accuracy=0.95,
    )

    assert summary.has_samples


def test_empty_summary():
    summary = StatisticalSummary(
        sample_size=0,
        mean_runtime=0.0,
        median_runtime=0.0,
        std_runtime=0.0,
        fastest_runtime=0.0,
        slowest_runtime=0.0,
        mean_absolute_error=0.0,
        median_absolute_error=0.0,
        std_absolute_error=0.0,
        mean_relative_error=0.0,
        mean_accuracy=0.0,
    )

    assert not summary.has_samples
