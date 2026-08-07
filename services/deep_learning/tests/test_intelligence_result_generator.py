"""
Tests for intelligence result generator.
"""

from __future__ import annotations

from dl.models.optimization.quantum_inspired_result import (
    QuantumInspiredResult,
)
from dl.optimization.intelligence_result_generator import (
    IntelligenceResultGenerator,
)


def test_result_generation() -> None:
    """
    Intelligence result is generated.
    """

    generator = IntelligenceResultGenerator()

    result = generator.generate(
        strategy="adaptive_hybrid",
        modules_used=(
            "qubo",
            "annealing",
            "tensor",
        ),
        confidence=0.95,
        reasoning=("Hybrid optimization selected."),
    )

    assert isinstance(
        result,
        QuantumInspiredResult,
    )

    assert result.status == "completed"

    assert result.strategy == ("adaptive_hybrid")
