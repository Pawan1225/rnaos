"""
RNA Sequence Validator

Responsible for validating RNA sequences before they enter
the RNAOS analysis pipeline.
"""

from dataclasses import dataclass, field

from rna_intelligence.parsers.sequence_parser import RNASequence


@dataclass(slots=True)
class ValidationResult:
    """Represents the result of RNA sequence validation."""

    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class RNASequenceValidator:
    """Validates RNA sequences."""

    VALID_BASES = {"A", "U", "G", "C"}

    MIN_LENGTH = 1
    MAX_LENGTH = 100_000

    LOW_GC_THRESHOLD = 0.20
    HIGH_GC_THRESHOLD = 0.80

    def validate(self, rna: RNASequence) -> ValidationResult:
        """
        Validate an RNASequence object.

        Parameters
        ----------
        rna : RNASequence

        Returns
        -------
        ValidationResult
        """

        errors: list[str] = []
        warnings: list[str] = []

        if rna.length < self.MIN_LENGTH:
            errors.append("RNA sequence is empty.")

        if rna.length > self.MAX_LENGTH:
            errors.append(f"RNA sequence exceeds maximum length ({self.MAX_LENGTH}).")

        invalid = sorted(set(rna.sequence) - self.VALID_BASES)

        if invalid:
            errors.append(f"Invalid nucleotide(s): {', '.join(invalid)}")

        if rna.length > 0:
            gc_content = (rna.sequence.count("G") + rna.sequence.count("C")) / rna.length

            if gc_content < self.LOW_GC_THRESHOLD:
                warnings.append("Low GC content.")

            if gc_content > self.HIGH_GC_THRESHOLD:
                warnings.append("High GC content.")

        return ValidationResult(
            is_valid=not errors,
            errors=errors,
            warnings=warnings,
        )
