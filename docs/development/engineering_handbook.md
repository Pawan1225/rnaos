# RNAOS Engineering Handbook

Version: 1.0

Status: Locked

---

# Purpose

This handbook defines the engineering standards, workflows, and best practices for developing RNAOS.

Every contributor should follow these guidelines to ensure consistency, maintainability, and production-quality software.

---

# Engineering Principles

- Simplicity over complexity
- Readability over cleverness
- Explicit over implicit
- Modularity by default
- Reproducibility first
- Documentation alongside implementation
- Test every important feature

---

# Repository Structure

The repository follows a hybrid monorepo architecture.

Top-level directories:

- apps/
- services/
- packages/
- platform/
- contracts/
- configs/
- research/
- experiments/
- artifacts/
- docs/
- tests/

No new top-level directories should be introduced without an ADR.

---

# Git Workflow

Main branches:

- main
- develop
- feature/*
- hotfix/*
- release/*

Never commit directly to main.

---

# Commit Message Convention

Format:

type: short description

Examples:

docs: add engineering handbook

feat: implement RNA parser

fix: resolve API validation bug

refactor: simplify AOIE planner

test: add RNA parser tests

---

# Coding Standards

Python

- Python 3.11+
- Type hints required
- Ruff for linting
- MyPy for static analysis
- Pytest for testing

TypeScript

- Strict mode enabled
- ESLint
- Prettier
- Functional React components

---

# Formatting

Python

- Line length: 100
- Use Ruff formatter

TypeScript

- Follow project ESLint and Prettier configuration

---

# Testing Strategy

Every feature should include:

- Unit tests
- Integration tests (when applicable)

Target:

- Core modules: >90% coverage
- Overall project: >80% coverage

---

# Documentation Standards

Every module should include:

- Purpose
- Responsibilities
- Public API
- Example usage (when applicable)

Major architectural changes require an ADR.

---

# Logging

Use the centralized logging framework.

Avoid print() statements in production code.

---

# Configuration

Do not hardcode configuration values.

Use the centralized settings module.

---

# Error Handling

Use centralized exception handlers.

Return standardized API responses.

Do not expose internal stack traces to API clients.

---

# Code Review Checklist

Before merging:

- Tests pass
- Linting passes
- Type checking passes
- Documentation updated
- No unnecessary dependencies added

---

# Definition of Done

A task is complete only when:

- Implementation finished
- Tests added
- Documentation updated
- Code reviewed
- Quality checks passed

---

# Engineering Philosophy

RNAOS is built as production-quality research software.

Every line of code should contribute to maintainability, reproducibility, and scientific reliability.
