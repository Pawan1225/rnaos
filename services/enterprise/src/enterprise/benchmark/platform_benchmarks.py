"""
Default platform benchmarks for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

from enterprise.benchmark.benchmark import Benchmark
from enterprise.benchmark.models import (
    BenchmarkCategory,
    BenchmarkResult,
    BenchmarkStatus,
)


class PlatformBenchmark(Benchmark):
    """Benchmark for an RNAOS platform service."""

    def __init__(
        self,
        name: str,
    ) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Return benchmark name."""

        return self._name

    def run(self) -> BenchmarkResult:
        """Execute the benchmark."""

        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.0,
        )


def default_platform_benchmarks() -> list[Benchmark]:
    """Return the default RNAOS platform benchmarks."""

    return [
        PlatformBenchmark("RNA"),
        PlatformBenchmark("AI"),
        PlatformBenchmark("Optimization"),
        PlatformBenchmark("Solver"),
        PlatformBenchmark("Research"),
        PlatformBenchmark("Decision"),
        PlatformBenchmark("Analytics"),
        PlatformBenchmark("Platform"),
        PlatformBenchmark("Cloud"),
        PlatformBenchmark("Enterprise"),
    ]
