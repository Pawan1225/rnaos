from enterprise.release import release_manager


def test_end_to_end_release():
    report = release_manager()

    assert report.total == 10
    assert report.success
