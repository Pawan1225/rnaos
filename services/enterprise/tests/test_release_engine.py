from enterprise.release import (
    Release,
    ReleaseChannel,
    ReleaseResult,
    ReleaseStatus,
    ReleaseSuite,
)


class DummyRelease:
    @property
    def version(self) -> str:
        return "1.0.0"

    def release(self) -> ReleaseResult:
        return ReleaseResult(
            version=self.version,
            description="RNAOS Stable",
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.STABLE,
        )


def test_run_release():
    suite = ReleaseSuite()

    release: Release = DummyRelease()

    result = suite.run(release)

    assert result.version == "1.0.0"
    assert result.passed
    assert len(suite.results()) == 1


class ReleaseOne:
    @property
    def version(self) -> str:
        """Return the release version."""

        return "1.0.0"

    def release(self) -> ReleaseResult:
        """Execute release."""

        return ReleaseResult(
            version=self.version,
            description="Stable Release",
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.STABLE,
        )


class ReleaseTwo:
    @property
    def version(self) -> str:
        """Return the release version."""

        return "2.0.0"

    def release(self) -> ReleaseResult:
        """Execute release."""

        return ReleaseResult(
            version=self.version,
            description="LTS Release",
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.LTS,
        )


def test_run_all():
    suite = ReleaseSuite()

    suite.register(ReleaseOne())
    suite.register(ReleaseTwo())

    report = suite.run_all()

    assert report.total == 2
    assert report.passed == 2
    assert report.failed == 0


def test_statistics():
    suite = ReleaseSuite()

    suite.register(ReleaseOne())
    suite.register(ReleaseTwo())

    suite.run_all()

    stats = suite.statistics()

    assert stats["total"] == 2
    assert stats["passed"] == 2
    assert stats["failed"] == 0


def test_add_result():
    suite = ReleaseSuite()

    result = suite.run(
        DummyRelease(),
    )

    assert result.version == "1.0.0"
    assert result.passed
    assert len(suite.results()) == 1
