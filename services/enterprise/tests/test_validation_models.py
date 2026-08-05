from enterprise.validation import (
    ValidationCategory,
    ValidationReport,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)


def test_result_defaults():

    result = ValidationResult(
        name="RNA",
        status=ValidationStatus.PASSED,
        category=ValidationCategory.UNIT,
    )

    assert result.passed

    assert result.severity == ValidationSeverity.MEDIUM


def test_failed_result():

    result = ValidationResult(
        name="Cloud",
        status=ValidationStatus.FAILED,
        category=ValidationCategory.INTEGRATION,
    )

    assert not result.passed


def test_report_counts():

    report = ValidationReport(
        results=[
            ValidationResult(
                name="One",
                status=ValidationStatus.PASSED,
                category=ValidationCategory.UNIT,
            ),
            ValidationResult(
                name="Two",
                status=ValidationStatus.FAILED,
                category=ValidationCategory.SYSTEM,
            ),
            ValidationResult(
                name="Three",
                status=ValidationStatus.SKIPPED,
                category=ValidationCategory.SECURITY,
            ),
            ValidationResult(
                name="Four",
                status=ValidationStatus.WARNING,
                category=ValidationCategory.PERFORMANCE,
            ),
        ]
    )

    assert report.total == 4

    assert report.passed == 1

    assert report.failed == 1

    assert report.skipped == 1

    assert report.warnings == 1

    assert not report.success
