"""
Tests for tensor contraction engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.tensor_contraction import (
    TensorContractionResult,
)
from dl.optimization.tensor_contraction_engine import (
    TensorContractionEngine,
)


def test_tensor_contraction() -> None:
    """
    Matching tensors contract.
    """

    engine = TensorContractionEngine()

    result = engine.contract(
        left=(
            1.0,
            2.0,
            3.0,
        ),
        right=(
            4.0,
            5.0,
            6.0,
        ),
    )

    assert isinstance(
        result,
        TensorContractionResult,
    )

    assert result.values == (
        4.0,
        10.0,
        18.0,
    )


def test_dimension_mismatch() -> None:
    """
    Different dimensions fail.
    """

    engine = TensorContractionEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.contract(
            left=(1.0,),
            right=(
                1.0,
                2.0,
            ),
        )
