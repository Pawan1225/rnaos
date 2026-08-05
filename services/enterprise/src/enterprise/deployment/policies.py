"""
Deployment policies for the RNAOS Enterprise Deployment Framework.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from enterprise.deployment.models import (
    DeploymentProfile,
    DeploymentStatus,
)


class DeploymentPolicy(ABC):
    """Base deployment policy."""

    @abstractmethod
    def deploy(
        self,
        profile: DeploymentProfile,
    ) -> DeploymentProfile:
        """Deploy a profile."""


class LocalDeploymentPolicy(DeploymentPolicy):
    """Local deployment policy."""

    def deploy(
        self,
        profile: DeploymentProfile,
    ) -> DeploymentProfile:
        """Deploy locally."""

        profile.status = DeploymentStatus.RUNNING

        return profile
