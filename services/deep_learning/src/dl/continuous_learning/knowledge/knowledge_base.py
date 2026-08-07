"""
RNAOS knowledge base.
"""

from __future__ import annotations

from dl.models.learning.knowledge_item import (
    KnowledgeItem,
)


class KnowledgeBase:
    """
    Stores learned optimization knowledge.
    """

    def __init__(self) -> None:
        self._knowledge: list[KnowledgeItem] = []

    def add(
        self,
        item: KnowledgeItem,
    ) -> None:
        """
        Store knowledge item.
        """

        self._knowledge.append(
            item,
        )

    def get_all(
        self,
    ) -> tuple[
        KnowledgeItem,
        ...,
    ]:
        """
        Return all knowledge.
        """

        return tuple(
            self._knowledge,
        )

    def get_by_category(
        self,
        category: str,
    ) -> tuple[
        KnowledgeItem,
        ...,
    ]:
        """
        Retrieve knowledge by category.
        """

        return tuple(item for item in self._knowledge if item.category == category)
