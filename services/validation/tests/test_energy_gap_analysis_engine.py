"""
Tests for energy gap analysis engine.
"""

from validation.analyzers.energy_gap_analysis_engine import (
    EnergyGapAnalysisEngine,
)


def test_energy_gap_analysis():

    engine = EnergyGapAnalysisEngine()

    result = engine.analyze(
        (
            0.2,
            0.4,
            0.6,
        )
    )

    assert result.sample_count == 3

    assert result.average_gap == 0.4

    assert result.minimum_gap == 0.2

    assert result.maximum_gap == 0.6

    assert result.benchmark_version == ("1.0.0")
