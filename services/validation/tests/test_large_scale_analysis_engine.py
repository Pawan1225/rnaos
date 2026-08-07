"""
Tests for large scale analysis.
"""

from validation.analyzers.large_scale_analysis_engine import (
    LargeScaleAnalysisEngine,
)


def test_large_scale_analysis():

    engine = LargeScaleAnalysisEngine()

    result = engine.analyze(
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

    assert result.average_accuracy == 0.95

    assert result.average_energy_gap == 0.3

    assert result.average_runtime == 2.0

    assert result.benchmark_version == ("1.0.0")
