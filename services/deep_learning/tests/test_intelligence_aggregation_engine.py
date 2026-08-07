"""
Tests for intelligence aggregation engine.
"""

from __future__ import annotations

from dl.models.optimization.intelligence_aggregation import (
    IntelligenceAggregation,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)
from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)
from dl.models.optimization.solver_capability import (
    SolverCapability,
)
from dl.optimization.intelligence_aggregation_engine import (
    IntelligenceAggregationEngine,
)


def test_intelligence_aggregation() -> None:
    """
    Intelligence is aggregated.
    """

    capabilities = (
        SolverCapability(
            solver_name="genetic",
            capabilities=(
                0.95,
                0.90,
            ),
            category="evolutionary",
        ),
        SolverCapability(
            solver_name="pso",
            capabilities=(
                0.85,
                0.80,
            ),
            category="swarm",
        ),
    )

    learning = LearningProfile(
        total_experiences=10,
        best_solver="genetic",
        average_reward=0.90,
        confidence=0.90,
    )

    meta = MetaIntelligenceProfile(
        best_algorithm="genetic",
        generations=20,
        best_fitness=0.95,
        confidence=0.95,
    )

    engine = IntelligenceAggregationEngine()

    result = engine.aggregate(
        capabilities=capabilities,
        learning_profile=learning,
        meta_profile=meta,
    )

    assert isinstance(
        result,
        IntelligenceAggregation,
    )

    assert result.total_features == 4

    assert result.average_capability > 0

    assert result.learning_confidence == 0.90

    assert result.meta_confidence == 0.95

    assert result.unified_score > 0
