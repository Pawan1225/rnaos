from enterprise.validation import (
    ValidationCategory,
    ValidationSeverity,
    ValidationSuite,
)


def test_success():

    suite = ValidationSuite()

    suite.validate(
        "RNA",
        True,
    )

    report = suite.report()

    assert report.success

    assert report.total == 1

    assert report.passed == 1


def test_failure():

    suite = ValidationSuite()

    suite.validate(
        "Cloud",
        False,
    )

    report = suite.report()

    assert not report.success

    assert report.failed == 1


def test_clear():

    suite = ValidationSuite()

    suite.validate(
        "RNA",
        True,
    )

    suite.clear()

    assert suite.count() == 0


def test_add_result():

    suite = ValidationSuite()

    result = suite.validate(
        "Analytics",
        True,
    )

    assert suite.results[0] == result


def test_metadata():

    suite = ValidationSuite()

    result = suite.validate(
        "Platform",
        True,
        category=ValidationCategory.PLATFORM,
        severity=ValidationSeverity.HIGH,
        duration=1.25,
        metadata={
            "version": "1.0.0",
        },
    )

    assert result.category is ValidationCategory.PLATFORM

    assert result.severity is ValidationSeverity.HIGH

    assert result.duration == 1.25

    assert result.metadata["version"] == "1.0.0"


def test_multiple_results():

    suite = ValidationSuite()

    suite.validate("One", True)

    suite.validate("Two", False)

    suite.validate("Three", True)

    assert suite.count() == 3

    report = suite.report()

    assert report.total == 3

    assert report.passed == 2

    assert report.failed == 1
