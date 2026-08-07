"""
Tests for result aggregation engine.
"""

from validation.analyzers.result_aggregation_engine import (
    ResultAggregationEngine,
)
from validation.models.comparison_result import (
    ComparisonResult,
)


def test_result_aggregation() -> None:
    """
    Benchmark results are aggregated.
    """

    engine = ResultAggregationEngine()

    results = (
        ComparisonResult(
            sequence="AUGCUA",
            structure_accuracy=1.0,
            energy_gap=0.2,
            runtime_difference=1.0,
            qubit_difference=0,
            overall_score=0.83,
        ),
        ComparisonResult(
            sequence="GGGAAA",
            structure_accuracy=0.8,
            energy_gap=0.5,
            runtime_difference=2.0,
            qubit_difference=2,
            overall_score=0.53,
        ),
    )

    summary = engine.aggregate(
        results,
    )

    assert summary.total_experiments == 2

    assert summary.average_energy_gap == 0.35

    assert summary.average_accuracy == 0.9

    assert summary.version == "1.0.0"
