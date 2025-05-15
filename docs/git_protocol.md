---
date: '2025-05-15T07:38:59.824210'
title: git_protocol.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:31:22.121656'
title: git_protocol.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:30:42.935666'
title: git_protocol.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:28:25.635001'
title: git_protocol.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
# Git Protocol & Best Practices

> **This document outlines the standardized workflow, branch strategy, commit conventions, and ignore rules for managing the JIA Sandbox codebase safely and consistently.**

## Table of Contents

1. [Workflow & Branching Strategy](#workflow--branching-strategy)
2. [Commit Message Conventions](#commit-message-conventions)
3. [Release & Tagging](#release--tagging)
4. [Code Review & Merging](#code-review--merging)
5. [.gitignore Guidelines](#gitignore-guidelines)
6. [Pre-Push Checklist](#pre-push-checklist)
7. [Security & Compliance](#security--compliance)

## Workflow & Branching Strategy

### Main Branches

- `main` — Production-ready releases only
- `develop` — Integration branch for completed features before release

### Feature Branches

- **Naming**: `feature/phase<1|2|...>-<short-desc>`
- Created off `develop`
- Merge back via PR when a phase or sub-feature is complete

### Release Branches

- **Naming**: `release/vX.Y-phase<1|2|...>`
- Created off `develop` at phase milestones
- Used for version bump, changelog, QA
- Tag commits with `vX.Y-phase<phase>`

### Hotfix Branches

- **Naming**: `hotfix/<issue>-<short-desc>`
- Created off `main` to fix critical bugs
- Merge back into both `main` and `develop`

## Commit Message Conventions

### Format
```
<type>(<scope>): <brief summary>
```

### Types
- `feat` — New feature or phase implementation
- `fix` — Bug fix
- `docs` — Documentation only changes
- `test` — Adding or updating tests
- `chore` — Maintenance tasks
- `refactor` — Code refactoring without behavior change
- `perf` — Performance improvements

### Examples
```
feat(cell): implement CD4TCell activation logic
docs: add diffusion model rationale to cell_ai_mapping.md
fix(engine): correct time-step scheduler bug
```

## Release & Tagging

### Version Bump
- Update version in `setup.py` or `pyproject.toml` (e.g., 0.1.0 → 0.2.0)
- Append phase summary to `CHANGELOG.md`

### Tag Creation
```bash
git tag -a v0.2.0-phase2 -m "Phase 2 release: Blueprint & Canonical Structure"
git push origin v0.2.0-phase2
```

## Code Review & Merging

### Pull Request Requirements
- Link to relevant phase or issue
- All tests must pass in CI
- At least two approvals required (one must be a project maintainer)
- No merge conflicts with target branch

### Merge Method
- Squash-and-merge preferred for clean history

## .gitignore Guidelines

### Environment & IDE
```
.venv/
.vscode/
.idea/
```

### Python Artifacts
```
__pycache__/
*.pyc
```

### Sensitive Files
```
.env
.env.*
*.key
*.pem
```

### Simulation Outputs & Logs
```
logbook.db
results/
*.json
```

### Build & Distribution
```
dist/
build/
*.egg-info/
```

> **Note**: Never commit API keys, private config, or core engine secrets. See `docs/anti_misuse_protocol.md` for protected modules.

## Pre-Push Checklist

Before pushing or merging, ensure:
1. All tests pass
2. Documentation is updated
3. Code style is consistent
4. No sensitive data is included
5. Commit messages follow conventions
6. Branch is up to date with target

## Security & Compliance

### Core Engine Logic Privacy
- Keep core simulation algorithms private until Ethics Board approval
- Tag any sensitive modules in `.gitignore` or use a private submodule

### Contributor Accountability
- All committers must have signed the Humanity-First Contributor Agreement
- See `docs/anti_misuse_protocol.md` for details


> **Note**: Adhering to this Git protocol ensures traceability, reproducibility, and security as the JIA Sandbox evolves through its development phases.