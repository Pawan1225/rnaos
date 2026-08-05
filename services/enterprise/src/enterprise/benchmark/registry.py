"""
Benchmark registry for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

from enterprise.benchmark.benchmark import (
    Benchmark,
)


class BenchmarkRegistry:
    """Registry of platform benchmarks."""

    def __init__(self) -> None:
        self._benchmarks: dict[str, Benchmark] = {}

    def register(
        self,
        benchmark: Benchmark,
    ) -> None:
        """Register a benchmark."""

        self._benchmarks[benchmark.name] = benchmark

    def get(
        self,
        name: str,
    ) -> Benchmark | None:
        """Return a benchmark."""

        return self._benchmarks.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a benchmark exists."""

        return name in self._benchmarks

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a benchmark."""

        self._benchmarks.pop(name, None)

    def clear(
        self,
    ) -> None:
        """Clear the registry."""

        self._benchmarks.clear()

    def list_benchmarks(
        self,
    ) -> list[str]:
        """Return benchmark names."""

        return sorted(self._benchmarks)

    def items(
        self,
    ) -> tuple[Benchmark, ...]:
        """Return registered benchmarks."""

        return tuple(self._benchmarks[name] for name in sorted(self._benchmarks))

    def count(
        self,
    ) -> int:
        """Return the number of registered benchmarks."""

        return len(self._benchmarks)
