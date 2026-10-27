# CLAUDE REBUILD PROMPT - Master Website Plugin for OpenCode

## TASK
Recreate the master-website OpenCode skill from scratch. This is an autonomous website-production system that takes a brief and delivers a production-ready website through a 13-phase pipeline (A-M) with hard gates.

---

## SOURCE REPOSITORY (Reference)
- GitHub: https://github.com/vietnamtrainingpilot-oss/master-website-system
- Branch: main
- Current State: Working, validated (37/39 PASS, 2 FAIL optional)

---

## CORE PHILOSOPHY (Non-Negotiable)

### The 3 Taste Dials (from taste-skill)
| Dial | Range | Meaning |
|------|-------|---------|
| VARIANCE | 0-100 | Deviation from defaults - Corporate: 10-30, Creative: 60-80 |
| MOTION | 0-100 | Animation intensity - Dashboard: 20-40, Landing: 40-60, Creative: 60-80 |
| DENSITY | 0-100 | Information density - Financial: 70-80, Lifestyle: 20-40 |

Baseline: VARIANCE=50, MOTION=40, DENSITY=30 - use unless design read overrides.

### 30+ Banned LLM Defaults (from taste-skill)
- AI-purple gradients, centered hero over dark mesh, three equal feature cards
- Generic glassmorphism on everything, infinite-loop micro-animations everywhere
- Inter + slate-900, default rounded corners, default shadows
- Rule: Reach past defaults deliberately based on design read.

### Must-Use Rules (from _must-use-rules.md)
- WCAG 2.2 AA (47 items across POUR)
- Core Web Vitals: LCP < 2.5s, INP < 150ms, CLS < 0.1
- review-animations hard gate - must return Approve
- Never invent hex values - copy tokens.css :root verbatim from selected design system
- One design system per project - never mix Fluent + Carbon, etc.

---

## 13-PHASE PIPELINE (A-M)

### Phase A - Design Read and Taste Dials
Hard Gate: Design Read complete + dials set - Proceed to B
Inputs: Brand context, business goals, user needs, content strategy, design prefs, tech requirements, constraints
Output: references/dials.json + Design Read doc

### Phase B - Research and Discovery
Hard Gate: Source Package verified - Proceed to C
Tools: visual-research, Graphify, web-clone
Output: Source attribution, competitive references, asset patterns

### Phase C - Design Direction and Taste (CORE - Mandatory Skills)
Hard Gate: Anti-defaults applied, dials justified, system selected - Proceed to D
Mandatory Skills (MUST use during Phase C):
1. svg-creator (Sec 10): SVG background props when VARIANCE > 5 or MOTION > 4
2. pixabay-fetcher (Sec 11): Hero backgrounds, textures from Pixabay (needs PIXABAY_API_KEY)
3. agent-spawner (Sec 12): Parallel sub-agents (design-agent, svg-agent, image-agent) - ~47% token reduction

Design System Selection (reach for official packages first):
| Brief Reads As... | System | Package |
|------------------|--------|---------|
| Microsoft/Enterprise | Fluent UI | @fluentui/react-components |
| Google/Material | Material 3 | @material/web |
| IBM/Analytics | Carbon | @carbon/react |
| Shopify | Polaris | polaris.js |
| Atlassian/Jira | Atlassian | @atlaskit/* |
| UK Public Sector | GOV.UK | govuk-frontend |
| US Public Sector | USWDS | uswds |
| Fast MVP | Bootstrap | bootstrap |
| Accessible React Base | Radix Themes | @radix-ui/themes |
| Own Components | shadcn/ui | npx shadcn@latest add ... |
| Indie SaaS | Tailwind v4 | tailwindcss |

### Phase D - Design System Setup
Hard Gate: tokens.css + component specs + DESIGN.md + a11y baseline - Proceed to E

### Phase E - Template Selection
Hard Gate: Template Package ready (initialized, tokens, content, assets) - Proceed to F
Catalog: 115 templates in references/design-templates/AGENTS.md

### Phase F - Plan and Implement
Hard Gate: All steps done + tests pass + polish applied - Proceed to G
Patterns: React Server/Client components, parallel fetching, TDD, 70+ perf rules

### Phase G - Animation Engineering (CORE)
Hard Gate: review-animations returns Approve on all elements - Proceed to H
6-Step Build Sequence: Frequency - Tool - Properties - Easing - Interruption - Reduced Motion
10 Non-Negotiable Standards from review-animations

### Phase H - Engineering and Accessibility
Hard Gate: A11y AA + CWV Good + Security clean + Lint/Typecheck clean - Proceed to I

### Phase I - Browser QA
Hard Gate: SHIP verdict (visual regression, CWV, a11y, interactions all green) - Proceed to J
Tool: Playwright at breakpoints 1440, 768, 375 + axe-core

### Phase J - Test, Review, Verify
Hard Gate: All 6 phases green - Proceed to K
6-Phase Verification: build - type - lint - test - security - diff

### Phase K - Fix and Refine
Hard Gate: Zero critical/high + polish applied + review addressed - Proceed to L

### Phase L - Deliver
Hard Gate: All pre-ship PASS + deploy successful + monitoring green - Complete

### Phase M - Video Creation and Editing (OPTIONAL - Skip if not video)
Hard Gate: review-animations + browser-qa + caption accuracy + platform specs - Return to G/F
Pipelines: HyperFrames (compose-assets-design-animate-preview-render) OR Remotion (init-compose-animate-audio-render)
Export: TikTok/Reels/Shorts (9:16), YouTube (16:9), LinkedIn, Twitter/X, Web embed

---

## REQUIRED FILES TO PROVIDE CLAUDE

### 1. Root Skill File (System Prompt)
File: SKILL.md (19.3 KB)
Contains: Phase guide, hard gates table, resource root discovery, environment config, all 13 phases with usage instructions
Must include: How to use each phase, read-first requirements, gate conditions

### 2. System Prompt (AGENTS.md)
File: AGENTS.md (18.6 KB)
13 non-negotiable rules
Role priorities (safety - user request - design system - existing product - references - design direction - defaults)
Design-system discipline, visual quality, UX/content rules, build rules, accessibility/motion/interaction, verification/delivery

### 3. README.md (Installation and Usage)
File: README.md (22 KB)
Prerequisites table (Node 18+, Python 3.10+, uv, Graphify, Playwright, OpenCode)
Usage examples, command arguments, 13-phase pipeline table
Phase C mandatory skills documentation
Design systems and templates catalog counts
Live OpenCode skills table (17 skills)

### 4. 13 Phase Playbooks
| Phase | File | Size | Key Content |
|-------|------|------|-------------|
| A | references/phase-a-intake.md | 2.8 KB | Design Read template, dials table, skills discovery |
| B | references/phase-b-research.md | 2.1 KB | Web clone recon, asset harvest, source verification |
| C | references/phase-c-design-direction.md | 95 KB | CORE - Full taste-skill, dials, anti-defaults, design system map, Sections 10-14 (svg-creator, pixabay-fetcher, agent-spawner) |
| D | references/phase-d-design-system.md | 1.6 KB | Tokenize, component specs, DESIGN.md, a11y baseline |
| E | references/phase-e-template.md | 4.6 KB | Template selection, init, content mapping, assets |
| F | references/phase-f-implement.md | 5.5 KB | Phased impl, React/backend patterns, perf budgets, TDD |
| G | references/phase-g-animation.md | 8.2 KB | CORE - Build sequence, 10 standards, component patterns |
| H | references/phase-h-engineering.md | 6.7 KB | A11y audit, perf optimization, security, code quality |
| I | references/phase-i-browser.md | 2.5 KB | Browser QA: visual regression, CWV, a11y, interactions |
| J | references/phase-j-test.md | 2.6 KB | 6-phase verification loop, TDD enforcement |
| K | references/phase-k-fix.md | 3.6 KB | Systematic debugging, 6-mode polish, code review |
| L | references/phase-l-deliver.md | 5.1 KB | Ship-it pipeline, deploy, monitor, handoff |
| M | references/phase-m-video.md | 7.2 KB | Video: HyperFrames, Remotion, captions, platform export |

### 5. Specialty Guides (5)
| Guide | File |
|-------|------|
| Presentation/Slides | references/pptx-guide.md |
| Docs/Content | references/docs-guide.md |
| Brand/Visual Systems | references/brand-guide.md |
| Animation/Motion | references/animation-guide.md |
| Video Creation | references/video-guide.md |

### 6. Catalogs
| Catalog | File | Count |
|---------|------|-------|
| Design Systems | references/design-systems/AGENTS.md | 152 systems |
| Design Templates | references/design-templates/AGENTS.md | 115 templates |
| Skills | references/skills/AGENTS.md | 172 skills (169 source + 3 mandatory) |

### 7. Craft References (Universal Design Rules)
Dir: references/craft/ (12 files)
- typography.md, typography-hierarchy.md, typography-hierarchy-editorial.md
- color.md, anti-ai-slop.md, state-coverage.md
- animation-discipline.md, accessibility-baseline.md
- rtl-and-bidi.md, form-validation.md, laws-of-ux.md

### 8. 3 Mandatory Phase C Skills (Global Install Required)
Each must be a separate OpenCode skill at ~/.config/opencode/skills/:

#### svg-creator
name: svg-creator
description: Create SVG background props (circles, geometric shapes, gradient meshes, grid patterns) for web backgrounds and animated props. Used in Phase C when VARIANCE > 5 or MOTION > 4.
Types: grid, gradient-mesh, circles, geometric, noise
Output: assets/images/svg-props/
Upstream: https://github.com/upbrew-tech/svg-creator-skill

#### pixabay-fetcher
name: pixabay-fetcher
description: Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots. Used in Phase C Section 11. Requires PIXABAY_API_KEY env var.
Params: --query, --orientation, --min-width, --category, --count, --output-dir
Output: assets/images/pixabay/ + ATTRIBUTION.md entries

#### agent-spawner
name: agent-spawner
description: Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution during Phase C. Reduces tokens ~47% by distributing work across focused agents.
Sub-agents: design-agent (design direction), svg-agent (SVG props), image-agent (Pixabay fetching)
Coordination: Main agent creates task specs - sub-agents execute parallel - main collects/validates

### 9. Validation Script
File: validate.py - 39 structural checks (37 PASS, 2 FAIL optional)

### 10. Prompt Examples
File: references/prompt-examples.md - 8 test prompts + main plugin website prompt

---

## INSTALLATION REQUIREMENTS (User Must Have)

# Prerequisites
Node.js 18+        # winget install OpenJS.NodeJS
Python 3.10+       # winget install Python.Python.3.11
uv                 # winget install astral-sh.uv
Graphify 0.9.95+   # uv tool install graphifyy && graphify install --platform opencode
Playwright         # npx playwright install chromium
OpenCode           # https://opencode.ai

# Environment Variables
export MASTER_DESIGN_ROOT=D:\Master Design   # Path to design library (craft, design-systems, design-templates, frames, skills)
export PIXABAY_API_KEY=your-key              # Optional, for Phase C Section 11

# Global Skills (must be installed at ~/.config/opencode/skills/)
~/.config/opencode/skills/svg-creator/
~/.config/opencode/skills/pixabay-fetcher/
~/.config/opencode/skills/agent-spawner/
~/.config/opencode/skills/master-website/

---

## DESIGN LIBRARY STRUCTURE (MASTER_DESIGN_ROOT)
D:\Master Design\
- craft/                 # 12 universal craft rule files
- design-systems/        # 152 systems (each: manifest.json, DESIGN.md, tokens.css, components.html, USAGE.md)
- design-templates/      # 115 templates (each: SKILL.md, example.html, assets/, references/)
- frames/                # Device mockups (iPhone, iPad, MacBook, Android, Browser)
- skills/                # 169 skill stubs (catalogue entries pointing to upstreams)
- references/            # Phase guides, specialty guides, catalogs, audit data

Never modified - all originals preserved verbatim. Working copies made to output directory.

---

## OUTPUT STRUCTURE
website-output/
- index.html              # Entry point (vanilla HTML or framework)
- tokens.css              # Design system :root block (verbatim)
- styles.css              # Project styles
- scripts/
  - motion.js           # IntersectionObserver reveals, reduced-motion
  - interactions.js     # Form handling, navigation, etc.
- assets/
  - images/             # Real photos (generated/sourced) + SVG props
  - fonts/              # Self-hosted fonts (if any)
- ATTRIBUTION.md          # Full source registry, licenses, upstream URLs
- DECISION_RECORD.md      # Template choice, dials, rationale
- VERIFICATION_REPORT.md  # Browser QA, verification-loop, audit results
- README.md               # How to run, deploy, extend

---

## GITHUB REPOSITORIES TO REFERENCE

| Component | Repo | Purpose |
|-----------|------|---------|
| taste-skill | https://github.com/Leonxlnx/taste-skill | 87 KB - dials, anti-defaults, design system map |
| emil-design-eng | https://github.com/emilkowalski/skills | Component/motion philosophy, spring presets |
| review-animations | https://github.com/emilkowalski/skills | 10 standards, Block/Approve gate |
| svg-creator | https://github.com/upbrew-tech/svg-creator-skill | SVG background props |
| html-ppt | https://github.com/lewislulu/html-ppt-skill | 36 themes, 31 layouts, presenter mode |
| Vercel Web Guidelines | https://github.com/vercel-labs/web-interface-guidelines | 70+ perf rules |
| Graphify | https://github.com/Graphify-Labs/graphify | Code graph for research |
| Superpowers | https://github.com/obra/superpowers | brainstorming skill |

---

## CRITICAL RULES FOR CLAUDE

1. Global install only - Skills at ~/.config/opencode/skills/, not project-local .opencode/
2. Phase C MUST invoke svg-creator, pixabay-fetcher, agent-spawner - not optional
3. Design system = official package - Never recreate CSS by hand, copy :root verbatim
4. Hard gates are absolute - Cannot proceed without passing
5. Phase M is optional - Skip if not video project
6. Validation must pass - python validate.py - 37 PASS minimum
7. Attribution required - Every asset/source tracked in ATTRIBUTION.md
8. Original library never touched - MASTER_DESIGN_ROOT is read-only

---

## COMMAND TO RUN
# In OpenCode terminal:
/master-website "Build a premium SaaS landing for a developer analytics tool with dark mode, scroll-reveal animations, and pricing"

# With options:
/master-website "Build a portfolio site" --design_system editorial --template web-prototype-taste-editorial --framework nextjs

---

## FILES TO GIVE CLAUDE (Attach or Paste)

### Minimum Required (Paste in order):
1. SKILL.md - Full system prompt with phase guide
2. AGENTS.md - 13 non-negotiable rules
3. README.md - Installation, usage, catalogs
4. references/phase-c-design-direction.md - 95 KB core (taste-skill + Phase C sections 10-14)
5. references/phase-g-animation.md - 8 KB core (animation build sequence + 10 standards)
6. references/phase-m-video.md - 7 KB video pipeline
7. references/craft/ - All 12 craft files
8. references/design-systems/AGENTS.md - 152 systems catalog
9. references/design-templates/AGENTS.md - 115 templates catalog
10. references/skills/AGENTS.md - 172 skills catalog (with 3 mandatory)
11. 3 skill files: svg-creator/SKILL.md, pixabay-fetcher/SKILL.md, agent-spawner/SKILL.md
12. validate.py - Validation script
13. references/prompt-examples.md - Test prompts

### Reference Only (Claude can fetch):
- GitHub repo: https://github.com/vietnamtrainingpilot-oss/master-website-system
- All upstream skill repos listed above

---

## WHAT CLAUDE SHOULD PRODUCE

A complete, working master-website OpenCode skill that:
1. Installs globally at ~/.config/opencode/skills/master-website/
2. Has 13 phase playbooks with hard gates
3. Mandatory Phase C skills properly integrated
4. Validates with python validate.py - 37 PASS
5. Generates production websites from briefs
6. Optionally creates videos (Phase M)
7. Follows all 30+ banned defaults, 3 taste dials, WCAG 2.2 AA, CWV targets

---

## TEST PROMPTS FOR CLAUDE TO VERIFY

# 1. Minimal smoke test
/master-website "Simple hello world page with title, paragraph, and button. Dark mode. No animations."

# 2. Full SaaS landing
/master-website "SaaS landing for DevPulse - real-time API monitoring. Hero with live metrics demo, features grid (5 items), pricing table (3 tiers), testimonials carousel, footer with GitHub/Discord links. Dark mode default, cobalt accent. LCP < 2.5s."

# 3. Portfolio (editorial)
/master-website "Designer portfolio for Maya Chen - editorial aesthetic, warm paper tones, italic serif display (Atelier Zero), collage-on-grid case studies, generous whitespace. Minimal motion (MOTION 30), low density (DENSITY 25)."

# 4. Video project
/master-website "Product launch video for DevPulse SaaS - 60s vertical (9:16) for TikTok/Reels/Shorts. Hero demo (15s), feature walkthrough (30s), pricing + CTA (15s). Beat-synced cuts, kinetic typography, caption accuracy > 95%."

---

This prompt contains everything needed to rebuild the master-website plugin from scratch. The original repo at https://github.com/vietnamtrainingpilot-oss/master-website-system is the reference implementation.
