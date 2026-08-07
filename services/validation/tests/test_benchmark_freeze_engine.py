"""
Tests for benchmark freeze engine.
"""

from validation.release.benchmark_freeze_engine import (
    BenchmarkFreezeEngine,
)


def test_benchmark_freeze():

    engine = BenchmarkFreezeEngine()

    result = engine.freeze(
        total_experiments=400,
        artifact_count=7,
    )

    assert result.freeze_id == ("FREEZE_V1")

    assert result.total_experiments == 400

    assert result.artifact_count == 7

    assert result.status == ("FROZEN")

    assert result.benchmark_version == ("1.0.0")
