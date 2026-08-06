"""
Tests for RNAOS contrastive learning.
"""

from __future__ import annotations

from dl.learning.contrastive_learning import (
    ContrastiveLearningEngine,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)


def test_embedding_similarity() -> None:
    """
    Similar embeddings produce high similarity.
    """

    engine = ContrastiveLearningEngine()

    embedding_a = RNAEmbedding(
        values=(
            1.0,
            0.0,
        ),
        embedding_dimension=2,
        encoder_version="v1",
        source_sequence_length=2,
    )

    embedding_b = RNAEmbedding(
        values=(
            1.0,
            0.0,
        ),
        embedding_dimension=2,
        encoder_version="v1",
        source_sequence_length=2,
    )

    score = engine.similarity(
        embedding_a,
        embedding_b,
    )

    assert score == 1.0


def test_embedding_distance() -> None:
    """
    Distance is inverse of similarity.
    """

    engine = ContrastiveLearningEngine()

    embedding_a = RNAEmbedding(
        values=(
            1.0,
            0.0,
        ),
        embedding_dimension=2,
        encoder_version="v1",
        source_sequence_length=2,
    )

    embedding_b = RNAEmbedding(
        values=(
            0.0,
            1.0,
        ),
        embedding_dimension=2,
        encoder_version="v1",
        source_sequence_length=2,
    )

    distance = engine.distance(
        embedding_a,
        embedding_b,
    )

    assert distance == 1.0
