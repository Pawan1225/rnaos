"""
RNAOS platform event model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from rnaos_platform.events.event_type import EventType


@dataclass(
    frozen=True,
    slots=True,
)
class Event:
    """Immutable platform event."""

    event_type: EventType

    source: str

    payload: dict[str, Any] = field(
        default_factory=dict,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    event_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            UTC,
        ),
    )
