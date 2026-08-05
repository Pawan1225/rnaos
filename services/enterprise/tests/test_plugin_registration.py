from enterprise.validation import (
    ValidationCategory,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
    ValidationSuite,
)


class ValidatorOne:
    @property
    def name(self) -> str:
        return "One"

    def validate(self) -> ValidationResult:
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


class ValidatorTwo:
    @property
    def name(self) -> str:
        return "Two"

    def validate(self) -> ValidationResult:
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


def test_register():
    suite = ValidationSuite()

    suite.register(ValidatorOne())

    assert suite._registry.exists("One")


def test_unregister():
    suite = ValidationSuite()

    suite.register(ValidatorOne())

    suite.unregister("One")

    assert not suite._registry.exists("One")


def test_run_registered():
    suite = ValidationSuite()

    suite.register(ValidatorOne())

    report = suite.run_registered()

    assert report.total == 1
    assert report.passed == 1
    assert report.success


def test_run_multiple_registered():
    suite = ValidationSuite()

    suite.register(ValidatorOne())
    suite.register(ValidatorTwo())

    report = suite.run_registered()

    assert report.total == 2
    assert report.passed == 2
    assert report.failed == 0
    assert report.success
