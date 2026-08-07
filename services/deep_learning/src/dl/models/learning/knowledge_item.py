"""
RNAOS learned knowledge item.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class KnowledgeItem:
    """
    Immutable learned knowledge record.
    """

    knowledge_id: str

    category: str

    key: str

    value: str

    confidence: float
