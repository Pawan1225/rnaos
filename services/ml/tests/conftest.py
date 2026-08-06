"""
Shared pytest fixtures for the RNAOS machine learning test suite.
"""

from __future__ import annotations

import pytest
from ml.analyzers.model_evaluation_engine import (
    ModelEvaluationEngine,
)
from ml.analyzers.model_training_engine import (
    ModelTrainingEngine,
)
from ml.constants import (
    DEFAULT_CROSS_VALIDATION_FOLDS,
    DEFAULT_RANDOM_SEED,
    DEFAULT_SHUFFLE,
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


@pytest.fixture
def dataset() -> MLDataset:
    """
    Create a deterministic dataset.
    """

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
    """
    Create deterministic training configuration.
    """

    return TrainingConfiguration(
        model_name="random_forest",
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )


@pytest.fixture
def training_engine() -> ModelTrainingEngine:
    """
    Create model training engine.
    """

    return ModelTrainingEngine()


@pytest.fixture
def trained_model(
    training_engine: ModelTrainingEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> TrainedModel:
    """
    Create trained model.
    """

    return training_engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )


@pytest.fixture
def evaluation_engine() -> ModelEvaluationEngine:
    """
    Create model evaluation engine.
    """

    return ModelEvaluationEngine()


@pytest.fixture
def experiment_id() -> str:
    """
    Create deterministic experiment identifier.
    """

    return "exp_test"
