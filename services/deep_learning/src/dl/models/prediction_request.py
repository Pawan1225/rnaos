"""
RNAOS prediction request model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PredictionRequest:
    """
    Immutable inference prediction request.
    """

    sequence: str

    prediction_task: str

    model_version: str = "v1"

    metadata: tuple[str, ...] = ()
