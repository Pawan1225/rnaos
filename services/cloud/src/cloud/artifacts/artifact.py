"""
RNAOS artifact model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from cloud.artifacts.artifact_kind import ArtifactKind


@dataclass(slots=True, frozen=True)
class Artifact:
    """Immutable workflow artifact."""

    name: str

    kind: ArtifactKind

    data: Any

    version: str = "1.0.0"

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    checksum: str | None = None

    artifact_id: str = field(
        default_factory=lambda: str(uuid4()),
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
