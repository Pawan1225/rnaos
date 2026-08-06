"""
Integration tests for the RNAOS Prediction Engine.
"""

from __future__ import annotations

from math import isfinite

from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)
from ml.analyzers.dataset_builder import (
    DatasetBuilder,
)
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
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
from ml.models.prediction_result import (
    PredictionResult,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)


def test_complete_prediction_pipeline() -> None:
    """
    Complete Biology → AI → ML → Prediction pipeline.
    """

    biology = BiologicalIntelligenceEngine()

    feature_engine = FeatureEngineeringEngine()

    dataset_builder = DatasetBuilder()

    selector = FeatureSelectionEngine()

    training_engine = ModelTrainingEngine()

    prediction_engine = PredictionEngine()

    profile = biology.analyze(
        "AUGCGGAUACCGGAUUAGCUAGCUAGGCUA",
    )

    feature_vector = feature_engine.extract(
        profile,
    )

    dataset = dataset_builder.build(
        feature_vectors=[
            feature_vector,
            feature_vector,
            feature_vector,
            feature_vector,
            feature_vector,
        ],
        targets=[
            0.10,
            0.20,
            0.30,
            0.40,
            0.50,
        ],
    )

    selected = selector.analyze(
        feature_vector,
        top_k=10,
    )

    assert selected.feature_count == 10

    configuration = TrainingConfiguration(
        model_name="random_forest",
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    trained_model = training_engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )

    prediction = prediction_engine.analyze(
        trained_model=trained_model,
        features=feature_vector,
        experiment_id="exp_prediction_test",
    )

    assert isinstance(
        prediction,
        PredictionResult,
    )

    assert prediction.prediction_count == 6

    assert 0.0 <= prediction.confidence_score <= 1.0

    assert prediction.experiment_id == "exp_prediction_test"

    assert prediction.model_name == trained_model.model_name

    assert prediction.prediction_timestamp

    values = (
        prediction.folding_difficulty,
        prediction.expected_mfe,
        prediction.structural_stability,
        prediction.solver_suitability,
        prediction.runtime_estimation,
        prediction.optimization_complexity,
        prediction.confidence_score,
    )

    assert all(
        isfinite(
            value,
        )
        for value in values
    )
