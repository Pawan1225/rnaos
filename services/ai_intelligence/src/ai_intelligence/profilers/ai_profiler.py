"""
AI Profiling Engine

Coordinates all AI Intelligence components.
"""

from __future__ import annotations

from dataclasses import dataclass

from rna_intelligence.profilers.rna_profiler import RNAProfile

from ai_intelligence.complexity.complexity_estimator import (
    ComplexityEstimate,
    ComplexityEstimator,
)
from ai_intelligence.embeddings.embedding_engine import (
    RNAEmbedding,
    RNAEmbeddingEngine,
)
from ai_intelligence.features.feature_engine import (
    FeatureEngineeringEngine,
    FeatureVector,
)
from ai_intelligence.predictors.solver_predictor import (
    SolverRecommendation,
    SolverSuitabilityPredictor,
)


@dataclass(slots=True)
class AIProfile:
    """Complete AI analysis for an RNA sequence."""

    features: FeatureVector
    embedding: RNAEmbedding
    complexity: ComplexityEstimate
    recommendation: SolverRecommendation


class AIProfiler:
    """High-level AI Intelligence pipeline."""

    def __init__(self) -> None:
        self.feature_engine = FeatureEngineeringEngine()
        self.embedding_engine = RNAEmbeddingEngine()
        self.complexity_engine = ComplexityEstimator()
        self.predictor = SolverSuitabilityPredictor()

    def profile(self, profile: RNAProfile) -> AIProfile:
        """
        Generate a complete AI profile from an RNA profile.
        """

        features = self.feature_engine.transform(profile)

        embedding = self.embedding_engine.embed(profile)

        complexity = self.complexity_engine.estimate(profile)

        recommendation = self.predictor.predict(
            features=features,
            embedding=embedding,
            complexity=complexity,
        )

        return AIProfile(
            features=features,
            embedding=embedding,
            complexity=complexity,
            recommendation=recommendation,
        )
