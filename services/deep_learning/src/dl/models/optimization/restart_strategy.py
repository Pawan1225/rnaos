"""
RNAOS restart strategy models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RestartDecision:
    """
    Immutable restart decision.
    """

    restart: bool

    reason: str
