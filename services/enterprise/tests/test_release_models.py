from enterprise.release import (
    ReleaseArtifact,
    ReleaseChannel,
    ReleaseReport,
    ReleaseResult,
    ReleaseStatus,
)


def test_result_defaults():
    result = ReleaseResult(
        version="1.0.0",
        description="RNAOS",
        status=ReleaseStatus.PASSED,
        channel=ReleaseChannel.STABLE,
    )

    assert result.passed
    assert result.version == "1.0.0"


def test_failed_result():
    result = ReleaseResult(
        version="0.9.0",
        description="Beta",
        status=ReleaseStatus.FAILED,
        channel=ReleaseChannel.BETA,
    )

    assert not result.passed


def test_report_counts():
    report = ReleaseReport(
        releases=[
            ReleaseResult(
                version="1.0.0",
                description="Stable",
                status=ReleaseStatus.PASSED,
                channel=ReleaseChannel.STABLE,
            ),
            ReleaseResult(
                version="0.9.0",
                description="Beta",
                status=ReleaseStatus.FAILED,
                channel=ReleaseChannel.BETA,
            ),
        ]
    )

    assert report.total == 2
    assert report.passed == 1
    assert report.failed == 1
    assert not report.success


def test_release_artifact():
    artifact = ReleaseArtifact(
        name="wheel",
        path="dist/rnaos.whl",
    )

    assert artifact.name == "wheel"
    assert artifact.path == "dist/rnaos.whl"
