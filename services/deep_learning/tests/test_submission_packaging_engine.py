"""
Tests for submission packaging engine.
"""

from __future__ import annotations

from dl.submission.packaging.submission_packaging_engine import (
    SubmissionPackagingEngine,
)


def test_submission_package_creation() -> None:
    """
    Submission manifest is generated.
    """

    engine = SubmissionPackagingEngine()

    manifest = engine.build()

    assert manifest.submission_id == ("SUBMISSION_001")

    assert "scientific_report" in manifest.artifacts

    assert "presentation" in manifest.directories

    assert manifest.version == ("1.0.0")
