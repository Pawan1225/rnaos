"""
RNAOS gateway response model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(
    frozen=True,
    slots=True,
)
class GatewayResponse:
    """Immutable gateway response."""

    success: bool

    data: dict[str, Any] = field(
        default_factory=dict,
    )

    errors: list[str] = field(
        default_factory=list,
    )

    trace_id: str | None = None

    request_id: str | None = None

    duration_ms: float | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )
