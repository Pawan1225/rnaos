"""
Tests for RNAOS Quantum Adapter.
"""

from __future__ import annotations

from dl.adapters.quantum_adapter import (
    QuantumAdapter,
)


def test_quantum_embedding_conversion() -> None:
    """
    Quantum embedding conversion works.
    """

    adapter = QuantumAdapter()

    result = adapter.convert_embedding(
        [0.1, 0.2],
    )

    assert result["quantum_embedding"] == [
        0.1,
        0.2,
    ]


def test_quantum_prediction_conversion() -> None:
    """
    Quantum prediction conversion works.
    """

    adapter = QuantumAdapter()

    result = adapter.convert_prediction(
        0.95,
    )

    assert result["quantum_prediction"] == 0.95
