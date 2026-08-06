"""
RNAOS multi-modal RNA fusion encoder.
"""

from __future__ import annotations

from dl.models.rna_embedding import (
    RNAEmbedding,
)


class RNAMultiModalEncoder:
    """
    Combines RNA sequence, structure,
    and thermodynamic representations.
    """

    def encode(
        self,
        sequence_tensor: tuple[tuple[float, ...], ...],
        structure_tensor: tuple[tuple[float, ...], ...],
        thermodynamic_features: tuple[float, ...],
    ) -> RNAEmbedding:
        """
        Create unified RNA embedding.
        """

        flattened_sequence = tuple(value for token in sequence_tensor for value in token)

        flattened_structure = tuple(value for token in structure_tensor for value in token)

        embedding = flattened_sequence + flattened_structure + thermodynamic_features

        return RNAEmbedding(
            values=embedding,
            embedding_dimension=len(embedding),
            encoder_version="v1",
            source_sequence_length=len(
                sequence_tensor,
            ),
        )
