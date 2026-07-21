from ai_intelligence.complexity.complexity_estimator import (
    ComplexityEstimator,
)
from ai_intelligence.embeddings.embedding_engine import (
    RNAEmbeddingEngine,
)
from ai_intelligence.features.feature_engine import (
    FeatureEngineeringEngine,
)
from ai_intelligence.predictors.solver_predictor import (
    SolverSuitabilityPredictor,
)


def test_solver_prediction(rna_profile):
    feature_engine = FeatureEngineeringEngine()
    embedding_engine = RNAEmbeddingEngine()
    complexity_engine = ComplexityEstimator()

    features = feature_engine.transform(rna_profile)
    embedding = embedding_engine.embed(rna_profile)
    complexity = complexity_engine.estimate(rna_profile)

    predictor = SolverSuitabilityPredictor()

    recommendation = predictor.predict(
        features,
        embedding,
        complexity,
    )

    assert recommendation.solver in {
        "classical",
        "hybrid",
        "quantum",
    }

    assert 0.0 <= recommendation.confidence <= 1.0


def test_prediction_reasoning(rna_profile):
    feature_engine = FeatureEngineeringEngine()
    embedding_engine = RNAEmbeddingEngine()
    complexity_engine = ComplexityEstimator()

    recommendation = SolverSuitabilityPredictor().predict(
        feature_engine.transform(rna_profile),
        embedding_engine.embed(rna_profile),
        complexity_engine.estimate(rna_profile),
    )

    assert recommendation.reasoning != ""


def test_prediction_confidence(rna_profile):
    feature_engine = FeatureEngineeringEngine()
    embedding_engine = RNAEmbeddingEngine()
    complexity_engine = ComplexityEstimator()

    recommendation = SolverSuitabilityPredictor().predict(
        feature_engine.transform(rna_profile),
        embedding_engine.embed(rna_profile),
        complexity_engine.estimate(rna_profile),
    )

    assert 0.0 <= recommendation.confidence <= 1.0
