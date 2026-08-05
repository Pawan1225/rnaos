"""
Distributed execution worker.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from cloud.execution.worker_state import WorkerState


@dataclass(slots=True)
class Worker:
    """Represents one execution worker."""

    worker_id: str

    hostname: str

    capabilities: set[str] = field(default_factory=set)

    labels: dict[str, str] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    state: WorkerState = WorkerState.ONLINE

    active_jobs: int = 0

    max_jobs: int = 1

    last_heartbeat: datetime = field(default_factory=lambda: datetime.now(UTC))

    def can_accept_job(self) -> bool:
        """Return True if the worker can accept another job."""
        return self.state == WorkerState.ONLINE and self.active_jobs < self.max_jobs

    def assign_job(self) -> None:
        """Assign a job to this worker."""
        if not self.can_accept_job():
            raise RuntimeError(f"Worker '{self.worker_id}' cannot accept more jobs.")

        self.active_jobs += 1

        if self.active_jobs >= self.max_jobs:
            self.state = WorkerState.BUSY

    def complete_job(self) -> None:
        """Mark one job as completed."""
        if self.active_jobs > 0:
            self.active_jobs -= 1

        if self.state != WorkerState.MAINTENANCE:
            self.state = WorkerState.ONLINE

    def heartbeat(self) -> None:
        """Update heartbeat timestamp."""
        self.last_heartbeat = datetime.now(UTC)
