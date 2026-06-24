# IMPLEMENTATION_RULES.md

# Implementation Rules

## No Assumptions

Never invent requirements.

Never guess behavior.

Never extend functionality without approval.

If information is missing:

STOP

ASK

CLARIFY

CONFIRM

CONTINUE

---

## Clarification First

When multiple implementation options exist:

1. Ask a question.
2. Wait for an answer.
3. Update the plan.
4. Continue implementation.

---

## Specification Driven

Implementation must follow PROJECT.md.

Any deviation requires approval.

---

## Minimal Dependencies

Prefer:

* Python Standard Library
* FastAPI
* Uvicorn

Do not add dependencies without justification.

---

## Development Environment

All development must happen inside Docker containers.

Do not require Python installation on the host.

Do not require FastAPI installation on the host.

Do not require Uvicorn installation on the host.

---

## Git Rules

If repository information is missing:

Ask for:

* Repository URL
* Branch Strategy
* Git Execution Instructions

Do not guess.

---

## Kubernetes Rules

If cluster information is missing:

Ask for:

* Kubernetes Context
* Namespace
* kubectl Execution Instructions
* kubeconfig Access Method

Do not guess.
