"""
RNAOS experiment storage engine.
"""

from __future__ import annotations

import json
from pathlib import Path

from validation.models.experiment_record import (
    ExperimentRecord,
)


class ExperimentStorageEngine:
    """
    Stores validation experiments.
    """

    def save(
        self,
        record: ExperimentRecord,
        path: str,
    ) -> None:
        """
        Save experiment record.
        """

        file_path = Path(path)

        data = {
            "experiment_id": record.experiment_id,
            "sequence": record.rna_sequence,
            "vienna_energy": record.vienna_energy,
            "rnaos_energy": record.rnaos_energy,
            "energy_gap": record.energy_gap,
            "accuracy": record.accuracy,
            "solver": record.solver,
        }

        file_path.write_text(
            json.dumps(
                data,
                indent=4,
            ),
            encoding="utf-8",
        )

    def load(
        self,
        path: str,
    ) -> dict[str, object]:
        """
        Load experiment record.
        """

        return json.loads(
            Path(path).read_text(
                encoding="utf-8",
            )
        )
