"""
RNAOS Enterprise Benchmark Engine.
"""

from __future__ import annotations

import time
from collections.abc import Callable

from enterprise.benchmark.benchmark import Benchmark
from enterprise.benchmark.models import (
    BenchmarkCategory,
    BenchmarkReport,
    BenchmarkResult,
    BenchmarkStatus,
)
from enterprise.benchmark.registry import BenchmarkRegistry


class BenchmarkSuite:
    """Run RNAOS benchmarks."""

    def __init__(self) -> None:
        self._registry = BenchmarkRegistry()
        self._results: list[BenchmarkResult] = []

    def benchmark(
        self,
        name: str,
        func: Callable[[], object],
        *,
        category: BenchmarkCategory = BenchmarkCategory.PERFORMANCE,
    ) -> BenchmarkResult:
        """Benchmark a callable."""

        start = time.perf_counter()

        func()

        runtime = time.perf_counter() - start

        result = BenchmarkResult(
            name=name,
            status=BenchmarkStatus.PASSED,
            category=category,
            runtime_seconds=runtime,
        )

        self._results.append(result)

        return result

    def register(
        self,
        benchmark: Benchmark,
    ) -> None:
        """Register a benchmark."""

        self._registry.register(benchmark)

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a benchmark."""

        self._registry.remove(name)

    def run(
        self,
        benchmark: Benchmark,
    ) -> BenchmarkResult:
        """Run one benchmark."""

        result = benchmark.run()

        self._results.append(result)

        return result

    def run_all(
        self,
    ) -> BenchmarkReport:
        """Run all registered benchmarks."""

        for benchmark in self._registry.items():
            self.run(benchmark)

        return self.report()

    def report(
        self,
    ) -> BenchmarkReport:
        """Return benchmark report."""

        return BenchmarkReport(
            results=list(self._results),
        )

    def statistics(
        self,
    ) -> dict[str, float]:
        """Return benchmark statistics."""

        report = self.report()

        return {
            "total": report.total,
            "passed": report.passed,
            "failed": report.failed,
            "runtime": report.total_runtime,
            "average_runtime": report.average_runtime,
        }

    def clear(
        self,
    ) -> None:
        """Clear benchmark results."""

        self._results.clear()

    def results(
        self,
    ) -> list[BenchmarkResult]:
        """Return benchmark results."""

        return list(self._results)
