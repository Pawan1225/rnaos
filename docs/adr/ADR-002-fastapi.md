# ADR-002 — Why FastAPI

Status: Accepted

Date: 2026-07-20

---

# Context

RNAOS requires a high-performance backend supporting REST APIs, asynchronous execution, automatic documentation, and strong typing.

---

# Decision

FastAPI is selected as the primary backend framework.

---

# Rationale

Advantages include:

- High performance
- Native async support
- Automatic OpenAPI documentation
- Pydantic validation
- Excellent Python ecosystem integration
- Strong developer productivity

---

# Consequences

Positive

- Fast development
- Reliable APIs
- Easy testing
- Scalable architecture

Negative

- Requires understanding of async programming
