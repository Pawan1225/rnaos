"""
Tests for RNA embedding network.
"""

from __future__ import annotations

from dl.models.rna_embedding import (
    RNAEmbedding,
)
from dl.models.rna_embedding_network import (
    RNAEmbeddingNetwork,
)


def test_embedding_generation() -> None:
    """
    Network generates RNA embedding.
    """

    network = RNAEmbeddingNetwork(
        embedding_dimension=8,
    )

    embedding = network.encode(
        sequence_tensor=(
            (
                1.0,
                0.0,
            ),
        ),
        structure_tensor=(
            (
                0.5,
                0.5,
            ),
        ),
        thermodynamic_features=(-2.0,),
    )

    assert isinstance(
        embedding,
        RNAEmbedding,
    )

    assert embedding.dimension == 8

    assert embedding.encoder_version == "embedding-network-v1"
