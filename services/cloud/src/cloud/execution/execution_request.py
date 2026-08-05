"""
Distributed execution request.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class ExecutionRequest:
    """Represents one execution request."""

    workflow: str

    payload: dict[str, Any] = field(default_factory=dict)

    priority: int = 0

    metadata: dict[str, Any] = field(default_factory=dict)

    request_id: str = field(default_factory=lambda: str(uuid4()))

    submitted_at: datetime = field(default_factory=lambda: datetime.now(UTC))
