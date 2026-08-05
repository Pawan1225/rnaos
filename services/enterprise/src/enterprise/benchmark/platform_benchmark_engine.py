"""
Platform benchmark engine.
"""

from __future__ import annotations

from enterprise.benchmark.models import BenchmarkReport
from enterprise.benchmark.service_benchmarks import benchmark_services


def benchmark_platform() -> BenchmarkReport:
    """Benchmark the complete RNAOS platform."""

    return benchmark_services()
