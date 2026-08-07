"""
Tests for result comparison engine.
"""

from validation.analyzers.result_comparison_engine import (
    ResultComparisonEngine,
)
from validation.models.rnaos_result import (
    RNAOSResult,
)
from validation.models.vienna_reference import (
    ViennaReference,
)


def test_result_comparison() -> None:
    """
    Comparison metrics are generated.
    """

    engine = ResultComparisonEngine()

    reference = ViennaReference(
        sequence="AUGCUA",
        structure="......",
        mfe_energy=-1.5,
        length=6,
        engine="ViennaRNA",
        version="2.x",
    )

    result = RNAOSResult(
        sequence="AUGCUA",
        structure="......",
        energy=-1.2,
        solver="hybrid_quantum_inspired",
        runtime=1.0,
        qubit_estimate=6,
        variable_count=12,
        iterations=100,
        version="1.0.0",
    )

    comparison = engine.compare(
        reference,
        result,
    )

    assert comparison.structure_accuracy == 1.0

    assert comparison.energy_gap == 0.3

    assert comparison.overall_score > 0
