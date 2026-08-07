"""
Tests for large benchmark configuration.
"""

from validation.models.large_benchmark_config import (
    LargeBenchmarkConfig,
)


def test_large_benchmark_config():

    config = LargeBenchmarkConfig(
        benchmark_id="RNAOS_LARGE_BENCHMARK_V1",
        sequence_lengths=(
            20,
            40,
            60,
            80,
        ),
        samples_per_length=100,
        random_seed=42,
        solver_version="1.0.0",
        benchmark_version="1.0.0",
        total_experiments=400,
    )

    assert config.benchmark_id == ("RNAOS_LARGE_BENCHMARK_V1")

    assert len(config.sequence_lengths) == 4

    assert config.samples_per_length == 100

    assert config.total_experiments == 400

    assert config.random_seed == 42
