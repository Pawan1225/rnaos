"""
Tests for tensor network encoder.
"""

from __future__ import annotations

from dl.models.optimization.tensor_network import (
    TensorNetwork,
)
from dl.optimization.tensor_network_encoder import (
    TensorNetworkEncoder,
)


def test_tensor_network_creation() -> None:
    """
    Tensor network is created.
    """

    encoder = TensorNetworkEncoder()

    network = encoder.encode(
        dimensions=(
            4,
            4,
            4,
        ),
    )

    assert isinstance(
        network,
        TensorNetwork,
    )

    assert (
        len(
            network.nodes,
        )
        == 3
    )


def test_tensor_connections() -> None:
    """
    Nodes are connected.
    """

    encoder = TensorNetworkEncoder()

    network = encoder.encode(
        dimensions=(
            2,
            2,
        ),
    )

    assert network.connections == (
        (
            "T0",
            "T1",
        ),
    )
