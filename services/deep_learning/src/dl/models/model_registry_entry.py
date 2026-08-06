"""
RNAOS model registry entry model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ModelRegistryEntry:
    """
    Immutable model registry metadata.
    """

    name: str

    version: str

    model_type: str

    description: str
