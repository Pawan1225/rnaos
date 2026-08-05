"""
RNAOS Digital Twin.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from statistics import mean

from analytics.models.experiment_record import ExperimentRecord
from analytics.performance.performance_analyzer import SolverPerformance


class HealthStatus(StrEnum):
    """Overall RNAOS platform health."""

    HEALTHY = "HEALTHY"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


@dataclass(slots=True)
class DigitalTwin:
    """Live representation of the RNAOS platform."""

    total_experiments: int = 0

    active_solvers: list[str] = field(default_factory=list)

    latest_experiment: ExperimentRecord | None = None

    solver_performance: list[SolverPerformance] = field(default_factory=list)

    average_confidence: float = 0.0

    average_runtime: float = 0.0

    benchmark_accuracy: float = 0.0

    health: HealthStatus = HealthStatus.HEALTHY


class DigitalTwinBuilder:
    """Construct a DigitalTwin from analytics data."""

    def build(
        self,
        *,
        records: list[ExperimentRecord],
        performance: list[SolverPerformance],
        benchmark_accuracy: float,
    ) -> DigitalTwin:
        """Build the current RNAOS Digital Twin."""

        if records:
            latest = records[-1]

            average_runtime = mean(record.runtime_seconds for record in records)

            average_confidence = mean(record.confidence for record in records)
        else:
            latest = None
            average_runtime = 0.0
            average_confidence = 0.0

        health = HealthStatus.HEALTHY

        if benchmark_accuracy < 0.60:
            health = HealthStatus.CRITICAL
        elif benchmark_accuracy < 0.80:
            health = HealthStatus.WARNING

        return DigitalTwin(
            total_experiments=len(records),
            active_solvers=sorted({record.solver for record in records}),
            latest_experiment=latest,
            solver_performance=performance,
            average_confidence=average_confidence,
            average_runtime=average_runtime,
            benchmark_accuracy=benchmark_accuracy,
            health=health,
        )
