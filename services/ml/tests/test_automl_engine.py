"""
Tests for the RNAOS AutoML engine.
"""

from __future__ import annotations

import pytest
from ml.analyzers.automl_engine import (
    AutoMLEngine,
)
from ml.constants import (
    DEFAULT_CROSS_VALIDATION_FOLDS,
    DEFAULT_RANDOM_SEED,
    DEFAULT_SHUFFLE,
    SUPPORTED_MODELS,
)
from ml.models.automl_result import (
    AutoMLResult,
)
from ml.models.ml_dataset import (
    MLDataset,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)


@pytest.fixture
def engine() -> AutoMLEngine:
    return AutoMLEngine()


@pytest.fixture
def dataset() -> MLDataset:
    features = [
        [0.1, 0.2, 0.3],
        [0.2, 0.3, 0.4],
        [0.3, 0.4, 0.5],
        [0.4, 0.5, 0.6],
        [0.5, 0.6, 0.7],
        [0.6, 0.7, 0.8],
        [0.7, 0.8, 0.9],
        [0.8, 0.9, 1.0],
        [0.9, 1.0, 1.1],
        [1.0, 1.1, 1.2],
    ]

    targets = [
        0.10,
        0.20,
        0.30,
        0.40,
        0.50,
        0.60,
        0.70,
        0.80,
        0.90,
        1.00,
    ]

    return MLDataset(
        features=features,
        targets=targets,
        feature_names=(
            "gc",
            "complexity",
            "entropy",
        ),
        dataset_version="v1",
        train_indices=(0, 1, 2, 3, 4, 5),
        validation_indices=(6, 7),
        test_indices=(8, 9),
    )


@pytest.fixture
def configuration() -> TrainingConfiguration:
    return TrainingConfiguration(
        model_names=SUPPORTED_MODELS,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )


@pytest.fixture
def result(
    engine: AutoMLEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> AutoMLResult:
    return engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )


def test_profile_creation(
    result: AutoMLResult,
) -> None:
    assert result is not None


def test_model_count(
    result: AutoMLResult,
) -> None:
    assert result.model_count == len(
        SUPPORTED_MODELS,
    )


def test_best_model_exists(
    result: AutoMLResult,
) -> None:
    assert result.best_model is not None


def test_best_model_name(
    result: AutoMLResult,
) -> None:
    assert result.best_model_name in SUPPORTED_MODELS


def test_ranking_size(
    result: AutoMLResult,
) -> None:
    assert len(
        result.ranking,
    ) == len(
        SUPPORTED_MODELS,
    )


def test_training_configuration(
    result: AutoMLResult,
    configuration: TrainingConfiguration,
) -> None:
    assert result.training_configuration == configuration


def test_total_training_time(
    result: AutoMLResult,
) -> None:
    assert result.total_training_time >= 0.0


def test_experiment_id(
    result: AutoMLResult,
) -> None:
    assert result.experiment_id.startswith(
        "exp_",
    )


def test_deterministic_training(
    engine: AutoMLEngine,
    dataset: MLDataset,
    configuration: TrainingConfiguration,
) -> None:
    first = engine.analyze(
        dataset,
        configuration,
    )

    second = engine.analyze(
        dataset,
        configuration,
    )

    assert first.best_model_name == second.best_model_name

    assert first.ranking == second.ranking

    assert first.experiment_id == second.experiment_id


def test_profile_is_immutable(
    result: AutoMLResult,
) -> None:
    with pytest.raises(
        AttributeError,
    ):
        result.best_model = None
