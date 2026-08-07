"""
Tests for optimization variable models.
"""

from __future__ import annotations

from dl.models.optimization.optimization_variable import (
    BasePairVariable,
    OptimizationVariable,
)


def test_optimization_variable_creation() -> None:
    """
    Optimization variable is created.
    """

    variable = OptimizationVariable(
        variable_id="x_001",
        index=0,
    )

    assert variable.variable_id == "x_001"

    assert variable.index == 0

    assert variable.binary is True


def test_base_pair_variable_creation() -> None:
    """
    Base pair variable is created.
    """

    variable = BasePairVariable(
        variable_id="bp_0_3",
        nucleotide_i=0,
        nucleotide_j=3,
        pair_type="GC",
    )

    assert variable.variable_id == "bp_0_3"

    assert variable.pair_type == "GC"

    assert variable.selected is False
