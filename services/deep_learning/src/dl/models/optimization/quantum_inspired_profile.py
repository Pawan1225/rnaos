"""
RNAOS quantum-inspired intelligence profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QuantumInspiredIntelligenceProfile:
    """
    Immutable quantum-inspired intelligence profile.
    """

    strategy: str

    selected_solver: str

    modules_used: tuple[str, ...]

    confidence: float

    status: str

    reasoning: str
