"""
RNAOS benchmark report artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkReportArtifact:
    """
    Immutable benchmark report metadata.
    """

    report_id: str

    title: str

    benchmarks: tuple[str, ...]

    metrics: tuple[str, ...]

    figures: tuple[str, ...]

    version: str

    metadata: tuple[str, ...]
