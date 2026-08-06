"""
RNAOS model selection result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ModelSelection:
    """
    Selected deep learning model information.
    """

    model_family: str

    reasoning: str
