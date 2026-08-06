"""
Integration test for the RNAOS machine learning pipeline.
"""

from __future__ import annotations

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


def build_feature_vector(
    offset: float,
) -> FeatureVector:
    """
    Create deterministic feature vector.
    """

    return FeatureVector(
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
            0.1 + offset,
            0.2 + offset,
            0.3 + offset,
            0.4 + offset,
            0.5 + offset,
            0.6 + offset,
            0.7 + offset,
            0.8 + offset,
            0.9 + offset,
            1.0 + offset,
        ),
        dimension=10,
    )


def test_complete_ml_pipeline(
    configuration,
) -> None:
    """
    Validate complete ML lifecycle.
    """

    engine = MLIntelligenceEngine(
        dataset_builder=DatasetBuilder(),
        feature_selector=FeatureSelectionEngine(),
        trainer=ModelTrainingEngine(),
        predictor=PredictionEngine(),
        evaluator=ModelEvaluationEngine(),
        registry=ModelRegistry(),
    )

    feature_vectors = (
        build_feature_vector(0.0),
        build_feature_vector(0.1),
        build_feature_vector(0.2),
        build_feature_vector(0.3),
        build_feature_vector(0.4),
        build_feature_vector(0.5),
    )

    profile = engine.analyze(
        feature_vectors=feature_vectors,
        prediction_features=feature_vectors[0],
        targets=(
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
        ),
        configuration=configuration,
        experiment_id="pipeline_test",
    )

    assert isinstance(
        profile,
        MLIntelligenceProfile,
    )

    assert profile.experiment_id == "pipeline_test"

    assert profile.model_name == configuration.model_name

    assert profile.prediction_result is not None

    assert profile.evaluation_result is not None

    assert profile.registered_model_id
