"""
Tests for the RNAOS stem-loop detector.
"""

from __future__ import annotations

import pytest
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)
from biology.analyzers.stem_loop_detector import (
    StemLoopDetector,
)


@pytest.fixture
def sequence_analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


@pytest.fixture
def stem_loop_detector() -> StemLoopDetector:
    """Create a stem-loop detector."""
    return StemLoopDetector()


def test_empty_sequence(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """No candidates should be detected in a very short sequence."""
    features = sequence_analyzer.analyze(
        "AUG",
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    assert profile.estimated_stems == 0
    assert profile.estimated_loops == 0
    assert profile.candidates == ()


def test_single_hairpin_profile(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Profile should remain internally consistent."""
    features = sequence_analyzer.analyze(
        "GCUAAAGC",
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    assert len(profile.candidates) == profile.estimated_stems
    assert profile.estimated_loops == profile.estimated_stems


def test_multiple_candidates(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Detector should complete successfully on larger inputs."""
    features = sequence_analyzer.analyze(
        "GCUAAAGCGCUAAAGC",
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    assert profile.estimated_stems >= 0
    assert profile.estimated_loops >= 0


def test_candidate_integrity(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Every detected candidate should satisfy detector constraints."""
    features = sequence_analyzer.analyze(
        "GCUAAAGCGCUAAAGC",
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    for candidate in profile.candidates:
        assert candidate.stem_length >= stem_loop_detector.min_stem_length

        assert (
            stem_loop_detector.min_loop_length
            <= candidate.loop_length
            <= stem_loop_detector.max_loop_length
        )

        assert 0.0 <= candidate.score <= 1.0


def test_profile_statistics(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Profile statistics should always be non-negative."""
    features = sequence_analyzer.analyze(
        "GCUAAAGCGCUAAAGC",
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    assert profile.average_stem_length >= 0.0
    assert profile.average_loop_length >= 0.0


def test_deterministic_analysis(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Repeated analysis should produce identical results."""
    features = sequence_analyzer.analyze(
        "GCUAAAGCGCUAAAGC",
    )

    profile1 = stem_loop_detector.analyze(
        features,
    )
    profile2 = stem_loop_detector.analyze(
        features,
    )

    assert profile1 == profile2


def test_long_sequence(
    sequence_analyzer: SequenceAnalyzer,
    stem_loop_detector: StemLoopDetector,
) -> None:
    """Long sequences should analyze successfully."""
    sequence = "GCGAAAUGC" * 20

    features = sequence_analyzer.analyze(
        sequence,
    )

    profile = stem_loop_detector.analyze(
        features,
    )

    assert profile.estimated_stems >= 0
    assert profile.average_stem_length >= 0.0


def test_detector_configuration() -> None:
    """Detector should expose its configuration."""
    detector = StemLoopDetector()

    assert detector.min_stem_length == 3
    assert detector.min_loop_length == 3
    assert detector.max_loop_length == 8
