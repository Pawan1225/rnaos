"""
RNA Embedding Engine

Generates fixed-length embedding vectors from RNA profiles.
"""

from __future__ import annotations

from dataclasses import dataclass

from rna_intelligence.profilers.rna_profiler import RNAProfile

from ai_intelligence.features.feature_engine import (
    FeatureEngineeringEngine,
)


@dataclass(slots=True)
class RNAEmbedding:
    """Vector representation of an RNA sequence."""

    vector: list[float]
    model_name: str

    @property
    def dimension(self) -> int:
        """Embedding dimension."""
        return len(self.vector)


class RNAEmbeddingEngine:
    """Generate RNA embeddings."""

    MODEL_NAME = "rnaos-feature-embedding-v1"

    def __init__(self) -> None:
        self.feature_engine = FeatureEngineeringEngine()

    def embed(self, profile: RNAProfile) -> RNAEmbedding:
        """
        Generate an embedding from an RNA profile.
        """

        features = self.feature_engine.transform(profile)

        # Version 1:
        # Directly reuse engineered features as the embedding.
        vector = features.values.copy()

        return RNAEmbedding(
            vector=vector,
            model_name=self.MODEL_NAME,
        )
