"""
Domain models for the RNAOS Enterprise Validation Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


class ValidationStatus(StrEnum):
    """Validation execution status."""

    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    WARNING = "warning"


class ValidationSeverity(StrEnum):
    """Validation severity."""

    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ValidationCategory(StrEnum):
    """Validation category."""

    UNIT = "unit"
    INTEGRATION = "integration"
    SYSTEM = "system"
    PERFORMANCE = "performance"
    SECURITY = "security"
    PLATFORM = "platform"


@dataclass(slots=True, frozen=True)
class ValidationResult:
    """Represents a single validation result."""

    name: str
    status: ValidationStatus
    category: ValidationCategory

    message: str = ""
    severity: ValidationSeverity = ValidationSeverity.MEDIUM
    duration: float = 0.0

    metadata: dict[str, object] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def passed(self) -> bool:
        """Return True if the validation passed."""

        return self.status is ValidationStatus.PASSED


@dataclass(slots=True)
class ValidationReport:
    """Validation report."""

    results: list[ValidationResult] = field(default_factory=list)

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def total(self) -> int:
        """Return total validations."""

        return len(self.results)

    @property
    def passed(self) -> int:
        """Return passed validations."""

        return sum(result.passed for result in self.results)

    @property
    def failed(self) -> int:
        """Return failed validations."""

        return sum(result.status is ValidationStatus.FAILED for result in self.results)

    @property
    def skipped(self) -> int:
        """Return skipped validations."""

        return sum(result.status is ValidationStatus.SKIPPED for result in self.results)

    @property
    def warnings(self) -> int:
        """Return warning validations."""

        return sum(result.status is ValidationStatus.WARNING for result in self.results)

    @property
    def success(self) -> bool:
        """Return True if there are no failed validations."""

        return self.failed == 0
