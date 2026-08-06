"""
RNAOS learned biological embedding model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RNAEmbedding:
    """
    Immutable RNA neural representation.

    Stores learned multi-modal biological features.
    """

    values: tuple[float, ...]

    embedding_dimension: int

    encoder_version: str

    source_sequence_length: int

    @property
    def dimension(
        self,
    ) -> int:
        """
        Return embedding size.
        """

        return self.embedding_dimension
