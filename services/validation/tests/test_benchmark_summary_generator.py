from validation.analyzers.benchmark_summary_generator import (
    BenchmarkSummaryGenerator,
)


def test_benchmark_summary_generation():

    generator = BenchmarkSummaryGenerator()

    summary = generator.generate(
        {
            "total_samples": 400,
            "average_accuracy": 0.94,
        },
        {
            "average_gap": 0.39,
            "minimum_gap": 0.0,
            "maximum_gap": 1.2,
        },
        {
            "average_runtime": 0.45,
            "scaling_by_length": {
                "20": 0.1,
            },
        },
        {
            "resource_scaling": {
                "20": 40,
            },
        },
    )

    assert summary["benchmark_id"] == "RNAOS_BENCHMARK_V1"

    assert summary["total_experiments"] == 400

    assert summary["accuracy"]["average"] == 0.94

    assert summary["energy"]["average_gap"] == 0.39
