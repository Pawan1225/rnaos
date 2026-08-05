"""
Tests for the RNA sequence analyzer.
"""

from __future__ import annotations

import pytest
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)
from biology.utils.sequence_validation import (
    InvalidRNASequenceError,
)


@pytest.fixture
def analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


def test_analyze_valid_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Analyze a valid RNA sequence."""
    features = analyzer.analyze("AUGCGGAU")

    assert features.sequence == "AUGCGGAU"
    assert features.length == 8
    assert features.is_valid is True


def test_nucleotide_counts(
    analyzer: SequenceAnalyzer,
) -> None:
    """Verify nucleotide counts."""
    features = analyzer.analyze("AUGCGGAU")

    counts = features.nucleotide_counts

    assert counts.adenine == 2
    assert counts.uracil == 2
    assert counts.guanine == 3
    assert counts.cytosine == 1


def test_purine_count(
    analyzer: SequenceAnalyzer,
) -> None:
    """Verify purine count."""
    features = analyzer.analyze("AUGCGGAU")

    assert features.purine_count == 5


def test_pyrimidine_count(
    analyzer: SequenceAnalyzer,
) -> None:
    """Verify pyrimidine count."""
    features = analyzer.analyze("AUGCGGAU")

    assert features.pyrimidine_count == 3


def test_lowercase_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Lowercase RNA should normalize."""
    features = analyzer.analyze("augcggau")

    assert features.sequence == "AUGCGGAU"


def test_mixed_case_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Mixed-case RNA should normalize."""
    features = analyzer.analyze("AuGcGgAu")

    assert features.sequence == "AUGCGGAU"


def test_empty_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Empty sequences are invalid."""
    with pytest.raises(
        InvalidRNASequenceError,
    ):
        analyzer.analyze("")


def test_invalid_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Invalid nucleotides raise an exception."""
    with pytest.raises(
        InvalidRNASequenceError,
    ):
        analyzer.analyze("AUTGCX")


def test_single_nucleotide(
    analyzer: SequenceAnalyzer,
) -> None:
    """Analyze a single nucleotide."""
    features = analyzer.analyze("A")

    assert features.length == 1

    assert features.nucleotide_counts.adenine == 1


def test_long_sequence(
    analyzer: SequenceAnalyzer,
) -> None:
    """Analyze a long RNA sequence."""
    sequence = "AUGC" * 1000

    features = analyzer.analyze(sequence)

    assert features.length == 4000

    assert features.nucleotide_counts.total == 4000
