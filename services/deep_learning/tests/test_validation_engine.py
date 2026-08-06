"""
Tests for validation engine.
"""

from __future__ import annotations

from dl.models.validation_result import (
    ValidationResult,
)
from dl.trainers.validation_engine import (
    ValidationEngine,
)


class DummyModel:
    """
    Minimal evaluation model.
    """

    def evaluate(
        self,
        dataset,
    ) -> dict[str, float]:
        return {
            "loss": 0.25,
            "accuracy": 0.95,
        }


def test_validation_execution() -> None:
    """
    Validation executes successfully.
    """

    engine = ValidationEngine()

    result = engine.validate(
        model=DummyModel(),
        dataset=(
            1,
            2,
            3,
        ),
    )

    assert isinstance(
        result,
        ValidationResult,
    )

    assert result.validation_loss == 0.25

    assert result.validation_accuracy == 0.95

    assert result.samples_evaluated == 3

    assert result.success is True
