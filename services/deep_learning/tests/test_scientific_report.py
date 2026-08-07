"""
Tests for scientific report.
"""

from __future__ import annotations

from dl.models.benchmark.scientific_report import (
    ScientificReport,
)


def test_scientific_report() -> None:
    """
    Scientific report can be created.
    """

    report = ScientificReport(
        report_id="REPORT_001",
        title="RNAOS Benchmark Report",
        experiment_id="EXP_001",
        summary="Hybrid optimization evaluation",
        results=("CASE_001",),
        statistics=("STAT_001",),
        figures=("VIS_REPORT_001",),
        conclusions=("RNAOS improved baseline performance",),
        metadata=("version=14.7",),
    )

    assert report.report_id == ("REPORT_001")

    assert report.experiment_id == ("EXP_001")

    assert (
        len(
            report.figures,
        )
        == 1
    )

    assert "STAT_001" in report.statistics
