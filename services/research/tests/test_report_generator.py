from research.analysis.statistical_summary import StatisticalSummary
from research.reporting.report_generator import ReportGenerator
from research.reporting.research_report import ResearchReport


def build_report():
    summary = StatisticalSummary(
        sample_size=10,
        mean_runtime=0.12,
        median_runtime=0.11,
        std_runtime=0.02,
        fastest_runtime=0.08,
        slowest_runtime=0.18,
        mean_absolute_error=0.30,
        median_absolute_error=0.28,
        std_absolute_error=0.05,
        mean_relative_error=0.04,
        mean_accuracy=0.94,
    )

    return ResearchReport(
        title="RNAOS Benchmark",
        summary=summary,
        authors=["J. K. Pawan Kumar"],
    )


def test_markdown_report():
    report = build_report()

    markdown = ReportGenerator().to_markdown(report)

    assert "# RNAOS Benchmark" in markdown
    assert "J. K. Pawan Kumar" in markdown
    assert "Sample Size" in markdown
    assert "Mean Runtime" in markdown
    assert "Mean Accuracy" in markdown


def test_markdown_without_authors():
    report = build_report()

    report = ResearchReport(
        title=report.title,
        summary=report.summary,
    )

    markdown = ReportGenerator().to_markdown(report)

    assert "Unknown" in markdown
