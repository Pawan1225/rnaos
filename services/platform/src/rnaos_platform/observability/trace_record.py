"""
RNAOS trace record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(
    frozen=True,
    slots=True,
)
class TraceRecord:
    """Immutable distributed trace record."""

    trace_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    span_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    parent_span_id: str | None = None

    component: str = ""

    operation: str = ""

    started_at: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )

    completed_at: datetime | None = None

    duration_ms: float | None = None
