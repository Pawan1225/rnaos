from rna_intelligence.parsers.sequence_parser import (
    RNASequenceParser,
)
from rna_intelligence.validators.sequence_validator import (
    RNASequenceValidator,
)


def test_valid_sequence():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    result = validator.validate(parser.parse("AUGCGC"))

    assert result.is_valid
    assert result.errors == []
    assert result.warnings == []


def test_invalid_nucleotide():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    rna = parser.parse("AUGCGX")

    result = validator.validate(rna)

    assert not result.is_valid
    assert any("Invalid nucleotide" in error for error in result.errors)


def test_lowercase_sequence():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    result = validator.validate(parser.parse("augc"))

    assert result.is_valid


def test_long_sequence():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    sequence = "A" * (validator.MAX_LENGTH + 1)

    result = validator.validate(parser.parse(sequence))

    assert not result.is_valid

    assert any("maximum length" in error for error in result.errors)


def test_low_gc_warning():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    result = validator.validate(parser.parse("AAAAAAA"))

    assert result.is_valid
    assert "Low GC content." in result.warnings


def test_high_gc_warning():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    result = validator.validate(parser.parse("GGGGGGG"))

    assert result.is_valid
    assert "High GC content." in result.warnings


def test_balanced_gc_content():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    result = validator.validate(parser.parse("AUGCGCAU"))

    assert result.is_valid
    assert result.warnings == []


def test_multiple_invalid_nucleotides():
    parser = RNASequenceParser()
    validator = RNASequenceValidator()

    rna = parser.parse("AUGXYZ")

    result = validator.validate(rna)

    assert not result.is_valid

    assert any("Invalid nucleotide" in error for error in result.errors)

    for nucleotide in ("X", "Y", "Z"):
        assert any(nucleotide in error for error in result.errors)
