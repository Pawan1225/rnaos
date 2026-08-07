"""
Tests for scientific report generator.
"""

from __future__ import annotations

from dl.submission.reports.scientific_report_generator import (
    ScientificReportGenerator,
)


def test_scientific_report_generation() -> None:
    """
    Scientific report artifact is generated.
    """

    generator = ScientificReportGenerator()

    report = generator.generate()

    assert report.report_id == ("SCIENTIFIC_REPORT_001")

    assert "Architecture" in report.sections

    assert report.version == ("1.0.0")

    assert report.benchmark_reference == "BENCHMARK_REPORT_001"
