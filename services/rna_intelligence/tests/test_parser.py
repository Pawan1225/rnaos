import pytest
from rna_intelligence.parsers.sequence_parser import (
    RNASequenceParser,
)


def test_parser():
    parser = RNASequenceParser()

    sequence = parser.parse("AUGCGC")

    assert sequence.sequence == "AUGCGC"
    assert sequence.length == 6


def test_lowercase_sequence():
    parser = RNASequenceParser()

    sequence = parser.parse("augc")

    assert sequence.sequence == "AUGC"
    assert sequence.length == 4


def test_whitespace_sequence():
    parser = RNASequenceParser()

    sequence = parser.parse("   AUGC   ")

    assert sequence.sequence == "AUGC"
    assert sequence.length == 4


def test_empty_sequence():
    parser = RNASequenceParser()

    with pytest.raises(
        ValueError,
        match="Sequence cannot be empty.",
    ):
        parser.parse("")


def test_whitespace_only_sequence():
    parser = RNASequenceParser()

    with pytest.raises(
        ValueError,
        match="Sequence cannot be empty.",
    ):
        parser.parse("      ")


def test_none_sequence():
    parser = RNASequenceParser()

    with pytest.raises(
        ValueError,
        match="Sequence cannot be None.",
    ):
        parser.parse(None)
