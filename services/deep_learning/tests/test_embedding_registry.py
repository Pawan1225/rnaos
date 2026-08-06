"""
Tests for RNAOS embedding registry.
"""

from __future__ import annotations

from dl.models.embedding_metadata import (
    EmbeddingMetadata,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)
from dl.registry.embedding_registry import (
    EmbeddingRegistry,
)


def create_embedding() -> RNAEmbedding:
    """
    Create deterministic RNA embedding.
    """

    return RNAEmbedding(
        values=(
            0.1,
            0.2,
            0.3,
        ),
        embedding_dimension=3,
        encoder_version="v1",
        source_sequence_length=3,
    )


def create_metadata() -> EmbeddingMetadata:
    """
    Create deterministic embedding metadata.
    """

    return EmbeddingMetadata(
        embedding_id="rna_embedding_001",
        version="v1",
        model_name="rna_embedding_network",
        dimension=3,
    )


def test_register_embedding() -> None:
    """
    Embedding can be registered.
    """

    registry = EmbeddingRegistry()

    embedding = create_embedding()

    metadata = create_metadata()

    registry.register(
        embedding_id="rna_embedding_001",
        embedding=embedding,
        metadata=metadata,
    )

    assert "rna_embedding_001" in registry.list_embeddings()


def test_retrieve_embedding() -> None:
    """
    Registered embedding can be retrieved.
    """

    registry = EmbeddingRegistry()

    embedding = create_embedding()

    registry.register(
        embedding_id="rna_embedding_001",
        embedding=embedding,
        metadata=create_metadata(),
    )

    result = registry.get(
        "rna_embedding_001",
    )

    assert result == embedding


def test_retrieve_metadata() -> None:
    """
    Embedding metadata can be retrieved.
    """

    registry = EmbeddingRegistry()

    metadata = create_metadata()

    registry.register(
        embedding_id="rna_embedding_001",
        embedding=create_embedding(),
        metadata=metadata,
    )

    result = registry.metadata(
        "rna_embedding_001",
    )

    assert result == metadata


def test_list_embeddings() -> None:
    """
    Registry returns all embedding identifiers.
    """

    registry = EmbeddingRegistry()

    registry.register(
        embedding_id="embedding_a",
        embedding=create_embedding(),
        metadata=create_metadata(),
    )

    registry.register(
        embedding_id="embedding_b",
        embedding=create_embedding(),
        metadata=create_metadata(),
    )

    embeddings = registry.list_embeddings()

    assert embeddings == (
        "embedding_a",
        "embedding_b",
    )
