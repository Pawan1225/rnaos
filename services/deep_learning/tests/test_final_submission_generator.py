"""
Tests for final submission generator.
"""

from __future__ import annotations

from dl.submission.engine.final_submission_generator import (
    FinalSubmissionGenerator,
)


def test_final_submission_generation() -> None:
    """
    Final submission profile is generated.
    """

    generator = FinalSubmissionGenerator()

    profile = generator.generate()

    assert profile.submission_id == ("FINAL_SUBMISSION_001")

    assert profile.version == ("1.0.0")

    assert "scientific_report" in profile.components

    assert profile.release_ready is True
