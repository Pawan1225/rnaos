from enterprise.benchmark.release_benchmark import (
    benchmark_release,
)


def test_benchmark_release():
    report = benchmark_release()

    assert report.total == 10
    assert report.success
