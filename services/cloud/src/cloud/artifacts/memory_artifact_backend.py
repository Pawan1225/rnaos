"""
In-memory artifact backend.
"""

from __future__ import annotations

from threading import RLock

from cloud.artifacts.artifact import Artifact
from cloud.artifacts.artifact_backend import ArtifactBackend


class MemoryArtifactBackend(ArtifactBackend):
    """Thread-safe in-memory artifact backend."""

    def __init__(self) -> None:
        self._artifacts: dict[str, Artifact] = {}
        self._lock = RLock()

    def save(
        self,
        artifact: Artifact,
    ) -> None:
        with self._lock:
            self._artifacts[artifact.artifact_id] = artifact

    def get(
        self,
        artifact_id: str,
    ) -> Artifact | None:
        with self._lock:
            return self._artifacts.get(
                artifact_id,
            )

    def remove(
        self,
        artifact_id: str,
    ) -> None:
        with self._lock:
            self._artifacts.pop(
                artifact_id,
                None,
            )

    def list(
        self,
    ) -> list[Artifact]:
        with self._lock:
            return sorted(
                self._artifacts.values(),
                key=lambda artifact: (
                    artifact.created_at,
                    artifact.artifact_id,
                ),
            )

    def count(
        self,
    ) -> int:
        with self._lock:
            return len(
                self._artifacts,
            )
