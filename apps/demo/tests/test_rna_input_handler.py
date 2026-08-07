"""
Tests for RNA input handler.
"""

import pytest

from apps.demo.demo_engine.rna_input_handler import (
    RNAInputHandler,
)


def test_valid_rna_input():

    handler = RNAInputHandler()

    result = handler.validate("ggcau")

    assert result == "GGCAU"


def test_invalid_rna_input():

    handler = RNAInputHandler()

    with pytest.raises(ValueError):
        handler.validate("GGCTX")


def test_empty_rna_input():

    handler = RNAInputHandler()

    with pytest.raises(ValueError):
        handler.validate("")
