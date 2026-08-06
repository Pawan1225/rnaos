"""
Tests for RNA multi-modal encoder.
"""

from __future__ import annotations

from dl.fusion.rna_multimodal_encoder import (
    RNAMultiModalEncoder,
)
from dl.models.rna_embedding import (
    RNAEmbedding,
)


def test_multimodal_embedding_creation() -> None:
    """
    Multi-modal representations are fused.
    """

    encoder = RNAMultiModalEncoder()

    result = encoder.encode(
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
        thermodynamic_features=(-2.5,),
    )

    assert isinstance(
        result,
        RNAEmbedding,
    )

    assert result.dimension == 5

    assert result.source_sequence_length == 1
