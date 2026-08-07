"""
RNAOS artifact data contract.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ArtifactRecord:
    """
    Immutable generated artifact metadata.
    """

    artifact_id: str

    artifact_type: str

    artifact_name: str

    version: str

    location: str

    generator: str

    created_at: str

    checksum: str

    metadata: tuple[str, ...]
