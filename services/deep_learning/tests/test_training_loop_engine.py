"""
Tests for training loop engine.
"""

from __future__ import annotations

from dl.models.training_configuration import (
    TrainingConfiguration,
)
from dl.models.training_result import (
    TrainingResult,
)
from dl.trainers.training_loop_engine import (
    TrainingLoopEngine,
)


class DummyModel:
    """
    Minimal training model.
    """

    def __init__(self) -> None:
        self.calls = 0

    def train(
        self,
        dataset,
    ) -> None:
        self.calls += 1


def test_training_loop_execution() -> None:
    """
    Training loop executes epochs.
    """

    engine = TrainingLoopEngine()

    model = DummyModel()

    configuration = TrainingConfiguration(
        epochs=3,
    )

    result = engine.train(
        model=model,
        dataset=None,
        configuration=configuration,
    )

    assert isinstance(
        result,
        TrainingResult,
    )

    assert result.epochs_completed == 3

    assert result.success is True

    assert model.calls == 3


def test_training_history() -> None:
    """
    Training history is recorded.
    """

    engine = TrainingLoopEngine()

    result = engine.train(
        model=DummyModel(),
        dataset=None,
        configuration=TrainingConfiguration(
            epochs=2,
        ),
    )

    assert result.training_history == (
        0.0,
        0.0,
    )
