"""
Tests for the RNAOS ML Intelligence Engine.
"""

from __future__ import annotations

import pytest
from ai.models.feature_vector import (
    FeatureVector,
)
from ml.analyzers.dataset_builder import (
    DatasetBuilder,
)
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
)
from ml.analyzers.ml_intelligence_engine import (
    MLIntelligenceEngine,
)
from ml.analyzers.model_evaluation_engine import (
    ModelEvaluationEngine,
)
from ml.analyzers.model_registry import (
    ModelRegistry,
)
from ml.analyzers.model_training_engine import (
    ModelTrainingEngine,
)
from ml.analyzers.prediction_engine import (
    PredictionEngine,
)
from ml.models.ml_intelligence_profile import (
    MLIntelligenceProfile,
)


@pytest.fixture
def intelligence_engine() -> MLIntelligenceEngine:
    """
    Create ML intelligence engine.
    """

    return MLIntelligenceEngine(
        dataset_builder=DatasetBuilder(),
        feature_selector=FeatureSelectionEngine(),
        trainer=ModelTrainingEngine(),
        predictor=PredictionEngine(),
        evaluator=ModelEvaluationEngine(),
        registry=ModelRegistry(),
    )


@pytest.fixture
def feature_vectors() -> tuple[FeatureVector, ...]:
    """
    Create deterministic ML feature dataset.
    """

    return (
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.1,
                0.2,
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
            ),
            dimension=10,
        ),
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.2,
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
                1.1,
            ),
            dimension=10,
        ),
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
                1.1,
                1.2,
            ),
            dimension=10,
        ),
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
                1.1,
                1.2,
                1.3,
            ),
            dimension=10,
        ),
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
                1.1,
                1.2,
                1.3,
                1.4,
            ),
            dimension=10,
        ),
        FeatureVector(
            feature_names=(
                "feature_1",
                "feature_2",
                "feature_3",
                "feature_4",
                "feature_5",
                "feature_6",
                "feature_7",
                "feature_8",
                "feature_9",
                "feature_10",
            ),
            values=(
                0.6,
                0.7,
                0.8,
                0.9,
                1.0,
                1.1,
                1.2,
                1.3,
                1.4,
                1.5,
            ),
            dimension=10,
        ),
    )


@pytest.fixture
def prediction_features(
    feature_vectors: tuple[FeatureVector, ...],
) -> FeatureVector:
    """
    Select prediction input.
    """

    return feature_vectors[0]


def test_ml_intelligence_pipeline(
    intelligence_engine: MLIntelligenceEngine,
    feature_vectors: tuple[FeatureVector, ...],
    prediction_features: FeatureVector,
    configuration,
) -> None:
    """
    Complete ML intelligence workflow.
    """

    profile = intelligence_engine.analyze(
        feature_vectors=feature_vectors,
        prediction_features=prediction_features,
        targets=(
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
        ),
        configuration=configuration,
        experiment_id="exp_test",
    )

    assert isinstance(
        profile,
        MLIntelligenceProfile,
    )

    assert profile.experiment_id == "exp_test"

    assert profile.prediction_result is not None

    assert profile.evaluation_result is not None

    assert profile.registered_model_id


def test_registry_reference(
    intelligence_engine: MLIntelligenceEngine,
    feature_vectors: tuple[FeatureVector, ...],
    prediction_features: FeatureVector,
    configuration,
) -> None:
    """
    Verify registered model reference exists.
    """

    profile = intelligence_engine.analyze(
        feature_vectors=feature_vectors,
        prediction_features=prediction_features,
        targets=(
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
        ),
        configuration=configuration,
        experiment_id="exp_registry",
    )

    assert profile.registered_model_id == "random_forest_exp_registry"
