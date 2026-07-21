from pathlib import Path

import pytest
from rna_intelligence.loaders.dataset_loader import (
    DatasetLoader,
)

TEST_DIR = Path(__file__).parent


def test_csv_loader():
    loader = DatasetLoader()

    dataset = loader.load(TEST_DIR / "sample.csv")

    assert dataset.name == "sample.csv"
    assert len(dataset.sequences) == 3

    assert dataset.sequences[0].sequence == "GGGAAAUCC"
    assert dataset.sequences[1].sequence == "AUGCGCGAA"
    assert dataset.sequences[2].sequence == "CCCGGGAAA"


def test_fasta_loader():
    loader = DatasetLoader()

    dataset = loader.load(TEST_DIR / "sample.fasta")

    assert dataset.name == "sample.fasta"
    assert len(dataset.sequences) == 3

    assert dataset.sequences[0].sequence == "GGGAAAUCC"
    assert dataset.sequences[1].sequence == "AUGCGCGAA"
    assert dataset.sequences[2].sequence == "CCCGGGAAA"


def test_missing_file():
    loader = DatasetLoader()

    with pytest.raises(FileNotFoundError):
        loader.load("missing.csv")


def test_invalid_extension(tmp_path):
    loader = DatasetLoader()

    invalid = tmp_path / "invalid.txt"
    invalid.write_text("RNA")

    with pytest.raises(ValueError):
        loader.load(invalid)
