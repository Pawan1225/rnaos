"""
RNAOS Enterprise Release Manager.
"""

from __future__ import annotations

from enterprise.release.models import ReleaseReport
from enterprise.release.platform_release_engine import (
    release_platform,
)


def release_manager() -> ReleaseReport:
    """Execute the RNAOS release workflow."""

    return release_platform()
