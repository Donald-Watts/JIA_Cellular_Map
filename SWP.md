---
date: '2025-05-15T07:38:59.814142'
title: SWP.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:31:22.111947'
title: SWP.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:30:42.926298'
title: SWP.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:28:25.627748'
title: SWP.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
# SymWghtPtcl Phase Weights (SWP)

> **This document is the single source of truth for phase weight calculations in the JIA Cellular AI Mapping project.**
>
> The weights are used to tag and prioritize markdown files, source code modules, and commits across all project phases.

## Weight Calculation Scheme

1. **Raw Sum Calculation**:
   - Convert each letter of the phase title (spaces and punctuation removed) to its A=1…Z=26 value
   - Sum all letter values to get the Raw Sum

2. **Reduced Sum Calculation**:
   - Repeatedly sum the digits of the Raw Sum until a single digit remains
   - This becomes the Reduced Sum (1-9)

3. **Tie Breaker**:
   - If multiple phases have the same Reduced Sum, use the Raw Sum as tiebreaker
   - Higher Raw Sum takes precedence

## Phase Weights

| Phase | Title | Raw Sum | Reduced Sum | Status | Last Updated |
|-------|-------|---------|-------------|---------|--------------|
| Phase 1 | Foundation and Definition | 243 | 9 | ✔ Completed | 2024-03-19 |
| Phase 2 | Blueprint and Canonical Structure | 353 | 2 | ✔ Completed | 2024-03-19 |
| Phase 3 | Scaffolding and Schema Definition | 269 | 8 | ✔ Completed | 2024-03-19 |
| Phase 4 | Core Feature Development | 243 | 9 | 🔄 In Progress | 2024-03-19 |
| Phase 5 | Intelligence Learning and Test Suites | 353 | 2 | ⏳ Pending | 2024-03-19 |
| Phase 6 | User Interface and Orchestration | 269 | 8 | ⏳ Pending | 2024-03-19 |
| Phase 7 | Finalization and Product | 243 | 9 | ⏳ Pending | 2024-03-19 |

## Weight Application

### File Tagging
- Add weight to markdown files: `[SWP-9]` for Phase 1 files
- Add weight to source code: `# SWP-9` in module headers
- Add weight to commits: `[SWP-9]` in commit messages

### Priority Levels
1. **High Priority (9)**: Foundation, Core Features, Finalization
2. **Medium Priority (8)**: Scaffolding, UI/Orchestration
3. **Low Priority (2)**: Blueprint, Intelligence Learning

### Example Usage

# Cell Activation Module [SWP-9]
# Core feature implementation for Phase 4


## Maintenance

- Update this file whenever phase titles change
- Recalculate weights for any title modifications
- Keep status and last updated dates current
- Document any weight calculation rule changes

## References

- See `docs/development_phases.md` for detailed phase descriptions
- See `docs/blueprint.md` for technical architecture
- See `docs/navigation.md` for project navigation



> **Note**: These weights are foundational to the project's organization and should be referenced in all major documentation and code changes.