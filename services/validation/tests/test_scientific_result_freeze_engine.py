"""
Tests for scientific result freeze.
"""

from validation.release.scientific_result_freeze_engine import (
    ScientificResultFreezeEngine,
)


def test_scientific_result_freeze():

    engine = ScientificResultFreezeEngine()

    result = engine.freeze(
        benchmark_id=("RNAOS_LARGE_BENCHMARK_V1"),
        total_experiments=400,
    )

    assert result.freeze_id == ("SCIENCE_FREEZE_V1")

    assert result.total_experiments == 400

    assert result.status == ("FROZEN")

    assert result.result_version == ("1.0.0")
