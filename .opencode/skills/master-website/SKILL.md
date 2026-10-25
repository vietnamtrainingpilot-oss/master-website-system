---
type: skill
description: "Master Website â€” Autonomous full-stack website production from brief to deployable HTML/CSS/JS/video. Synthesized playbooks with zero content loss from 169 skills + video pipeline."
---
# /master-website â€” Complete Website Production System

## Purpose
Build a complete, portable, autonomous website-production system that synthesizes all 169 skills from `D:\Master Design\skills\` into 13 actionable phase playbooks (Aâ€“M). Each phase is a coherent playbook with zero content loss — every technique, config table, example, banned default, spring preset, and workflow step from the source skills is preserved and organized for execution.

## ⚠️ REQUIRED READING ORDER
**Before running any phase, you MUST read the following in order. This SKILL.md is the system prompt — it configures the agent behavior, and ALL referenced files must be loaded.**

1. **`references/craft/`** — Universal craft rules (typography, color, anti-ai-slop, motion, etc.). Skill frontmatter `od.craft.requires` will inject only the needed sections.
2. **`references/AGENTS.md` (root)** — Global rules, priorities, non-negotiable requirements, design-system discipline, visual quality standards, UX/content rules, build/implementation rules, accessibility/motion/interaction verification, and delivery rules. **This IS the system prompt — read first.**
3. **`references/dials.json`** — Taste dials configuration (VARIANCE, MOTION, DENSITY).
4. **Phase playbooks** — Read phases in order: A → B → C → D → E → F → G → H → I → J → K → L → M (skip M if not video).
5. **Design system & template catalogs** — `references/design-systems/AGENTS.md` and `references/design-templates/AGENTS.md`.
6. **Source skills** — `references/skills/` (169 skills for specific-task deep-dive).
7. **Specialty guides** — `references/pptx-guide.md`, `references/docs-guide.md`, `references/brand-guide.md`, `references/animation-guide.md`, `references/video-guide.md`.

## Usage
```bash
# Run the master skill
/master-website

# Or use the command with options
master-website --project "My Website" --design_system editorial --template web-prototype --framework nextjs --dials variance=50 motion=40 density=30
```

## Phase Playbooks (13 Phases A-M)

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

## Phase Guide: How to Use Each Playbook

Each phase is a sequential playbook with a hard gate. You must pass the gate before proceeding to the next phase. Skip Phase M (Video) if your project is not video-focused.

### Phase A — Design Read & Taste Dials
**Purpose**: Capture the project brief, set the three taste dials (VARIANCE, MOTION, DENSITY), and produce a Design Read document that drives all subsequent phases.
**How to use**:
1. Fill in the Design Read template (references/phase-a-intake.md) with brand context, business goals, user needs, content strategy, design preferences, and technical requirements.
2. Set the three dials: VARIANCE (0-100, deviation from defaults), MOTION (0-100, animation intensity), DENSITY (0-100, information density).
3. Record dial values in references/dials.json — they propagate to all phases.
4. Hard gate: Design Read complete + dials set → Proceed to Phase B. If incomplete, return to stakeholder.
**Read first**: `references/craft/`, root `references/AGENTS.md`, `references/dials.json`.

### Phase B — Research & Discovery
**Purpose**: Web clone recon, asset harvest, and source verification. Build the source package for design direction.
**How to use**:
1. Run visual-research, Graphify, and web-clone tools to gather competitive references and asset patterns.
2. Verify all sources and record attributions in references/source-attribution.md.
3. Hard gate: Source Package verified → Proceed to Phase C. If incomplete, expand research.
**Read first**: Phase A Design Read, `references/skill-integration-map.md`.

### Phase C — Design Direction & Taste (CORE)
**Purpose**: Establish visual direction by applying taste dials, anti-default discipline, and design system selection. This is the central design configuration phase.
**How to use** (critical — MUST use svg-creator, pixabay-fetcher, agent-spawner):
1. **Infer the design read** from the brief (page kind, vibe words, reference signals, audience, existing brand assets).
2. **Set the three dials** using the design read signal table (e.g., "minimalist/clean/calm" → VARIANCE 5-6, MOTION 3-4, DENSITY 2-3).
3. **Apply anti-default discipline** — do not default to AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism, infinite-loop micro-animations everywhere, Inter + slate-900.
4. **Select design system** using the design system map (Color → Typography → Spacing → Shadows → Motion). Reach for official packages first (@fluentui/react, @material/web, @carbon/react, polaris.js, @atlaskit/*, govuk-frontend, uswds, Bootstrap 5.3, @radix-ui/themes, shadcn/ui, Tailwind v4).
5. **USE REQUIRED SKILLS**:
   - `svg-creator` (Phase C, Section 10): Create SVG background props when VARIANCE > 5 for background props, MOTION > 4 for animated props.
   - `pixabay-fetcher` (Phase C, Section 11): Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots.
   - `agent-spawner` (Phase C, Section 12): Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution — reduces tokens ~47%.
6. **Complete Section 10** (SVG Asset Creation) and **Section 11** (Pixabay Image Fetching) and **Section 12** (Agent Spawning Architecture) from references/phase-c-design-direction.md.
7. **Hard gate**: Design Direction Approved — Anti-defaults applied, dials justified, system selected → Proceed to Phase D. If not approved, adjust dials and regenerate.
**Read first**: Phase A Design Read, Phase B Research, `references/craft/`, root `references/AGENTS.md`, dials.json, `references/design-systems/AGENTS.md`, `references/design-templates/AGENTS.md`, `references/skills/svg-creator/SKILL.md`, `references/skills/pixabay-fetcher/SKILL.md`, `references/skills/agent-spawner/SKILL.md`.

### Phase D — Design System Setup
**Purpose**: Tokenize the design system, create component specs, DESIGN.md, and a11y baseline.
**How to use**:
1. Copy `tokens.css` `:root` block verbatim from the selected design system — never invent new hex values.
2. Create DESIGN.md with color roles, typography hierarchy, spacing scale, component rules, motion principles.
3. Generate component specs from the design system's components.html.
4. Establish a11y baseline using WCAG 2.2 AA checklist (47 items across POUR).
5. Hard gate: tokens.css + component specs + DESIGN.md + a11y baseline complete → Proceed to Phase E.
**Read first**: Phase C Design Direction, `references/craft/` (typography, color, anti-ai-slop, animation-discipline, form-validation, state-coverage, rtl-and-bidi), root `references/AGENTS.md`.

### Phase E — Template Selection
**Purpose**: Select and initialize the template package (tokens, content, assets).
**How to use**:
1. Browse references/design-templates/AGENTS.md (115 templates) to find a matching template.
2. Use the template selection guide (references/template-selection-guide.md) — 10-step process.
3. Initialize the template: copy assets/template.html, paste section skeletons from references/layouts.md, fill with real copy.
4. Self-check via references/checklist.md.
5. Hard gate: Template Package ready (initialized, tokens, content, assets) → Proceed to Phase F.
**Read first**: Phase D Design System, `references/template-selection-guide.md`, `references/design-templates/AGENTS.md`.

### Phase F — Plan & Implement
**Purpose**: Phased implementation with TDD, React patterns, performance budgets.
**How to use**:
1. Use writing-plans for phased planning with self-contained context briefs.
2. Follow React patterns: Server/Client components, parallel fetching from frontend-patterns, react-patterns.
3. Apply state management decision tree from frontend-patterns.
4. Implement backend patterns (API, DB, Auth, Infra) from 20+ backend skills.
5. Performance budgets: CWV targets (LCP < 2.5s, INP < 150ms, CLS < 0.1) and 70+ optimization rules from vercel-react-best-practices.
6. TDD: Write failing test first, implement smallest change to green, then refactor with 80%+ coverage.
7. Hard gate: All steps done + tests pass + polish applied → Proceed to Phase G.
**Read first**: Phase E Template, `references/writing-plans/`, `references/frontend-patterns/`, `references/vercel-react-best-practices/`.

### Phase G — Animation Engineering (CORE)
**Purpose**: Build animation sequence, apply 10 non-negotiable standards, component motion patterns.
**How to use**:
1. Follow the 6-step build sequence: Frequency → Tool → Properties → Easing → Interruption → Reduced Motion.
2. Apply the 10 non-negotiable standards from review-animations (must return Approve on all elements).
3. Use component motion patterns: buttons, popovers, tooltips, modals, lists, pages from emil-design-eng, motion-patterns.
4. Configure spring presets (5 configs) from emil-design-eng.
5. Library integration: GSAP, Motion/React, CSS with code examples.
6. Performance budget: 16ms/frame, max 3 concurrent animations.
7. Hard gate: `review-animations` returns Approve on all elements → Proceed to Phase H. If Block, fix or remove animation per remedial hierarchy (delete → reduce → fix easing → change tool → adjust frequency → ...).
**Read first**: Phase F Implementation, `references/emil-design-eng/` files, `references/review-animations/`, `references/animate/`, `references/fixing-motion-performance/`.

### Phase H — Engineering & Accessibility
**Purpose**: A11y audit, perf optimization, security, code quality.
**How to use**:
1. WCAG 2.2 AA Checklist: 47 items across POUR (Perceivable, Operable, Understandable, Robust).
2. Core Web Vitals Optimization: 8 categories, 70+ rules from vercel-react-best-practices.
3. Security Hardening: dependencies, code, auth, headers from security, security-review.
4. Code Quality: Ponytail YAGNI, TypeScript strict, linting from ponytail-*, coding-standards.
5. Generic Site Audit: 6-phase audit (Visual, Copy, Layout, Motion, Technical) from generic-site-auditor.
6. Hard gate: A11y AA + CWV Good + Security clean + Lint/Typecheck clean → Proceed to Phase I.
**Read first**: Phase F Implementation, `references/accessibility/`, `references/frontend-a11y/`, `references/vercel-react-best-practices/`, `references/ponytail/`, `references/coding-standards/`.

### Phase I — Browser QA
**Purpose**: Playwright QA: visual regression, CWV, a11y, interactions. Verdict must be SHIP.
**How to use**:
1. Run Playwright browser-qa smoke tests: console errors, CWV measurement, form interactions, screenshots at breakpoints (1440, 768, 375).
2. Accessibility assertions with axe-core.
3. Visual regression comparison.
4. Hard gate: SHIP verdict (visual regression, CWV, a11y, interactions all green) → Proceed to Phase J. If DO-NOT-SHIP, open BROWSER_QA_REPORT.md, fix P0 findings, re-run.
**Read first**: Phase H Engineering, `references/browser-qa/`.

### Phase J — Test, Review, Verify
**Purpose**: 6-phase verification loop, TDD enforcement, coverage enforcement.
**How to use**:
1. Run 6-phase verification: build → type → lint → test → security → diff from verification-loop.
2. TDD: Ensure failing tests were written first, smallest change to green, refactored.
3. Coverage: 80%+ minimum across unit/integration/E2E.
4. Security grep for vulnerabilities.
5. Diff review against base branch.
6. Hard gate: All 6 phases green → Proceed to Phase K. If any phase fails, fix and re-run from Phase 1.
**Read first**: Phase I Browser QA, `references/verification-loop/`.

### Phase K — Fix & Refine
**Purpose**: Systematic debugging, 6-mode polish, code review.
**How to use**:
1. Use systematic-debugging before proposing fixes.
2. Apply 6-mode polish workflow from impeccable-design-polish: Audit → Tighten → Harden → Animate → Live → Ship.
3. Address code review feedback. Keep tests green.
4. Hard gate: Zero critical/high bugs + polish applied + review addressed → Proceed to Phase L.
**Read first**: Phase J Verification Loop, `references/systematic-debugging/`, `references/impeccable-design-polish/`.

### Phase L — Deliver
**Purpose**: Ship-it pipeline, deploy, monitor, handoff.
**How to use**:
1. Execute ship-it end-to-end delivery coordination.
2. Deploy to target environment.
3. Set up monitoring (error tracking, performance monitoring).
4. Create handoff documentation.
5. Hard gate: All pre-ship PASS + deploy successful + monitoring green → Project complete. Address blockers if any.
**Read first**: Phase K Fix & Refine, `references/ship-it/`.

### Phase M — Video Creation & Editing (OPTIONAL)
**Purpose**: HyperFrames/Remotion pipelines for video deliverables.
**How to use** (skip if not video project):
1. For video tasks, pull from references/design-templates/design-templates/: hyperframes/, video-shortform/, video-hyperframes/, video-production/.
2. HyperFrames pipeline: compose → assets → design → animate → preview → render.
3. Remotion pipeline: init → compose → animate → audio → render.
4. Asset resolution via media-use (BGM, voiceover, images, SFX).
5. Captioning: HyperFrames `<hf-captions>` + Remotion `remotion-captions`.
6. Platform export: TikTok/Reels/Shorts (9:16), YouTube (16:9), LinkedIn, Twitter/X, Web embed.
7. Hard gates: `review-animations` + browser-qa + caption accuracy + platform specs.
8. **Skip Phase M** if the project is not video-focused. The 12-phase pipeline (A-L) completes without M.
**Read first**: Phase L Deliver, `references/video-guide.md`, `references/hyperframes/`, `references/remotion/`, `references/media-use/`.

## Specialty Guides (5)

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
⚡ SKILL.md              # This file (system prompt)
⚡ references/
  ⚡ phase-a-intake.md
  ⚡ phase-b-research.md
  ⚡ phase-c-design-direction.md
  ⚡ phase-d-design-system.md
  ⚡ phase-e-template.md
  ⚡ phase-f-implement.md
  ⚡ phase-g-animation.md
  ⚡ phase-h-engineering.md
  ⚡ phase-i-browser.md
  ⚡ phase-j-test.md
  ⚡ phase-k-fix.md
  ⚡ phase-l-deliver.md
  ⚡ phase-m-video.md
  ⚡ pptx-guide.md
  ⚡ docs-guide.md
  ⚡ brand-guide.md
  ⚡ animation-guide.md
  ⚡ video-guide.md
  ⚡ design-systems/
    ⚡ AGENTS.md       # 152 design systems catalog
    ⚡ _must-use-rules.md
  ⚡ design-templates/
    ⚡ AGENTS.md       # 115 templates catalog
  ⚡ skills/           # 169 source skills (for specific-task deep-dive)
  ⚡ skills-phase-mapping.md
  ⚡ source-attribution.md
  ⚡ skill-integration-map.md
  ⚡ template-selection-guide.md
  ⚡ design-read-template.md
  ⚡ dials.json
  ⚡ decision-record-template.md
  ⚡ hard-gates.md
  ⚡ docs/
    ⚡ master-website/
      ⚡ audit/
        ⚡ source-audit-enhanced.jsonl  # 5,243 entries
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

### Path Resolution (Python)

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

### Phase J — Verification Loop
- **6-Phase Verification** (build → type → lint → test → security → diff) from `verification-loop`
- **TDD Enforcement** — write failing test first, implement smallest change to green, then refactor
- **Coverage Enforcement** — 80%+ minimum across unit/integration/E2E

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

## Live OpenCode Skills Used

The skill invokes these installed skills (must be present in `~/.config/opencode/skills/`):

| Skill | Purpose |
|-------|---------|
| `brainstorming` | Design read, dials, approach selection, design doc gate |
| `design-taste-frontend` | Taste authority: dials, design-system map, anti-slop rules |
| `frontend-design` | Stack defaults (React/Next, Tailwind v4, Motion) |
| `emil-design-eng` | Component/motion philosophy, animation decision framework |
| `review-animations` | Hard animation gate (10 standards, Block/Approve) |
| `animate` | Animation build sequence, recipes |
| `browser-qa` | Playwright QA: console, CWV, forms, screenshots, axe |
| `verification-loop` | 6-phase verification (build, type, lint, test, security, diff) |
| `generic-site-auditor` | 6-phase audit (Visual, Copy, Layout, Motion, Technical) |
| `frontend-a11y` | WCAG 2.2 AA patterns for React/Next.js |
| `vercel-react-best-practices` | 70+ perf rules from Vercel Engineering |
| `ultimate-frontend-skills` | House style fallback, engines (gradient.js, depth.js, etc.) |
| `impeccable-design-polish` | Post-gen audit, critique, polish, harden |
| `systematic-debugging` | Bug diagnosis before fixes |
| `ship-it` | End-to-end delivery coordination |
| `svg-creator` | SVG asset creation, background props, patterns |
| `pixabay-fetcher` | High-quality free image fetching from Pixabay |
| `agent-spawner` | Sub-agent architecture for parallel execution |

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

*All substantive instructional content has been synthesized into phase playbooks with zero loss — organized for execution, not archival. Video pipeline (Phase M) extends the 13-phase pipeline for video deliverables; skip if not needed.*

**Critical**: Read `references/craft/` and `references/AGENTS.md` (root) before any phase. These are the system prompts that govern agent behavior. The `od.craft.requires` frontmatter on invoked skills will selectively inject only the needed craft sections.