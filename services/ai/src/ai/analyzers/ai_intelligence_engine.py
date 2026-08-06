"""
RNAOS AI intelligence engine.
"""

from __future__ import annotations

from ai.analyzers.explainable_ai_engine import (
    ExplainableAIEngine,
)
from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from ai.analyzers.knowledge_graph_engine import (
    KnowledgeGraphEngine,
)
from ai.analyzers.meta_feature_engine import (
    MetaFeatureEngine,
)
from ai.analyzers.rna_embedding_engine import (
    RNAEmbeddingEngine,
)
from ai.analyzers.solver_recommendation_engine import (
    SolverRecommendationEngine,
)
from ai.models.ai_intelligence_profile import (
    AIIntelligenceProfile,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class AIIntelligenceEngine:
    """
    Unified AI intelligence engine.

    Orchestrates every AI module into a single
    immutable AI intelligence profile.

    Complexity
    ----------
    Time Complexity: O(1)
    """

    def __init__(
        self,
    ) -> None:
        self._feature_engine = FeatureEngineeringEngine()

        self._embedding_engine = RNAEmbeddingEngine()

        self._knowledge_graph_engine = KnowledgeGraphEngine()

        self._meta_feature_engine = MetaFeatureEngine()

        self._solver_engine = SolverRecommendationEngine()

        self._explainable_engine = ExplainableAIEngine()

    def analyze(
        self,
        profile: BiologicalIntelligenceProfile,
    ) -> AIIntelligenceProfile:
        """
        Generate a unified AI intelligence profile.
        """
        feature_vector = self._feature_engine.extract(
            profile,
        )

        embedding = self._embedding_engine.embed(
            feature_vector,
        )

        knowledge_graph = self._knowledge_graph_engine.build(
            profile,
        )

        meta_features = self._meta_feature_engine.analyze(
            profile,
        )

        solver_recommendation = self._solver_engine.analyze(
            profile,
            meta_features,
        )

        explanation = self._explainable_engine.analyze(
            profile,
            meta_features,
            solver_recommendation,
        )

        return AIIntelligenceProfile(
            feature_vector=feature_vector,
            embedding=embedding,
            knowledge_graph=knowledge_graph,
            meta_features=meta_features,
            solver_recommendation=solver_recommendation,
            explanation=explanation,
        )
