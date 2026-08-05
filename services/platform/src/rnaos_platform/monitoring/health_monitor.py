"""
RNAOS health monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass

from rnaos_platform.events import Event, EventBus, EventType
from rnaos_platform.monitoring.component_health import (
    ComponentHealth,
)
from rnaos_platform.monitoring.health_check import (
    HealthCheck,
)
from rnaos_platform.monitoring.health_status import (
    HealthStatus,
)


@dataclass(
    frozen=True,
    slots=True,
)
class HealthReport:
    """Immutable platform health report."""

    overall_status: HealthStatus

    components: tuple[
        ComponentHealth,
        ...,
    ]

    @property
    def healthy(
        self,
    ) -> bool:
        """Return True if every component is healthy."""
        return self.overall_status == HealthStatus.HEALTHY


class HealthMonitor:
    """Evaluate platform component health."""

    def __init__(
        self,
        event_bus: EventBus | None = None,
    ) -> None:
        self._checks: dict[
            str,
            HealthCheck,
        ] = {}

        self._last_status: dict[
            str,
            HealthStatus,
        ] = {}

        self._event_bus = event_bus if event_bus is not None else EventBus()

    def register(
        self,
        check: HealthCheck,
    ) -> None:
        """Register a health check."""

        self._checks[check.name] = check

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a health check."""

        self._checks.pop(
            name,
            None,
        )

        self._last_status.pop(
            name,
            None,
        )

    def report(
        self,
    ) -> HealthReport:
        """Evaluate every registered component."""

        components: list[ComponentHealth] = []

        overall = HealthStatus.HEALTHY

        for check in self._checks.values():
            health = check.check()

            previous = self._last_status.get(
                health.name,
            )

            if previous != health.status:
                self._event_bus.publish(
                    Event(
                        event_type=EventType.HEALTH_CHANGED,
                        source="health_monitor",
                        payload={
                            "component": health.name,
                            "status": health.status.value,
                        },
                    ),
                )

            self._last_status[health.name] = health.status

            components.append(
                health,
            )

            if health.status == HealthStatus.CRITICAL:
                overall = HealthStatus.CRITICAL

            elif health.status == HealthStatus.WARNING and overall != HealthStatus.CRITICAL:
                overall = HealthStatus.WARNING

            elif health.status == HealthStatus.UNKNOWN and overall == HealthStatus.HEALTHY:
                overall = HealthStatus.UNKNOWN

        return HealthReport(
            overall_status=overall,
            components=tuple(
                components,
            ),
        )

    def component_count(
        self,
    ) -> int:
        """Return the number of registered health checks."""
        return len(
            self._checks,
        )

    def clear(
        self,
    ) -> None:
        """Remove every registered health check."""

        self._checks.clear()

        self._last_status.clear()
