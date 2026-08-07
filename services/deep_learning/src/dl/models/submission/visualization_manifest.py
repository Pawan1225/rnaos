"""
RNAOS visualization artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class VisualizationManifest:
    """
    Immutable visualization metadata.
    """

    visualization_id: str

    figures: tuple[str, ...]

    formats: tuple[str, ...]

    generator: str

    version: str

    metadata: tuple[str, ...]
