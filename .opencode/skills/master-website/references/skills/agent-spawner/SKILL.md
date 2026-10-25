---
name: agent-spawner
description: Spawn specialized sub-agents for specific tasks to reduce token usage and improve quality. Main agent delegates to specialized sub-agents for focused tasks.
---

# Agent Spawner Skill

## Purpose
Enable the main agent to spawn specialized sub-agents for focused tasks, reducing token usage and improving quality through specialization.

## Architecture

### Main Agent (Orchestrator)
- Receives high-level task
- Decomposes into subtasks
- Spawns appropriate sub-agents
- Aggregates results
- Delivers final output

### Sub-Agent Types
| Agent Type | Specialization | Token Savings |
|------------|----------------|---------------|
| `design-agent` | Visual design, UI/UX, color, typography | ~60% |
| `code-agent` | Implementation, components, logic | ~50% |
| `research-agent` | Web research, competitive analysis | ~70% |
| `svg-agent` | SVG creation, icons, illustrations | ~65% |
| `image-agent` | Image fetching, optimization | ~60% |
| `video-agent` | Video creation, editing | ~65% |
| `qa-agent` | Testing, accessibility, performance | ~55% |
| `content-agent` | Copywriting, SEO, content strategy | ~55% |

## Spawning Protocol

### Spawn Request
```json
{
  "agent_type": "design-agent",
  "task": "Create hero section design with SVG background props",
  "context": {
    "design_system": "tokens.css",
    "dials": {"variance": 60, "motion": 50, "density": 40},
    "references": ["references/skills/svg-creator/", "references/skills/pixabay-fetcher/"]
  },
  "output_format": "design_spec.json",
  "max_tokens": 3000
}
```

### Sub-Agent Response
```json
{
  "agent_type": "design-agent",
  "status": "completed",
  "output": {
    "hero_design": {...},
    "svg_props": ["circle-bg.svg", "geometric-shapes.svg"],
    "pixabay_images": ["hero-bg.jpg", "pattern-overlay.jpg"]
  },
  "tokens_used": 2847
}
```

## Spawning Workflow

### 1. Task Decomposition (Main Agent)
```
Main Task → Analyze → Decompose → Identify Sub-Agent Types → Spawn
```

### 2. Sub-Agent Execution (Parallel)
```
design-agent    → Design hero + SVG props
image-agent     → Fetch Pixabay hero images
svg-agent       → Create background props
content-agent   → Write hero copy
```

### 3. Result Aggregation (Main Agent)
```
Collect Results → Validate → Integrate → Deliver
```

## Token Optimization

### Before (Monolithic Agent)
- Single agent does everything: ~15,000 tokens
- Context pollution from unrelated tasks
- Quality suffers from divided attention

### After (Agent Swarm)
- Main agent: ~2,000 tokens (orchestration only)
- Sub-agents: ~3,000 tokens each (focused)
- Total: ~8,000 tokens (~47% reduction)
- Higher quality from specialization

## Integration with Master Website

### Phase C Integration (Design Direction)
```python
# Main agent spawns for Phase C
spawn("design-agent", "Create design direction with SVG props", context)
spawn("svg-agent", "Create background props: circles, geometric shapes", context)
spawn("image-agent", "Fetch Pixabay hero images for background", context)
```

### Phase F Integration (Implementation)
```python
# Main agent spawns for Phase F
spawn("code-agent", "Implement hero component with SVG props", context)
spawn("code-agent", "Implement image optimization pipeline", context)
spawn("svg-agent", "Generate optimized SVG sprites", context)
```

### Phase M Integration (Video)
```python
# Main agent spawns for Phase M
spawn("video-agent", "Create product launch video", context)
spawn("svg-agent", "Create animated SVG overlays", context)
spawn("image-agent", "Fetch video thumbnail images", context)
```

## Sub-Agent Implementation

Each sub-agent is a focused skill with:
- Narrow, well-defined scope
- Specific input/output contracts
- Access to relevant skill references
- Token budget enforcement
- Output validation

## Configuration
```yaml
agent_spawner:
  max_concurrent: 4
  default_token_budget: 3000
  max_retries: 2
  timeout_seconds: 120
  sub_agents:
    design-agent:
      skill_refs: ["design-taste", "svg-creator", "pixabay-fetcher"]
      token_budget: 3000
    code-agent:
      skill_refs: ["frontend-patterns", "react-patterns"]
      token_budget: 4000
    svg-agent:
      skill_refs: ["svg-creator"]
      token_budget: 3000
    image-agent:
      skill_refs: ["pixabay-fetcher"]
      token_budget: 2000
    video-agent:
      skill_refs: ["video-production", "hyperframes", "remotion"]
      token_budget: 5000
```