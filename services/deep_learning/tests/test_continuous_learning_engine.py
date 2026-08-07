"""
Tests for continuous learning engine.
"""

from __future__ import annotations

from dl.continuous_learning.engine.continuous_learning_engine import (
    ContinuousLearningEngine,
)
from dl.continuous_learning.knowledge.knowledge_base import (
    KnowledgeBase,
)
from dl.continuous_learning.repository.experiment_repository import (
    ExperimentRepository,
)
from dl.models.learning.experiment_record import (
    ExperimentRecord,
)
from dl.models.learning.knowledge_item import (
    KnowledgeItem,
)
from dl.models.learning.solver_performance_profile import (
    SolverPerformanceProfile,
)


def create_record() -> ExperimentRecord:
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
        selected_solver="solver_a",
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


def test_continuous_learning() -> None:
    """
    Learning pipeline works.
    """

    repository = ExperimentRepository()

    repository.add(
        create_record(),
    )

    knowledge = KnowledgeBase()

    knowledge.add(
        KnowledgeItem(
            knowledge_id="KNOW_001",
            category="solver",
            key="complex",
            value="solver_a",
            confidence=0.9,
        ),
    )

    engine = ContinuousLearningEngine()

    profile = engine.learn(
        repository,
        knowledge,
        (
            SolverPerformanceProfile(
                solver_name="solver_a",
                total_runs=1,
                success_rate=1.0,
                average_accuracy=0.9,
                average_energy=-30.0,
                average_runtime=10.0,
            ),
        ),
    )

    assert profile.total_experiments == 1

    assert profile.recommended_solver == ("solver_a")

    assert profile.knowledge_items == 1
