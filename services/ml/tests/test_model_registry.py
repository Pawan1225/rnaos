"""
Tests for the RNAOS Model Registry.
"""

from __future__ import annotations

import pytest
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
from ml.models.trained_model import (
    TrainedModel,
)


class DummyEstimator:
    """
    Minimal estimator for registry tests.
    """


@pytest.fixture
def registered_model() -> RegisteredModel:
    """
    Create deterministic registered model.
    """

    metadata = ModelMetadata(
        model_id="model_001",
        model_name="random_forest",
        version="v1",
        training_time=1.0,
        feature_count=3,
        sample_count=10,
        created_at="2026-08-06",
    )

    trained_model = TrainedModel(
        model_name="random_forest",
        estimator=DummyEstimator(),
        metric_name="score",
        metric_value=0.95,
        training_time=1.0,
        feature_count=3,
        sample_count=10,
        training_status="completed",
    )

    evaluation = ModelEvaluation(
        model_name="random_forest",
        metrics={
            "rmse": 0.1,
            "mae": 0.05,
            "r2": 0.95,
        },
        evaluation_version="v1",
        sample_count=10,
    )

    return RegisteredModel(
        metadata=metadata,
        trained_model=trained_model,
        evaluation=evaluation,
    )


@pytest.fixture
def registry() -> ModelRegistry:
    """
    Create model registry.
    """

    return ModelRegistry()


def test_register_model(
    registry: ModelRegistry,
    registered_model: RegisteredModel,
) -> None:
    """
    Register model successfully.
    """

    registry.register(
        registered_model,
    )

    assert "model_001" in registry.list_models()


def test_get_model(
    registry: ModelRegistry,
    registered_model: RegisteredModel,
) -> None:
    """
    Retrieve registered model.
    """

    registry.register(
        registered_model,
    )

    result = registry.get(
        "model_001",
    )

    assert result == registered_model


def test_metadata_preserved(
    registry: ModelRegistry,
    registered_model: RegisteredModel,
) -> None:
    """
    Metadata remains unchanged.
    """

    registry.register(
        registered_model,
    )

    result = registry.get(
        "model_001",
    )

    assert result.metadata.model_name == "random_forest"


def test_remove_model(
    registry: ModelRegistry,
    registered_model: RegisteredModel,
) -> None:
    """
    Remove registered model.
    """

    registry.register(
        registered_model,
    )

    registry.remove(
        "model_001",
    )

    assert registry.list_models() == ()


def test_missing_model(
    registry: ModelRegistry,
) -> None:
    """
    Missing model raises error.
    """

    with pytest.raises(KeyError):
        registry.get(
            "unknown",
        )
