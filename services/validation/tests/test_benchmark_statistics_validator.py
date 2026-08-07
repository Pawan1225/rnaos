from validation.analysis.benchmark_statistics_validator import (
    BenchmarkStatisticsValidator,
)


def test_statistics_generation():

    results = [
        {
            "accuracy": 0.90,
            "energy_gap": 0.2,
            "runtime_seconds": 0.1,
            "estimated_qubits": 40,
        },
        {
            "accuracy": 1.00,
            "energy_gap": 0.4,
            "runtime_seconds": 0.3,
            "estimated_qubits": 80,
        },
    ]

    validator = BenchmarkStatisticsValidator()

    report = validator.generate(results)

    assert report["benchmark"] == "RNAOS_LARGE_V1"

    assert report["experiments"] == 2

    assert report["accuracy"]["mean"] == 0.95

    assert report["quantum_resources"]["max_estimated_qubits"] == 80
