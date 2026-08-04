"""
Research report generator.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from io import StringIO
from pathlib import Path

from research.reporting.research_report import ResearchReport


class ReportGenerator:
    """
    Generate publication-ready research reports.
    """

    def to_markdown(
        self,
        report: ResearchReport,
    ) -> str:
        """
        Generate a Markdown representation of a research report.
        """
        summary = report.summary

        authors = ", ".join(report.authors) if report.has_authors else "Unknown"

        return f"""# {report.title}

## Authors

{authors}

---

## Benchmark Summary

| Metric | Value |
|--------|------:|
| Sample Size | {summary.sample_size} |
| Mean Runtime | {summary.mean_runtime:.4f} s |
| Median Runtime | {summary.median_runtime:.4f} s |
| Runtime Std Dev | {summary.std_runtime:.4f} s |
| Fastest Runtime | {summary.fastest_runtime:.4f} s |
| Slowest Runtime | {summary.slowest_runtime:.4f} s |
| Mean Absolute Error | {summary.mean_absolute_error:.4f} |
| Median Absolute Error | {summary.median_absolute_error:.4f} |
| Absolute Error Std Dev | {summary.std_absolute_error:.4f} |
| Mean Relative Error | {summary.mean_relative_error:.4f} |
| Mean Accuracy | {summary.mean_accuracy:.4f} |
"""

    def to_json(
        self,
        report: ResearchReport,
    ) -> str:
        """
        Generate a JSON representation of a research report.
        """
        report_dict = {
            "title": report.title,
            "authors": report.authors,
            "metadata": report.metadata,
            "summary": asdict(report.summary),
        }

        return json.dumps(
            report_dict,
            indent=4,
        )

    def to_csv(
        self,
        report: ResearchReport,
    ) -> str:
        """
        Generate a CSV representation of a research report.
        """
        summary = report.summary

        output = StringIO()
        writer = csv.writer(output)

        writer.writerow(["Metric", "Value"])

        writer.writerow(["Sample Size", summary.sample_size])
        writer.writerow(["Mean Runtime", summary.mean_runtime])
        writer.writerow(["Median Runtime", summary.median_runtime])
        writer.writerow(["Runtime Std Dev", summary.std_runtime])
        writer.writerow(["Fastest Runtime", summary.fastest_runtime])
        writer.writerow(["Slowest Runtime", summary.slowest_runtime])
        writer.writerow(["Mean Absolute Error", summary.mean_absolute_error])
        writer.writerow(["Median Absolute Error", summary.median_absolute_error])
        writer.writerow(["Absolute Error Std Dev", summary.std_absolute_error])
        writer.writerow(["Mean Relative Error", summary.mean_relative_error])
        writer.writerow(["Mean Accuracy", summary.mean_accuracy])

        return output.getvalue()

    def save(
        self,
        report: ResearchReport,
        path: str | Path,
        *,
        format: str = "markdown",
    ) -> None:
        """
        Save a report to disk.

        Supported formats:
        - markdown
        - json
        - csv
        """
        path = Path(path)

        match format.lower():
            case "markdown" | "md":
                content = self.to_markdown(report)

            case "json":
                content = self.to_json(report)

            case "csv":
                content = self.to_csv(report)

            case _:
                raise ValueError(f"Unsupported report format: {format}")

        path.write_text(
            content,
            encoding="utf-8",
        )
