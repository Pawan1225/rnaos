"""
Tests for statistical analysis engine.
"""

from validation.analyzers.statistical_analysis_engine import (
    StatisticalAnalysisEngine,
)


def test_statistical_analysis() -> None:
    """
    Statistical metrics are calculated.
    """

    engine = StatisticalAnalysisEngine()

    result = engine.analyze(
        (
            1.0,
            2.0,
            3.0,
        ),
        "accuracy",
    )

    assert result.sample_count == 3

    assert result.mean == 2.0

    assert result.minimum == 1.0

    assert result.maximum == 3.0

    assert result.version == "1.0.0"
