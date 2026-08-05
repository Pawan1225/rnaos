from enterprise.release import release_services


def test_release_services():
    report = release_services()

    assert report.total == 10
    assert report.passed == 10
    assert report.failed == 0
