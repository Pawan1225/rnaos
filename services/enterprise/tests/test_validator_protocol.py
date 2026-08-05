from enterprise.validation.models import (
    ValidationCategory,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)
from enterprise.validation.validator import Validator


class DummyValidator:
    @property
    def name(self) -> str:
        """Return the validator name."""

        return "Dummy"

    def validate(self) -> ValidationResult:
        """Execute validation."""

        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


def test_validator_protocol():
    validator: Validator = DummyValidator()

    result = validator.validate()

    assert validator.name == "Dummy"
    assert result.name == "Dummy"
    assert result.status is ValidationStatus.PASSED
    assert result.category is ValidationCategory.SYSTEM
    assert result.severity is ValidationSeverity.LOW
    assert result.passed
