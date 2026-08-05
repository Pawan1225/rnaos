"""
RNAOS Enterprise Release Engine.
"""

from __future__ import annotations

from enterprise.release.models import ReleaseReport, ReleaseResult
from enterprise.release.registry import ReleaseRegistry
from enterprise.release.release import Release


class ReleaseSuite:
    """Execute RNAOS release plugins."""

    def __init__(self) -> None:
        self._registry = ReleaseRegistry()
        self._results: list[ReleaseResult] = []

    def register(
        self,
        release: Release,
    ) -> None:
        """Register a release."""

        self._registry.register(release)

    def unregister(
        self,
        version: str,
    ) -> None:
        """Remove a release."""

        self._registry.remove(version)

    def run(
        self,
        release: Release,
    ) -> ReleaseResult:
        """Execute one release."""

        result = release.release()

        self._results.append(result)

        return result

    def run_all(
        self,
    ) -> ReleaseReport:
        """Execute all registered releases."""

        for release in self._registry.items():
            self.run(release)

        return self.report()

    def report(
        self,
    ) -> ReleaseReport:
        """Return a release report."""

        return ReleaseReport(
            releases=list(self._results),
        )

    def statistics(
        self,
    ) -> dict[str, int]:
        """Return release statistics."""

        report = self.report()

        return {
            "total": report.total,
            "passed": report.passed,
            "failed": report.failed,
        }

    def results(
        self,
    ) -> list[ReleaseResult]:
        """Return release results."""

        return list(self._results)

    def clear(
        self,
    ) -> None:
        """Clear release results."""

        self._results.clear()
