"""
Tests for learning rate scheduler.
"""

from __future__ import annotations

from dl.trainers.learning_rate_scheduler import (
    LearningRateScheduler,
)


def test_initial_learning_rate() -> None:
    """
    Scheduler initializes correctly.
    """

    scheduler = LearningRateScheduler()

    assert scheduler.get_learning_rate() == 0.001


def test_learning_rate_decay() -> None:
    """
    Scheduler reduces learning rate.
    """

    scheduler = LearningRateScheduler(
        initial_learning_rate=0.001,
        decay_factor=0.5,
    )

    updated = scheduler.step()

    assert updated == 0.0005

    assert scheduler.get_learning_rate() == 0.0005


def test_scheduler_reset() -> None:
    """
    Scheduler resets state.
    """

    scheduler = LearningRateScheduler()

    scheduler.step()

    scheduler.reset()

    assert scheduler.get_learning_rate() == 0.001
