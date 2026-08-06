"""
Tests for RNAOS CNN architecture.
"""

from __future__ import annotations

from dl.architectures.cnn import (
    CNNModel,
)


def test_cnn_initialization() -> None:
    """
    CNN initializes correctly.
    """

    model = CNNModel(
        input_channels=4,
    )

    assert model.input_channels == 4

    assert model.kernel_size == 3

    assert model.filters == 32


def test_cnn_prediction() -> None:
    """
    CNN generates prediction.
    """

    model = CNNModel(
        input_channels=4,
    )

    prediction = model.predict(
        (
            1.0,
            2.0,
            3.0,
        ),
    )

    assert prediction == (2.0,)


def test_cnn_evaluation() -> None:
    """
    CNN evaluation returns metrics.
    """

    model = CNNModel(
        input_channels=4,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
