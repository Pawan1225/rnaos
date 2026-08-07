"""
Tests for low-rank approximation engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.low_rank_tensor import (
    LowRankTensor,
)
from dl.optimization.low_rank_engine import (
    LowRankApproximationEngine,
)


def test_low_rank_compression() -> None:
    """
    Tensor is compressed.
    """

    engine = LowRankApproximationEngine()

    result = engine.approximate(
        values=(
            1.0,
            2.0,
            3.0,
            4.0,
        ),
        target_rank=2,
    )

    assert isinstance(
        result,
        LowRankTensor,
    )

    assert result.compressed_rank == 2

    assert result.values == (
        1.0,
        2.0,
    )


def test_invalid_rank() -> None:
    """
    Invalid rank fails.
    """

    engine = LowRankApproximationEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.approximate(
            values=(
                1.0,
                2.0,
            ),
            target_rank=5,
        )
