from __future__ import annotations

from dataclasses import FrozenInstanceError
from math import isfinite

import pytest
from ai.models.feature_vector import (
    FeatureVector,
)
from ml.analyzers.model_training_engine import (
    ModelTrainingEngine,
)
from ml.analyzers.prediction_engine import (
    PredictionEngine,
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
from ml.models.prediction_result import (
    PredictionResult,
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
def engine() -> PredictionEngine:
    """Create prediction engine."""

    return PredictionEngine()


@pytest.fixture
def feature_vector() -> FeatureVector:
    """Create deterministic prediction features."""

    return FeatureVector(
        feature_names=(
            "feature_1",
            "feature_2",
            "feature_3",
        ),
        values=(
            0.25,
            0.35,
            0.45,
        ),
        dimension=3,
    )


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_profile_creation(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Prediction returns a PredictionResult."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert isinstance(
        profile,
        PredictionResult,
    )


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_model_name(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Prediction preserves model name."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert profile.model_name == model_name


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_confidence_range(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Confidence is normalized."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert 0.0 <= profile.confidence_score <= 1.0


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_prediction_timestamp_exists(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Timestamp exists."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert profile.prediction_timestamp


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_experiment_id(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Experiment ID is preserved."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert profile.experiment_id == "exp_test"


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_prediction_count(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Prediction interface is stable."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert profile.prediction_count == 6


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_prediction_values_are_finite(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Prediction values are finite."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    values = (
        profile.folding_difficulty,
        profile.expected_mfe,
        profile.structural_stability,
        profile.solver_suitability,
        profile.runtime_estimation,
        profile.optimization_complexity,
        profile.confidence_score,
    )

    assert all(
        isfinite(
            value,
        )
        for value in values
    )


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_deterministic_prediction(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Predictions are deterministic."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    first = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    second = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    assert first.folding_difficulty == second.folding_difficulty

    assert first.expected_mfe == second.expected_mfe

    assert first.structural_stability == second.structural_stability

    assert first.solver_suitability == second.solver_suitability

    assert first.runtime_estimation == second.runtime_estimation

    assert first.optimization_complexity == second.optimization_complexity

    assert first.confidence_score == second.confidence_score


def test_invalid_feature_vector(
    engine: PredictionEngine,
    dataset: MLDataset,
) -> None:
    """Empty feature vectors are rejected."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name="random_forest",
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    invalid_vector = FeatureVector(
        feature_names=(),
        values=(),
        dimension=0,
    )

    with pytest.raises(
        ValueError,
    ):
        engine.analyze(
            trained_model=trained_model,
            features=invalid_vector,
            experiment_id="exp_test",
        )


@pytest.mark.parametrize(
    "model_name",
    SUPPORTED_MODELS,
)
def test_profile_is_immutable(
    engine: PredictionEngine,
    dataset: MLDataset,
    feature_vector: FeatureVector,
    model_name: str,
) -> None:
    """Prediction result is immutable."""

    training_engine = ModelTrainingEngine()

    configuration = TrainingConfiguration(
        model_name=model_name,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset,
        configuration,
    )

    profile = engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_test",
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        profile.model_name = "changed"
