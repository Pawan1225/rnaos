"""
RNAOS scientific report builder.
"""

from __future__ import annotations

from dl.models.benchmark.scientific_report import (
    ScientificReport,
)


class ReportBuilder:
    """
    Builds scientific benchmark reports.
    """

    def build(
        self,
        report_id: str,
        experiment_id: str,
        summary: str,
        results: tuple[str, ...],
        statistics: tuple[str, ...],
        figures: tuple[str, ...],
        conclusions: tuple[str, ...],
        metadata: tuple[str, ...],
    ) -> ScientificReport:
        """
        Assemble scientific report.
        """

        return ScientificReport(
            report_id=report_id,
            title=("RNAOS Scientific Benchmark Report"),
            experiment_id=experiment_id,
            summary=summary,
            results=results,
            statistics=statistics,
            figures=figures,
            conclusions=conclusions,
            metadata=metadata,
        )
