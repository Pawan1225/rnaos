"""
Tests for the RNAOS GC content analyzer.
"""

from __future__ import annotations

import pytest
from biology.analyzers.gc_content_analyzer import (
    GCContentAnalyzer,
)
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)


@pytest.fixture
def sequence_analyzer() -> SequenceAnalyzer:
    """Create a sequence analyzer."""
    return SequenceAnalyzer()


@pytest.fixture
def gc_analyzer() -> GCContentAnalyzer:
    """Create a GC content analyzer."""
    return GCContentAnalyzer()


def test_balanced_sequence(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Balanced GC/AU composition."""
    features = sequence_analyzer.analyze("AUGC")

    gc = gc_analyzer.analyze(features)

    assert gc.gc_content == pytest.approx(0.5)
    assert gc.au_content == pytest.approx(0.5)


def test_high_gc_sequence(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """High GC composition."""
    features = sequence_analyzer.analyze("GGGGCCCC")

    gc = gc_analyzer.analyze(features)

    assert gc.gc_content == pytest.approx(1.0)
    assert gc.au_content == pytest.approx(0.0)


def test_high_au_sequence(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """High AU composition."""
    features = sequence_analyzer.analyze("AAAAUUUU")

    gc = gc_analyzer.analyze(features)

    assert gc.gc_content == pytest.approx(0.0)
    assert gc.au_content == pytest.approx(1.0)


def test_gc_skew(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Verify GC skew."""
    features = sequence_analyzer.analyze("GGGC")

    gc = gc_analyzer.analyze(features)

    assert gc.gc_skew == pytest.approx(0.5)


def test_gc_au_ratio(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Verify GC/AU ratio."""
    features = sequence_analyzer.analyze("GGCCAU")

    gc = gc_analyzer.analyze(features)

    assert gc.gc_au_ratio == pytest.approx(2.0)


def test_purine_pyrimidine_ratio(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Verify purine/pyrimidine ratio."""
    features = sequence_analyzer.analyze("AAGCUU")

    gc = gc_analyzer.analyze(features)

    assert gc.purine_pyrimidine_ratio == pytest.approx(1.0)


def test_deterministic_analysis(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Analyzer should be deterministic."""
    features = sequence_analyzer.analyze("AUGCGGAU")

    result1 = gc_analyzer.analyze(features)
    result2 = gc_analyzer.analyze(features)

    assert result1 == result2


def test_long_sequence(
    sequence_analyzer: SequenceAnalyzer,
    gc_analyzer: GCContentAnalyzer,
) -> None:
    """Large sequence analysis."""
    features = sequence_analyzer.analyze(
        "AUGC" * 5000,
    )

    gc = gc_analyzer.analyze(features)

    assert gc.gc_content == pytest.approx(0.5)
    assert gc.au_content == pytest.approx(0.5)
