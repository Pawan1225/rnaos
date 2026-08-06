"""
Tests for early stopping controller.
"""

from __future__ import annotations

from dl.trainers.early_stopping import (
    EarlyStoppingController,
)


def test_improvement_resets_counter() -> None:
    """
    Improvement resets patience.
    """

    controller = EarlyStoppingController(
        patience=2,
    )

    assert (
        controller.update(
            1.0,
        )
        is False
    )

    assert (
        controller.update(
            0.8,
        )
        is False
    )

    assert controller.wait_count == 0


def test_stops_after_patience() -> None:
    """
    Controller stops after no improvement.
    """

    controller = EarlyStoppingController(
        patience=2,
    )

    controller.update(
        1.0,
    )

    controller.update(
        1.1,
    )

    result = controller.update(
        1.2,
    )

    assert result is True

    assert controller.should_stop is True


def test_reset() -> None:
    """
    Controller resets correctly.
    """

    controller = EarlyStoppingController()

    controller.update(
        1.0,
    )

    controller.reset()

    assert controller.best_loss is None

    assert controller.wait_count == 0
