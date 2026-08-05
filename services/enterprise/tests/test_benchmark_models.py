from enterprise.benchmark import (
    BenchmarkCategory,
    BenchmarkReport,
    BenchmarkResult,
    BenchmarkStatus,
)


def test_result_defaults():
    result = BenchmarkResult(
        name="RNA",
        status=BenchmarkStatus.PASSED,
        category=BenchmarkCategory.PLATFORM,
        runtime_seconds=0.25,
    )

    assert result.passed
    assert result.runtime_seconds == 0.25
    assert result.iterations == 1


def test_failed_result():
    result = BenchmarkResult(
        name="Solver",
        status=BenchmarkStatus.FAILED,
        category=BenchmarkCategory.PERFORMANCE,
        runtime_seconds=1.5,
    )

    assert not result.passed


def test_report_counts():
    report = BenchmarkReport(
        results=[
            BenchmarkResult(
                name="One",
                status=BenchmarkStatus.PASSED,
                category=BenchmarkCategory.PLATFORM,
                runtime_seconds=1.0,
            ),
            BenchmarkResult(
                name="Two",
                status=BenchmarkStatus.FAILED,
                category=BenchmarkCategory.PLATFORM,
                runtime_seconds=2.0,
            ),
        ]
    )

    assert report.total == 2
    assert report.passed == 1
    assert report.failed == 1
    assert report.total_runtime == 3.0
    assert report.average_runtime == 1.5
