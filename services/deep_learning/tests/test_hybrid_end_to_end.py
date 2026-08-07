"""
End-to-end hybrid optimization validation.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_request import (
    HybridOptimizationRequest,
)
from dl.models.optimization.hybrid_solution import (
    HybridSolution,
)
from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)
from dl.optimization.runtime.hybrid_optimizer import (
    HybridOptimizationEngine,
)


def test_hybrid_end_to_end() -> None:
    """
    Complete RNAOS hybrid optimization workflow.
    """

    pipeline = OptimizationPipeline(
        pipeline_id=100,
        name="rna_hybrid_pipeline",
        stages=(
            OptimizationStage(
                stage_id=1,
                name="exploration",
                solver_name="genetic",
                priority=1,
                status="pending",
            ),
            OptimizationStage(
                stage_id=2,
                name="energy_optimization",
                solver_name="annealing",
                priority=2,
                status="pending",
            ),
            OptimizationStage(
                stage_id=3,
                name="refinement",
                solver_name="local_search",
                priority=3,
                status="pending",
            ),
        ),
        status="pending",
    )

    request = HybridOptimizationRequest(
        request_id=100,
        problem_id="rna_structure_001",
        pipeline=pipeline,
        target_accuracy=0.98,
        priority=1,
        status="pending",
    )

    engine = HybridOptimizationEngine()

    solution = engine.optimize(
        request,
    )

    assert isinstance(
        solution,
        HybridSolution,
    )

    assert solution.success is True

    assert solution.objective_score == 0.98
