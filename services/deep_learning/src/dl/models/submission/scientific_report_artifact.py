"""
RNAOS scientific report artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ScientificReportArtifact:
    """
    Immutable scientific report metadata.
    """

    report_id: str

    title: str

    sections: tuple[str, ...]

    figures: tuple[str, ...]

    benchmark_reference: str

    version: str

    metadata: tuple[str, ...]
