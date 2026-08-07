"""
Tests for refinement request.
"""

from __future__ import annotations

from dl.models.optimization.refinement_request import (
    RefinementRequest,
)


def test_refinement_request() -> None:
    """
    Refinement request can be created.
    """

    request = RefinementRequest(
        candidate_id=1,
        structure=(
            "A",
            "U",
            "G",
        ),
        current_energy=-45.2,
        strategy="local_search",
    )

    assert request.candidate_id == 1

    assert (
        len(
            request.structure,
        )
        == 3
    )

    assert request.current_energy == -45.2

    assert request.strategy == ("local_search")
