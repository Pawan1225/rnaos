"""
Tests for combined candidate generator.
"""

from validation.generation.combined_candidate_generator import (
    CombinedCandidateGenerator,
)


def test_combined_candidates():

    generator = CombinedCandidateGenerator()

    candidates = generator.generate(
        "GGGAAACCC",
    )

    assert len(candidates) >= 2


def test_combined_length():

    generator = CombinedCandidateGenerator()

    sequence = "GGGAAACCC"

    candidates = generator.generate(
        sequence,
    )

    for candidate in candidates:
        assert len(candidate) == len(sequence)
