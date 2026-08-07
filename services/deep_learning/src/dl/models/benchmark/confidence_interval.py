"""
RNAOS confidence interval model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ConfidenceInterval:
    """
    Immutable confidence interval result.
    """

    confidence_level: float

    lower_bound: float

    upper_bound: float

    margin_of_error: float
