"""
RNAOS Q matrix models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class QMatrix:
    """
    Immutable QUBO matrix representation.
    """

    variables: tuple[str, ...]

    values: tuple[tuple[float, ...], ...]
