"""
Tests for RNAOS BiLSTM architecture.
"""

from __future__ import annotations

from dl.architectures.bilstm import (
    BiLSTMModel,
)


def test_bilstm_initialization() -> None:
    """
    BiLSTM initializes correctly.
    """

    model = BiLSTMModel(
        input_dimension=128,
    )

    assert model.input_dimension == 128

    assert model.hidden_dimension == 64


def test_bilstm_prediction() -> None:
    """
    BiLSTM generates sequence prediction.
    """

    model = BiLSTMModel(
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


def test_bilstm_evaluation() -> None:
    """
    BiLSTM evaluation returns metrics.
    """

    model = BiLSTMModel(
        input_dimension=3,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
