"""
Tests for benchmark export engine.
"""

from validation.export.benchmark_export_engine import (
    BenchmarkExportEngine,
)


def test_benchmark_export(
    tmp_path,
) -> None:
    """
    Benchmark artifacts are exported.
    """

    engine = BenchmarkExportEngine()

    manifest = engine.export(
        str(tmp_path),
    )

    assert manifest.export_id == ("EXPORT_001")

    assert "benchmark_results.json" in manifest.files

    assert manifest.benchmark_version == ("1.0.0")
