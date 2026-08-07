"""
Tests for quantum-inspired profile engine.
"""

from __future__ import annotations

from dl.models.optimization.quantum_inspired_profile import (
    QuantumInspiredIntelligenceProfile,
)
from dl.optimization.quantum_inspired_profile_engine import (
    QuantumInspiredProfileEngine,
)


def test_profile_generation() -> None:
    """
    Final profile is generated.
    """

    engine = QuantumInspiredProfileEngine()

    profile = engine.generate(
        strategy="adaptive_hybrid",
        selected_solver="annealing",
        modules_used=(
            "qubo",
            "annealing",
            "tensor",
            "hybrid",
        ),
        confidence=0.95,
        status="completed",
        reasoning=("Hybrid optimization selected based on RNA complexity."),
    )

    assert isinstance(
        profile,
        QuantumInspiredIntelligenceProfile,
    )

    assert profile.selected_solver == ("annealing")

    assert profile.status == ("completed")
