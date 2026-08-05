"""
Deployment management for the RNAOS Enterprise Deployment Framework.
"""

from __future__ import annotations

from enterprise.deployment.models import DeploymentProfile
from enterprise.deployment.registry import DeploymentRegistry


class DeploymentManager:
    """Manage deployment profiles."""

    def __init__(
        self,
        registry: DeploymentRegistry | None = None,
    ) -> None:
        self._registry = registry if registry is not None else DeploymentRegistry()

    def register(
        self,
        profile: DeploymentProfile,
    ) -> None:
        """Register a deployment profile."""

        self._registry.register(profile)

    def get(
        self,
        name: str,
    ) -> DeploymentProfile | None:
        """Retrieve a deployment profile."""

        return self._registry.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """Check whether a deployment profile exists."""

        return self._registry.exists(name)

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a deployment profile."""

        self._registry.remove(name)

    def list_profiles(
        self,
    ) -> list[DeploymentProfile]:
        """Return all deployment profiles."""

        return self._registry.list_profiles()

    def count(
        self,
    ) -> int:
        """Return the number of deployment profiles."""

        return self._registry.count()

    def clear(
        self,
    ) -> None:
        """Remove all deployment profiles."""

        self._registry.clear()
