"""
RNAOS statistical significance result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SignificanceResult:
    """
    Immutable significance testing result.
    """

    test_name: str

    p_value: float

    alpha: float

    significant: bool

    sample_size: int
