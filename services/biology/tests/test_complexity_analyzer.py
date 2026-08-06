"""
Tests for the RNAOS complexity analyzer.
"""

from __future__ import annotations

import pytest
from biology.analyzers.complexity_analyzer import (
    ComplexityAnalyzer,
)
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)


@pytest.fixture
def sequence_analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


@pytest.fixture
def complexity_analyzer() -> ComplexityAnalyzer:
    """Create a complexity analyzer."""
    return ComplexityAnalyzer()


def test_entropy_of_uniform_sequence(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Uniform sequence should have zero entropy."""
    features = sequence_analyzer.analyze("AAAAAAAA")

    profile = complexity_analyzer.analyze(features)

    assert profile.entropy == pytest.approx(0.0)


def test_entropy_of_balanced_sequence(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Balanced sequence should have high entropy."""
    features = sequence_analyzer.analyze("AUGC")

    profile = complexity_analyzer.analyze(features)

    assert profile.entropy == pytest.approx(2.0)


def test_sequence_diversity(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Sequence diversity is correctly computed."""
    features = sequence_analyzer.analyze("AUGC")

    profile = complexity_analyzer.analyze(features)

    assert profile.sequence_diversity == pytest.approx(1.0)


def test_repetition_score(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Highly repetitive sequences have high repetition."""
    features = sequence_analyzer.analyze("AAAAAAAA")

    profile = complexity_analyzer.analyze(features)

    assert profile.repetition_score == pytest.approx(0.75)


def test_complexity_score_range(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Complexity score remains normalized."""
    features = sequence_analyzer.analyze("AUGCGGAU")

    profile = complexity_analyzer.analyze(features)

    assert 0.0 <= profile.complexity_score <= 1.0


def test_compression_ratio_positive(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Compression ratio should be positive."""
    features = sequence_analyzer.analyze("AUGCGGAU")

    profile = complexity_analyzer.analyze(features)

    assert profile.compression_ratio > 0.0


def test_deterministic_analysis(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Analyzer should be deterministic."""
    features = sequence_analyzer.analyze("AUGCGGAU")

    profile1 = complexity_analyzer.analyze(features)
    profile2 = complexity_analyzer.analyze(features)

    assert profile1 == profile2


def test_long_sequence(
    sequence_analyzer: SequenceAnalyzer,
    complexity_analyzer: ComplexityAnalyzer,
) -> None:
    """Long sequences should be analyzed successfully."""
    features = sequence_analyzer.analyze("AUGC" * 5000)

    profile = complexity_analyzer.analyze(features)

    assert profile.entropy > 0.0
    assert profile.complexity_score >= 0.0
