"""
Validator protocol for the RNAOS Enterprise Validation Framework.
"""

from __future__ import annotations

from typing import Protocol

from enterprise.validation.models import ValidationResult


class Validator(Protocol):
    """Protocol implemented by all validation plugins."""

    @property
    def name(self) -> str:
        """Return the validator name."""
        ...

    def validate(self) -> ValidationResult:
        """Execute validation."""
        ...
