"""
Tests for structure validator.
"""

from validation.structure.structure_validator import (
    StructureValidator,
)


def test_valid_structure():

    validator = StructureValidator()

    assert validator.validate("(((...)))")


def test_invalid_structure():

    validator = StructureValidator()

    assert not validator.validate("(((..)")
