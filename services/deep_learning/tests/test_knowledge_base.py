"""
Tests for knowledge base.
"""

from __future__ import annotations

from dl.continuous_learning.knowledge.knowledge_base import (
    KnowledgeBase,
)
from dl.models.learning.knowledge_item import (
    KnowledgeItem,
)


def test_add_knowledge() -> None:
    """
    Knowledge can be stored.
    """

    database = KnowledgeBase()

    database.add(
        KnowledgeItem(
            knowledge_id="KNOW_001",
            category="solver",
            key="high_complexity",
            value="tensor_network",
            confidence=0.92,
        ),
    )

    assert (
        len(
            database.get_all(),
        )
        == 1
    )


def test_category_search() -> None:
    """
    Knowledge retrieval works.
    """

    database = KnowledgeBase()

    database.add(
        KnowledgeItem(
            knowledge_id="KNOW_001",
            category="solver",
            key="complex",
            value="hybrid",
            confidence=0.90,
        ),
    )

    results = database.get_by_category(
        "solver",
    )

    assert len(results) == 1
