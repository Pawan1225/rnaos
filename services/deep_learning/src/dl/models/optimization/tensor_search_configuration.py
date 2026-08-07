"""
RNAOS tensor search configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorSearchConfiguration:
    """
    Immutable tensor search configuration.
    """

    candidates: int

    seed: int
