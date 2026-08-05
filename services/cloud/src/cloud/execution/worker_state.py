"""
Worker lifecycle states.
"""

from __future__ import annotations

from enum import StrEnum


class WorkerState(StrEnum):
    """Supported worker states."""

    ONLINE = "online"
    BUSY = "busy"
    OFFLINE = "offline"
    DRAINING = "draining"
    MAINTENANCE = "maintenance"
