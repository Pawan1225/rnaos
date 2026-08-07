"""
RNAOS large benchmark campaign runner.
"""

from __future__ import annotations

import sys
from pathlib import Path


def setup_import_path() -> None:
    """
    Add validation src directory to Python path.
    """

    src_path = Path(__file__).resolve().parents[1] / "src"

    sys.path.insert(
        0,
        str(src_path),
    )


def main() -> None:
    """
    Execute large benchmark campaign.
    """

    setup_import_path()

    from validation.datasets.large_dataset_generator import (
        LargeDatasetGenerator,
    )
    from validation.export.benchmark_artifact_writer import (
        BenchmarkArtifactWriter,
    )
    from validation.export.campaign_result_exporter import (
        CampaignResultExporter,
    )
    from validation.runners.campaign_execution_engine import (
        CampaignExecutionEngine,
    )

    print("Starting RNAOS Large Benchmark Campaign")

    dataset = LargeDatasetGenerator().generate(
        samples_per_length=100,
        seed=42,
    )

    print(f"Dataset size: {dataset.total_sequences}")

    runner = CampaignExecutionEngine()

    result = runner.run(dataset)

    print("Campaign Complete")

    print(f"Total experiments: {result.total_experiments}")

    print(f"Completed: {result.completed_experiments}")

    print(f"Failed: {result.failed_experiments}")

    exporter = CampaignResultExporter()

    experiment_results = exporter.export(result)

    summary = {
        "total_experiments": (result.total_experiments),
        "completed": (result.completed_experiments),
        "failed": (result.failed_experiments),
        "benchmark_id": ("RNAOS_LARGE_BENCHMARK_V1"),
        "dataset_size": (dataset.total_sequences),
        "seed": 42,
    }

    writer = BenchmarkArtifactWriter("validation_results/large_benchmark_v1")

    writer.write_results(experiment_results)

    writer.write_summary(summary)

    writer.write_manifest(
        {
            "benchmark_id": ("RNAOS_LARGE_BENCHMARK_V1"),
            "dataset": ("Synthetic RNA"),
            "sequence_lengths": [
                20,
                40,
                60,
                80,
            ],
            "experiments": (dataset.total_sequences),
            "seed": 42,
            "status": "COMPLETED",
        }
    )

    print("Artifacts written:")

    print("validation_results/large_benchmark_v1/")

    print("- experiment_results.json")

    print("- benchmark_summary.json")

    print("- manifest.json")


if __name__ == "__main__":
    main()
