#!/usr/bin/env python3

"""
RNAOS Repository Initializer

Creates the complete project directory structure and placeholder files.

Run:
    python scripts/bootstrap/init_repository.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DIRECTORIES = [
    "apps/backend",
    "apps/frontend",
    "apps/dashboard",
    "apps/admin",
    "packages/core",
    "packages/common",
    "packages/config",
    "packages/database",
    "packages/logging",
    "packages/schemas",
    "services/aoie",
    "services/optimization",
    "services/quantum",
    "services/ai",
    "services/reflection",
    "services/repository",
    "services/analytics",
    "services/reasoning",
    "services/hypothesis",
    "research/papers",
    "research/benchmarks",
    "research/notebooks",
    "research/reports",
    "research/references",
    "research/datasets",
    "experiments",
    "artifacts/experiments",
    "artifacts/models",
    "artifacts/reports",
    "artifacts/figures",
    "artifacts/circuits",
    "artifacts/exports",
    "data/raw",
    "data/processed",
    "data/external",
    "data/cache",
    "docs/architecture",
    "docs/adr",
    "docs/api",
    "docs/sprint",
    "docs/setup",
    "docs/development",
    "docs/deployment",
    "docs/diagrams",
    "deployment/docker",
    "deployment/kubernetes",
    "deployment/scripts",
    "scripts/setup",
    "scripts/development",
    "scripts/release",
    "scripts/verify",
    "tests/unit",
    "tests/integration",
    "tests/api",
    "tests/frontend",
    "tests/benchmark",
    ".github/workflows",
    "tools",
]

FILES = {
    ".env.example": "# Environment variables\n",
    "docker-compose.yml": "# Docker Compose configuration\n",
    "Makefile": "# RNAOS Makefile\n",
    ".gitignore": "",
}

GITKEEP_DIRS = [
    "experiments",
    "artifacts/experiments",
    "artifacts/models",
    "artifacts/reports",
    "artifacts/figures",
    "artifacts/circuits",
    "artifacts/exports",
    "data/raw",
    "data/processed",
    "data/external",
    "data/cache",
]


def create_directories():
    for directory in DIRECTORIES:
        path = ROOT / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {directory}")


def create_gitkeeps():
    for directory in GITKEEP_DIRS:
        gitkeep = ROOT / directory / ".gitkeep"
        gitkeep.touch(exist_ok=True)


def create_files():
    for filename, content in FILES.items():
        file = ROOT / filename
        if not file.exists():
            file.write_text(content)
            print(f"[FILE] {filename}")


def main():
    print("\nRNAOS Repository Initializer\n")

    create_directories()
    create_gitkeeps()
    create_files()

    print("\nRepository initialized successfully.")


if __name__ == "__main__":
    main()
