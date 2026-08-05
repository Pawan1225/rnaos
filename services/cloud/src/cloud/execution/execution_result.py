"""
Distributed execution result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from cloud.execution.execution_status import ExecutionStatus


@dataclass(slots=True, frozen=True)
class ExecutionResult:
    """Result returned from a worker."""

    request_id: str

    worker_id: str

    status: ExecutionStatus

    output: Any = None

    error: str | None = None

    started_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    completed_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    metadata: dict[str, Any] = field(default_factory=dict)
