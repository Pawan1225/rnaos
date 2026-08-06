"""
Tests for the RNAOS thermodynamic feature extractor.
"""

from __future__ import annotations

import pytest
from biology.analyzers.gc_content_analyzer import (
    GCContentAnalyzer,
)
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)
from biology.analyzers.stem_loop_detector import (
    StemLoopDetector,
)
from biology.analyzers.thermodynamic_feature_extractor import (
    ThermodynamicFeatureExtractor,
)


@pytest.fixture
def sequence_analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


@pytest.fixture
def gc_analyzer() -> GCContentAnalyzer:
    """Create a GC content analyzer."""
    return GCContentAnalyzer()


@pytest.fixture
def stem_detector() -> StemLoopDetector:
    """Create a stem-loop detector."""
    return StemLoopDetector()


@pytest.fixture
def thermodynamic_extractor() -> ThermodynamicFeatureExtractor:
    """Create a thermodynamic feature extractor."""
    return ThermodynamicFeatureExtractor()


def test_profile_creation(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Thermodynamic profile should be created successfully."""
    features = sequence_analyzer.analyze("GCGAAACGC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert profile is not None


def test_gc_stability_range(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """GC stability should be normalized."""
    features = sequence_analyzer.analyze("GGGGCCCC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert 0.0 <= profile.gc_stability <= 1.0


def test_au_stability_range(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """AU stability should be normalized."""
    features = sequence_analyzer.analyze("AAAAUUUU")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert 0.0 <= profile.au_stability <= 1.0


def test_pair_density_range(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Pair density should be normalized."""
    features = sequence_analyzer.analyze("GCGAAACGC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert 0.0 <= profile.pair_density <= 1.0


def test_stability_index_range(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Overall stability index should be normalized."""
    features = sequence_analyzer.analyze("GCGAAACGC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert 0.0 <= profile.stability_index <= 1.0


def test_free_energy_is_negative(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Approximate free energy should be non-positive."""
    features = sequence_analyzer.analyze("GCGAAACGC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert profile.approximate_free_energy <= 0.0


def test_deterministic_analysis(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Repeated analyses should produce identical results."""
    features = sequence_analyzer.analyze("GCGAAACGC")

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile1 = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    profile2 = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert profile1 == profile2


def test_long_sequence(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
    stem_detector: StemLoopDetector,
    thermodynamic_extractor: ThermodynamicFeatureExtractor,
) -> None:
    """Long RNA sequences should be analyzed successfully."""
    sequence = "GCGAAACGC" * 20

    features = sequence_analyzer.analyze(sequence)

    gc_features = gc_analyzer.analyze(features)

    stem_profile = stem_detector.analyze(features)

    profile = thermodynamic_extractor.analyze(
        features,
        gc_features,
        stem_profile,
    )

    assert profile.stability_index >= 0.0
