"""
RNAOS variable neighborhood search configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class NeighborhoodConfiguration:
    """
    Immutable VNS configuration.
    """

    levels: tuple[int, ...]

    max_iterations: int
