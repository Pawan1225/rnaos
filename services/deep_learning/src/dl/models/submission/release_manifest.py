"""
RNAOS release manifest model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ReleaseManifest:
    """
    Immutable release metadata.
    """

    release_id: str

    version: str

    package_name: str

    artifacts: tuple[str, ...]

    checksum_file: str

    changelog_file: str

    metadata: tuple[str, ...]
