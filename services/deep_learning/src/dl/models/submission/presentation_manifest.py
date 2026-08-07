"""
RNAOS presentation artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PresentationManifest:
    """
    Immutable presentation metadata.
    """

    presentation_id: str

    title: str

    slides: tuple[str, ...]

    figures: tuple[str, ...]

    version: str

    metadata: tuple[str, ...]
