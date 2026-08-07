"""
Tests for pairing candidate generator.
"""

from validation.generation.pairing_candidate_generator import (
    PairingCandidateGenerator,
)


def test_pairing_candidate_generation():

    generator = PairingCandidateGenerator()

    candidates = generator.generate(
        "GGGAAACCC",
    )

    assert len(candidates) >= 1


def test_candidate_lengths():

    generator = PairingCandidateGenerator()

    sequence = "GGGAAACCC"

    candidates = generator.generate(
        sequence,
    )

    for candidate in candidates:
        assert len(candidate) == len(sequence)
