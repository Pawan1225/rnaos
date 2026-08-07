"""
Tests for RNAOS solver.
"""

from validation.solvers.rnaos_solver import (
    RNAOSSolver,
)


class MockEnergyEvaluator:
    """
    Mock RNA energy evaluator.
    """

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:
        """
        Return mock energy value.
        """

        return -1.0


def test_rnaos_solver_generation():
    """
    RNAOS solver generates structure.
    """

    solver = RNAOSSolver(
        evaluator=MockEnergyEvaluator(),
    )

    structure = solver.solve(
        "GGGAAACCC",
    )

    assert isinstance(
        structure,
        str,
    )

    assert len(structure) == 9
