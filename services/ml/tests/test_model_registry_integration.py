"""
Integration tests for the RNAOS Model Registry pipeline.
"""

from __future__ import annotations

from ml.analyzers.model_evaluation_engine import (
    ModelEvaluationEngine,
)
from ml.analyzers.model_registry import (
    ModelRegistry,
)
from ml.models.model_evaluation import (
    ModelEvaluation,
)
from ml.models.model_metadata import (
    ModelMetadata,
)
from ml.models.registered_model import (
    RegisteredModel,
)


def test_training_evaluation_registry_pipeline(
    trained_model,
    evaluation_engine: ModelEvaluationEngine,
    dataset,
) -> None:
    """
    Validate complete model lifecycle.

    Training
        ↓
    Evaluation
        ↓
    Registry
        ↓
    Retrieval
    """

    evaluation = evaluation_engine.evaluate(
        trained_model=trained_model,
        dataset=dataset,
    )

    assert isinstance(
        evaluation,
        ModelEvaluation,
    )

    metadata = ModelMetadata(
        model_id="model_001",
        model_name=trained_model.model_name,
        version="v1",
        training_time=trained_model.training_time,
        feature_count=trained_model.feature_count,
        sample_count=trained_model.sample_count,
        created_at="2026-08-06",
    )

    registered_model = RegisteredModel(
        metadata=metadata,
        trained_model=trained_model,
        evaluation=evaluation,
    )

    registry = ModelRegistry()

    registry.register(
        registered_model,
    )

    retrieved = registry.get(
        "model_001",
    )

    assert retrieved == registered_model

    assert retrieved.metadata.model_name == trained_model.model_name

    assert retrieved.evaluation.evaluation_version == "v1"


def test_registry_preserves_evaluation_metrics(
    trained_model,
    evaluation_engine: ModelEvaluationEngine,
    dataset,
) -> None:
    """
    Validate evaluation metrics survive registration.
    """

    evaluation = evaluation_engine.evaluate(
        trained_model=trained_model,
        dataset=dataset,
    )

    metadata = ModelMetadata(
        model_id="model_002",
        model_name=trained_model.model_name,
        version="v1",
        training_time=trained_model.training_time,
        feature_count=trained_model.feature_count,
        sample_count=trained_model.sample_count,
        created_at="2026-08-06",
    )

    registered_model = RegisteredModel(
        metadata=metadata,
        trained_model=trained_model,
        evaluation=evaluation,
    )

    registry = ModelRegistry()

    registry.register(
        registered_model,
    )

    result = registry.get(
        "model_002",
    )

    assert result.evaluation.metrics == evaluation.metrics
