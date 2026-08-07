"""
Tests for RNAOS pairing optimizer.
"""

from validation.solvers.pairing_optimizer import (
    PairingOptimizer,
)


def test_pairing_optimizer():

    optimizer = PairingOptimizer()

    structure = optimizer.optimize("GGGAAACCC")

    assert isinstance(
        structure,
        str,
    )

    assert len(structure) == 9
