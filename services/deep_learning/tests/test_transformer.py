"""
Tests for RNAOS Transformer architecture.
"""

from __future__ import annotations

from dl.architectures.transformer import (
    TransformerEncoderModel,
)


def test_transformer_initialization() -> None:
    """
    Transformer initializes correctly.
    """

    model = TransformerEncoderModel(
        input_dimension=128,
    )

    assert model.input_dimension == 128

    assert model.attention_heads == 8


def test_transformer_prediction() -> None:
    """
    Transformer generates prediction.
    """

    model = TransformerEncoderModel(
        input_dimension=3,
    )

    prediction = model.predict(
        (
            1.0,
            2.0,
            3.0,
        ),
    )

    assert prediction == (2.0,)


def test_transformer_evaluation() -> None:
    """
    Transformer evaluation returns metrics.
    """

    model = TransformerEncoderModel(
        input_dimension=3,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
