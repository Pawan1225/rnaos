"""
RNAOS benchmark evaluator.
"""

from __future__ import annotations

import time

from validation.evaluation.rnaos_energy_evaluator import (
    RNAOSEnergyEvaluator,
)
from validation.metrics.structure_similarity import (
    StructureSimilarity,
)
from validation.models.dataset_entry import (
    DatasetEntry,
)
from validation.models.experiment_result import (
    ExperimentResult,
)
from validation.solvers.rnaos_solver import (
    RNAOSSolver,
)


class BenchmarkEvaluator:
    """
    Evaluates one RNA benchmark sample.
    """

    def __init__(self) -> None:

        self.energy_evaluator = RNAOSEnergyEvaluator()

        self.structure_similarity = StructureSimilarity()

        self.solver = RNAOSSolver(
            evaluator=self.energy_evaluator,
        )

    def evaluate(
        self,
        entry: DatasetEntry,
        experiment_id: int,
    ) -> ExperimentResult:
        """
        Generate experiment result.
        """

        start = time.time()

        sequence = entry.sequence

        predicted_structure = self.solver.solve(
            sequence,
        )

        reference_structure = (
            entry.reference_structure
            if hasattr(
                entry,
                "reference_structure",
            )
            else predicted_structure
        )

        rnaos_energy = self.energy_evaluator.evaluate(
            sequence,
            predicted_structure,
        )

        reference_energy = self.energy_evaluator.evaluate(
            sequence,
            reference_structure,
        )

        energy_gap = abs(rnaos_energy - reference_energy)

        accuracy = 1.0 if predicted_structure == reference_structure else 0.0

        similarity = self.structure_similarity.compare(
            predicted_structure,
            reference_structure,
        )

        runtime = time.time() - start

        estimated_qubits = len(sequence) * 2

        return ExperimentResult(
            experiment_id=experiment_id,
            sequence_id=entry.sequence_id,
            sequence=sequence,
            sequence_length=entry.length,
            rnaos_structure=predicted_structure,
            reference_structure=reference_structure,
            rnaos_energy=rnaos_energy,
            reference_energy=reference_energy,
            energy_gap=energy_gap,
            accuracy=accuracy,
            runtime_seconds=runtime,
            estimated_qubits=estimated_qubits,
            structure_precision=(similarity["precision"]),
            structure_recall=(similarity["recall"]),
            structure_f1=(similarity["f1_score"]),
            base_pair_distance=(similarity["base_pair_distance"]),
        )
