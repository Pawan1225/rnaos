"""
Artifact backend abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from cloud.artifacts.artifact import Artifact


class ArtifactBackend(ABC):
    """Abstract artifact storage backend."""

    @abstractmethod
    def save(
        self,
        artifact: Artifact,
    ) -> None:
        """Persist an artifact."""
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        artifact_id: str,
    ) -> Artifact | None:
        """Return an artifact by ID."""
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        artifact_id: str,
    ) -> None:
        """Remove an artifact."""
        raise NotImplementedError

    @abstractmethod
    def list(
        self,
    ) -> list[Artifact]:
        """Return all stored artifacts."""
        raise NotImplementedError

    @abstractmethod
    def count(
        self,
    ) -> int:
        """Return the number of stored artifacts."""
        raise NotImplementedError
