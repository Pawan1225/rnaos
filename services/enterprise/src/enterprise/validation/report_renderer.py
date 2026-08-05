"""
Enterprise validation report renderer.
"""

from __future__ import annotations

import json

from enterprise.validation.models import (
    ValidationReport,
)


class ValidationReportRenderer:
    """Render validation reports in multiple formats."""

    def render_json(
        self,
        report: ValidationReport,
    ) -> str:
        """Render a validation report as JSON."""

        return json.dumps(
            {
                "total": report.total,
                "passed": report.passed,
                "failed": report.failed,
                "skipped": report.skipped,
                "warnings": report.warnings,
                "success": report.success,
            },
            indent=4,
        )

    def render_markdown(
        self,
        report: ValidationReport,
    ) -> str:
        """Render a validation report as Markdown."""

        return (
            "# RNAOS Validation Report\n\n"
            f"- Total: {report.total}\n"
            f"- Passed: {report.passed}\n"
            f"- Failed: {report.failed}\n"
            f"- Skipped: {report.skipped}\n"
            f"- Warnings: {report.warnings}\n"
            f"- Success: {report.success}\n"
        )

    def render_summary(
        self,
        report: ValidationReport,
    ) -> str:
        """Render a one-line validation summary."""

        return f"{report.passed}/{report.total} validations passed ({report.failed} failed)"
