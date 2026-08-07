"""
Tests for acceptance probability engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.acceptance_result import (
    AcceptanceResult,
)
from dl.solvers.acceptance_engine import (
    AcceptanceProbabilityEngine,
)


def test_better_solution_accepts() -> None:
    """
    Better energy is always accepted.
    """

    engine = AcceptanceProbabilityEngine()

    result = engine.calculate(
        current_energy=-5.0,
        new_energy=-8.0,
        temperature=10.0,
    )

    assert isinstance(
        result,
        AcceptanceResult,
    )

    assert result.accepted is True


def test_invalid_temperature() -> None:
    """
    Zero temperature fails.
    """

    engine = AcceptanceProbabilityEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.calculate(
            current_energy=-5.0,
            new_energy=-4.0,
            temperature=0.0,
        )
