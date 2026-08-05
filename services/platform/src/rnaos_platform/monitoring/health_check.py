"""
RNAOS health check abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from rnaos_platform.monitoring.component_health import ComponentHealth


class HealthCheck(ABC):
    """Base class for all platform health checks."""

    @property
    @abstractmethod
    def name(
        self,
    ) -> str:
        """Return the component name."""

    @abstractmethod
    def check(
        self,
    ) -> ComponentHealth:
        """Evaluate the component health."""
