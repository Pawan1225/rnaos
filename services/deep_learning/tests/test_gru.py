"""
Tests for RNAOS GRU architecture.
"""

from __future__ import annotations

from dl.architectures.gru import (
    GRUModel,
)


def test_gru_initialization() -> None:
    """
    GRU initializes correctly.
    """

    model = GRUModel(
        input_dimension=128,
    )

    assert model.input_dimension == 128

    assert model.hidden_dimension == 64


def test_gru_prediction() -> None:
    """
    GRU generates prediction.
    """

    model = GRUModel(
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


def test_gru_evaluation() -> None:
    """
    GRU evaluation returns metrics.
    """

    model = GRUModel(
        input_dimension=3,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
