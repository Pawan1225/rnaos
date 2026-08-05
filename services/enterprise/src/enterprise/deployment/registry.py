"""
Deployment registry for the RNAOS Enterprise Deployment Framework.
"""

from __future__ import annotations

from enterprise.deployment.models import DeploymentProfile


class DeploymentRegistry:
    """Registry of deployment profiles."""

    def __init__(
        self,
    ) -> None:
        self._profiles: dict[
            str,
            DeploymentProfile,
        ] = {}

    def register(
        self,
        profile: DeploymentProfile,
    ) -> None:
        """Register or update a deployment profile."""

        self._profiles[profile.name] = profile

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a deployment profile."""

        self._profiles.pop(
            name,
            None,
        )

    def get(
        self,
        name: str,
    ) -> DeploymentProfile | None:
        """Retrieve a deployment profile."""

        return self._profiles.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """Check whether a deployment profile exists."""

        return name in self._profiles

    def list_profiles(
        self,
    ) -> list[DeploymentProfile]:
        """Return all deployment profiles."""

        return sorted(
            self._profiles.values(),
            key=lambda profile: profile.name,
        )

    def count(
        self,
    ) -> int:
        """Return the number of deployment profiles."""

        return len(self._profiles)

    def clear(
        self,
    ) -> None:
        """Remove all deployment profiles."""

        self._profiles.clear()
