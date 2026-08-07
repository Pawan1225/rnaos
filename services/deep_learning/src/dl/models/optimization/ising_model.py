"""
RNAOS Ising optimization models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IsingModel:
    """
    Immutable Ising representation.

    Energy:

    E(s) = h*s + s*J*s
    """

    variables: tuple[str, ...]

    local_fields: tuple[float, ...]

    couplings: tuple[tuple[float, ...], ...]

    offset: float = 0.0
