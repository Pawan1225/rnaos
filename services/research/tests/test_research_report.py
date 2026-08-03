from research.analysis.statistical_summary import StatisticalSummary
from research.reporting.research_report import ResearchReport


def build_summary():
    return StatisticalSummary(
        sample_size=10,
        mean_runtime=0.2,
        median_runtime=0.2,
        std_runtime=0.01,
        fastest_runtime=0.1,
        slowest_runtime=0.3,
        mean_absolute_error=0.4,
        median_absolute_error=0.4,
        std_absolute_error=0.05,
        mean_relative_error=0.05,
        mean_accuracy=0.95,
    )


def test_report_creation():
    report = ResearchReport(
        title="RNAOS Benchmark",
        summary=build_summary(),
    )

    assert report.title == "RNAOS Benchmark"
    assert report.summary.sample_size == 10


def test_has_authors():
    report = ResearchReport(
        title="RNAOS Benchmark",
        summary=build_summary(),
        authors=["J. K. Pawan Kumar"],
    )

    assert report.has_authors
