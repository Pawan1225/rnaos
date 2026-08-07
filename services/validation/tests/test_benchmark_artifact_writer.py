"""
Tests for benchmark artifact writer.
"""

import json

from validation.export.benchmark_artifact_writer import (
    BenchmarkArtifactWriter,
)


def test_artifact_writer(tmp_path):

    writer = BenchmarkArtifactWriter(str(tmp_path))

    results = [
        {
            "experiment_id": 1,
            "accuracy": 0.95,
        }
    ]

    writer.write_results(results)

    writer.write_summary(
        {
            "total_experiments": 1,
        }
    )

    writer.write_manifest(
        {
            "version": "1.0.0",
        }
    )

    result_file = tmp_path / "experiment_results.json"

    summary_file = tmp_path / "benchmark_summary.json"

    manifest_file = tmp_path / "manifest.json"

    assert result_file.exists()

    assert summary_file.exists()

    assert manifest_file.exists()

    data = json.loads(result_file.read_text())

    assert data[0]["accuracy"] == 0.95
