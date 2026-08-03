from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DatasetInfo:
    """
    Metadata describing a benchmark dataset.
    """

    name: str
    version: str
    description: str
    source: str
    citation: str | None = None
    license: str | None = None
