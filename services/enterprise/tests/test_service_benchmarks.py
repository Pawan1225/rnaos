from enterprise.benchmark.service_benchmarks import (
    benchmark_services,
)


def test_benchmark_services():
    report = benchmark_services()

    assert report.total == 10
    assert report.passed == 10
