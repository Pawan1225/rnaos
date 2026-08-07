"""
Tests for solver execution request model.
"""

from __future__ import annotations

from dl.models.optimization.solver_execution_request import (
    SolverExecutionRequest,
)


def test_solver_execution_request_creation() -> None:
    """
    Solver execution request can be created.
    """

    request = SolverExecutionRequest(
        request_id=1,
        problem_type="rna_folding",
        strategy_name="quantum_evolutionary",
        priority=1,
    )

    assert request.request_id == 1

    assert request.problem_type == ("rna_folding")

    assert request.strategy_name == ("quantum_evolutionary")

    assert request.priority == 1
