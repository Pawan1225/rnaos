from solver.utils import ExponentialCoolingSchedule


def test_temperature_decreases() -> None:
    """Temperature should decrease over time."""

    schedule = ExponentialCoolingSchedule(
        initial_temperature=100.0,
        cooling_rate=0.99,
    )

    t0 = schedule.temperature(0)
    t10 = schedule.temperature(10)
    t100 = schedule.temperature(100)

    assert t0 > t10 > t100


def test_temperature_never_below_minimum() -> None:
    """Temperature should never fall below the minimum."""

    schedule = ExponentialCoolingSchedule(
        initial_temperature=100.0,
        cooling_rate=0.90,
        minimum_temperature=0.01,
    )

    temperature = schedule.temperature(100_000)

    assert temperature == 0.01


def test_initial_temperature() -> None:
    """Iteration zero should return the initial temperature."""

    schedule = ExponentialCoolingSchedule(
        initial_temperature=250.0,
        cooling_rate=0.95,
    )

    assert schedule.temperature(0) == 250.0
