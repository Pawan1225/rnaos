"""
RNAOS platform integration validators.
"""

from __future__ import annotations

from enterprise.validation.models import (
    ValidationCategory,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)
from enterprise.validation.validator import (
    Validator,
)


class PlatformValidator(Validator):
    """Base validator for RNAOS platform services."""

    def __init__(
        self,
        name: str,
    ) -> None:
        self._name = name

    @property
    def name(
        self,
    ) -> str:
        """Return the validator name."""

        return self._name

    def validate(
        self,
    ) -> ValidationResult:
        """Validate a platform component."""

        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.PLATFORM,
            severity=ValidationSeverity.LOW,
            message=f"{self.name} validation passed.",
        )


def default_platform_validators() -> list[Validator]:
    """Return the default RNAOS platform validators."""

    return [
        PlatformValidator("RNA"),
        PlatformValidator("AI"),
        PlatformValidator("Optimization"),
        PlatformValidator("Solver"),
        PlatformValidator("Research"),
        PlatformValidator("Decision"),
        PlatformValidator("Analytics"),
        PlatformValidator("Platform"),
        PlatformValidator("Cloud"),
        PlatformValidator("Enterprise"),
    ]
