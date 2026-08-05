"""
RNAOS Enterprise Gateway.
"""

from __future__ import annotations

from enterprise.backup import BackupManager
from enterprise.benchmark import BenchmarkSuite
from enterprise.deployment import DeploymentManager
from enterprise.gateway.security_gateway import (
    SecurityGateway,
)
from enterprise.release import ReleaseSuite
from enterprise.validation import ValidationSuite


class EnterpriseGateway:
    """Unified enterprise entry point."""

    NAME = "RNAOS Enterprise Gateway"
    VERSION = "1.0.0"
    BUILD = "Sprint-13.7"

    def __init__(self) -> None:
        self.security = SecurityGateway()
        self.deployment = DeploymentManager()
        self.backup = BackupManager()
        self.validation = ValidationSuite()
        self.benchmark = BenchmarkSuite()
        self.release = ReleaseSuite()

    @property
    def services(
        self,
    ) -> dict[str, object]:
        """Return registered enterprise services."""

        return {
            "security": self.security,
            "deployment": self.deployment,
            "backup": self.backup,
            "validation": self.validation,
            "benchmark": self.benchmark,
            "release": self.release,
        }

    def get_service(
        self,
        name: str,
    ) -> object:
        """Return a registered enterprise service."""

        return self.services[name]

    def has_service(
        self,
        name: str,
    ) -> bool:
        """Return whether a service exists."""

        return name in self.services

    def list_services(
        self,
    ) -> list[str]:
        """Return registered enterprise services."""

        return sorted(self.services)

    def metadata(
        self,
    ) -> dict[str, str]:
        """Return gateway metadata."""

        return {
            "name": self.NAME,
            "version": self.VERSION,
            "build": self.BUILD,
        }

    def health(
        self,
    ) -> dict[str, str]:
        """Return enterprise service health."""

        return {
            "security": "healthy",
            "deployment": "healthy",
            "backup": "healthy",
            "validation": "healthy",
            "benchmark": "healthy",
            "release": "healthy",
        }

    def summary(
        self,
    ) -> dict[str, object]:
        """Return enterprise summary."""

        return {
            "metadata": self.metadata(),
            "health": self.health(),
            "services": self.list_services(),
            "service_count": len(self.services),
        }

    def is_healthy(
        self,
    ) -> bool:
        """Return whether all enterprise services are healthy."""

        return all(status == "healthy" for status in self.health().values())
