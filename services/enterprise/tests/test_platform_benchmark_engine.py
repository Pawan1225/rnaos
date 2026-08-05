from enterprise.benchmark.platform_benchmark_engine import (
    benchmark_platform,
)


def test_benchmark_platform():
    report = benchmark_platform()

    assert report.total == 10
    assert report.success
