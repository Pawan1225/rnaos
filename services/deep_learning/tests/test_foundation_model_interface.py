"""
Tests for RNA foundation model interface.
"""

from __future__ import annotations

from dl.foundation.foundation_model_interface import (
    RNAFoundationModelInterface,
)
from dl.models.foundation_model import (
    FoundationModelInfo,
)


def test_foundation_model_metadata() -> None:
    """
    Foundation model metadata works.
    """

    info = FoundationModelInfo(
        name="rna_foundation_v1",
        version="1.0",
        embedding_dimension=256,
        description="RNA transformer model",
    )

    interface = RNAFoundationModelInterface(
        info,
    )

    assert interface.info == info


def test_sequence_encoding() -> None:
    """
    Interface generates embeddings.
    """

    interface = RNAFoundationModelInterface(
        FoundationModelInfo(
            name="rna_foundation_v1",
            version="1.0",
            embedding_dimension=256,
            description="RNA model",
        ),
    )

    embedding = interface.encode(
        "AUGC",
    )

    assert embedding == (
        0.0,
        1.0,
        2.0,
        3.0,
    )
