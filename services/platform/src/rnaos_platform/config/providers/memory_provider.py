"""
In-memory configuration provider.
"""

from __future__ import annotations

from rnaos_platform.config.provider import ConfigProvider


class MemoryProvider(ConfigProvider):
    """Store configuration values in memory."""

    def __init__(self) -> None:
        self._config: dict[str, object] = {}

    def get(
        self,
        key: str,
    ) -> object | None:
        """Retrieve a configuration value."""
        return self._config.get(key)

    def set(
        self,
        key: str,
        value: object,
    ) -> None:
        """Store a configuration value."""
        self._config[key] = value

    def exists(
        self,
        key: str,
    ) -> bool:
        """Check whether a configuration key exists."""
        return key in self._config

    def remove(
        self,
        key: str,
    ) -> None:
        """Remove a configuration key."""
        self._config.pop(key, None)

    def all(
        self,
    ) -> dict[str, object]:
        """Return a copy of all configuration values."""
        return dict(self._config)
