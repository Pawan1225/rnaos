"""
RNAOS workflow execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from rnaos_platform.workflow.workflow_status import WorkflowStatus


@dataclass(
    slots=True,
)
class WorkflowContext:
    """Shared workflow execution context."""

    workflow_id: str = field(
        default_factory=lambda: str(
            uuid4(),
        ),
    )

    status: WorkflowStatus = WorkflowStatus.PENDING

    data: dict[str, Any] = field(
        default_factory=dict,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    started_at: datetime | None = None

    completed_at: datetime | None = None

    def start(self) -> None:
        """Mark the workflow as running."""
        self.status = WorkflowStatus.RUNNING

        self.started_at = datetime.now(
            UTC,
        )

    def complete(self) -> None:
        """Mark the workflow as completed."""
        self.status = WorkflowStatus.COMPLETED

        self.completed_at = datetime.now(
            UTC,
        )

    def fail(self) -> None:
        """Mark the workflow as failed."""
        self.status = WorkflowStatus.FAILED

        self.completed_at = datetime.now(
            UTC,
        )

    def cancel(self) -> None:
        """Mark the workflow as cancelled."""
        self.status = WorkflowStatus.CANCELLED

        self.completed_at = datetime.now(
            UTC,
        )
