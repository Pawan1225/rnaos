"""
Release report renderer for the RNAOS Enterprise Release Framework.
"""

from __future__ import annotations

import json

from enterprise.release.models import ReleaseReport


class ReleaseReportRenderer:
    """Render release reports."""

    def render_json(
        self,
        report: ReleaseReport,
    ) -> str:
        """Render report as JSON."""

        return json.dumps(
            {
                "total": report.total,
                "passed": report.passed,
                "failed": report.failed,
                "success": report.success,
            },
            indent=2,
        )

    def render_markdown(
        self,
        report: ReleaseReport,
    ) -> str:
        """Render report as Markdown."""

        return (
            "# Release Report\n\n"
            f"- Total: {report.total}\n"
            f"- Passed: {report.passed}\n"
            f"- Failed: {report.failed}\n"
            f"- Success: {report.success}\n"
        )

    def render_summary(
        self,
        report: ReleaseReport,
    ) -> str:
        """Render a one-line summary."""

        return f"{report.passed}/{report.total} releases passed."
