"""
Tests for runtime scaling analysis.
"""

from validation.analyzers.runtime_scaling_analysis_engine import (
    RuntimeScalingAnalysisEngine,
)


def test_runtime_scaling_analysis():

    engine = RuntimeScalingAnalysisEngine()

    result = engine.analyze(
        (
            1.0,
            2.0,
            4.0,
        )
    )

    assert result.sample_count == 3

    assert result.average_runtime == (7.0 / 3.0)

    assert result.minimum_runtime == 1.0

    assert result.maximum_runtime == 4.0

    assert result.scaling_factor == 4.0

    assert result.benchmark_version == ("1.0.0")
