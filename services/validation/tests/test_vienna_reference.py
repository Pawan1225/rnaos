"""
Tests for ViennaRNA reference adapter.
"""

from validation.reference.vienna_reference import (
    ViennaReference,
)


def test_vienna_reference_fold():

    sequence = "GGAGCAAAACUUGUCGAUUGAGAACAAAAUACAGAAUUUGCUUG"

    reference = ViennaReference()

    structure, energy = reference.fold(sequence)

    assert isinstance(
        structure,
        str,
    )

    assert len(structure) == len(sequence)

    assert isinstance(
        energy,
        float,
    )
