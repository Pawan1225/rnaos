"""
RNAOS job model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from cloud.queue.job_status import JobStatus


@dataclass(slots=True, frozen=True)
class Job:
    """Represents a queued execution job."""

    task: str

    payload: dict[str, Any] = field(
        default_factory=dict,
    )

    priority: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    job_id: str = field(
        default_factory=lambda: str(uuid4()),
    )

    status: JobStatus = JobStatus.PENDING

    submitted_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
