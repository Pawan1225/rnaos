from enterprise.validation import (
    ValidationSuite,
    default_platform_validators,
)


def test_default_platform_validators():
    validators = default_platform_validators()

    assert len(validators) == 10


def test_platform_validation():
    suite = ValidationSuite()

    for validator in default_platform_validators():
        suite.register(validator)

    report = suite.run_registered()

    assert report.total == 10
    assert report.passed == 10
    assert report.failed == 0
    assert report.success


def test_platform_statistics():
    suite = ValidationSuite()

    for validator in default_platform_validators():
        suite.register(validator)

    suite.run_registered()

    stats = suite.statistics()

    assert stats["total"] == 10
    assert stats["passed"] == 10
    assert stats["failed"] == 0
