"""
Tests for RNAOS Base Encoder.
"""

from __future__ import annotations

from dl.core.base_encoder import (
    BaseEncoder,
)


def test_base_encoder_is_abstract() -> None:
    """
    Base encoder cannot be instantiated directly.
    """

    try:
        BaseEncoder()

    except TypeError:
        return

    raise AssertionError(
        "BaseEncoder should be abstract.",
    )
