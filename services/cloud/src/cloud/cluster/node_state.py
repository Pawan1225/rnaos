"""
Cluster node states.
"""

from __future__ import annotations

from enum import StrEnum


class NodeState(StrEnum):
    """Supported cluster node states."""

    ONLINE = "online"

    OFFLINE = "offline"

    STARTING = "starting"

    DRAINING = "draining"

    MAINTENANCE = "maintenance"

    FAILED = "failed"
