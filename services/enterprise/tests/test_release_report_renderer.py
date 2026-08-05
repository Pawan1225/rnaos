from enterprise.release import (
    ReleaseChannel,
    ReleaseReport,
    ReleaseReportRenderer,
    ReleaseResult,
    ReleaseStatus,
)


def sample_report() -> ReleaseReport:
    return ReleaseReport(
        releases=[
            ReleaseResult(
                version="1.0.0",
                description="RNAOS Stable",
                status=ReleaseStatus.PASSED,
                channel=ReleaseChannel.STABLE,
            ),
        ]
    )


def test_render_json():
    renderer = ReleaseReportRenderer()

    output = renderer.render_json(
        sample_report(),
    )

    assert '"total": 1' in output
    assert '"passed": 1' in output


def test_render_markdown():
    renderer = ReleaseReportRenderer()

    output = renderer.render_markdown(
        sample_report(),
    )

    assert "# Release Report" in output
    assert "Total:" in output


def test_render_summary():
    renderer = ReleaseReportRenderer()

    output = renderer.render_summary(
        sample_report(),
    )

    assert "1/1 releases passed" in output
