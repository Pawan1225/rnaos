"""
RNAOS parallel tempering profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ParallelTemperingProfile:
    """
    Immutable parallel tempering intelligence profile.
    """

    best_replica_id: int

    best_energy: float

    replica_count: int

    exchanges: int

    confidence: float
