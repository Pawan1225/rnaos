"""
Tests for RNA candidate generator.
"""

from validation.generation.candidate_generator import (
    CandidateGenerator,
)


def test_candidate_generation():

    generator = CandidateGenerator()

    candidates = generator.generate(
        "GGGAAACCC",
    )

    assert len(candidates) >= 2


def test_candidate_structure_length():

    generator = CandidateGenerator()

    sequence = "GGGAAACCC"

    candidates = generator.generate(
        sequence,
    )

    for structure in candidates:
        assert len(structure) == len(sequence)
