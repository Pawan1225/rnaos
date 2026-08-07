"""
Tests for scientific report generator.
"""

from validation.reports.scientific_report_generator import (
    ScientificReportGenerator,
)


def test_scientific_report_generation() -> None:
    """
    Scientific report is generated.
    """

    generator = ScientificReportGenerator()

    report = generator.generate()

    assert report.report_id == ("REPORT_001")

    assert "Benchmark Results" in report.sections

    assert "ViennaRNA Baseline" in report.sections

    assert report.version == ("1.0.0")
