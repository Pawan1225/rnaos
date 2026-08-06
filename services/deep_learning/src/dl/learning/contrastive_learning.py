"""
RNAOS contrastive learning foundation.
"""

from __future__ import annotations

from math import sqrt

from dl.models.rna_embedding import (
    RNAEmbedding,
)


class ContrastiveLearningEngine:
    """
    Measures similarity between RNA embeddings.

    Foundation for self-supervised representation
    learning.
    """

    def similarity(
        self,
        first: RNAEmbedding,
        second: RNAEmbedding,
    ) -> float:
        """
        Calculate cosine similarity.
        """

        numerator = sum(
            a * b
            for a, b in zip(
                first.values,
                second.values,
                strict=False,
            )
        )

        first_norm = sqrt(sum(value * value for value in first.values))

        second_norm = sqrt(sum(value * value for value in second.values))

        if first_norm == 0.0 or second_norm == 0.0:
            return 0.0

        return numerator / (first_norm * second_norm)

    def distance(
        self,
        first: RNAEmbedding,
        second: RNAEmbedding,
    ) -> float:
        """
        Calculate embedding distance.
        """

        similarity = self.similarity(
            first,
            second,
        )

        return 1.0 - similarity
