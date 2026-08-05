from enterprise.benchmark import (
    BenchmarkReportRenderer,
)
from enterprise.benchmark.release_benchmark import (
    benchmark_release,
)


def test_end_to_end_benchmark():
    report = benchmark_release()

    renderer = BenchmarkReportRenderer()

    summary = renderer.render_summary(report)

    assert "10/10 benchmarks passed" in summary
