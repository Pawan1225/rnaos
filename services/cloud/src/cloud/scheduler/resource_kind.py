"""
Supported compute resource kinds.
"""

from __future__ import annotations

from enum import StrEnum


class ResourceKind(StrEnum):
    """Supported execution resource types."""

    CPU = "cpu"

    GPU = "gpu"

    QPU = "qpu"

    FPGA = "fpga"

    TPU = "tpu"
