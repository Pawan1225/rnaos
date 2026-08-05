"""
Release benchmark entry point.
"""

from __future__ import annotations

from enterprise.benchmark.models import BenchmarkReport
from enterprise.benchmark.platform_benchmark_engine import (
    benchmark_platform,
)


def benchmark_release() -> BenchmarkReport:
    """Execute release benchmarks."""

    return benchmark_platform()
