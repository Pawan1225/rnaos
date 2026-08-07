"""
Tests for tensor search optimizer.
"""

from __future__ import annotations

from dl.models.optimization.tensor_candidate import (
    TensorCandidate,
)
from dl.optimization.tensor_search_optimizer import (
    TensorSearchOptimizer,
)


def test_tensor_search() -> None:
    """
    Tensor search produces candidate.
    """

    optimizer = TensorSearchOptimizer(
        seed=42,
    )

    result = optimizer.search(
        dimension=4,
        candidates=10,
    )

    assert isinstance(
        result,
        TensorCandidate,
    )

    assert (
        len(
            result.state,
        )
        == 4
    )


def test_candidate_score() -> None:
    """
    Score is calculated.
    """

    optimizer = TensorSearchOptimizer()

    result = optimizer.search(
        dimension=3,
        candidates=5,
    )

    assert result.score >= 0
