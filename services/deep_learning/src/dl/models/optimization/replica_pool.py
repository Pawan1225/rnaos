"""
RNAOS replica pool model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.temperature_replica import (
    TemperatureReplica,
)


@dataclass(
    slots=True,
    frozen=True,
)
class ReplicaPool:
    """
    Immutable replica collection.
    """

    replicas: tuple[TemperatureReplica, ...]
