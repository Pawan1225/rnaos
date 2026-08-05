"""
RNA sequence validation utilities.
"""

from __future__ import annotations

from biology.utils.constants import RNA_NUCLEOTIDES


class InvalidRNASequenceError(ValueError):
    """
    Raised when an RNA sequence fails validation.
    """


def normalize_sequence(sequence: str) -> str:
    """
    Normalize an RNA sequence.

    Parameters
    ----------
    sequence
        Raw RNA sequence.

    Returns
    -------
    str
        Uppercase sequence with surrounding whitespace removed.
    """
    return sequence.strip().upper()


def validate_sequence(sequence: str) -> None:
    """
    Validate an RNA sequence.

    Parameters
    ----------
    sequence
        Normalized RNA sequence.

    Raises
    ------
    InvalidRNASequenceError
        If the sequence is invalid.
    """
    if not sequence:
        raise InvalidRNASequenceError("RNA sequence cannot be empty.")

    invalid = sorted(
        set(sequence) - RNA_NUCLEOTIDES,
    )

    if invalid:
        raise InvalidRNASequenceError(f"Invalid RNA nucleotides: {', '.join(invalid)}")


def is_valid_sequence(sequence: str) -> bool:
    """
    Check whether an RNA sequence is valid.

    Parameters
    ----------
    sequence
        RNA sequence.

    Returns
    -------
    bool
        True if valid, otherwise False.
    """
    try:
        normalized = normalize_sequence(sequence)
        validate_sequence(normalized)
    except InvalidRNASequenceError:
        return False

    return True
