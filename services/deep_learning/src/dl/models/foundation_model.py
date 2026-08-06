"""
RNAOS foundation model metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class FoundationModelInfo:
    """
    Immutable foundation model metadata.
    """

    name: str

    version: str

    embedding_dimension: int

    description: str
