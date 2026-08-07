"""
Tests for quantum-inspired feature mapper.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.quantum_feature import (
    QuantumFeatureVector,
)
from dl.optimization.quantum_feature_mapper import (
    QuantumFeatureMapper,
)


def test_feature_mapping() -> None:
    """
    Embedding is mapped.
    """

    mapper = QuantumFeatureMapper()

    result = mapper.map(
        (
            1.0,
            1.0,
        ),
    )

    assert isinstance(
        result,
        QuantumFeatureVector,
    )

    assert result.dimension == 2

    assert (
        round(
            result.normalization,
            4,
        )
        == 1.4142
    )


def test_empty_embedding_fails() -> None:
    """
    Empty embedding is invalid.
    """

    mapper = QuantumFeatureMapper()

    with pytest.raises(
        ValueError,
    ):
        mapper.map(
            (),
        )
