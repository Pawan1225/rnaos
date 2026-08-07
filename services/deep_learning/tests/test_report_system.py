"""
Tests for scientific report system.
"""

from __future__ import annotations

from dl.benchmark.reporting.export_manager import (
    ExportManager,
)
from dl.benchmark.reporting.report_builder import (
    ReportBuilder,
)
from dl.benchmark.reporting.result_summary_generator import (
    ResultSummaryGenerator,
)


def test_complete_report_pipeline() -> None:
    """
    Complete report generation pipeline works.
    """

    summary_generator = ResultSummaryGenerator()

    summary = summary_generator.generate()

    builder = ReportBuilder()

    report = builder.build(
        report_id="REPORT_001",
        experiment_id="EXP_001",
        summary=summary.summary_text,
        results=("CASE_001",),
        statistics=("STAT_001",),
        figures=("VIS_REPORT_001",),
        conclusions=summary.key_findings,
        metadata=("version=14.7",),
    )

    exporter = ExportManager()

    exported = exporter.export_json(
        report,
    )

    assert report.report_id == ("REPORT_001")

    assert report.experiment_id == ("EXP_001")

    assert exported["title"]

    assert (
        len(
            report.conclusions,
        )
        == 3
    )


def test_markdown_report_generation() -> None:
    """
    Markdown report generation works.
    """

    builder = ReportBuilder()

    report = builder.build(
        report_id="REPORT_002",
        experiment_id="EXP_002",
        summary="RNAOS evaluation",
        results=(),
        statistics=(),
        figures=(),
        conclusions=(),
        metadata=(),
    )

    exporter = ExportManager()

    markdown = exporter.export_markdown(
        report,
    )

    assert "RNAOS Scientific" in markdown
