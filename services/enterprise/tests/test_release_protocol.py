from enterprise.release import (
    Release,
    ReleaseChannel,
    ReleaseResult,
    ReleaseStatus,
)


class DummyRelease:
    @property
    def version(self) -> str:
        """Return the release version."""

        return "1.0.0"

    def release(self) -> ReleaseResult:
        """Execute the release."""

        return ReleaseResult(
            version=self.version,
            description="RNAOS Release",
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.STABLE,
        )


def test_release_protocol():
    release: Release = DummyRelease()

    result = release.release()

    assert release.version == "1.0.0"
    assert result.version == "1.0.0"
    assert result.status is ReleaseStatus.PASSED
    assert result.channel is ReleaseChannel.STABLE
    assert result.passed
