"""
Tests for RNAOS embedding trainer.
"""

from __future__ import annotations

from dl.trainers.embedding_trainer import (
    EmbeddingTrainer,
)


def test_embedding_training_workflow() -> None:
    """
    Trainer executes lifecycle.
    """

    trainer = EmbeddingTrainer()

    model = object()

    result = trainer.train(
        model=model,
        dataset=None,
    )

    assert result is model

    assert (
        len(
            trainer.training_history,
        )
        == 1
    )


def test_embedding_validation() -> None:
    """
    Validation returns metrics.
    """

    trainer = EmbeddingTrainer()

    metrics = trainer.validate(
        model=None,
        dataset=None,
    )

    assert metrics["embedding_quality"] == 1.0

    assert metrics["validation_loss"] == 0.0
