from enterprise.release import (
    PlatformRelease,
    ReleaseSuite,
    default_platform_releases,
)


def test_default_platform_releases():
    releases = default_platform_releases()

    assert len(releases) == 10


def test_platform_release():
    release = PlatformRelease(
        version="1.0.0",
        description="RNAOS Stable",
    )

    result = release.release()

    assert result.version == "1.0.0"
    assert result.description == "RNAOS Stable"
    assert result.passed


def test_platform_statistics():
    suite = ReleaseSuite()

    for release in default_platform_releases():
        suite.register(release)

    report = suite.run_all()

    assert report.total == 10
    assert report.passed == 10
    assert report.failed == 0
