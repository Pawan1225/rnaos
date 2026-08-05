"""
Domain models for the RNAOS Enterprise Benchmark Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


class BenchmarkStatus(StrEnum):
    """Benchmark execution status."""

    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"


class BenchmarkCategory(StrEnum):
    """Benchmark category."""

    PERFORMANCE = "performance"
    MEMORY = "memory"
    CPU = "cpu"
    THROUGHPUT = "throughput"
    SCALABILITY = "scalability"
    PLATFORM = "platform"


@dataclass(slots=True, frozen=True)
class BenchmarkResult:
    """Single benchmark result."""

    name: str

    status: BenchmarkStatus

    category: BenchmarkCategory

    runtime_seconds: float

    iterations: int = 1

    memory_mb: float | None = None

    cpu_percent: float | None = None

    throughput: float | None = None

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def passed(self) -> bool:
        """Return whether the benchmark passed."""

        return self.status is BenchmarkStatus.PASSED


@dataclass(slots=True)
class BenchmarkReport:
    """Benchmark report."""

    results: list[BenchmarkResult] = field(
        default_factory=list,
    )

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def total(self) -> int:
        """Return total benchmarks."""

        return len(self.results)

    @property
    def passed(self) -> int:
        """Return passed benchmarks."""

        return sum(result.passed for result in self.results)

    @property
    def failed(self) -> int:
        """Return failed benchmarks."""

        return sum(result.status is BenchmarkStatus.FAILED for result in self.results)

    @property
    def skipped(self) -> int:
        """Return skipped benchmarks."""

        return sum(result.status is BenchmarkStatus.SKIPPED for result in self.results)

    @property
    def success(self) -> bool:
        """Return whether the report succeeded."""

        return self.failed == 0

    @property
    def total_runtime(self) -> float:
        """Return total runtime."""

        return sum(result.runtime_seconds for result in self.results)

    @property
    def average_runtime(self) -> float:
        """Return average runtime."""

        if not self.results:
            return 0.0

        return self.total_runtime / self.total
