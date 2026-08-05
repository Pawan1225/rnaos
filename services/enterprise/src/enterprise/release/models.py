"""
Release models for the RNAOS Enterprise Release Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


class ReleaseStatus(StrEnum):
    """Release execution status."""

    PASSED = "passed"
    FAILED = "failed"


class ReleaseChannel(StrEnum):
    """Release channel."""

    ALPHA = "alpha"
    BETA = "beta"
    RC = "rc"
    STABLE = "stable"
    LTS = "lts"


@dataclass(slots=True)
class ReleaseArtifact:
    """Release artifact."""

    name: str

    path: str

    metadata: dict[str, object] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class ReleaseResult:
    """Single release result."""

    version: str

    description: str

    status: ReleaseStatus

    channel: ReleaseChannel

    artifacts: list[ReleaseArtifact] = field(
        default_factory=list,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    @property
    def passed(self) -> bool:
        """Return True if the release passed."""

        return self.status is ReleaseStatus.PASSED


@dataclass(slots=True)
class ReleaseReport:
    """Release report."""

    releases: list[ReleaseResult] = field(
        default_factory=list,
    )

    @property
    def total(self) -> int:
        """Return the total number of releases."""

        return len(self.releases)

    @property
    def passed(self) -> int:
        """Return the number of successful releases."""

        return sum(release.passed for release in self.releases)

    @property
    def failed(self) -> int:
        """Return the number of failed releases."""

        return self.total - self.passed

    @property
    def success(self) -> bool:
        """Return True if all releases passed."""

        return self.failed == 0
