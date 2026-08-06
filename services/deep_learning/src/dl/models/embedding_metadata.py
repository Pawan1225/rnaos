"""
RNAOS embedding metadata model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class EmbeddingMetadata:
    """
    Immutable embedding metadata.
    """

    embedding_id: str

    version: str

    model_name: str

    dimension: int
