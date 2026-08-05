"""
RNAOS Artifact Store.
"""

from __future__ import annotations

from cloud.artifacts.artifact import Artifact
from cloud.artifacts.artifact_backend import ArtifactBackend
from cloud.artifacts.memory_artifact_backend import (
    MemoryArtifactBackend,
)


class ArtifactStore:
    """Public interface for RNAOS artifact storage."""

    def __init__(
        self,
        backend: ArtifactBackend | None = None,
    ) -> None:
        self._backend = backend if backend is not None else MemoryArtifactBackend()

    def save(
        self,
        artifact: Artifact,
    ) -> None:
        """Save an artifact."""
        self._backend.save(artifact)

    def get(
        self,
        artifact_id: str,
    ) -> Artifact | None:
        """Retrieve an artifact."""
        return self._backend.get(artifact_id)

    def remove(
        self,
        artifact_id: str,
    ) -> None:
        """Remove an artifact."""
        self._backend.remove(artifact_id)

    def list(
        self,
    ) -> list[Artifact]:
        """Return all stored artifacts."""
        return self._backend.list()

    def count(
        self,
    ) -> int:
        """Return the number of stored artifacts."""
        return self._backend.count()
