"""
Tests for the RNAOS biological intelligence engine.
"""

from __future__ import annotations

import pytest
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)


@pytest.fixture
def engine() -> BiologicalIntelligenceEngine:
    """Create a biological intelligence engine."""
    return BiologicalIntelligenceEngine()


def test_engine_creation() -> None:
    """Engine should be created successfully."""
    engine = BiologicalIntelligenceEngine()

    assert engine.sequence_analyzer is not None
    assert engine.gc_analyzer is not None
    assert engine.complexity_analyzer is not None
    assert engine.motif_detector is not None
    assert engine.stem_loop_detector is not None
    assert engine.thermodynamic_extractor is not None


def test_complete_analysis(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """The engine should produce a complete profile."""
    profile = engine.analyze(
        "GCGAAACGC",
    )

    assert profile is not None


def test_sequence_preserved(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Original sequence should be preserved."""
    sequence = "AUGCGCAU"

    profile = engine.analyze(
        sequence,
    )

    assert profile.sequence.sequence == sequence


def test_gc_profile_present(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """GC content profile should be available."""
    profile = engine.analyze(
        "GGGGCCCC",
    )

    assert profile.gc_content is not None


def test_complexity_profile_present(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Complexity profile should be available."""
    profile = engine.analyze(
        "AUGCGCAU",
    )

    assert profile.complexity is not None


def test_motif_profile_present(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Motif profile should be available."""
    profile = engine.analyze(
        "AUGAAAUAG",
    )

    assert profile.motifs is not None


def test_stem_loop_profile_present(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Stem-loop profile should be available."""
    profile = engine.analyze(
        "GCGAAACGC",
    )

    assert profile.stem_loops is not None


def test_thermodynamic_profile_present(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Thermodynamic profile should be available."""
    profile = engine.analyze(
        "GCGAAACGC",
    )

    assert profile.thermodynamics is not None


def test_deterministic_analysis(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Repeated analyses should produce identical results."""
    sequence = "GCGAAACGC"

    profile1 = engine.analyze(
        sequence,
    )

    profile2 = engine.analyze(
        sequence,
    )

    assert profile1 == profile2


def test_long_sequence(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """Long RNA sequences should be analyzed successfully."""
    sequence = "GCGAAACGC" * 20

    profile = engine.analyze(
        sequence,
    )

    assert profile.sequence.length == len(sequence)


def test_profile_consistency(
    engine: BiologicalIntelligenceEngine,
) -> None:
    """All biological sub-profiles should be populated."""
    profile = engine.analyze(
        "GCGAAACGC",
    )

    assert profile.sequence is not None
    assert profile.gc_content is not None
    assert profile.complexity is not None
    assert profile.motifs is not None
    assert profile.stem_loops is not None
    assert profile.thermodynamics is not None
