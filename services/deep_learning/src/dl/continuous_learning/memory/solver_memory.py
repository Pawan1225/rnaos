"""
RNAOS solver performance memory.
"""

from __future__ import annotations

from dl.models.learning.experiment_record import (
    ExperimentRecord,
)
from dl.models.learning.solver_performance_profile import (
    SolverPerformanceProfile,
)


class SolverPerformanceMemory:
    """
    Builds solver performance profiles.
    """

    def build_profile(
        self,
        records: tuple[
            ExperimentRecord,
            ...,
        ],
        solver_name: str,
    ) -> SolverPerformanceProfile:
        """
        Generate solver profile.
        """

        solver_records = tuple(
            record for record in records if record.selected_solver == solver_name
        )

        if not solver_records:
            return SolverPerformanceProfile(
                solver_name=solver_name,
                total_runs=0,
                success_rate=0.0,
                average_accuracy=0.0,
                average_energy=0.0,
                average_runtime=0.0,
            )

        total = len(solver_records)

        successful = sum(1 for record in solver_records if record.success)

        return SolverPerformanceProfile(
            solver_name=solver_name,
            total_runs=total,
            success_rate=successful / total,
            average_accuracy=sum(record.accuracy_score for record in solver_records) / total,
            average_energy=sum(record.energy_score for record in solver_records) / total,
            average_runtime=sum(record.runtime for record in solver_records) / total,
        )
