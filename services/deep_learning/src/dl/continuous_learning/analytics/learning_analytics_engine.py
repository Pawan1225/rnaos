"""
RNAOS learning analytics engine.
"""

from __future__ import annotations

from dl.continuous_learning.repository.experiment_repository import (
    ExperimentRepository,
)
from dl.models.learning.learning_analytics import (
    LearningAnalytics,
)


class LearningAnalyticsEngine:
    """
    Analyzes experiment history.
    """

    def analyze(
        self,
        repository: ExperimentRepository,
    ) -> LearningAnalytics:
        """
        Generate analytics.
        """

        records = repository.get_all()

        if not records:
            return LearningAnalytics(
                total_experiments=0,
                success_rate=0.0,
                average_runtime=0.0,
                average_accuracy=0.0,
                average_energy=0.0,
                best_solver="",
            )

        total = len(records)

        successful = sum(1 for record in records if record.success)

        solver_scores: dict[str, int] = {}

        for record in records:
            solver_scores[record.selected_solver] = (
                solver_scores.get(
                    record.selected_solver,
                    0,
                )
                + 1
            )

        best_solver = max(
            solver_scores,
            key=solver_scores.get,
        )

        return LearningAnalytics(
            total_experiments=total,
            success_rate=successful / total,
            average_runtime=sum(record.runtime for record in records) / total,
            average_accuracy=sum(record.accuracy_score for record in records) / total,
            average_energy=sum(record.energy_score for record in records) / total,
            best_solver=best_solver,
        )
