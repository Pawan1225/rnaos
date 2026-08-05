from enterprise.validation import (
    ValidationCategory,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
    ValidationSuite,
    Validator,
)


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


class ValidatorOne:
    @property
    def name(self) -> str:
        """Return the validator name."""
        return "One"

    def validate(self) -> ValidationResult:
        """Execute validation."""
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


class ValidatorTwo:
    @property
    def name(self) -> str:
        """Return the validator name."""
        return "Two"

    def validate(self) -> ValidationResult:
        """Execute validation."""
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


def test_add_result():
    suite = ValidationSuite()

    suite.add_result(
        ValidationResult(
            name="Manual",
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )
    )

    report = suite.report()

    assert report.total == 1
    assert report.passed == 1
    assert report.success


def test_run_validator():
    suite = ValidationSuite()

    validator: Validator = DummyValidator()

    result = suite.run(validator)

    assert result.name == "Dummy"
    assert result.status is ValidationStatus.PASSED

    report = suite.report()

    assert report.total == 1
    assert report.passed == 1
    assert report.success


def test_run_all():
    suite = ValidationSuite()

    report = suite.run_all(
        [
            ValidatorOne(),
            ValidatorTwo(),
        ]
    )

    assert report.total == 2
    assert report.passed == 2
    assert report.failed == 0
    assert report.success


def test_statistics():
    suite = ValidationSuite()

    suite.add_result(
        ValidationResult(
            name="One",
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )
    )

    suite.add_result(
        ValidationResult(
            name="Two",
            status=ValidationStatus.FAILED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.HIGH,
        )
    )

    stats = suite.statistics()

    assert stats["total"] == 2
    assert stats["passed"] == 1
    assert stats["failed"] == 1
    assert stats["skipped"] == 0
    assert stats["warnings"] == 0
