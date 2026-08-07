"""
Tests for RNA candidate mutator.
"""

from validation.generation.candidate_mutator import (
    CandidateMutator,
)


def test_candidate_mutation_generation():

    mutator = CandidateMutator()

    candidates = mutator.mutate(
        "(((...)))",
    )

    assert len(candidates) >= 2


def test_mutated_structure_length():

    mutator = CandidateMutator()

    candidates = mutator.mutate(
        "(((...)))",
    )

    for candidate in candidates:
        assert len(candidate) == 9
