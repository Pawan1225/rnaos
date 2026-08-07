"""
Tests for restart strategy engine.
"""

from __future__ import annotations

from dl.models.optimization.restart_strategy import (
    RestartDecision,
)
from dl.solvers.restart_engine import (
    RestartStrategyEngine,
)


def test_restart_on_stagnation() -> None:
    """
    Stagnation triggers restart.
    """

    engine = RestartStrategyEngine(
        patience=10,
    )

    result = engine.evaluate(
        iterations_without_improvement=20,
    )

    assert isinstance(
        result,
        RestartDecision,
    )

    assert result.restart is True


def test_no_restart_when_progressing() -> None:
    """
    Progress does not restart.
    """

    engine = RestartStrategyEngine(
        patience=10,
    )

    result = engine.evaluate(
        iterations_without_improvement=5,
    )

    assert result.restart is False
