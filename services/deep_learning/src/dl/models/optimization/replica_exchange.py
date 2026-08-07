"""
RNAOS replica exchange models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ReplicaExchangeResult:
    """
    Immutable replica exchange result.
    """

    replica_a: int

    replica_b: int

    accepted: bool

    probability: float
