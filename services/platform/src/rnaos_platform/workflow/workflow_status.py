"""
RNAOS workflow status definitions.
"""

from __future__ import annotations

from enum import StrEnum


class WorkflowStatus(StrEnum):
    """Workflow lifecycle states."""

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
