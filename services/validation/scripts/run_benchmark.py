"""
RNAOS benchmark execution script.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(
    0,
    str(SRC_PATH),
)


from validation.pipelines.validation_pipeline import (  # noqa: E402
    ValidationPipeline,
)


def main() -> None:
    """
    Execute RNAOS benchmark.
    """

    pipeline = ValidationPipeline()

    summary = pipeline.run(
        count=10,
        length=20,
    )

    print("RNAOS Benchmark Complete")

    print(f"Experiments: {summary.total_experiments}")

    print(f"Average Energy Gap: {summary.average_energy_gap}")

    print(f"Average Accuracy: {summary.average_accuracy}")


if __name__ == "__main__":
    main()
