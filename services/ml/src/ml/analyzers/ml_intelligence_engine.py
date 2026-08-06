"""
RNAOS machine learning intelligence engine.
"""

from __future__ import annotations

from datetime import (
    UTC,
    datetime,
)

from ai.models.feature_vector import (
    FeatureVector,
)
from ml.analyzers.dataset_builder import (
    DatasetBuilder,
)
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
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
from ml.models.model_metadata import (
    ModelMetadata,
)
from ml.models.registered_model import (
    RegisteredModel,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)


class MLIntelligenceEngine:
    """
    Orchestrates the complete machine learning pipeline.

    Responsible only for coordinating existing ML engines.
    """

    def __init__(
        self,
        dataset_builder: DatasetBuilder,
        feature_selector: FeatureSelectionEngine,
        trainer: ModelTrainingEngine,
        predictor: PredictionEngine,
        evaluator: ModelEvaluationEngine,
        registry: ModelRegistry,
    ) -> None:
        """
        Initialize ML pipeline dependencies.
        """

        self.dataset_builder = dataset_builder
        self.feature_selector = feature_selector
        self.trainer = trainer
        self.predictor = predictor
        self.evaluator = evaluator
        self.registry = registry

    def analyze(
        self,
        feature_vectors: tuple[FeatureVector, ...],
        prediction_features: FeatureVector,
        targets: tuple[float, ...],
        configuration: TrainingConfiguration,
        experiment_id: str,
    ) -> MLIntelligenceProfile:
        """
        Execute complete ML intelligence pipeline.
        """

        dataset = self.dataset_builder.build(
            feature_vectors=feature_vectors,
            targets=targets,
        )

        self.feature_selector.analyze(
            feature_vector=feature_vectors[0],
        )

        trained_model = self.trainer.analyze(
            dataset=dataset,
            configuration=configuration,
        )

        prediction_result = self.predictor.analyze(
            trained_model=trained_model,
            features=prediction_features,
            experiment_id=experiment_id,
        )

        evaluation_result = self.evaluator.evaluate(
            trained_model=trained_model,
            dataset=dataset,
        )

        metadata = ModelMetadata(
            model_id=f"{trained_model.model_name}_{experiment_id}",
            model_name=trained_model.model_name,
            version="v1",
            training_time=trained_model.training_time,
            feature_count=trained_model.feature_count,
            sample_count=trained_model.sample_count,
            created_at=datetime.now(
                UTC,
            ).isoformat(),
        )

        registered_model = RegisteredModel(
            metadata=metadata,
            trained_model=trained_model,
            evaluation=evaluation_result,
        )

        self.registry.register(
            registered_model,
        )

        return MLIntelligenceProfile(
            experiment_id=experiment_id,
            dataset_version=dataset.dataset_version,
            selected_features=dataset.feature_names,
            model_name=trained_model.model_name,
            prediction_result=prediction_result,
            evaluation_result=evaluation_result,
            registered_model_id=metadata.model_id,
        )
