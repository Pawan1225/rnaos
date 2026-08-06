"""
RNAOS RNA embedding network.
"""

from __future__ import annotations

from dl.models.rna_embedding import (
    RNAEmbedding,
)


class RNAEmbeddingNetwork:
    """
    Learns biological representations from
    neural RNA inputs.

    Initial implementation provides the
    representation learning contract.
    """

    def __init__(
        self,
        embedding_dimension: int = 128,
    ) -> None:
        self.embedding_dimension = embedding_dimension

    def encode(
        self,
        sequence_tensor: tuple[tuple[float, ...], ...],
        structure_tensor: tuple[tuple[float, ...], ...],
        thermodynamic_features: tuple[float, ...],
    ) -> RNAEmbedding:
        """
        Generate RNA embedding representation.
        """

        values = (
            self._flatten(
                sequence_tensor,
            )
            + self._flatten(
                structure_tensor,
            )
            + thermodynamic_features
        )

        resized = self._resize(
            values,
        )

        return RNAEmbedding(
            values=resized,
            embedding_dimension=(self.embedding_dimension),
            encoder_version="embedding-network-v1",
            source_sequence_length=len(
                sequence_tensor,
            ),
        )

    def _flatten(
        self,
        values: tuple[tuple[float, ...], ...],
    ) -> tuple[float, ...]:
        """
        Flatten tensor representation.
        """

        return tuple(value for row in values for value in row)

    def _resize(
        self,
        values: tuple[float, ...],
    ) -> tuple[float, ...]:
        """
        Normalize representation size.

        Placeholder for future neural layers.
        """

        if len(values) >= self.embedding_dimension:
            return values[: self.embedding_dimension]

        return values + (0.0,) * (self.embedding_dimension - len(values))
