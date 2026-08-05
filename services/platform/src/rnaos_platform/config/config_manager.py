"""
Central configuration manager.
"""

from __future__ import annotations

from rnaos_platform.config.provider import ConfigProvider
from rnaos_platform.config.providers.memory_provider import MemoryProvider


class ConfigManager:
    """Centralized platform configuration manager."""

    def __init__(
        self,
        provider: ConfigProvider | None = None,
    ) -> None:
        self._provider = provider or MemoryProvider()

    def set(
        self,
        key: str,
        value: object,
    ) -> None:
        """Store a configuration value."""
        self._provider.set(
            key,
            value,
        )

    def get(
        self,
        key: str,
        default: object | None = None,
    ) -> object:
        """Retrieve a configuration value."""
        value = self._provider.get(key)

        if value is None:
            return default

        return value

    def exists(
        self,
        key: str,
    ) -> bool:
        """Check whether a configuration key exists."""
        return self._provider.exists(key)

    def remove(
        self,
        key: str,
    ) -> None:
        """Remove a configuration key."""
        self._provider.remove(key)

    def all(
        self,
    ) -> dict[str, object]:
        """Return all configuration values."""
        return self._provider.all()
