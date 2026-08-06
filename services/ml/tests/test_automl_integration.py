"""
Integration tests for the RNAOS AutoML engine.
"""

from __future__ import annotations

from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)
from ml.analyzers.automl_engine import (
    AutoMLEngine,
)
from ml.analyzers.dataset_builder import (
    DatasetBuilder,
)
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
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


def test_complete_ml_pipeline() -> None:
    """
    Complete Biology → AI → ML pipeline.
    """

    biology = BiologicalIntelligenceEngine()

    feature_engine = FeatureEngineeringEngine()

    dataset_builder = DatasetBuilder()

    selector = FeatureSelectionEngine()

    automl = AutoMLEngine()

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

    configuration = AutoMLConfiguration(
        model_names=SUPPORTED_MODELS,
        cross_validation_folds=DEFAULT_CROSS_VALIDATION_FOLDS,
        random_seed=DEFAULT_RANDOM_SEED,
        shuffle=DEFAULT_SHUFFLE,
    )

    result = automl.analyze(
        dataset=dataset,
        configuration=configuration,
    )

    assert result.model_count == len(
        SUPPORTED_MODELS,
    )

    assert result.best_model is not None

    assert result.best_model_name in SUPPORTED_MODELS

    assert result.training_configuration == configuration

    assert result.experiment_id.startswith(
        "exp_",
    )
