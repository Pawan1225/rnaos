"""
Validation registry for the RNAOS Enterprise Validation Framework.
"""

from __future__ import annotations

from enterprise.validation.validator import Validator


class ValidationRegistry:
    """Registry of platform validators."""

    def __init__(self) -> None:
        self._validators: dict[str, Validator] = {}

    def register(
        self,
        validator: Validator,
    ) -> None:
        """Register a validator."""

        self._validators[validator.name] = validator

    def get(
        self,
        name: str,
    ) -> Validator | None:
        """Return a validator."""

        return self._validators.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a validator exists."""

        return name in self._validators

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a validator."""

        self._validators.pop(name, None)

    def clear(
        self,
    ) -> None:
        """Clear the registry."""

        self._validators.clear()

    def list_validators(
        self,
    ) -> list[str]:
        """Return registered validator names."""

        return sorted(self._validators)

    def items(
        self,
    ) -> tuple[Validator, ...]:
        """Return registered validators."""

        return tuple(self._validators[name] for name in sorted(self._validators))

    def count(
        self,
    ) -> int:
        """Return number of registered validators."""

        return len(self._validators)
