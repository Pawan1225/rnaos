"""
RNAOS parallel tempering result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ParallelTemperingResult:
    """
    Immutable parallel tempering result.
    """

    best_replica_id: int

    best_energy: float

    exchanges: int

    converged: bool
