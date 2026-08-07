"""
RNAOS final submission profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class FinalSubmissionProfile:
    """
    Immutable final submission metadata.
    """

    submission_id: str

    version: str

    components: tuple[str, ...]

    package_name: str

    release_ready: bool

    metadata: tuple[str, ...]
