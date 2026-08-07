"""
RNAOS benchmark export manifest.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExportManifest:
    """
    Immutable benchmark export metadata.
    """

    export_id: str

    files: tuple[str, ...]

    format_versions: tuple[str, ...]

    benchmark_version: str

    metadata: tuple[str, ...]
