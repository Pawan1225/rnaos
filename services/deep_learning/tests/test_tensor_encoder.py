"""
Tests for tensor encoder.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.tensor_representation import (
    TensorRepresentation,
)
from dl.optimization.tensor_encoder import (
    TensorEncoder,
)


def test_tensor_encoding() -> None:
    """
    Values are converted to tensor.
    """

    encoder = TensorEncoder()

    tensor = encoder.encode(
        values=(
            1.0,
            2.0,
            3.0,
            4.0,
        ),
        dimensions=(
            2,
            2,
        ),
    )

    assert isinstance(
        tensor,
        TensorRepresentation,
    )

    assert tensor.rank == 2


def test_invalid_dimensions() -> None:
    """
    Invalid shape fails.
    """

    encoder = TensorEncoder()

    with pytest.raises(
        ValueError,
    ):
        encoder.encode(
            values=(
                1.0,
                2.0,
            ),
            dimensions=(
                2,
                2,
            ),
        )
