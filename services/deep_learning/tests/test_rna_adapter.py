"""
Tests for RNAOS RNA Adapter.
"""

from __future__ import annotations

from dl.adapters.rna_adapter import (
    RNAAdapter,
)


def test_sequence_conversion() -> None:
    """
    RNA sequence conversion works.
    """

    adapter = RNAAdapter()

    result = adapter.convert_sequence(
        "AUGCG",
    )

    assert result["sequence"] == "AUGCG"

    assert result["length"] == 5


def test_profile_conversion() -> None:
    """
    RNA profile conversion works.
    """

    adapter = RNAAdapter()

    profile = {
        "gc_content": 0.5,
    }

    result = adapter.convert_profile(
        profile,
    )

    assert result["features"] == profile
