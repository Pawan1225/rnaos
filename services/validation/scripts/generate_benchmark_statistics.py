"""
Generate RNAOS benchmark statistics.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"

sys.path.insert(
    0,
    str(ROOT),
)

from validation.analysis.benchmark_statistics import (  # noqa: E402
    BenchmarkStatistics,
)

INPUT = "validation_results/large_benchmark_v1/experiment_results.json"

OUTPUT = "validation_results/large_benchmark_v1/benchmark_statistics.json"


def main() -> None:
    print("Generating benchmark statistics")

    with open(INPUT) as file:
        results = json.load(file)

    analyzer = BenchmarkStatistics()

    statistics = analyzer.generate(
        results,
    )

    with open(
        OUTPUT,
        "w",
    ) as file:
        json.dump(
            statistics,
            file,
            indent=2,
        )

    print("Benchmark statistics generated")

    print(OUTPUT)


if __name__ == "__main__":
    main()
