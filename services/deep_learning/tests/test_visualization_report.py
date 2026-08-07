"""
Tests for visualization report.
"""

from __future__ import annotations

from dl.models.benchmark.visualization_report import (
    VisualizationReport,
)


def test_visualization_report() -> None:
    """
    Visualization report can be created.
    """

    report = VisualizationReport(
        report_id="VIS_001",
        experiment_id="EXP_001",
        figures=(
            "runtime_comparison",
            "energy_comparison",
        ),
        formats=(
            "PNG",
            "PDF",
        ),
        metadata=("version=14.7",),
    )

    assert report.report_id == ("VIS_001")

    assert report.experiment_id == ("EXP_001")

    assert (
        len(
            report.figures,
        )
        == 2
    )

    assert "PDF" in (report.formats)
