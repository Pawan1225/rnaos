"""
RNAOS scientific report export manager.
"""

from __future__ import annotations

from dataclasses import asdict

from dl.models.benchmark.scientific_report import (
    ScientificReport,
)


class ExportManager:
    """
    Exports scientific reports.
    """

    def export_json(
        self,
        report: ScientificReport,
    ) -> dict:
        """
        Export report as dictionary.
        """

        return asdict(
            report,
        )

    def export_markdown(
        self,
        report: ScientificReport,
    ) -> str:
        """
        Export report as markdown text.
        """

        return f"# {report.title}\n\n{report.summary}\n"
