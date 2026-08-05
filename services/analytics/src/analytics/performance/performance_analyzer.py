"""
Performance analytics.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from analytics.models.experiment_record import ExperimentRecord


@dataclass(slots=True)
class SolverPerformance:
    """Aggregated solver performance statistics."""

    solver: str
    experiments: int
    mean_runtime: float
    mean_objective: float
    mean_confidence: float


class PerformanceAnalyzer:
    """Analyze historical solver performance."""

    def summarize(
        self,
        records: list[ExperimentRecord],
    ) -> list[SolverPerformance]:
        """Return aggregated statistics grouped by solver."""

        if not records:
            return []

        grouped: dict[str, list[ExperimentRecord]] = {}

        for record in records:
            grouped.setdefault(record.solver, []).append(record)

        summaries: list[SolverPerformance] = []

        for solver, items in grouped.items():
            summaries.append(
                SolverPerformance(
                    solver=solver,
                    experiments=len(items),
                    mean_runtime=mean(record.runtime_seconds for record in items),
                    mean_objective=mean(record.objective_value for record in items),
                    mean_confidence=mean(record.confidence for record in items),
                )
            )

        summaries.sort(
            key=lambda summary: (
                summary.mean_runtime,
                summary.solver,
            )
        )

        return summaries
