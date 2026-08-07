"""
Tests for accuracy analysis engine.
"""

from validation.analyzers.accuracy_analysis_engine import (
    AccuracyAnalysisEngine,
)


def test_accuracy_analysis():

    engine = AccuracyAnalysisEngine()

    result = engine.analyze(
        (
            0.95,
            0.90,
            1.00,
        )
    )

    assert result.sample_count == 3

    assert result.average_accuracy == (0.95)

    assert result.minimum_accuracy == (0.90)

    assert result.maximum_accuracy == (1.00)

    assert result.benchmark_version == ("1.0.0")
