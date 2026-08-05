"""
Domain models for the RNAOS Enterprise Deployment Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


class DeploymentEnvironment(StrEnum):
    """Deployment environments."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"
    HPC = "hpc"
    CLOUD = "cloud"


class DeploymentStatus(StrEnum):
    """Deployment status."""

    PENDING = "pending"
    DEPLOYING = "deploying"
    RUNNING = "running"
    FAILED = "failed"
    STOPPED = "stopped"
    ROLLED_BACK = "rolled_back"


@dataclass(slots=True)
class DeploymentProfile:
    """Deployment profile."""

    name: str

    environment: DeploymentEnvironment

    version: str

    description: str = ""

    status: DeploymentStatus = DeploymentStatus.PENDING

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
