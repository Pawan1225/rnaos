import json

from enterprise.validation import (
    ValidationCategory,
    ValidationReport,
    ValidationReportRenderer,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)


def make_report() -> ValidationReport:
    """Create a sample validation report."""

    report = ValidationReport()

    report.results.append(
        ValidationResult(
            name="RNA",
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )
    )

    report.results.append(
        ValidationResult(
            name="Cloud",
            status=ValidationStatus.FAILED,
            category=ValidationCategory.PLATFORM,
            severity=ValidationSeverity.HIGH,
            message="Connection timeout",
        )
    )

    return report


def test_render_json():
    renderer = ValidationReportRenderer()

    report = make_report()

    data = json.loads(renderer.render_json(report))

    assert data["total"] == 2
    assert data["passed"] == 1
    assert data["failed"] == 1
    assert data["success"] is False


def test_render_markdown():
    renderer = ValidationReportRenderer()

    report = make_report()

    markdown = renderer.render_markdown(report)

    assert "# RNAOS Validation Report" in markdown
    assert "Total: 2" in markdown
    assert "Passed: 1" in markdown
    assert "Failed: 1" in markdown


def test_render_summary():
    renderer = ValidationReportRenderer()

    report = make_report()

    summary = renderer.render_summary(report)

    assert "1/2" in summary
    assert "1 failed" in summary
