"""
RNA Solver Suitability Predictor

Predicts the most appropriate optimization strategy.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_intelligence.complexity.complexity_estimator import (
    ComplexityEstimate,
)
from ai_intelligence.embeddings.embedding_engine import RNAEmbedding
from ai_intelligence.features.feature_engine import FeatureVector


@dataclass(slots=True)
class SolverRecommendation:
    """Recommended optimization strategy."""

    solver: str
    confidence: float
    reasoning: str


class SolverSuitabilityPredictor:
    """Predict the most suitable optimization solver."""

    def predict(
        self,
        features: FeatureVector,
        embedding: RNAEmbedding,
        complexity: ComplexityEstimate,
    ) -> SolverRecommendation:
        """
        Predict the most suitable optimization strategy.
        """

        score = complexity.score

        if score < 0.33:
            solver = "classical"
        elif score < 0.66:
            solver = "hybrid"
        else:
            solver = "quantum"

        confidence = round(
            0.60 + 0.40 * score,
            3,
        )

        return SolverRecommendation(
            solver=solver,
            confidence=confidence,
            reasoning=(
                f"Complexity={complexity.score:.3f}, "
                f"Category={complexity.category}, "
                f"EmbeddingDim={embedding.dimension}, "
                f"Features={features.dimension}"
            ),
        )
