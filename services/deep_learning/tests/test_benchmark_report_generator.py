"""
Tests for benchmark report generator.
"""

from __future__ import annotations

from dl.submission.reports.benchmark_report_generator import (
    BenchmarkReportGenerator,
)


def test_benchmark_report_generation() -> None:
    """
    Benchmark report artifact is generated.
    """

    generator = BenchmarkReportGenerator()

    report = generator.generate()

    assert report.report_id == ("BENCHMARK_REPORT_001")

    assert "accuracy" in report.metrics

    assert "ViennaRNA comparison" in report.benchmarks

    assert report.version == ("1.0.0")
