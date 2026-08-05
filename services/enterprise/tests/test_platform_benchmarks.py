from enterprise.benchmark import (
    BenchmarkSuite,
    PlatformBenchmark,
    default_platform_benchmarks,
)


def test_default_platform_benchmarks():
    benchmarks = default_platform_benchmarks()

    assert len(benchmarks) == 10


def test_platform_benchmark():
    benchmark = PlatformBenchmark("RNA")

    result = benchmark.run()

    assert result.name == "RNA"
    assert result.passed


def test_platform_statistics():
    suite = BenchmarkSuite()

    for benchmark in default_platform_benchmarks():
        suite.register(benchmark)

    report = suite.run_all()

    assert report.total == 10
    assert report.passed == 10
    assert report.failed == 0
