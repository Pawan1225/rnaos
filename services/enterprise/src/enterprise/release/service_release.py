"""
RNAOS Release Service.
"""

from __future__ import annotations

from enterprise.release.models import ReleaseReport
from enterprise.release.platform_releases import (
    default_platform_releases,
)
from enterprise.release.release_suite import (
    ReleaseSuite,
)


def release_services() -> ReleaseReport:
    """Run all RNAOS platform releases."""

    suite = ReleaseSuite()

    for release in default_platform_releases():
        suite.register(release)

    return suite.run_all()
