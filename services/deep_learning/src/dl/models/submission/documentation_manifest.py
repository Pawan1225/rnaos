"""
RNAOS documentation manifest model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DocumentationManifest:
    """
    Immutable documentation metadata.
    """

    documentation_id: str

    version: str

    sections: tuple[str, ...]

    files: tuple[str, ...]

    generator: str

    metadata: tuple[str, ...]
