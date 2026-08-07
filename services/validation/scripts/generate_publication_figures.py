"""
Generate fresh RNAOS benchmark figures.
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

from validation.export.publication_figure_exporter import (  # noqa: E402
    PublicationFigureExporter,
)

INPUT = "validation_results/large_benchmark_v1/experiment_results.json"

OUTPUT = "validation_results/large_benchmark_v1/figures"


def main() -> None:

    print("Generating fresh RNAOS figures")

    with open(INPUT) as file:
        results = json.load(file)

    exporter = PublicationFigureExporter(
        OUTPUT,
    )

    manifest = exporter.export(
        results,
    )

    print("Figures generated")

    print(manifest)


if __name__ == "__main__":
    main()
