"""
RNAOS reproducibility manifest model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ReproducibilityManifest:
    """
    Immutable reproducibility metadata.
    """

    reproducibility_id: str

    files: tuple[str, ...]

    environment: str

    dependencies: tuple[str, ...]

    configs: tuple[str, ...]

    seeds: tuple[str, ...]

    version: str

    metadata: tuple[str, ...]
