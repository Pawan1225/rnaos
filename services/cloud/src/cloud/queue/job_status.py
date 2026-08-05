"""
Job lifecycle states.
"""

from __future__ import annotations

from enum import StrEnum


class JobStatus(StrEnum):
    """Supported job states."""

    PENDING = "pending"

    QUEUED = "queued"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"
