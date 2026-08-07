"""
Tests for experiment repository.
"""

from __future__ import annotations

from dl.continuous_learning.repository.experiment_repository import (
    ExperimentRepository,
)
from dl.models.learning.experiment_record import (
    ExperimentRecord,
)


def create_record(
    solver: str,
) -> ExperimentRecord:
    """
    Create test experiment.
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
        success=True,
    )


def test_repository_add_and_count() -> None:
    """
    Repository stores records.
    """

    repository = ExperimentRepository()

    repository.add(
        create_record(
            "solver_a",
        ),
    )

    assert repository.count() == 1


def test_repository_search_solver() -> None:
    """
    Solver history retrieval works.
    """

    repository = ExperimentRepository()

    repository.add(
        create_record(
            "solver_a",
        ),
    )

    repository.add(
        create_record(
            "solver_b",
        ),
    )

    results = repository.get_by_solver(
        "solver_a",
    )

    assert len(results) == 1
