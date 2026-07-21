"""
RNA Dataset Loader

Provides a unified interface for loading RNA datasets.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from rna_intelligence.parsers.sequence_parser import (
    RNASequence,
    RNASequenceParser,
)


@dataclass(slots=True)
class RNADataset:
    """Collection of RNA sequences."""

    name: str
    sequences: list[RNASequence]


class DatasetLoader:
    """Loads RNA datasets."""

    SUPPORTED_EXTENSIONS = {
        ".csv",
        ".fasta",
        ".fa",
    }

    def __init__(self) -> None:
        self.parser = RNASequenceParser()

    def load(self, path: str | Path) -> RNADataset:
        """
        Load an RNA dataset.

        Parameters
        ----------
        path : str | Path

        Returns
        -------
        RNADataset
        """

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported dataset format: {suffix}")

        sequences = self._load_csv(path) if suffix == ".csv" else self._load_fasta(path)

        return RNADataset(
            name=path.name,
            sequences=sequences,
        )

    def _load_csv(
        self,
        path: Path,
    ) -> list[RNASequence]:
        """Load RNA sequences from a CSV dataset."""

        sequences: list[RNASequence] = []

        with path.open(
            newline="",
            encoding="utf-8",
        ) as csv_file:
            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None or "sequence" not in reader.fieldnames:
                raise ValueError("CSV must contain a 'sequence' column.")

            for row in reader:
                sequence = row["sequence"].strip()

                if sequence:
                    sequences.append(self.parser.parse(sequence))

        return sequences

    def _load_fasta(
        self,
        path: Path,
    ) -> list[RNASequence]:
        """Load RNA sequences from a FASTA dataset."""

        sequences: list[RNASequence] = []
        current_sequence: list[str] = []

        with path.open(
            encoding="utf-8",
        ) as fasta_file:
            for line in fasta_file:
                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):
                    if current_sequence:
                        sequences.append(self.parser.parse("".join(current_sequence)))
                        current_sequence = []
                else:
                    current_sequence.append(line)

        if current_sequence:
            sequences.append(self.parser.parse("".join(current_sequence)))

        return sequences
