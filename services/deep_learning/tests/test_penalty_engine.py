"""
Tests for constraint penalty engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.penalty import (
    PenaltyConfiguration,
)
from dl.optimization.penalty_engine import (
    ConstraintPenaltyEngine,
)


def test_create_penalty() -> None:
    """
    Penalty configuration is created.
    """

    engine = ConstraintPenaltyEngine()

    penalty = engine.create(
        constraint_name="unique_pairing",
        penalty_value=10.0,
    )

    assert isinstance(
        penalty,
        PenaltyConfiguration,
    )

    assert penalty.penalty_value == 10.0


def test_invalid_penalty() -> None:
    """
    Negative penalties fail.
    """

    engine = ConstraintPenaltyEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.create(
            constraint_name="invalid",
            penalty_value=-1.0,
        )
