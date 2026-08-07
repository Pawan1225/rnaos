"""
RNAOS continuous learning engine.
"""

from __future__ import annotations

from dl.continuous_learning.analytics.learning_analytics_engine import (
    LearningAnalyticsEngine,
)
from dl.continuous_learning.knowledge.knowledge_base import (
    KnowledgeBase,
)
from dl.continuous_learning.recommendation.adaptive_recommendation_engine import (
    AdaptiveRecommendationEngine,
)
from dl.continuous_learning.repository.experiment_repository import (
    ExperimentRepository,
)
from dl.models.learning.continuous_learning_profile import (
    ContinuousLearningProfile,
)
from dl.models.learning.solver_performance_profile import (
    SolverPerformanceProfile,
)


class ContinuousLearningEngine:
    """
    Master continuous learning orchestrator.
    """

    def __init__(self) -> None:
        self._analytics = LearningAnalyticsEngine()

        self._recommendation = AdaptiveRecommendationEngine()

    def learn(
        self,
        repository: ExperimentRepository,
        knowledge_base: KnowledgeBase,
        solver_profiles: tuple[
            SolverPerformanceProfile,
            ...,
        ],
    ) -> ContinuousLearningProfile:
        """
        Generate learning profile.
        """

        analytics = self._analytics.analyze(
            repository,
        )

        recommendation = self._recommendation.recommend(
            solver_profiles,
        )

        return ContinuousLearningProfile(
            total_experiments=(analytics.total_experiments),
            best_solver=(analytics.best_solver),
            recommended_solver=(recommendation.recommended_solver),
            confidence=(recommendation.confidence),
            success_rate=(analytics.success_rate),
            knowledge_items=len(
                knowledge_base.get_all(),
            ),
        )
