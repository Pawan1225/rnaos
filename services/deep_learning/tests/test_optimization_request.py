"""
Tests for optimization intelligence request.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.optimization_request import (
    OptimizationIntelligenceRequest,
)
from dl.optimization.request_validator import (
    OptimizationRequestValidator,
)


def test_valid_request() -> None:
    """
    Valid request passes.
    """

    request = OptimizationIntelligenceRequest(
        sequence_id="rna_001",
        sequence_length=120,
        complexity_score=0.5,
        predicted_energy=-12.5,
        folding_difficulty=0.7,
        solver_hint="adaptive",
    )

    validator = OptimizationRequestValidator()

    assert (
        validator.validate(
            request,
        )
        is True
    )


def test_invalid_sequence_length() -> None:
    """
    Invalid sequence length fails.
    """

    request = OptimizationIntelligenceRequest(
        sequence_id="rna_001",
        sequence_length=0,
        complexity_score=0.5,
        predicted_energy=-12.5,
        folding_difficulty=0.7,
        solver_hint="adaptive",
    )

    validator = OptimizationRequestValidator()

    with pytest.raises(
        ValueError,
    ):
        validator.validate(
            request,
        )
