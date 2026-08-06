"""
RNAOS RNA embedding model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RNAEmbedding:
    """
    Immutable RNA embedding.

    Represents a dense numerical embedding generated
    from an AI feature vector. The embedding is intended
    to serve as the common representation for machine
    learning, deep learning, quantum machine learning,
    and optimization engines.
    """

    values: tuple[float, ...]

    dimension: int

    @property
    def size(
        self,
    ) -> int:
        """
        Return the embedding dimension.
        """
        return self.dimension
