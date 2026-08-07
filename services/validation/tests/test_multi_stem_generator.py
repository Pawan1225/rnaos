"""
Tests for multi stem generator.
"""

from validation.generation.multi_stem_generator import (
    MultiStemGenerator,
)


def test_multi_stem_generation():

    generator = MultiStemGenerator()

    candidates = generator.generate(
        "GGGAAACCC",
    )

    assert len(candidates) >= 1


def test_structure_length():

    generator = MultiStemGenerator()

    sequence = "GGGAAACCC"

    candidates = generator.generate(
        sequence,
    )

    for candidate in candidates:
        assert len(candidate) == len(sequence)
