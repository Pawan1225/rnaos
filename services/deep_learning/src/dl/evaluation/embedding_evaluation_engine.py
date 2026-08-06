"""
RNAOS embedding evaluation engine.
"""

from __future__ import annotations

from math import sqrt

from dl.models.embedding_evaluation import (
    EmbeddingEvaluationReport,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)


class EmbeddingEvaluationEngine:
    """
    Evaluates RNA embedding quality.
    """

    def evaluate(
        self,
        embedding: RNAEmbedding,
    ) -> EmbeddingEvaluationReport:
        """
        Generate embedding evaluation report.
        """

        norm = sqrt(sum(value * value for value in embedding.values))

        sparsity = self._calculate_sparsity(
            embedding,
        )

        quality = self._quality_score(
            norm,
            sparsity,
        )

        return EmbeddingEvaluationReport(
            embedding_dimension=embedding.dimension,
            embedding_norm=norm,
            sparsity_score=sparsity,
            quality_score=quality,
            evaluation_version="v1",
        )

    def _calculate_sparsity(
        self,
        embedding: RNAEmbedding,
    ) -> float:
        """
        Calculate zero-value ratio.
        """

        if not embedding.values:
            return 1.0

        zeros = sum(1 for value in embedding.values if value == 0.0)

        return zeros / len(
            embedding.values,
        )

    def _quality_score(
        self,
        norm: float,
        sparsity: float,
    ) -> float:
        """
        Generate deterministic quality score.
        """

        return max(
            0.0,
            min(
                1.0,
                (1.0 - sparsity)
                * min(
                    norm,
                    1.0,
                ),
            ),
        )
