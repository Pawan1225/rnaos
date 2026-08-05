"""
RNAOS component health model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from rnaos_platform.monitoring.health_status import HealthStatus


@dataclass(
    frozen=True,
    slots=True,
)
class ComponentHealth:
    """Health snapshot for a platform component."""

    name: str

    status: HealthStatus

    message: str = ""

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    checked_at: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )

    response_time_ms: float | None = None
