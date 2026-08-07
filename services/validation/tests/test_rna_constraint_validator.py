"""
Tests RNA biological constraints.
"""

from validation.structure.rna_constraint_validator import (
    RNAConstraintValidator,
)


def test_valid_rna_structure():

    validator = RNAConstraintValidator()

    assert validator.validate(
        "GGGAAACCC",
        "(((...)))",
    )


def test_invalid_hairpin():

    validator = RNAConstraintValidator()

    assert not validator.validate(
        "GGGAAACCC",
        "((()))",
    )
