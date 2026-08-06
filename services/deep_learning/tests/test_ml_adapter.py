"""
Tests for RNAOS ML Adapter.
"""

from __future__ import annotations

from dl.adapters.ml_adapter import (
    MLAdapter,
)


def test_feature_conversion() -> None:
    """
    ML feature conversion works.
    """

    adapter = MLAdapter()

    result = adapter.convert_features(
        [0.1, 0.2],
    )

    assert result["features"] == [
        0.1,
        0.2,
    ]


def test_prediction_conversion() -> None:
    """
    ML prediction conversion works.
    """

    adapter = MLAdapter()

    result = adapter.convert_prediction(
        0.91,
    )

    assert result["prediction"] == 0.91
