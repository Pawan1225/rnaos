import pytest
from analytics.performance import SolverPerformance
from analytics.recommendation import (
    RecommendationEngine,
    RecommendationLevel,
)


def test_recommend_solver() -> None:
    performance = [
        SolverPerformance(
            solver="SA",
            experiments=20,
            mean_runtime=0.20,
            mean_objective=-12.0,
            mean_confidence=0.91,
        ),
        SolverPerformance(
            solver="GA",
            experiments=20,
            mean_runtime=0.35,
            mean_objective=-13.0,
            mean_confidence=0.88,
        ),
        SolverPerformance(
            solver="Exact",
            experiments=5,
            mean_runtime=1.00,
            mean_objective=-15.0,
            mean_confidence=1.00,
        ),
    ]

    recommendation = RecommendationEngine().recommend(performance)

    assert recommendation.recommended_solver == "SA"

    assert recommendation.level == RecommendationLevel.RECOMMENDED

    assert recommendation.score > 0

    assert len(recommendation.alternatives) == 2


def test_empty_history() -> None:
    engine = RecommendationEngine()

    with pytest.raises(ValueError):
        engine.recommend([])
