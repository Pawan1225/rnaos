"""
Tests for result collection engine.
"""

from validation.storage.result_collection_engine import (
    ResultCollectionEngine,
)


def test_result_collection():

    engine = ResultCollectionEngine()

    summary = engine.collect(50)

    assert summary.collection_id == ("COLLECTION_V1")

    assert summary.total_results == 50

    assert summary.stored_results == 50

    assert summary.failed_results == 0

    assert summary.benchmark_version == ("1.0.0")
