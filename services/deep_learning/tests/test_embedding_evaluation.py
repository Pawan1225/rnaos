"""
Tests for embedding evaluation engine.
"""

from __future__ import annotations

from dl.evaluation.embedding_evaluation_engine import (
    EmbeddingEvaluationEngine,
)
from dl.models.embedding_evaluation import (
    EmbeddingEvaluationReport,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)


def test_embedding_evaluation() -> None:
    """
    Embedding quality is evaluated.
    """

    engine = EmbeddingEvaluationEngine()

    embedding = RNAEmbedding(
        values=(
            1.0,
            0.5,
            0.0,
        ),
        embedding_dimension=3,
        encoder_version="v1",
        source_sequence_length=3,
    )

    report = engine.evaluate(
        embedding,
    )

    assert isinstance(
        report,
        EmbeddingEvaluationReport,
    )

    assert report.embedding_dimension == 3

    assert report.sparsity_score == 1 / 3
