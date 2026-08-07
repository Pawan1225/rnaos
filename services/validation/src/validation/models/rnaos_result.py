"""
RNAOS experiment result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RNAOSResult:
    """
    Immutable RNAOS execution result.
    """

    sequence: str

    structure: str

    energy: float

    solver: str

    runtime: float

    qubit_estimate: int

    variable_count: int

    iterations: int

    version: str
