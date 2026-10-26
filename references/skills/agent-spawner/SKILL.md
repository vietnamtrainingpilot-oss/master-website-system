---
name: agent-spawner
description: "Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution during Phase C. Reduces tokens ~47% by distributing work across focused agents."
triggers:
  - "spawn agent"
  - "parallel execution"
  - "sub-agent"
  - "agent spawner"
od:
  mode: utility
  category: parallel
---
# agent-spawner — Sub-Agent Architecture for Parallel Execution

## Purpose
Spawn specialized sub-agents during Phase C (Design Direction) to parallelize design direction, SVG asset creation, and image fetching. Reduces token usage by ~47% compared to sequential execution.

## Architecture

```
Phase C Main Agent
├── design-agent  → Design direction, dials, anti-defaults, design system selection
├── svg-agent     → SVG background props (grid, gradient-mesh, circles, geometric)
└── image-agent   → Pixabay fetching, optimization, attribution
```

## Usage
```bash
# In OpenCode (automatic during Phase C):
/agent-spawner --phase C --tasks design-direction,svg-props,image-fetch
```

## Sub-Agent Specifications

### design-agent
- **Focus**: Design read inference, dial setting, anti-default discipline, design system selection
- **Inputs**: Phase A Design Read, Phase B Research Package
- **Outputs**: Design Direction Doc, dial values, selected design system

### svg-agent
- **Focus**: SVG background prop generation using svg-creator skill
- **Inputs**: VARIANCE/MOTION dials, design system color tokens
- **Outputs**: SVG files to `assets/images/svg-props/`

### image-agent
- **Focus**: Pixabay image fetching using pixabay-fetcher skill
- **Inputs**: Design direction (hero concept, texture needs), PIXABAY_API_KEY
- **Outputs**: Optimized images to `assets/images/pixabay/`, attribution entries

## Coordination Protocol
1. Main agent creates task specs with clear inputs/outputs
2. Sub-agents execute in parallel (no shared state)
3. Main agent collects outputs, validates, assembles into Phase C deliverable
4. Token savings: ~47% vs monolithic agent (each sub-agent only loads relevant context)

## Configuration
```json
{
  "maxParallelAgents": 3,
  "timeoutMs": 120000,
  "tokenBudgetPerAgent": 15000
}
```

## Installation
Installed globally at `~/.config/opencode/skills/agent-spawner/`
