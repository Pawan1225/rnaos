"""
Tests for export manager.
"""

from __future__ import annotations

from dl.benchmark.reporting.export_manager import (
    ExportManager,
)
from dl.models.benchmark.scientific_report import (
    ScientificReport,
)


def test_json_export() -> None:
    """
    JSON export works.
    """

    manager = ExportManager()

    report = ScientificReport(
        report_id="REPORT_001",
        title="RNAOS Report",
        experiment_id="EXP_001",
        summary="Benchmark evaluation",
        results=("CASE_001",),
        statistics=(),
        figures=(),
        conclusions=(),
        metadata=(),
    )

    exported = manager.export_json(
        report,
    )

    assert exported["report_id"] == ("REPORT_001")


def test_markdown_export() -> None:
    """
    Markdown export works.
    """

    manager = ExportManager()

    report = ScientificReport(
        report_id="REPORT_001",
        title="RNAOS Report",
        experiment_id="EXP_001",
        summary="Benchmark evaluation",
        results=(),
        statistics=(),
        figures=(),
        conclusions=(),
        metadata=(),
    )

    markdown = manager.export_markdown(
        report,
    )

    assert "# RNAOS Report" in markdown
