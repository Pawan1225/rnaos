"""
RNAOS metric record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(
    frozen=True,
    slots=True,
)
class MetricRecord:
    """Immutable metric record."""

    name: str

    value: float

    unit: str = ""

    labels: dict[str, str] = field(
        default_factory=dict,
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )
