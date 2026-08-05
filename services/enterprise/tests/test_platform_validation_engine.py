from enterprise.validation import ValidationSuite


def test_validate_platform():
    suite = ValidationSuite()

    report = suite.validate_platform()

    assert report.total == 10
    assert report.passed == 10
    assert report.success
