"""
Tests for benchmark adapter interface.
"""

from __future__ import annotations

import pytest
from dl.benchmark.adapters.base_adapter import (
    BenchmarkAdapter,
)


def test_adapter_is_abstract() -> None:
    """
    Base adapter cannot be instantiated.
    """

    with pytest.raises(
        TypeError,
    ):
        BenchmarkAdapter()
