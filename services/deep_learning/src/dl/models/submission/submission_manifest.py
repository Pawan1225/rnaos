"""
RNAOS submission manifest model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SubmissionManifest:
    """
    Immutable submission package metadata.
    """

    submission_id: str

    version: str

    artifacts: tuple[str, ...]

    directories: tuple[str, ...]

    package_name: str

    metadata: tuple[str, ...]
