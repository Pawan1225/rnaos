"""
RNAOS quantum-inspired result models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QuantumInspiredResult:
    """
    Immutable quantum-inspired intelligence result.
    """

    strategy: str

    modules_used: tuple[str, ...]

    confidence: float

    status: str

    reasoning: str
