"""
RNAOS Platform Release Engine.
"""

from __future__ import annotations

from enterprise.release.models import ReleaseReport
from enterprise.release.service_release import (
    release_services,
)


def release_platform() -> ReleaseReport:
    """Execute the platform release."""

    return release_services()
