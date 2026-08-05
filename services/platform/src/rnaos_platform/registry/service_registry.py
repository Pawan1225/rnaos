"""
RNAOS Service Registry.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ServiceInfo:
    """Registered platform service."""

    name: str
    version: str
    description: str
    endpoint: str | None = None
    metadata: dict[str, object] = field(
        default_factory=dict,
    )


class ServiceRegistry:
    """Central registry of platform services."""

    def __init__(self) -> None:
        self._services: dict[
            str,
            ServiceInfo,
        ] = {}

    def register(
        self,
        service: ServiceInfo,
    ) -> None:
        """Register a service."""
        self._services[service.name] = service

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a service from the registry."""
        self._services.pop(
            name,
            None,
        )

    def get(
        self,
        name: str,
    ) -> ServiceInfo | None:
        """Retrieve a registered service."""
        return self._services.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """Check whether a service exists."""
        return name in self._services

    def list_services(
        self,
    ) -> list[ServiceInfo]:
        """Return all registered services sorted by name."""
        return sorted(
            self._services.values(),
            key=lambda service: service.name,
        )

    def count(
        self,
    ) -> int:
        """Return the number of registered services."""
        return len(self._services)
