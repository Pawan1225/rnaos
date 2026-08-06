"""
RNAOS experiment utilities.
"""

from __future__ import annotations

import hashlib


def generate_experiment_id(
    dataset_version: str,
) -> str:
    """
    Generate a deterministic experiment identifier.

    Parameters
    ----------
    dataset_version
        Dataset version identifier.

    Returns
    -------
    str
        Deterministic experiment identifier.
    """
    digest = hashlib.sha256(
        dataset_version.encode(
            "utf-8",
        ),
    ).hexdigest()

    return f"exp_{digest}"
