"""
Configuration provider abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class ConfigProvider(ABC):
    """Abstract base class for configuration providers."""

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> object | None:
        """Retrieve a configuration value."""

    @abstractmethod
    def set(
        self,
        key: str,
        value: object,
    ) -> None:
        """Store a configuration value."""

    @abstractmethod
    def exists(
        self,
        key: str,
    ) -> bool:
        """Check whether a configuration key exists."""

    @abstractmethod
    def remove(
        self,
        key: str,
    ) -> None:
        """Remove a configuration key."""

    @abstractmethod
    def all(
        self,
    ) -> dict[str, object]:
        """Return all configuration values."""
