"""
RNAOS quantum resource scaling model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QuantumResourceAnalysis:
    """
    Immutable quantum resource analysis.
    """

    analysis_id: str

    sample_count: int

    average_qubits: float

    maximum_qubits: int

    average_variables: float

    average_depth: float

    scaling_factor: float

    benchmark_version: str
