"""
Tests for large benchmark result analyzer.
"""

from validation.analyzers.large_benchmark_result_analyzer import (
    LargeBenchmarkResultAnalyzer,
)


def test_large_benchmark_analysis():

    analyzer = LargeBenchmarkResultAnalyzer()

    result = analyzer.analyze(
        accuracies=(
            0.90,
            0.95,
            1.00,
        ),
        energy_gaps=(
            0.2,
            0.3,
            0.4,
        ),
        runtimes=(
            1.0,
            2.0,
            3.0,
        ),
    )

    assert result.total_experiments == 3

    assert (
        round(
            result.average_accuracy,
            2,
        )
        == 0.95
    )

    assert (
        round(
            result.average_energy_gap,
            2,
        )
        == 0.30
    )

    assert (
        round(
            result.average_runtime,
            2,
        )
        == 2.0
    )

    assert result.best_score == 1.0

    assert result.version == ("1.0.0")
