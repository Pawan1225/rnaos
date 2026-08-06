"""
RNAOS inference configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class InferenceConfiguration:
    """
    Immutable inference execution settings.
    """

    model_version: str = "v1"

    device: str = "cpu"

    batch_size: int = 1

    deterministic: bool = True

    return_confidence: bool = True
