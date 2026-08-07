"""
RNAOS temperature replica model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TemperatureReplica:
    """
    Immutable parallel tempering replica.
    """

    replica_id: int

    temperature: float

    state: tuple[int, ...]

    energy: float
