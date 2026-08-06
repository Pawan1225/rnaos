"""
Tests for the RNAOS AutoML engine.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

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
from ml.models.automl_configuration import (
    AutoMLConfiguration,
)
from ml.models.automl_result import (
    AutoMLResult,
)
from ml.models.ml_dataset import (
    MLDataset,
)


@pytest.fixture
def engine() -> AutoMLEngine:
    """Create an AutoML engine."""

    return AutoMLEngine()


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
    )

    return MLDataset(
        feature_names=(
            "gc",
            "complexity",
            "entropy",
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
        dataset_version="v1",
    )


@pytest.fixture
def configuration() -> AutoMLConfiguration:
    """Create a deterministic AutoML configuration."""

    return AutoMLConfiguration(
        model_names=SUPPORTED_MODELS,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )


@pytest.fixture
def result(
    engine: AutoMLEngine,
    dataset: MLDataset,
    configuration: AutoMLConfiguration,
) -> AutoMLResult:
    """Run the AutoML engine."""

    return engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )


def test_profile_creation(
    result: AutoMLResult,
) -> None:
    """AutoML returns a result."""

    assert result is not None


def test_model_count(
    result: AutoMLResult,
) -> None:
    """All configured models are trained."""

    assert result.model_count == len(
        SUPPORTED_MODELS,
    )


def test_best_model_exists(
    result: AutoMLResult,
) -> None:
    """A best model is selected."""

    assert result.best_model is not None


def test_best_model_name(
    result: AutoMLResult,
) -> None:
    """Best model belongs to supported models."""

    assert result.best_model_name in SUPPORTED_MODELS


def test_ranking_size(
    result: AutoMLResult,
) -> None:
    """Ranking contains every model."""

    assert len(
        result.ranking,
    ) == len(
        SUPPORTED_MODELS,
    )


def test_training_configuration(
    result: AutoMLResult,
    configuration: AutoMLConfiguration,
) -> None:
    """Configuration is preserved."""

    assert result.training_configuration == configuration


def test_total_training_time(
    result: AutoMLResult,
) -> None:
    """Training time is recorded."""

    assert result.total_training_time >= 0.0


def test_experiment_id(
    result: AutoMLResult,
) -> None:
    """Experiment ID is generated."""

    assert result.experiment_id.startswith(
        "exp_",
    )


def test_deterministic_training(
    engine: AutoMLEngine,
    dataset: MLDataset,
    configuration: AutoMLConfiguration,
) -> None:
    """AutoML is deterministic."""

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
    """Result model is immutable."""

    with pytest.raises(
        FrozenInstanceError,
    ):
        result.best_model = None
