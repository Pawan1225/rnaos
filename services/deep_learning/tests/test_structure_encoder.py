"""
Tests for RNA structure encoder.
"""

from __future__ import annotations

from dl.encoders.structure_encoder import (
    RNAStructureEncoder,
)


def test_structure_encoding() -> None:
    """
    Secondary structure is encoded correctly.
    """

    encoder = RNAStructureEncoder()

    result = encoder.encode(
        "().",
    )

    assert result == (
        (
            1.0,
            0.0,
        ),
        (
            1.0,
            0.0,
        ),
        (
            0.0,
            1.0,
        ),
    )


def test_unknown_structure_symbol() -> None:
    """
    Unknown symbols produce zero vectors.
    """

    encoder = RNAStructureEncoder()

    result = encoder.encode(
        "?",
    )

    assert result == (
        (
            0.0,
            0.0,
        ),
    )


def test_structure_dimension() -> None:
    """
    Structure encoder dimension is two.
    """

    encoder = RNAStructureEncoder()

    assert encoder.output_dimension() == 2
