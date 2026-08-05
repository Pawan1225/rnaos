"""
Benchmark report renderer for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

import json

from enterprise.benchmark.models import BenchmarkReport


class BenchmarkReportRenderer:
    """Render benchmark reports."""

    def render_json(
        self,
        report: BenchmarkReport,
    ) -> str:
        """Render report as JSON."""

        return json.dumps(
            {
                "total": report.total,
                "passed": report.passed,
                "failed": report.failed,
                "success": report.success,
                "total_runtime": report.total_runtime,
                "average_runtime": report.average_runtime,
            },
            indent=2,
        )

    def render_markdown(
        self,
        report: BenchmarkReport,
    ) -> str:
        """Render report as Markdown."""

        return (
            "# Benchmark Report\n\n"
            f"- Total: {report.total}\n"
            f"- Passed: {report.passed}\n"
            f"- Failed: {report.failed}\n"
            f"- Success: {report.success}\n"
            f"- Total Runtime: {report.total_runtime:.6f}s\n"
            f"- Average Runtime: {report.average_runtime:.6f}s\n"
        )

    def render_summary(
        self,
        report: BenchmarkReport,
    ) -> str:
        """Render a one-line summary."""

        return f"{report.passed}/{report.total} benchmarks passed in {report.total_runtime:.6f}s."
