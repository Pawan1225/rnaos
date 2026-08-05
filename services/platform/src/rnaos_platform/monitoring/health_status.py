"""
RNAOS health status definitions.
"""

from __future__ import annotations

from enum import StrEnum


class HealthStatus(StrEnum):
    """Health lifecycle states."""

    HEALTHY = "healthy"

    WARNING = "warning"

    CRITICAL = "critical"

    UNKNOWN = "unknown"
