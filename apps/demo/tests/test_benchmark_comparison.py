"""
Tests for benchmark comparison.
"""

from apps.demo.comparison.benchmark_comparison_engine import (
    BenchmarkComparisonEngine,
)


class FakeRNAOSResult:
    """
    Fake RNAOS output.
    """

    sequence = "GGCAU"

    predicted_structure = "(((...)))"

    energy_gap = 0.1

    runtime = 1.0


class FakeReferenceResult:
    """
    Fake ViennaRNA output.
    """

    structure = "(((...)))"

    runtime = 0.5


def test_benchmark_comparison():

    engine = BenchmarkComparisonEngine()

    result = engine.compare(
        FakeRNAOSResult(),
        FakeReferenceResult(),
    )

    assert result.sequence == "GGCAU"

    assert result.structure_accuracy == 1.0

    assert result.energy_gap == 0.1

    assert result.reference_runtime == 0.5

    assert result.status == "COMPLETE"
