from ai_intelligence.features.feature_engine import (
    FeatureEngineeringEngine,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_feature_engine():
    profiler = RNAProfiler()

    profile = profiler.profile("GGGAAAUCC")

    engine = FeatureEngineeringEngine()

    vector = engine.transform(profile)

    assert len(vector.values) == 8

    assert vector.values[0] == 9.0

    assert vector.feature_names == [
        "length",
        "gc_content",
        "au_content",
        "frequency_a",
        "frequency_u",
        "frequency_g",
        "frequency_c",
        "sequence_entropy",
    ]


def test_feature_names(rna_profile):
    vector = FeatureEngineeringEngine().transform(rna_profile)

    assert len(vector.feature_names) == vector.dimension


def test_feature_values_are_numeric(rna_profile):
    vector = FeatureEngineeringEngine().transform(rna_profile)

    assert all(isinstance(value, float) for value in vector.values)
