"""
Tests for RNAOS MLP architecture.
"""

from __future__ import annotations

from dl.architectures.mlp import (
    MLPModel,
)


def test_mlp_initialization() -> None:
    """
    MLP initializes correctly.
    """

    model = MLPModel(
        input_dimension=128,
    )

    assert model.input_dimension == 128

    assert model.hidden_dimensions == (
        64,
        32,
    )


def test_mlp_prediction() -> None:
    """
    MLP generates prediction.
    """

    model = MLPModel(
        input_dimension=3,
    )

    prediction = model.predict(
        (
            1.0,
            2.0,
            3.0,
        ),
    )

    assert prediction == (6.0,)


def test_mlp_evaluation() -> None:
    """
    MLP evaluation returns metrics.
    """

    model = MLPModel(
        input_dimension=3,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
