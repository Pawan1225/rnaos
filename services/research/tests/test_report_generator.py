from pathlib import Path

from research.analysis.statistical_summary import StatisticalSummary
from research.reporting.report_generator import ReportGenerator
from research.reporting.research_report import ResearchReport


def build_report() -> ResearchReport:
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
    report = ResearchReport(
        title="RNAOS Benchmark",
        summary=build_report().summary,
    )

    markdown = ReportGenerator().to_markdown(report)

    assert "Unknown" in markdown


def test_json_export():
    report = build_report()

    json_output = ReportGenerator().to_json(report)

    assert '"title": "RNAOS Benchmark"' in json_output
    assert '"sample_size": 10' in json_output
    assert '"mean_accuracy": 0.94' in json_output


def test_csv_export():
    report = build_report()

    csv_output = ReportGenerator().to_csv(report)

    assert "Metric,Value" in csv_output
    assert "Sample Size,10" in csv_output
    assert "Mean Runtime,0.12" in csv_output
    assert "Mean Accuracy,0.94" in csv_output


def test_save_markdown(tmp_path: Path):
    report = build_report()

    output = tmp_path / "report.md"

    ReportGenerator().save(
        report,
        output,
        format="markdown",
    )

    assert output.exists()

    content = output.read_text(encoding="utf-8")

    assert "# RNAOS Benchmark" in content


def test_save_json(tmp_path: Path):
    report = build_report()

    output = tmp_path / "report.json"

    ReportGenerator().save(
        report,
        output,
        format="json",
    )

    assert output.exists()

    content = output.read_text(encoding="utf-8")

    assert '"title": "RNAOS Benchmark"' in content


def test_save_csv(tmp_path: Path):
    report = build_report()

    output = tmp_path / "report.csv"

    ReportGenerator().save(
        report,
        output,
        format="csv",
    )

    assert output.exists()

    content = output.read_text(encoding="utf-8")

    assert "Metric,Value" in content
