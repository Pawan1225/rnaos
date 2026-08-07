"""
Tests for benchmark statistics.
"""

from validation.analysis.benchmark_statistics import (
    BenchmarkStatistics,
)


def test_statistics_generation():

    analyzer = BenchmarkStatistics()

    results = [
        {
            "sequence_length": 20,
            "accuracy": 1.0,
            "structure_f1": 1.0,
            "energy_gap": 0.0,
            "runtime_seconds": 0.1,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 20,
            "accuracy": 0.5,
            "structure_f1": 0.8,
            "energy_gap": 2.0,
            "runtime_seconds": 0.2,
            "estimated_qubits": 40,
        },
    ]

    output = analyzer.generate(
        results,
    )

    assert output["20"]["samples"] == 2
    assert output["20"]["average_accuracy"] == 0.75
