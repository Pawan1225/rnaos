from enterprise.benchmark import (
    BenchmarkCategory,
    BenchmarkReport,
    BenchmarkReportRenderer,
    BenchmarkResult,
    BenchmarkStatus,
)


def sample_report() -> BenchmarkReport:
    return BenchmarkReport(
        results=[
            BenchmarkResult(
                name="RNA",
                status=BenchmarkStatus.PASSED,
                category=BenchmarkCategory.PLATFORM,
                runtime_seconds=0.25,
            ),
        ]
    )


def test_render_json():
    renderer = BenchmarkReportRenderer()

    output = renderer.render_json(
        sample_report(),
    )

    assert '"total": 1' in output
    assert '"passed": 1' in output


def test_render_markdown():
    renderer = BenchmarkReportRenderer()

    output = renderer.render_markdown(
        sample_report(),
    )

    assert "# Benchmark Report" in output
    assert "Total:" in output


def test_render_summary():
    renderer = BenchmarkReportRenderer()

    output = renderer.render_summary(
        sample_report(),
    )

    assert "1/1 benchmarks passed" in output
