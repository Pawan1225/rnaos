"""
Tests for RNA sequence encoder.
"""

from __future__ import annotations

from dl.encoders.sequence_encoder import (
    RNASequenceEncoder,
)


def test_sequence_one_hot_encoding() -> None:
    """
    RNA sequence is encoded correctly.
    """

    encoder = RNASequenceEncoder()

    result = encoder.encode(
        "AUGC",
    )

    assert result == (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def test_unknown_nucleotide_encoding() -> None:
    """
    Unknown nucleotide produces zero vector.
    """

    encoder = RNASequenceEncoder()

    result = encoder.encode(
        "N",
    )

    assert result == ((0.0, 0.0, 0.0, 0.0),)


def test_output_dimension() -> None:
    """
    Encoder dimension is four.
    """

    encoder = RNASequenceEncoder()

    assert encoder.output_dimension() == 4
