from rna_intelligence.features.feature_extractor import (
    FeatureExtractor,
)
from rna_intelligence.parsers.sequence_parser import (
    RNASequenceParser,
)


def test_feature_extraction():
    parser = RNASequenceParser()
    extractor = FeatureExtractor()

    rna = parser.parse("GGGAAAUCC")

    features = extractor.extract(rna)

    assert features.length == 9

    assert features.base_counts["G"] == 3
    assert features.base_counts["A"] == 3
    assert features.base_counts["U"] == 1
    assert features.base_counts["C"] == 2

    assert abs(features.gc_content - (5 / 9)) < 1e-6
    assert abs(features.au_content - (4 / 9)) < 1e-6

    assert features.nucleotide_frequencies["G"] == 3 / 9
    assert features.nucleotide_frequencies["A"] == 3 / 9
    assert features.nucleotide_frequencies["U"] == 1 / 9
    assert features.nucleotide_frequencies["C"] == 2 / 9

    assert features.sequence_entropy > 0
