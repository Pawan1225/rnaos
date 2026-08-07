"""
Tests for convergence detection engine.
"""

from __future__ import annotations

from dl.models.optimization.convergence_result import (
    ConvergenceResult,
)
from dl.solvers.convergence_engine import (
    ConvergenceDetectionEngine,
)


def test_convergence_detected() -> None:
    """
    Small improvement converges.
    """

    engine = ConvergenceDetectionEngine(
        tolerance=0.001,
    )

    result = engine.evaluate(
        previous_energy=-10.0,
        current_energy=-10.0005,
    )

    assert isinstance(
        result,
        ConvergenceResult,
    )

    assert result.converged is True


def test_continues_search() -> None:
    """
    Large improvement continues.
    """

    engine = ConvergenceDetectionEngine(
        tolerance=0.001,
    )

    result = engine.evaluate(
        previous_energy=-10.0,
        current_energy=-12.0,
    )

    assert result.converged is False
