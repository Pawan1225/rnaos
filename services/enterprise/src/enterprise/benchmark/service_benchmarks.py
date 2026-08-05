"""
Service benchmark pipeline for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

from enterprise.benchmark.benchmark_suite import BenchmarkSuite
from enterprise.benchmark.models import BenchmarkReport
from enterprise.benchmark.platform_benchmarks import (
    default_platform_benchmarks,
)


def benchmark_services() -> BenchmarkReport:
    """Benchmark all RNAOS platform services."""

    suite = BenchmarkSuite()

    for benchmark in default_platform_benchmarks():
        suite.register(benchmark)

    return suite.run_all()
