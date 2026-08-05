"""
RNAOS Enterprise Validation Engine.
"""

from __future__ import annotations

import time

from enterprise.validation.models import (
    ValidationCategory,
    ValidationReport,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)
from enterprise.validation.platform_validators import (
    default_platform_validators,
)
from enterprise.validation.registry import (
    ValidationRegistry,
)
from enterprise.validation.validator import (
    Validator,
)


class ValidationSuite:
    """Run platform validation."""

    def __init__(self) -> None:
        self._results: list[ValidationResult] = []
        self._registry = ValidationRegistry()

    def validate(
        self,
        name: str,
        condition: bool,
        *,
        category: ValidationCategory = ValidationCategory.UNIT,
        severity: ValidationSeverity = ValidationSeverity.MEDIUM,
        message: str = "",
        duration: float = 0.0,
        metadata: dict[str, object] | None = None,
    ) -> ValidationResult:
        """Record a validation result."""

        result = ValidationResult(
            name=name,
            status=(ValidationStatus.PASSED if condition else ValidationStatus.FAILED),
            category=category,
            severity=severity,
            message=message,
            duration=duration,
            metadata={} if metadata is None else dict(metadata),
        )

        self._results.append(result)

        return result

    def add_result(
        self,
        result: ValidationResult,
    ) -> None:
        """Add an existing validation result."""

        self._results.append(result)

    def register(
        self,
        validator: Validator,
    ) -> None:
        """Register a validator."""

        self._registry.register(validator)

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a validator."""

        self._registry.remove(name)

    def run(
        self,
        validator: Validator,
    ) -> ValidationResult:
        """Execute a validator and store its result."""

        start = time.perf_counter()

        try:
            result = validator.validate()

            duration = time.perf_counter() - start

            result.metadata["duration_seconds"] = duration

            self.add_result(result)

            return result

        except Exception as exc:
            duration = time.perf_counter() - start

            result = ValidationResult(
                name=validator.name,
                status=ValidationStatus.FAILED,
                category=ValidationCategory.SYSTEM,
                severity=ValidationSeverity.CRITICAL,
                message=str(exc),
                metadata={
                    "duration_seconds": duration,
                },
            )

            self.add_result(result)

            return result

    def run_all(
        self,
        validators: list[Validator],
    ) -> ValidationReport:
        """Execute all validators."""

        self.clear()

        for validator in validators:
            self.run(validator)

        return self.report()

    def validate_services(
        self,
        validators: list[Validator],
    ) -> ValidationReport:
        """Validate a collection of validators."""

        return self.run_all(validators)

    def validate_platform(
        self,
    ) -> ValidationReport:
        """Validate the complete RNAOS platform."""

        return self.validate_services(default_platform_validators())

    def validate_release(
        self,
    ) -> ValidationReport:
        """Validate release readiness."""

        return self.validate_platform()

    def run_registered(
        self,
    ) -> ValidationReport:
        """Run all registered validators."""

        self.clear()

        for validator in self._registry.items():
            self.run(validator)

        return self.report()

    def report(
        self,
    ) -> ValidationReport:
        """Generate a validation report."""

        return ValidationReport(
            results=list(self._results),
        )

    def clear(
        self,
    ) -> None:
        """Clear all validation results."""

        self._results.clear()

    def count(
        self,
    ) -> int:
        """Return the number of validation results."""

        return len(self._results)

    @property
    def results(
        self,
    ) -> tuple[ValidationResult, ...]:
        """Return immutable validation results."""

        return tuple(self._results)

    def statistics(
        self,
    ) -> dict[str, int]:
        """Return validation statistics."""

        report = self.report()

        return {
            "total": report.total,
            "passed": report.passed,
            "failed": report.failed,
            "skipped": report.skipped,
            "warnings": report.warnings,
        }
