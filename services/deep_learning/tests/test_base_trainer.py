"""
Tests for RNAOS Base Trainer.
"""

from __future__ import annotations

from dl.core.base_trainer import (
    BaseTrainer,
)


def test_base_trainer_is_abstract() -> None:
    """
    Base trainer cannot be instantiated directly.
    """

    try:
        BaseTrainer()

    except TypeError:
        return

    raise AssertionError(
        "BaseTrainer should be abstract.",
    )
