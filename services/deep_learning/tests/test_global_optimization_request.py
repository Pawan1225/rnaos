"""
Tests for global optimization request model.
"""

from __future__ import annotations

from dl.models.optimization.global_optimization_request import (
    GlobalOptimizationRequest,
)


def test_global_optimization_request() -> None:
    """
    Global optimization request can be created.
    """

    request = GlobalOptimizationRequest(
        request_id=1,
        problem_type="rna_folding",
        complexity=0.95,
        priority=1,
        accuracy_target=0.98,
    )

    assert request.request_id == 1

    assert request.problem_type == "rna_folding"

    assert request.complexity == 0.95

    assert request.priority == 1

    assert request.accuracy_target == 0.98
