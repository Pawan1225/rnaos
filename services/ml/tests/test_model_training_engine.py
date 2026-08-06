"""
Tests for the RNAOS Model Training Engine.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from ml.analyzers.model_training_engine import (
    ModelTrainingEngine,
)
from ml.constants import (
    DEFAULT_CROSS_VALIDATION_FOLDS,
    DEFAULT_RANDOM_SEED,
    DEFAULT_SHUFFLE,
)
from ml.model_registry import (
    MODEL_REGISTRY,
)
from ml.models.ml_dataset import (
    MLDataset,
)
from ml.models.trained_model import (
    TrainedModel,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)

SUPPORTED_MODELS = tuple(
    MODEL_REGISTRY.keys(),
)


@pytest.fixture
def dataset() -> MLDataset:
    """Create a deterministic dataset."""

    features = (
        (0.10, 0.20, 0.30),
        (0.20, 0.30, 0.40),
        (0.30, 0.40, 0.50),
        (0.40, 0.50, 0.60),
        (0.50, 0.60, 0.70),
        (0.60, 0.70, 0.80),
        (0.70, 0.80, 0.90),
        (0.80, 0.90, 1.00),
        (0.90, 1.00, 1.10),
        (1.00, 1.10, 1.20),
    )

    targets = (
        0.15,
        0.25,
        0.35,
        0.45,
        0.55,
        0.65,
        0.75,
        0.85,
        0.95,
        1.05,
    )

    return MLDataset(
        feature_names=(
            "feature_1",
            "feature_2",
            "feature_3",
        ),
        features=features,
        targets=targets,
        train_indices=(
            0,
            1,
            2,
            3,
            4,
            5,
        ),
        validation_indices=(
            6,
            7,
        ),
        test_indices=(
            8,
            9,
        ),
        dataset_version="v1.0.0",
    )


@pytest.fixture
def configuration() -> TrainingConfiguration:
    """Create a deterministic training configuration."""

    return TrainingConfiguration(
        model_name="random_forest",
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )


@pytest.fixture
def engine() -> ModelTrainingEngine:
    """Create training engine."""

    return ModelTrainingEngine()


def test_profile_creation(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Training returns a TrainedModel."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert isinstance(
        profile,
        TrainedModel,
    )


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_model_name(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
    model_name: str,
) -> None:
    """Every supported model can be trained."""

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=configuration.cross_validation_folds,
        random_seed=configuration.random_seed,
        shuffle=configuration.shuffle,
    )

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert profile.model_name == model_name


def test_score_range(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Cross-validation score is finite."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert isinstance(
        profile.score,
        float,
    )


def test_training_time(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Training time is recorded."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert profile.training_time >= 0.0


def test_feature_count(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Feature count is preserved."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert profile.feature_count == dataset.feature_count


def test_sample_count(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Sample count is preserved."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert profile.sample_count == dataset.sample_count


def test_estimator_exists(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Estimator is created."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    assert profile.estimator is not None


def test_deterministic_training(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Training is deterministic."""

    first = engine.analyze(
        dataset,
        configuration,
    )

    second = engine.analyze(
        dataset,
        configuration,
    )

    assert first.model_name == second.model_name

    assert (
        pytest.approx(
            first.score,
        )
        == second.score
    )


def test_invalid_model(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
) -> None:
    """Unknown models raise ValueError."""

    configuration = TrainingConfiguration(
        model_name="invalid_model",
        cross_validation_folds=5,
        random_seed=42,
        shuffle=True,
    )

    with pytest.raises(
        ValueError,
    ):
        engine.analyze(
            dataset,
            configuration,
        )


def test_profile_is_immutable(
    engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    """Returned model is immutable."""

    profile = engine.analyze(
        dataset,
        configuration,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        profile.model_name = "changed"
