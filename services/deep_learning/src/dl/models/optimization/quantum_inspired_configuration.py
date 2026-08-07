"""
RNAOS quantum-inspired configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QuantumInspiredConfiguration:
    """
    Immutable quantum-inspired configuration.
    """

    enable_qubo: bool

    enable_annealing: bool

    enable_tensor: bool

    enable_hybrid: bool

    optimization_mode: str

    seed: int
