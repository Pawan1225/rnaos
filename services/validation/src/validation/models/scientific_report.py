"""
RNAOS scientific benchmark report model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ScientificBenchmarkReport:
    """
    Immutable benchmark report metadata.
    """

    report_id: str

    title: str

    sections: tuple[str, ...]

    benchmark_version: str

    result_files: tuple[str, ...]

    version: str
