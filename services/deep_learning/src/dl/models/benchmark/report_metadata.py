"""
RNAOS scientific report metadata model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ReportMetadata:
    """
    Immutable experiment provenance metadata.
    """

    software_version: str

    model_versions: tuple[str, ...]

    hardware: str

    runtime_environment: str

    dataset_version: str

    random_seed: int

    timestamp: str
