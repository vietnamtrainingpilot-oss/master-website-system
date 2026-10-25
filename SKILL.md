---
name: master-website
description: "Master Website — Autonomous full-stack website production from brief to deployable HTML/CSS/JS/video. Synthesized playbooks with zero content loss from 169 skills + video pipeline."
---

# /master-website — Complete Website Production System

## Purpose
Build a complete, portable, autonomous website-production system that synthesizes all 169 skills from `D:\Master Design\skills\` into 13 actionable phase playbooks (A–M). Each phase is a coherent playbook with zero content loss — every technique, config table, example, banned default, spring preset, and workflow step from the source skills is preserved and organized for execution.

## Usage
```bash
# Run the master skill
/master-website

# Or use the command
master-website --project "My Website" --dials variance=50 motion=40 density=30
```

## Phase Playbooks (13)

| Phase | File | Size | Focus |
|-------|------|------|-------|
| A | `references/phase-a-intake.md` | ~3 KB | Design Read, taste dials, skills discovery |
| B | `references/phase-b-research.md` | ~2 KB | Web clone recon, asset harvest, source verification |
| C | `references/phase-c-design-direction.md` | ~9 KB | **Core** — Dials, anti-defaults, design system map, tokens |
| D | `references/phase-d-design-system.md` | ~5 KB | Tokenize, component specs, DESIGN.md, a11y baseline |
| E | `references/phase-e-template.md` | ~4 KB | Template selection, init, content mapping, assets |
| F | `references/phase-f-implement.md` | ~6 KB | Phased impl, React/backend patterns, perf budgets, TDD |
| G | `references/phase-g-animation.md` | ~6 KB | **Core** — Build sequence, 10 standards, component patterns |
| H | `references/phase-h-engineering.md` | ~5 KB | A11y audit, perf optimization, security, code quality |
| I | `references/phase-i-browser.md` | ~1 KB | Browser QA: visual regression, CWV, a11y, interactions |
| J | `references/phase-j-test.md` | ~1 KB | 6-phase verification loop, TDD enforcement |
| K | `references/phase-k-fix.md` | ~2 KB | Systematic debugging, 6-mode polish, code review |
| L | `references/phase-l-deliver.md` | ~4 KB | Ship-it pipeline, deploy, monitor, handoff |
| **M** | `references/phase-m-video.md` | **~8 KB** | **Video creation/editing: HyperFrames, Remotion, captions** |

## Specialty Guides

| Guide | Purpose |
|-------|---------|
| `references/pptx-guide.md` | Presentation/slide deck creation (html-ppt, slides, wowerpoint) |
| `references/docs-guide.md` | Documentation/content processing (article-writing, data-report) |
| `references/brand-guide.md` | Brand identity/visual systems (brandkit, brand-discovery, design) |
| `references/animation-guide.md` | Animation/motion reference (animate, gsap-*, motion-*, remotion) |
| `references/video-guide.md` | Video creation/editing (hyperframes, remotion, captions, media-use) |

## Hard Gates Table

| Phase | Gate Name | Pass Condition | If Fail |
|-------|-----------|----------------|---------|
| A | Project Brief Locked | Design Read complete, dials set | Return to stakeholder |
| B | Research Complete | Source Package verified | Expand research |
| C | Design Direction Approved | Anti-defaults applied, dials justified, system selected | Adjust dials, regenerate |
| D | Design System Ready | tokens.css + component specs + DESIGN.md + a11y baseline | Complete missing items |
| E | Template Selected | Template Package ready (initialized, tokens, content, assets) | Complete preparation |
| F | Implementation Complete | All steps done + tests pass + polish applied | Fix failing tests |
| G | Animation Approved | `review-animations` returns Approve on all elements | Fix or remove animation |
| H | Engineering Complete | A11y AA + CWV Good + Security clean + Lint/Typecheck clean | Fix failures |
| I | Browser QA Passed | SHIP verdict (visual regression, CWV, a11y, interactions green) | Return to H/F/G |
| J | Verification Loop Pass | All 6 phases green | Fix, re-run from Phase 1 |
| K | Bugs Fixed | Zero critical/high + polish applied + review addressed | Fix before proceeding |
| L | Ship Ready | All pre-ship PASS + deploy successful + monitoring green | Address blockers |
| M | Video Approved | `review-animations` + browser-qa + caption accuracy + platform specs | Return to G/F |

## Resource Root Discovery
This skill operates from its installed location. Resource discovery:

```
Resource Root: ~/.opencode/skills/master-website/
├── SKILL.md              # This file
├── references/
│   ├── phase-a-intake.md
│   ├── phase-b-research.md
│   ├── phase-c-design-direction.md
│   ├── phase-d-design-system.md
│   ├── phase-e-template.md
│   ├── phase-f-implement.md
│   ├── phase-g-animation.md
│   ├── phase-h-engineering.md
│   ├── phase-i-browser.md
│   ├── phase-j-test.md
│   ├── phase-k-fix.md
│   ├── phase-l-deliver.md
│   ├── phase-m-video.md
│   ├── pptx-guide.md
│   ├── docs-guide.md
│   ├── brand-guide.md
│   ├── animation-guide.md
│   ├── video-guide.md
│   ├── design-systems/
│   │   ├── AGENTS.md       # 152 design systems catalog
│   │   └── _must-use-rules.md
│   ├── design-templates/
│   │   └── AGENTS.md       # 115 templates catalog
│   ├── skills/             # 169 source skills (for specific-task deep-dive)
│   ├── skills-phase-mapping.md
│   ├── source-attribution.md
│   ├── skill-integration-map.md
│   ├── template-selection-guide.md
│   ├── design-read-template.md
│   ├── dials.json
│   ├── decision-record-template.md
│   └── hard-gates.md
└── docs/
    └── master-website/
        └── audit/
            └── source-audit-enhanced.jsonl  # 5,243 entries
```

## Environment Configuration

```bash
# Master Design root location (REQUIRED for validation)
export MASTER_DESIGN_ROOT="D:\Master Design"

# Output location (defaults to current directory)
export MASTER_WEBSITE_OUTPUT="./website-output"

# Dial settings (optional, defaults in dials.json)
export VARIANCE=50
export MOTION=40
export DENSITY=30
```

### Path Resolution
```python
import os
from pathlib import Path

MASTER_DESIGN_ROOT = os.environ.get('MASTER_DESIGN_ROOT', 'D:\\Master Design')
SKILL_ROOT = Path.home() / '.opencode' / 'skills' / 'master-website'
PRODUCT_ROOT = Path(MASTER_DESIGN_ROOT) / 'master-website-system'
REFERENCES = SKILL_ROOT / 'references'
```

## Key Synthesized Content (Zero Loss)

### Phase C — Design Direction (Core)
- **Three Taste Dials** (VARIANCE/MOTION/DENSITY) with full range tables from `taste-skill`
- **30+ Banned LLM Defaults** with before/after examples from `taste-skill`
- **Design System Map**: Color → Typography → Spacing → Shadows → Motion
- **Spring Config Table** with 5 presets from `emil-design-eng`
- **Typography Scale** (Display→Caption) with weights, line heights, tracking from `high-end-visual-design`
- **Shadow System** (4 levels) with colored shadows from `emil-design-eng`
- **Anti-Default Decisions** template (minimum 5 required)
- **Design Direction Doc** template consuming Phase A/B

### Phase G — Animation (Core)
- **6-Step Build Sequence** (Frequency → Tool → Properties → Easing → Interruption → Reduced Motion) from `animate`
- **10 Non-Negotiable Standards** with before/after table from `review-animations`
- **Component Motion Patterns** (Buttons, Popovers, Tooltips, Modals, Lists, Pages) from `emil-design-eng`, `motion-patterns`
- **Spring Presets** (5 configs) from `emil-design-eng`
- **Library Integration** (GSAP, Motion/React, CSS) with code examples
- **Performance Budget** (16ms/frame, max 3 concurrent) from `fixing-motion-performance`

### Phase M — Video Creation & Editing (New)
- **Tool Selection Matrix** (HyperFrames vs Remotion vs FFmpeg) from `video-production` router
- **HyperFrames Pipeline**: compose → assets → design → animate → preview → render
- **Remotion Pipeline**: init → compose → animate → audio → render
- **Asset Resolution** via `media-use` (BGM, voiceover, images, SFX)
- **Captioning**: HyperFrames `<hf-captions>` + Remotion `remotion-captions`
- **Platform Export**: TikTok/Reels/Shorts (9:16), YouTube (16:9), LinkedIn, Twitter/X, Web embed
- **Hard Gates**: `review-animations` + `browser-qa` + caption accuracy + platform specs

### Phase F — Implementation
- **Phased Planning** with self-contained context briefs from `writing-plans`, `orch-*`
- **React Patterns** (Server/Client components, parallel fetching) from `frontend-patterns`, `react-patterns`
- **State Management Decision Tree** from `frontend-patterns`
- **Backend Patterns** (API, DB, Auth, Infra) from 20+ backend skills
- **Performance Budgets** (CWV targets, 70+ optimization rules) from `vercel-react-best-practices`
- **6-Mode Polish Workflow** (Audit→Tighten→Harden→Animate→Live→Ship) from `impeccable-design-polish`

### Phase H — Engineering
- **WCAG 2.2 AA Checklist** (47 items across POUR) from `accessibility`, `frontend-a11y`
- **Core Web Vitals Optimization** (8 categories, 70+ rules) from `vercel-react-best-practices`
- **Security Hardening** (deps, code, auth, headers) from `security`, `security-review`
- **Code Quality** (Ponytail YAGNI, TypeScript strict, linting) from `ponytail-*`, `coding-standards`
- **Generic Site Audit** (6-phase) from `generic-site-auditor`

## Video-Specific Template Pulling

For video tasks, pull from `references/design-templates/design-templates/`:

| Template | Use For |
|----------|---------|
| `hyperframes/` | Base HyperFrames project structure, house style, patterns |
| `video-shortform/` | TikTok/Reels/Shorts vertical format |
| `video-hyperframes/` | Continuous animation / ambient video |
| `video-production/` | General video project scaffold |
| `web-prototype/` | If video embeds in website |
| `saas-landing/` | If video is hero on landing page |

## Validation
```bash
python validate.py
```
Expected: 30/30 structural checks PASS.

## Distribution
Copy `master-website-system/` to any machine. Run `install.ps1` to install locally.

## Source
Synthesized from 169 skills in `D:\Master Design\skills\` with zero content loss — every technique, config, example, and workflow preserved in actionable playbook form. Video pipeline adds Phase M with 20+ video skills.

## Integration Summary

| Metric | Value |
|--------|-------|
| Total Skills Synthesized | 169 |
| Phase Playbooks | 13 (A–M) |
| Specialty Guides | 5 (pptx, docs, brand, animation, video) |
| Design Systems Cataloged | 152 (via AGENTS.md) |
| Templates Cataloged | 115 (via AGENTS.md) |
| Source Skills Available | 169 (in references/skills/) |
| Total Playbook Content | ~60 KB (synthesized, not concatenated) |
| Source Audit Entries | 5,243 |

---

*All substantive instructional content has been synthesized into phase playbooks with zero loss — organized for execution, not archival. Video pipeline (Phase M) extends the 12-phase pipeline for video deliverables; skip if not needed.*
