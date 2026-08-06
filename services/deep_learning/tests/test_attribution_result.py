"""
Tests for attribution result model.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.attribution_result import (
    AttributionResult,
)


def test_attribution_result_creation() -> None:
    """
    Attribution result initializes correctly.
    """

    result = AttributionResult(
        method="saliency",
        features=(
            "A",
            "U",
            "G",
        ),
        importance_scores=(
            0.2,
            0.4,
            0.9,
        ),
        confidence=0.95,
    )

    assert result.method == "saliency"

    assert result.features == (
        "A",
        "U",
        "G",
    )

    assert result.importance_scores == (
        0.2,
        0.4,
        0.9,
    )

    assert result.confidence == 0.95


def test_custom_metadata() -> None:
    """
    Metadata is preserved.
    """

    result = AttributionResult(
        method="attention",
        features=("A",),
        importance_scores=(1.0,),
        metadata=("transformer_layer_1",),
    )

    assert result.metadata == ("transformer_layer_1",)


def test_result_is_immutable() -> None:
    """
    Attribution result cannot change.
    """

    result = AttributionResult(
        method="saliency",
        features=("A",),
        importance_scores=(1.0,),
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        result.method = "gradient"
