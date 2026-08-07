"""
RNAOS documentation generator.
"""

from __future__ import annotations

from dl.models.submission.documentation_manifest import (
    DocumentationManifest,
)


class DocumentationGenerator:
    """
    Generates documentation manifests.
    """

    def generate(
        self,
    ) -> DocumentationManifest:
        """
        Create documentation package definition.
        """

        return DocumentationManifest(
            documentation_id="DOC_001",
            version="1.0.0",
            sections=(
                "README",
                "INSTALLATION",
                "ARCHITECTURE",
                "DEVELOPER_GUIDE",
                "API_REFERENCE",
            ),
            files=(
                "README.md",
                "installation.md",
                "architecture.md",
                "developer_guide.md",
                "api_reference.md",
            ),
            generator=("DocumentationGenerator"),
            metadata=("release=RNAOS_v1",),
        )
