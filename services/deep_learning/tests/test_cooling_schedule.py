"""
Tests for cooling schedules.
"""

from __future__ import annotations

from dl.solvers.exponential_cooling import (
    ExponentialCooling,
)
from dl.solvers.linear_cooling import (
    LinearCooling,
)


def test_linear_cooling() -> None:
    """
    Linear cooling decreases temperature.
    """

    cooling = LinearCooling(
        rate=1.0,
    )

    result = cooling.calculate(
        temperature=10.0,
        iteration=5,
    )

    assert result == 5.0


def test_exponential_cooling() -> None:
    """
    Exponential cooling decreases temperature.
    """

    cooling = ExponentialCooling(
        rate=0.5,
    )

    result = cooling.calculate(
        temperature=10.0,
        iteration=2,
    )

    assert result == 2.5
