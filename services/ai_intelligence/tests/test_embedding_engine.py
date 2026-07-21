from ai_intelligence.embeddings.embedding_engine import (
    RNAEmbeddingEngine,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_embedding():
    profiler = RNAProfiler()

    profile = profiler.profile("GGGAAAUCC")

    engine = RNAEmbeddingEngine()

    embedding = engine.embed(profile)

    assert embedding.dimension == 8

    assert embedding.model_name == "rnaos-feature-embedding-v1"

    assert embedding.vector[0] == 9.0


def test_embedding_dimension(rna_profile):
    embedding = RNAEmbeddingEngine().embed(rna_profile)

    assert embedding.dimension == len(embedding.vector)


def test_embedding_is_deterministic(rna_profile):
    engine = RNAEmbeddingEngine()

    embedding_one = engine.embed(rna_profile)
    embedding_two = engine.embed(rna_profile)

    assert embedding_one.vector == embedding_two.vector
