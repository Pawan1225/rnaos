from enterprise.validation import (
    ValidationCategory,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
    ValidationSuite,
)


class DummyValidator:
    @property
    def name(self) -> str:
        return "Dummy"

    def validate(self) -> ValidationResult:
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


def test_validate_services():
    suite = ValidationSuite()

    report = suite.validate_services([DummyValidator()])

    assert report.total == 1
    assert report.passed == 1
    assert report.success
