"""
RNAOS checkpoint model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class Checkpoint:
    """
    Immutable training checkpoint.
    """

    checkpoint_id: str

    model_name: str

    epoch: int

    path: str

    created_at: str
