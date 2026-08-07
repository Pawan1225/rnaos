"""
RNAOS ViennaRNA reference model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ViennaReference:
    """
    Immutable ViennaRNA result.
    """

    sequence: str

    structure: str

    mfe_energy: float

    length: int

    engine: str

    version: str
