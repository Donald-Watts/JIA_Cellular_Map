---
date: '2025-05-15T07:38:59.834803'
title: Project_Rules.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:31:22.126892'
title: Project_Rules.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:30:42.939459'
title: Project_Rules.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
---
date: '2025-05-15T07:28:25.639712'
title: Project_Rules.md
weights:
  ai_direction: 0.0
  component: 1.0
  harmonics: 0.0
  interaction: 0.0
  resonance: 0.0
  state: 0.3
---
# Project Rules for Developers

> **This document serves as the definitive guide for developers working on the JIA Cellular AI Mapping project.**
>
> All developers must adhere to these rules to maintain project integrity and ensure successful collaboration with AI agents.

## Core Principles

1. **Phase-Based Development**
   - Follow the 7-phase development structure strictly
   - Respect SWP weights for prioritization
   - Complete each phase before moving to the next
   - Document phase completion in `development_phases.md`

2. **Code Organization**
   - Maintain the established directory structure:
     
     /src/
       /models/    # Cell and tissue models
       /agents/    # AI agent implementations
       /engine/    # Simulation engine
       /ui/        # User interface components
     /tests/
     /docs/
     /config/
     
   - Follow naming conventions in `git_protocol.md`
   - Keep documentation in sync with code changes

3. **Version Control**
   - Use the branching strategy defined in `git_protocol.md`
   - Follow commit message conventions
   - Complete pre-push checklist before merging
   - Never commit sensitive data or core engine secrets

4. **Documentation Requirements**
   - Update relevant documentation for all changes
   - Maintain cross-references between documents
   - Follow the documentation structure in `navigation.md`
   - Keep phase weights and tags current

5. **Testing Standards**
   - Write tests for all new features
   - Maintain minimum 80% test coverage
   - Include both unit and integration tests
   - Document test scenarios and requirements

6. **AI Collaboration**
   - Respect AI agent roles and responsibilities
   - Follow the weight system for AI direction
   - Maintain clear interfaces for AI interaction
   - Document AI-related changes thoroughly

7. **Security & Ethics**
   - Follow guidelines in `anti_misuse_protocol.md`
   - Protect sensitive algorithms and data
   - Maintain ethical standards in all development
   - Report potential misuse immediately

## Development Workflow

1. **Starting New Work**
   - Check current phase in `development_phases.md`
   - Review relevant documentation
   - Create appropriate feature branch
   - Update task tracking

2. **During Development**
   - Follow coding standards
   - Write tests alongside code
   - Update documentation
   - Regular commits with proper messages

3. **Completing Work**
   - Run full test suite
   - Update documentation
   - Create pull request
   - Get required approvals
   - Follow merge protocol

## Quality Assurance

1. **Code Review Requirements**
   - At least two approvals needed
   - One must be from project maintainer
   - All tests must pass
   - Documentation must be updated

2. **Performance Standards**
   - Meet defined performance benchmarks
   - Optimize resource usage
   - Document performance impacts
   - Include performance tests

3. **Security Checks**
   - Regular security audits
   - Vulnerability scanning
   - Access control verification
   - Data protection compliance

## Communication

1. **Team Coordination**
   - Regular status updates
   - Clear documentation of changes
   - Proper issue tracking
   - Phase progress reporting

2. **AI Interaction**
   - Clear interface documentation
   - Consistent API design
   - Proper error handling
   - Regular AI agent updates

## Compliance & Ethics

1. **Required Agreements**
   - Sign Humanity-First Contributor Agreement
   - Follow ethical guidelines
   - Maintain security protocols
   - Report violations

2. **Data Protection**
   - Follow data privacy guidelines
   - Secure sensitive information
   - Regular security audits
   - Proper access controls

## Emergency Procedures

1. **Critical Issues**
   - Follow hotfix protocol
   - Immediate security response
   - Clear communication
   - Proper documentation

2. **Rollback Procedures**
   - Document rollback steps
   - Maintain backup systems
   - Clear communication plan
   - Recovery testing

> **Note**: These rules are binding for all developers and must be followed to maintain project integrity and ensure successful collaboration with AI agents.

**Repository:**  
The canonical repository for this project is located at [github.com/Donald-Watts/JIA_Cellular_Map](https://github.com/Donald-Watts/JIA_Cellular_Map). 