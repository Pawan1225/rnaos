from validation.analyzers.large_benchmark_scientific_analyzer import (
    LargeBenchmarkScientificAnalyzer,
)


def test_scientific_analysis():

    results = [
        {
            "sequence_length": 20,
            "accuracy": 0.9,
            "energy_gap": 0.2,
            "runtime_seconds": 0.1,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 40,
            "accuracy": 1.0,
            "energy_gap": 0.4,
            "runtime_seconds": 0.3,
            "estimated_qubits": 80,
        },
    ]

    analyzer = LargeBenchmarkScientificAnalyzer()

    output = analyzer.analyze(results)

    assert output["accuracy_analysis"]["average_accuracy"] == 0.95

    assert output["energy_gap_analysis"]["average_gap"] == 0.3

    assert output["quantum_resource_scaling"]["estimated_resources"]["20"] == 40
