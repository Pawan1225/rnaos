"""
RNAOS RNA intelligence adapter.

Bridges RNAOS biological intelligence
with the deep learning platform.
"""

from __future__ import annotations

from typing import Any


class RNAAdapter:
    """
    Converts RNAOS biological representations
    into deep learning compatible inputs.
    """

    def convert_sequence(
        self,
        sequence: str,
    ) -> dict[str, Any]:
        """
        Convert RNA sequence into neural input format.
        """

        return {
            "sequence": sequence,
            "length": len(sequence),
        }

    def convert_profile(
        self,
        profile: Any,
    ) -> dict[str, Any]:
        """
        Convert RNA intelligence profile.

        This remains generic so the adapter
        can support future biological models.
        """

        return {
            "features": profile,
        }
