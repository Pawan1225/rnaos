"""
RNAOS structured log record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from rnaos_platform.observability.log_level import (
    LogLevel,
)


@dataclass(
    frozen=True,
    slots=True,
)
class LogRecord:
    """Immutable structured log record."""

    level: LogLevel

    component: str

    message: str

    trace_id: str | None = None

    workflow_id: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )
