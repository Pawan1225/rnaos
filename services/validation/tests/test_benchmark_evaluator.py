"""
Tests for RNAOS benchmark evaluator.
"""

from validation.evaluation.benchmark_evaluator import (
    BenchmarkEvaluator,
)
from validation.models.dataset_entry import (
    DatasetEntry,
)


def test_benchmark_evaluator():

    entry = DatasetEntry(
        sequence_id="RNA_001",
        sequence="GGCAU",
        length=5,
        category="RNA_5",
        seed=42,
        metadata=(),
    )

    evaluator = BenchmarkEvaluator()

    result = evaluator.evaluate(
        entry=entry,
        experiment_id=1,
    )

    assert result.experiment_id == 1

    assert result.sequence == "GGCAU"

    assert result.sequence_length == 5

    assert result.energy_gap == 0.0

    assert result.accuracy == 1.0

    assert result.estimated_qubits == 10
