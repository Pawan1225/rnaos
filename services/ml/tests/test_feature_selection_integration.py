"""
Integration tests for RNAOS feature selection.
"""

from __future__ import annotations

from ai.analyzers.feature_engineering_engine import (
    FeatureEngineeringEngine,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
)


def test_biology_ai_ml_pipeline() -> None:
    """
    Biology -> AI -> ML integration.
    """

    biology = BiologicalIntelligenceEngine()

    ai = FeatureEngineeringEngine()

    ml = FeatureSelectionEngine()

    profile = biology.analyze(
        "AUGCGGAUACCGGAUUAGCUAGCUAGGCUA",
    )

    feature_vector = ai.extract(
        profile,
    )

    selected = ml.analyze(
        feature_vector,
        top_k=10,
    )

    assert selected.feature_count == 10

    assert not selected.is_empty

    assert (
        len(
            selected.selected_names,
        )
        == 10
    )

    assert (
        len(
            selected.feature_scores,
        )
        == 10
    )
