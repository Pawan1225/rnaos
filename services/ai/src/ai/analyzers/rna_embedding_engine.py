"""
RNAOS RNA embedding engine.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)
from ai.models.rna_embedding import (
    RNAEmbedding,
)
from ai.utils.embedding_math import (
    normalize_embedding,
)


class RNAEmbeddingEngine:
    """
    Generate deterministic RNA embeddings from feature vectors.

    Architecture
    ------------
    Converts a deterministic feature vector into a normalized
    dense numerical representation suitable for downstream
    AI, machine learning, deep learning, and quantum
    intelligence engines.

    Complexity
    ----------
    Time Complexity: O(n)

    where n is the feature vector dimension.
    """

    def _project(
        self,
        feature_vector: FeatureVector,
    ) -> tuple[float, ...]:
        """
        Project a feature vector into embedding space.

        The current implementation performs an identity
        projection. Future versions may replace this with
        learned embeddings while preserving the public API.
        """
        return feature_vector.values

    def _build_embedding(
        self,
        values: tuple[float, ...],
    ) -> RNAEmbedding:
        """
        Build an immutable RNA embedding.
        """
        return RNAEmbedding(
            values=values,
            dimension=len(values),
        )

    def embed(
        self,
        feature_vector: FeatureVector,
    ) -> RNAEmbedding:
        """
        Generate an RNA embedding.

        Parameters
        ----------
        feature_vector
            AI feature vector.

        Returns
        -------
        RNAEmbedding
            Normalized dense embedding.
        """
        values = self._project(
            feature_vector,
        )

        values = normalize_embedding(
            values,
        )

        return self._build_embedding(
            values,
        )
