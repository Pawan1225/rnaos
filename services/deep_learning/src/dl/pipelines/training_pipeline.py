"""
RNAOS deep learning training pipeline.
"""

from __future__ import annotations

from typing import Any

from dl.models.checkpoint import (
    Checkpoint,
)
from dl.models.training_configuration import (
    TrainingConfiguration,
)
from dl.models.training_report import (
    TrainingReport,
)
from dl.trainers.checkpoint_manager import (
    CheckpointManager,
)
from dl.trainers.training_loop_engine import (
    TrainingLoopEngine,
)
from dl.trainers.validation_engine import (
    ValidationEngine,
)


class TrainingPipeline:
    """
    Orchestrates complete training lifecycle.
    """

    def __init__(
        self,
    ) -> None:
        self.training_engine = TrainingLoopEngine()

        self.validation_engine = ValidationEngine()

        self.checkpoint_manager = CheckpointManager()

    def run(
        self,
        model: Any,
        train_dataset: Any,
        validation_dataset: tuple[Any, ...],
        configuration: TrainingConfiguration,
        checkpoint: Checkpoint,
    ) -> TrainingReport:
        """
        Execute training pipeline.
        """

        training_result = self.training_engine.train(
            model=model,
            dataset=train_dataset,
            configuration=configuration,
        )

        validation_result = self.validation_engine.validate(
            model=model,
            dataset=validation_dataset,
        )

        self.checkpoint_manager.save(
            checkpoint,
        )

        return TrainingReport(
            training_result=training_result,
            validation_result=validation_result,
            checkpoint_id=checkpoint.checkpoint_id,
            completed=True,
        )
