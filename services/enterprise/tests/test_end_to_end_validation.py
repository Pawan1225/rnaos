import json

from enterprise.validation import (
    ValidationReportRenderer,
    ValidationSuite,
)


def test_end_to_end_validation():
    suite = ValidationSuite()

    report = suite.validate_release()

    renderer = ValidationReportRenderer()

    json_report = renderer.render_json(report)
    markdown_report = renderer.render_markdown(report)
    summary = renderer.render_summary(report)

    data = json.loads(json_report)

    assert report.success

    assert data["success"] is True
    assert data["total"] == 10

    assert "# RNAOS Validation Report" in markdown_report

    assert "10/10" in summary
