"""
Tests for tensor optimization engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.tensor_state import (
    TensorOptimizationState,
)
from dl.optimization.tensor_engine import (
    TensorOptimizationEngine,
)


def test_create_tensor_state() -> None:
    """
    Tensor state is created.
    """

    engine = TensorOptimizationEngine()

    state = engine.create(
        values=(
            0.1,
            0.2,
            0.3,
            0.4,
        ),
        shape=(
            2,
            2,
        ),
    )

    assert isinstance(
        state,
        TensorOptimizationState,
    )

    assert state.dimension == 2


def test_invalid_tensor_shape() -> None:
    """
    Invalid tensor shape fails.
    """

    engine = TensorOptimizationEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.create(
            values=(
                0.1,
                0.2,
            ),
            shape=(
                2,
                2,
            ),
        )
