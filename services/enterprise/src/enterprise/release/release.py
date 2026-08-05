"""
Release protocol for the RNAOS Enterprise Release Framework.
"""

from __future__ import annotations

from typing import Protocol

from enterprise.release.models import ReleaseResult


class Release(Protocol):
    """Protocol implemented by all release plugins."""

    @property
    def version(self) -> str:
        """Return the release version."""
        ...

    def release(self) -> ReleaseResult:
        """Execute the release."""
        ...
