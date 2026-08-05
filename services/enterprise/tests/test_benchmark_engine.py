from enterprise.benchmark import (
    Benchmark,
    BenchmarkCategory,
    BenchmarkResult,
    BenchmarkStatus,
    BenchmarkSuite,
)


class DummyBenchmark:
    @property
    def name(self) -> str:
        """Return the benchmark name."""

        return "Dummy"

    def run(self) -> BenchmarkResult:
        """Execute the benchmark."""

        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.25,
        )


def test_run_benchmark():
    suite = BenchmarkSuite()

    benchmark: Benchmark = DummyBenchmark()

    result = suite.run(benchmark)

    assert result.name == "Dummy"
    assert result.passed
    assert len(suite.results()) == 1


class BenchmarkOne:
    @property
    def name(self) -> str:
        """Return the benchmark name."""

        return "One"

    def run(self) -> BenchmarkResult:
        """Execute benchmark."""

        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.1,
        )


class BenchmarkTwo:
    @property
    def name(self) -> str:
        """Return the benchmark name."""

        return "Two"

    def run(self) -> BenchmarkResult:
        """Execute benchmark."""

        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.2,
        )


def test_run_all():
    suite = BenchmarkSuite()

    suite.register(BenchmarkOne())
    suite.register(BenchmarkTwo())

    report = suite.run_all()

    assert report.total == 2
    assert report.passed == 2
    assert report.failed == 0


def test_statistics():
    suite = BenchmarkSuite()

    suite.register(BenchmarkOne())
    suite.register(BenchmarkTwo())

    suite.run_all()

    stats = suite.statistics()

    assert stats["total"] == 2
    assert stats["passed"] == 2
    assert stats["failed"] == 0
    assert stats["runtime"] > 0.0
    assert stats["average_runtime"] > 0.0


def test_add_result():
    suite = BenchmarkSuite()

    result = suite.benchmark(
        "Simple Benchmark",
        lambda: sum(range(100)),
    )

    assert result.name == "Simple Benchmark"
    assert result.runtime_seconds >= 0.0
    assert len(suite.results()) == 1
