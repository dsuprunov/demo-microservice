# AGENTS.md

## Agent Workflow

Before making project changes, read and follow `PROJECT.md`.

## Review Requests

When asked to review changes:

* Prioritize bugs, risks, regressions, and missing tests.
* List findings first, ordered by severity.
* Include file and line references when possible.
* Keep summaries secondary to findings.
* If no issues are found, say that clearly and mention residual risk.

## Requirements Handling

Never invent requirements.

Never guess behavior.

Never extend functionality without approval.

If information is missing: STOP, ASK, CLARIFY, CONFIRM, CONTINUE.

When multiple implementation options exist:

1. Ask a clarifying question and explain the available options.
2. Wait for an answer.
3. Update the plan.
4. Continue implementation.

## Working Rules

Keep changes small, direct, and related to the task.

Do not refactor unrelated code.

Prefer existing project patterns over new conventions.

Run relevant checks when the required tools are available.

Before modifying any file:

* Read the current version from disk.
* Verify the file has not changed unexpectedly.
* If the file changed after reading, re-read it before editing.
* Apply a minimal diff.
* Do not patch stale assumptions.
* Never overwrite user changes without explicit confirmation.

## Generated Code Style

Match the style of nearby files before adding new code.

Follow the user's current approach instead of introducing a different design.

Keep generated code simple, explicit, and easy to maintain.

Prefer small focused changes over broad abstractions.

Use the same naming, formatting, file layout, and command style already used
in this repository.

If the local style is unclear, ask before making a large style decision.

## Git Ownership

Git repository actions are owned by the user.

The AI agent must not run commands that change git repository state.

Do not stage files.

Do not create commits.

Do not perform any remote git operation.

Do not run destructive git commands unless explicitly requested by the user.

## Commit Messages

When asked for commit message text:

* Check the current diff first.
* Base the commit message on the actual diff, not on conversation context.
* Write it in simple English.
* Use Conventional Commits format: `<type>(<scope>): <description>`.
* Use `<type>` for the change type, for example `feat`, `fix`, `docs`,
  `refactor`, or `chore`.
* Use `<scope>` for the affected area or component.
* Use `<description>` for a short summary.

The user will run git commands themselves.
