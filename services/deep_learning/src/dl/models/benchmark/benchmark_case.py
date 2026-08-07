"""
RNAOS benchmark case model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkCase:
    """
    Immutable benchmark execution case.
    """

    case_id: str

    sequence: str

    reference_structure: str

    reference_energy: float

    methods: tuple[str, ...]

    metadata: tuple[str, ...]
