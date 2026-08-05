"""
RNAOS gateway request model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass(
    frozen=True,
    slots=True,
)
class GatewayRequest:
    """Immutable gateway request."""

    service: str

    operation: str

    payload: dict[str, Any] = field(
        default_factory=dict,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    trace_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    request_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )
