"""
Tests for learning analytics engine.
"""

from __future__ import annotations

from dl.continuous_learning.analytics.learning_analytics_engine import (
    LearningAnalyticsEngine,
)
from dl.continuous_learning.repository.experiment_repository import (
    ExperimentRepository,
)
from dl.models.learning.experiment_record import (
    ExperimentRecord,
)


def create_record(
    solver: str,
    success: bool,
) -> ExperimentRecord:
    """
    Create experiment record.
    """

    return ExperimentRecord(
        experiment_id="EXP_001",
        timestamp="2026-08-07",
        version="14.8",
        sequence_length=100,
        gc_content=0.5,
        structure_complexity=0.7,
        biological_features=(),
        ai_profile=(),
        ml_prediction=(),
        dl_prediction=(),
        selected_solver=solver,
        optimization_strategy="hybrid",
        parameters=(),
        runtime=10.0,
        memory=256.0,
        iterations=100,
        energy_score=-30.0,
        accuracy_score=0.9,
        benchmark_score=0.85,
        success=success,
    )


def test_learning_analytics() -> None:
    """
    Analytics generation works.
    """

    repository = ExperimentRepository()

    repository.add(
        create_record(
            "solver_a",
            True,
        ),
    )

    repository.add(
        create_record(
            "solver_a",
            False,
        ),
    )

    engine = LearningAnalyticsEngine()

    analytics = engine.analyze(
        repository,
    )

    assert analytics.total_experiments == 2

    assert analytics.best_solver == ("solver_a")
