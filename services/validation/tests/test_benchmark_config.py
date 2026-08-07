"""
Tests for benchmark configuration.
"""

from validation.models.benchmark_config import (
    BenchmarkConfig,
)


def test_benchmark_config() -> None:
    """
    Benchmark configuration creation works.
    """

    config = BenchmarkConfig(
        config_id="BENCHMARK_V1",
        dataset_size=50,
        sequence_length=20,
        random_seed=42,
        solver="hybrid_quantum_inspired",
        optimization_method="quantum_inspired",
        version="1.0.0",
    )

    assert config.dataset_size == 50

    assert config.sequence_length == 20

    assert config.random_seed == 42

    assert config.version == "1.0.0"
