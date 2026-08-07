"""
Tests for experiment record.
"""

from __future__ import annotations

from dl.models.learning.experiment_record import (
    ExperimentRecord,
)


def test_experiment_record() -> None:
    """
    Experiment record creation works.
    """

    record = ExperimentRecord(
        experiment_id="EXP_001",
        timestamp="2026-08-07",
        version="14.8",
        sequence_length=120,
        gc_content=0.52,
        structure_complexity=0.80,
        biological_features=("hairpin",),
        ai_profile=("complex",),
        ml_prediction=("solver_a",),
        dl_prediction=("solver_a",),
        selected_solver="solver_a",
        optimization_strategy="hybrid",
        parameters=("temperature=0.8",),
        runtime=10.5,
        memory=512.0,
        iterations=1000,
        energy_score=-35.0,
        accuracy_score=0.95,
        benchmark_score=0.92,
        success=True,
    )

    assert record.experiment_id == "EXP_001"

    assert record.selected_solver == "solver_a"

    assert record.success is True
