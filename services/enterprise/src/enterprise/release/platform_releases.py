"""
Default platform releases for the RNAOS Enterprise Release Framework.
"""

from __future__ import annotations

from enterprise.release.models import (
    ReleaseChannel,
    ReleaseResult,
    ReleaseStatus,
)
from enterprise.release.release import Release


class PlatformRelease(Release):
    """Release plugin for an RNAOS platform service."""

    def __init__(
        self,
        version: str,
        description: str,
    ) -> None:
        self._version = version
        self._description = description

    @property
    def version(self) -> str:
        """Return release version."""

        return self._version

    def release(self) -> ReleaseResult:
        """Execute the release."""

        return ReleaseResult(
            version=self.version,
            description=self._description,
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.STABLE,
        )


def default_platform_releases() -> list[Release]:
    """Return the default RNAOS platform releases."""

    return [
        PlatformRelease("RNA", "RNA Service"),
        PlatformRelease("AI", "AI Service"),
        PlatformRelease("Optimization", "Optimization Service"),
        PlatformRelease("Solver", "Solver Service"),
        PlatformRelease("Research", "Research Service"),
        PlatformRelease("Decision", "Decision Service"),
        PlatformRelease("Analytics", "Analytics Service"),
        PlatformRelease("Platform", "Platform Service"),
        PlatformRelease("Cloud", "Cloud Service"),
        PlatformRelease("Enterprise", "Enterprise Service"),
    ]
