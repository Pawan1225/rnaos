"""
RNAOS publication package model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PublicationPackage:
    """
    Immutable research publication package.
    """

    package_id: str

    title: str

    benchmark_version: str

    sections: tuple[str, ...]

    figures: tuple[str, ...]

    datasets: tuple[str, ...]

    version: str
