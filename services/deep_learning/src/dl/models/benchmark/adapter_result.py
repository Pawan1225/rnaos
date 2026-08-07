"""
RNAOS benchmark adapter result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkAdapterResult:
    """
    Immutable benchmark adapter output.
    """

    method_name: str

    sequence: str

    structure: str

    energy: float

    runtime: float

    memory: float

    metadata: tuple[str, ...]
