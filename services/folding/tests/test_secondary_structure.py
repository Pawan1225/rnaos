from folding.models.secondary_structure import (
    BasePair,
    RNASecondaryStructure,
)


def test_secondary_structure():
    structure = RNASecondaryStructure(
        sequence="GGGAAAUCC",
        dot_bracket="(((...)))",
        mfe=-2.3,
        base_pairs=[
            BasePair(0, 8),
            BasePair(1, 7),
            BasePair(2, 6),
        ],
    )

    assert structure.length == 9

    assert structure.pair_count == 3

    assert structure.mfe == -2.3
