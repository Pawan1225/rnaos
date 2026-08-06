"""
RNAOS embedding registry.
"""

from __future__ import annotations

from dl.models.embedding_metadata import (
    EmbeddingMetadata,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)


class EmbeddingRegistry:
    """
    In-memory registry for RNA embeddings.
    """

    def __init__(
        self,
    ) -> None:
        self._embeddings: dict[
            str,
            tuple[
                RNAEmbedding,
                EmbeddingMetadata,
            ],
        ] = {}

    def register(
        self,
        embedding_id: str,
        embedding: RNAEmbedding,
        metadata: EmbeddingMetadata,
    ) -> None:
        """
        Register an embedding.
        """

        self._embeddings[embedding_id] = (
            embedding,
            metadata,
        )

    def get(
        self,
        embedding_id: str,
    ) -> RNAEmbedding:
        """
        Retrieve embedding.
        """

        return self._embeddings[embedding_id][0]

    def metadata(
        self,
        embedding_id: str,
    ) -> EmbeddingMetadata:
        """
        Retrieve metadata.
        """

        return self._embeddings[embedding_id][1]

    def list_embeddings(
        self,
    ) -> tuple[str, ...]:
        """
        List registered embeddings.
        """

        return tuple(self._embeddings.keys())
