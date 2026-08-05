from enterprise.validation import ValidationSuite


def test_validate_release():
    suite = ValidationSuite()

    report = suite.validate_release()

    assert report.total == 10
    assert report.passed == 10
    assert report.success
