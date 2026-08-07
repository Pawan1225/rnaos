"""
Tests for report builder.
"""

from __future__ import annotations

from dl.benchmark.reporting.report_builder import (
    ReportBuilder,
)


def test_report_builder() -> None:
    """
    Report builder creates reports.
    """

    builder = ReportBuilder()

    report = builder.build(
        report_id="REPORT_001",
        experiment_id="EXP_001",
        summary=("RNAOS benchmark evaluation"),
        results=("CASE_001",),
        statistics=("STAT_001",),
        figures=("VIS_REPORT_001",),
        conclusions=("Hybrid optimizer improved results",),
        metadata=("version=14.7",),
    )

    assert report.report_id == ("REPORT_001")

    assert report.experiment_id == ("EXP_001")

    assert (
        len(
            report.results,
        )
        == 1
    )

    assert (
        len(
            report.figures,
        )
        == 1
    )
