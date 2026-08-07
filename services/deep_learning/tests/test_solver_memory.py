"""
Tests for solver performance memory.
"""

from __future__ import annotations

from dl.continuous_learning.memory.solver_memory import (
    SolverPerformanceMemory,
)
from dl.models.learning.experiment_record import (
    ExperimentRecord,
)


def create_record(
    solver: str,
) -> ExperimentRecord:
    """
    Create test record.
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


def test_solver_profile_generation() -> None:
    """
    Solver profile is created.
    """

    memory = SolverPerformanceMemory()

    profile = memory.build_profile(
        (
            create_record("solver_a"),
            create_record("solver_a"),
        ),
        "solver_a",
    )

    assert profile.solver_name == ("solver_a")

    assert profile.total_runs == 2

    assert profile.success_rate == 1.0
