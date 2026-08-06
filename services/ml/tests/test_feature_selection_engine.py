"""
Tests for the RNAOS feature selection engine.
"""

from __future__ import annotations

import pytest
from ai.models.feature_vector import FeatureVector
from ml.analyzers.feature_selection_engine import (
    FeatureSelectionEngine,
)
from ml.models.selected_feature_set import (
    SelectedFeatureSet,
)


@pytest.fixture
def engine() -> FeatureSelectionEngine:
    return FeatureSelectionEngine()


@pytest.fixture
def feature_vector() -> FeatureVector:
    names = (
        "gc_content",
        "complexity",
        "embedding",
        "stability",
        "entropy",
    )

    values = (
        0.90,
        0.20,
        0.75,
        0.60,
        0.10,
    )

    return FeatureVector(
        feature_names=names,
        values=values,
        dimension=len(names),
    )


@pytest.fixture
def profile(
    engine: FeatureSelectionEngine,
    feature_vector: FeatureVector,
) -> SelectedFeatureSet:
    return engine.analyze(
        feature_vector,
        top_k=3,
    )


def test_profile_creation(
    profile: SelectedFeatureSet,
) -> None:
    assert profile is not None


def test_feature_count(
    profile: SelectedFeatureSet,
) -> None:
    assert profile.feature_count == 3


def test_selection_method(
    profile: SelectedFeatureSet,
) -> None:
    assert profile.selection_method == "variance_baseline"


def test_indices_count(
    profile: SelectedFeatureSet,
) -> None:
    assert len(profile.selected_indices) == 3


def test_names_count(
    profile: SelectedFeatureSet,
) -> None:
    assert len(profile.selected_names) == 3


def test_scores_count(
    profile: SelectedFeatureSet,
) -> None:
    assert len(profile.feature_scores) == 3


def test_not_empty(
    profile: SelectedFeatureSet,
) -> None:
    assert not profile.is_empty


def test_deterministic_selection(
    engine: FeatureSelectionEngine,
    feature_vector: FeatureVector,
) -> None:
    first = engine.analyze(
        feature_vector,
        top_k=3,
    )

    second = engine.analyze(
        feature_vector,
        top_k=3,
    )

    assert first == second


def test_invalid_top_k(
    engine: FeatureSelectionEngine,
    feature_vector: FeatureVector,
) -> None:
    with pytest.raises(
        ValueError,
    ):
        engine.analyze(
            feature_vector,
            top_k=100,
        )


def test_profile_is_immutable(
    profile: SelectedFeatureSet,
) -> None:
    with pytest.raises(
        AttributeError,
    ):
        profile.selection_method = "other"
