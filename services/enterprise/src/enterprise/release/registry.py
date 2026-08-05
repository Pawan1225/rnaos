"""
Release registry for the RNAOS Enterprise Release Framework.
"""

from __future__ import annotations

from enterprise.release.release import Release


class ReleaseRegistry:
    """Registry of RNAOS release plugins."""

    def __init__(self) -> None:
        self._releases: dict[str, Release] = {}

    def register(
        self,
        release: Release,
    ) -> None:
        """Register a release."""

        self._releases[release.version] = release

    def get(
        self,
        version: str,
    ) -> Release | None:
        """Return a release."""

        return self._releases.get(version)

    def exists(
        self,
        version: str,
    ) -> bool:
        """Return whether a release exists."""

        return version in self._releases

    def remove(
        self,
        version: str,
    ) -> None:
        """Remove a release."""

        self._releases.pop(version, None)

    def clear(
        self,
    ) -> None:
        """Clear the registry."""

        self._releases.clear()

    def list_releases(
        self,
    ) -> list[str]:
        """Return registered release versions."""

        return sorted(self._releases)

    def items(
        self,
    ) -> tuple[Release, ...]:
        """Return registered releases."""

        return tuple(self._releases[name] for name in sorted(self._releases))

    def count(
        self,
    ) -> int:
        """Return number of registered releases."""

        return len(self._releases)
