"""
Research report generator.
"""

from __future__ import annotations

from research.reporting.research_report import ResearchReport


class ReportGenerator:
    """
    Generate publication-ready reports.
    """

    def to_markdown(
        self,
        report: ResearchReport,
    ) -> str:
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
