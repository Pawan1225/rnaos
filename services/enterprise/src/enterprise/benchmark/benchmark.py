"""
Benchmark protocol for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

from typing import Protocol

from enterprise.benchmark.models import BenchmarkResult


class Benchmark(Protocol):
    """Protocol implemented by all benchmark plugins."""

    @property
    def name(self) -> str:
        """Return the benchmark name."""
        ...

    def run(self) -> BenchmarkResult:
        """Execute the benchmark."""
        ...
