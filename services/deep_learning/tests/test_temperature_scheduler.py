"""
Tests for temperature scheduler.
"""

from __future__ import annotations

from dl.models.optimization.temperature_state import (
    TemperatureState,
)
from dl.solvers.temperature_scheduler import (
    TemperatureScheduler,
)


def test_initial_temperature() -> None:
    """
    Initial temperature is preserved.
    """

    scheduler = TemperatureScheduler(
        initial_temperature=10.0,
        cooling_rate=0.9,
    )

    state = scheduler.temperature(
        0,
    )

    assert isinstance(
        state,
        TemperatureState,
    )

    assert state.temperature == 10.0


def test_temperature_decay() -> None:
    """
    Temperature decreases over iterations.
    """

    scheduler = TemperatureScheduler(
        initial_temperature=10.0,
        cooling_rate=0.5,
    )

    state = scheduler.temperature(
        2,
    )

    assert state.temperature == 2.5
