from enterprise.release import release_platform


def test_release_platform():
    report = release_platform()

    assert report.total == 10
    assert report.success
