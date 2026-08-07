"""
Tests for quantum-inspired orchestrator.
"""

from __future__ import annotations

from dl.models.optimization.orchestration_result import (
    OrchestrationResult,
)
from dl.models.optimization.quantum_inspired_configuration import (
    QuantumInspiredConfiguration,
)
from dl.optimization.quantum_inspired_orchestrator import (
    QuantumInspiredOrchestrator,
)


def test_orchestrator_execution() -> None:
    """
    Orchestrator enables configured modules.
    """

    orchestrator = QuantumInspiredOrchestrator()

    config = QuantumInspiredConfiguration(
        enable_qubo=True,
        enable_annealing=True,
        enable_tensor=True,
        enable_hybrid=True,
        optimization_mode="adaptive",
        seed=42,
    )

    result = orchestrator.execute(
        config,
    )

    assert isinstance(
        result,
        OrchestrationResult,
    )

    assert result.enabled_modules == (
        "qubo",
        "annealing",
        "tensor",
        "hybrid",
    )


def test_orchestrator_strategy() -> None:
    """
    Strategy is preserved.
    """

    orchestrator = QuantumInspiredOrchestrator()

    config = QuantumInspiredConfiguration(
        enable_qubo=True,
        enable_annealing=False,
        enable_tensor=False,
        enable_hybrid=False,
        optimization_mode="qubo_only",
        seed=42,
    )

    result = orchestrator.execute(
        config,
    )

    assert result.selected_strategy == ("qubo_only")
