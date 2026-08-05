from enterprise.benchmark import (
    Benchmark,
    BenchmarkCategory,
    BenchmarkResult,
    BenchmarkStatus,
)


class DummyBenchmark:
    @property
    def name(self) -> str:
        """Return the benchmark name."""

        return "Dummy"

    def run(self) -> BenchmarkResult:
        """Execute benchmark."""

        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.1,
        )


def test_benchmark_protocol():
    benchmark: Benchmark = DummyBenchmark()

    result = benchmark.run()

    assert benchmark.name == "Dummy"
    assert result.name == "Dummy"
    assert result.status is BenchmarkStatus.PASSED
    assert result.category is BenchmarkCategory.PLATFORM
    assert result.passed
