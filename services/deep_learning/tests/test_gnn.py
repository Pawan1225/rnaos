"""
Tests for RNAOS GNN architecture.
"""

from __future__ import annotations

from dl.architectures.gnn import (
    GNNModel,
)


def test_gnn_initialization() -> None:
    """
    GNN initializes correctly.
    """

    model = GNNModel(
        node_features=4,
    )

    assert model.node_features == 4

    assert model.hidden_dimension == 64


def test_gnn_prediction() -> None:
    """
    GNN generates graph prediction.
    """

    model = GNNModel(
        node_features=3,
    )

    prediction = model.predict(
        (
            1.0,
            2.0,
            3.0,
        ),
    )

    assert prediction == (2.0,)


def test_gnn_evaluation() -> None:
    """
    GNN evaluation returns metrics.
    """

    model = GNNModel(
        node_features=3,
    )

    metrics = model.evaluate(
        None,
    )

    assert metrics["loss"] == 0.0
