"""
RNA Profiling Engine

High-level orchestration for RNA sequence analysis.
"""

from dataclasses import dataclass

from rna_intelligence.features.feature_extractor import (
    FeatureExtractor,
    RNAFeatures,
)
from rna_intelligence.parsers.sequence_parser import (
    RNASequence,
    RNASequenceParser,
)
from rna_intelligence.validators.sequence_validator import (
    RNASequenceValidator,
    ValidationResult,
)


@dataclass(slots=True)
class RNAProfile:
    """Complete RNA analysis result."""

    sequence: RNASequence
    validation: ValidationResult
    features: RNAFeatures


class RNAProfiler:
    """High-level RNA analysis pipeline."""

    def __init__(self) -> None:
        self.parser = RNASequenceParser()
        self.validator = RNASequenceValidator()
        self.extractor = FeatureExtractor()

    def profile(self, sequence: str) -> RNAProfile:
        """
        Analyze an RNA sequence by parsing, validating,
        and extracting biological features.
        """

        # Step 1: Parse the raw sequence
        rna = self.parser.parse(sequence)

        # Step 2: Validate the parsed sequence
        validation = self.validator.validate(rna)

        if not validation.is_valid:
            raise ValueError("RNA sequence validation failed: " + "; ".join(validation.errors))

        # Step 3: Extract biological features
        features = self.extractor.extract(rna)

        # Step 4: Return the complete profile
        return RNAProfile(
            sequence=rna,
            validation=validation,
            features=features,
        )
