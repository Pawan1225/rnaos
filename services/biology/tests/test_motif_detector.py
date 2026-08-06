"""
Tests for the RNAOS motif detector.
"""

from __future__ import annotations

import pytest
from biology.analyzers.motif_detector import (
    MotifDetector,
)
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)


@pytest.fixture
def sequence_analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


@pytest.fixture
def motif_detector() -> MotifDetector:
    """Create a motif detector."""
    return MotifDetector()


def test_detect_start_codon(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Detect AUG."""
    features = sequence_analyzer.analyze(
        "CCAUGGGAUG",
    )

    profile = motif_detector.analyze(features)

    aug = profile.canonical[0]

    assert aug.motif == "AUG"
    assert aug.count == 2
    assert aug.positions == (2, 7)


def test_detect_stop_codons(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Detect stop codons."""
    features = sequence_analyzer.analyze(
        "UAAUAGUGA",
    )

    profile = motif_detector.analyze(features)

    assert profile.canonical[1].count == 1
    assert profile.canonical[2].count == 1
    assert profile.canonical[3].count == 1


def test_absent_motifs(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Absent motifs return zero counts."""
    features = sequence_analyzer.analyze(
        "CCCCCCCC",
    )

    profile = motif_detector.analyze(features)

    for motif in profile.canonical:
        assert motif.count == 0


def test_overlapping_search(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Search utility supports overlapping matches."""
    features = sequence_analyzer.analyze(
        "AAAAAA",
    )

    profile = motif_detector.analyze(features)

    assert profile.repetitive == ()


def test_deterministic(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Detection is deterministic."""
    features = sequence_analyzer.analyze(
        "CCAUGGGAUG",
    )

    result1 = motif_detector.analyze(features)
    result2 = motif_detector.analyze(features)

    assert result1 == result2


def test_profile_structure(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Profile structure remains stable."""
    features = sequence_analyzer.analyze(
        "AUG",
    )

    profile = motif_detector.analyze(features)

    assert len(profile.canonical) == 4
    assert isinstance(profile.repetitive, tuple)
    assert isinstance(profile.structural, tuple)
    assert isinstance(profile.regulatory, tuple)
    assert isinstance(profile.custom, tuple)


def test_long_sequence(
    sequence_analyzer: SequenceAnalyzer,
    motif_detector: MotifDetector,
) -> None:
    """Long sequences analyze successfully."""
    features = sequence_analyzer.analyze(
        "AUG" * 5000,
    )

    profile = motif_detector.analyze(features)

    assert profile.canonical[0].count == 5000
