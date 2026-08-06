"""
Tests for training pipeline.
"""

from __future__ import annotations

from dl.models.checkpoint import (
    Checkpoint,
)
from dl.models.training_configuration import (
    TrainingConfiguration,
)
from dl.models.training_report import (
    TrainingReport,
)
from dl.pipelines.training_pipeline import (
    TrainingPipeline,
)


class DummyModel:
    """
    Minimal model implementation.
    """

    def train(
        self,
        dataset,
    ) -> None:
        return None

    def evaluate(
        self,
        dataset,
    ) -> dict[str, float]:
        return {
            "loss": 0.1,
            "accuracy": 0.99,
        }


def test_training_pipeline_execution() -> None:
    """
    Pipeline executes complete workflow.
    """

    pipeline = TrainingPipeline()

    checkpoint = Checkpoint(
        checkpoint_id="run_001",
        model_name="transformer",
        epoch=10,
        path="/tmp/model.ckpt",
        created_at="2026-08-06",
    )

    report = pipeline.run(
        model=DummyModel(),
        train_dataset=None,
        validation_dataset=(
            1,
            2,
        ),
        configuration=TrainingConfiguration(
            epochs=2,
        ),
        checkpoint=checkpoint,
    )

    assert isinstance(
        report,
        TrainingReport,
    )

    assert report.completed is True

    assert report.checkpoint_id == "run_001"
