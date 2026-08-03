from __future__ import annotations

from research.datasets.benchmark_dataset import BenchmarkDataset
from research.models.benchmark_case import BenchmarkCase


def load_toy_dataset() -> BenchmarkDataset:
    dataset = BenchmarkDataset("Toy Benchmark")

    dataset.add_case(
        BenchmarkCase(
            sequence_id="toy_001",
            sequence="GGGAAAUCC",
            source="synthetic",
        )
    )

    dataset.add_case(
        BenchmarkCase(
            sequence_id="toy_002",
            sequence="AUGCGGAU",
            source="synthetic",
        )
    )

    dataset.add_case(
        BenchmarkCase(
            sequence_id="toy_003",
            sequence="GGCCAAUU",
            source="synthetic",
        )
    )

    return dataset
