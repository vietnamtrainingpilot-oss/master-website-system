# Master Website — OpenCode Skill

Autonomous website-production system for OpenCode. One command takes a brief and delivers a production-ready website through a complete 13-phase pipeline.

## Quick Start

```bash
# In OpenCode:
/master-website "Build a premium SaaS landing for a developer analytics tool with dark mode, scroll-reveal animations, and pricing"

# The skill will:
# 1. Research the domain & competitors
# 2. Brainstorm design direction (taste-skill dials)
# 3. Select design system & template from Master Design library
# 4. Implement with real tokens, components, motion
# 5. Test in browser (Playwright), audit for AI-slop
# 6. Fix issues, verify, deliver
```

## What You Get

```
website-output/
├── index.html              # Entry point (vanilla HTML or framework)
├── tokens.css              # Design system tokens (verbatim from design system)
├── styles.css              # Project styles
├── scripts/                # Motion, interaction, utilities
├── assets/                 # Real images, fonts, icons, SVG props
├── ATTRIBUTION.md          # Source registry, licenses, upstream URLs
├── DECISION_RECORD.md      # Resource selection, dials, rationale
├── VERIFICATION_REPORT.md  # Browser QA, verification-loop, audit results
└── README.md               # How to run, deploy, extend
```

## Installation

### Prerequisites

| Tool | Version | Install Command |
|------|---------|-----------------|
| Node.js | 18+ | `winget install OpenJS.NodeJS` or [nodejs.org](https://nodejs.org) |
| Python | 3.10+ | `winget install Python.Python.3.11` |
| uv | latest | `winget install astral-sh.uv` |
| Graphify | 0.9.95+ | `uv tool install graphifyy` + `graphify install --platform opencode` |
| Playwright | latest | `npx playwright install chromium` |
| OpenCode | latest | [opencode.ai](https://opencode.ai) |
| Pixabay API Key | (optional) | [pixabay.com/api/docs](https://pixabay.com/api/docs/) |

### Verify Installation

```bash
# Check all tools
node --version    # v18+
python --version  # 3.10+
uv --version      # 0.x+
graphify --version # 0.9.95+
opencode --version # latest

# Check Graphify OpenCode integration
graphify install --platform opencode --dry-run  # Should show skill + hook

# Check Master Design library exists
ls "D:\Master Design\"  # Should show: craft, design-systems, design-templates, frames, skills
```

## Usage

### Basic Invocation

```bash
# In OpenCode terminal:
/master-website "Build a premium landing page for [your project]"

# With options:
/master-website "Build a portfolio site" --design_system editorial --template web-prototype-taste-editorial --framework nextjs
```

### Command Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `brief` | Yes | Website description: purpose, audience, brand, functionality, constraints |
| `--design_system` | No | Specific design system from `D:\Master Design\design-systems\` |
| `--template` | No | Specific template from `D:\Master Design\design-templates\` |
| `--framework` | No | Target: `html` (default), `react`, `nextjs`, `astro` |
| `--output_dir` | No | Output directory (default: `./website-output`) |

### Examples

```bash
# SaaS landing
/master-website "Build a SaaS landing for a dev tool: hero with live demo, features grid, pricing table, testimonials, dark mode default"

# Portfolio
/master-website "Create a designer portfolio with editorial aesthetic, case studies, about, contact — minimal motion, serif display"

# Marketing site
/master-website "Local bakery site with online ordering, warm aesthetic, mobile-first, hero photo of pastries"

# Documentation
/master-website "Docs site for open-source library: search, dark mode, code playground, versioned sidebar"
```

## How It Works

The skill executes a **13-phase pipeline** with hard gates:

```
A. Intake & Design Read          → brainstorming (design doc approval gate)
B. Research & Discovery          → visual-research, Graphify, web-clone
C. Design Direction & Taste      → design-taste-frontend (dials locked) + SVG Creator + Pixabay + Agent Spawner
D. Design System Setup           → design-md, tokens.css pasted
E. Template Selection            → template-selection-guide.md (10 steps)
F. Plan & Implement              → writing-plans, TDD, frontend-patterns
G. Animation Engineering         → animate, review-animations (approve gate)
H. Engineering & Accessibility   → frontend-a11y, generic-site-auditor (P0=0)
I. Browser QA                    → browser-qa, Playwright (SHIP gate)
J. Test, Review, Verify          → verification-loop, security-audit (PASS gate)
K. Fix & Refine                  → systematic-debugging, impeccable-design-polish
L. Deliver                       → ship-it, ATTRIBUTION.md
M. Video Creation & Editing      → hyperframes, remotion, media-use (for video projects)
```

### Phase C — Design Direction (Key Integration Point)

**Agents MUST use these skills during Phase C:**

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **svg-creator** | Create SVG background props (circles, geometric shapes, gradient meshes, grid patterns) | `VARIANCE > 5` for background props, `MOTION > 4` for animated props |
| **pixabay-fetcher** | Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots | Hero backgrounds, section backgrounds, texture overlays |
| **agent-spawner** | Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution | Automatic during Phase C — reduces tokens ~47% |

**Phase C now includes:**
- **Section 10**: SVG Asset Creation & Background Props (svg-creator skill)
- **Section 11**: Pixabay Image Fetching (pixabay-fetcher skill)  
- **Section 12**: Agent Spawning Architecture (agent-spawner skill)
- **Section 13**: Updated checklist with SVG props, Pixabay images, agent spawning
- **Section 14**: Quick reference commands for asset creation

### Hard Gates (You Must Approve)

1. **Design Doc** (Phase A) — After brainstorming, you approve the design doc before any code.
2. **Animation Review** (Phase G) — `review-animations` must return **Approve**.
3. **Browser QA = SHIP** (Phase I) — Playwright audit verdict must be SHIP.
4. **Verification Loop = PASS** (Phase J) — All automated checks green.

### Phase M — Video Creation (Optional)

For video projects, Phase M runs after Phase L or in parallel with G/H:
- **HyperFrames** pipeline: compose → assets → design → animate → preview → render
- **Remotion** pipeline: init → compose → animate → audio → render
- **Asset Resolution**: `media-use` for BGM, voiceover, images, SFX
- **Captioning**: HyperFrames `<hf-captions>` + Remotion `remotion-captions`
- **Platform Export**: TikTok/Reels/Shorts (9:16), YouTube (16:9), LinkedIn, Twitter/X, Web

## Installation

### Prerequisites

| Tool | Version | Install Command |
|------|---------|-----------------|
| Node.js | 18+ | `winget install OpenJS.NodeJS` or [nodejs.org](https://nodejs.org) |
| Python | 3.10+ | `winget install Python.Python.3.11` |
| uv | latest | `winget install astral-sh.uv` |
| Graphify | 0.9.95+ | `uv tool install graphifyy` + `graphify install --platform opencode` |
| Playwright | latest | `npx playwright install chromium` |
| OpenCode | latest | [opencode.ai](https://opencode.ai) |
| Pixabay API Key | (optional) | [pixabay.com/api/docs](https://pixabay.com/api/docs/) |

### Verify Installation

```bash
# Check all tools
node --version    # v18+
python --version  # 3.10+
uv --version      # 0.x+
graphify --version # 0.9.95+
opencode --version # latest

# Check Graphify OpenCode integration
graphify install --platform opencode --dry-run  # Should show skill + hook

# Check Master Design library exists
ls "D:\Master Design\"  # Should show: craft, design-systems, design-templates, frames, skills
```

## Usage

### Basic Invocation

```bash
# In OpenCode terminal:
/master-website "Build a premium landing page for [your project]"

# With options:
/master-website "Build a portfolio site" --design_system editorial --template web-prototype-taste-editorial --framework nextjs
```

### Command Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `brief` | Yes | Website description: purpose, audience, brand, functionality, constraints |
| `--design_system` | No | Specific design system from `D:\Master Design\design-systems\` |
| `--template` | No | Specific template from `D:\Master Design\design-templates\` |
| `--framework` | No | Target: `html` (default), `react`, `nextjs`, `astro` |
| `--output_dir` | No | Output directory (default: `./website-output`) |

### Examples

```bash
# SaaS landing
/master-website "Build a SaaS landing for a dev tool: hero with live demo, features grid, pricing table, testimonials, dark mode default"

# Portfolio
/master-website "Create a designer portfolio with editorial aesthetic, case studies, about, contact — minimal motion, serif display"

# Marketing site
/master-website "Local bakery site with online ordering, warm aesthetic, mobile-first, hero photo of pastries"

# Documentation
/master-website "Docs site for open-source library: search, dark mode, code playground, versioned sidebar"

# Video project
/master-website "Product launch video for SaaS tool with hero demo, feature walkthrough, pricing — 60s vertical for TikTok/Reels"
```

## How It Works

### Phase C — Design Direction (Key Integration Point)

**Agents MUST use these skills during Phase C:**

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **svg-creator** | Create SVG background props (circles, geometric shapes, gradient meshes, grid patterns) | `VARIANCE > 5` for background props, `MOTION > 4` for animated props |
| **pixabay-fetcher** | Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots | Hero backgrounds, section backgrounds, texture overlays |
| **agent-spawner** | Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution | Automatic during Phase C — reduces tokens ~47% |

**Phase C now includes:**
- **Section 10**: SVG Asset Creation & Background Props (svg-creator skill)
- **Section 11**: Pixabay Image Fetching (pixabay-fetcher skill)  
- **Section 12**: Agent Spawning Architecture (agent-spawner skill)
- **Section 13**: Updated checklist with SVG props, Pixabay images, agent spawning
- **Section 14**: Quick reference commands for asset creation

### Hard Gates (You Must Approve)

1. **Design Doc** (Phase A) — After brainstorming, you approve the design doc before any code.
2. **Animation Review** (Phase G) — `review-animations` must return **Approve**.
3. **Browser QA = SHIP** (Phase I) — Playwright audit verdict must be SHIP.
4. **Verification Loop = PASS** (Phase J) — All automated checks green.

## Installation

### Prerequisites

| Tool | Version | Install Command |
|------|---------|-----------------|
| Node.js | 18+ | `winget install OpenJS.NodeJS` or [nodejs.org](https://nodejs.org) |
| Python | 3.10+ | `winget install Python.Python.3.11` |
| uv | latest | `winget install astral-sh.uv` |
| Graphify | 0.9.95+ | `uv tool install graphifyy` + `graphify install --platform opencode` |
| Playwright | latest | `npx playwright install chromium` |
| OpenCode | latest | [opencode.ai](https://opencode.ai) |
| Pixabay API Key | (optional) | [pixabay.com/api/docs](https://pixabay.com/api/docs/) |

### Verify Installation

```bash
# Check all tools
node --version    # v18+
python --version  # 3.10+
uv --version      # 0.x+
graphify --version # 0.9.95+
opencode --version # latest

# Check Graphify OpenCode integration
graphify install --platform opencode --dry-run  # Should show skill + hook

# Check Master Design library exists
ls "D:\Master Design\"  # Should show: craft, design-systems, design-templates, frames, skills
```

## Usage

### Basic Invocation

```bash
# In OpenCode terminal:
/master-website "Build a premium landing page for [your project]"

# With options:
/master-website "Build a portfolio site" --design_system editorial --template web-prototype-taste-editorial --framework nextjs
```

### Command Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `brief` | Yes | Website description: purpose, audience, brand, functionality, constraints |
| `--design_system` | No | Specific design system from `D:\Master Design\design-systems\` |
| `--template` | No | Specific template from `D:\Master Design\design-templates\` |
| `--framework` | No | Target: `html` (default), `react`, `nextjs`, `astro` |
| `--output_dir` | No | Output directory (default: `./website-output`) |

### Examples

```bash
# SaaS landing
/master-website "Build a SaaS landing for a dev tool: hero with live demo, features grid, pricing table, testimonials, dark mode default"

# Portfolio
/master-website "Create a designer portfolio with editorial aesthetic, case studies, about, contact — minimal motion, serif display"

# Marketing site
/master-website "Local bakery site with online ordering, warm aesthetic, mobile-first, hero photo of pastries"

# Documentation
/master-website "Docs site for open-source library: search, dark mode, code playground, versioned sidebar"

# Video project
/master-website "Product launch video for SaaS tool with hero demo, feature walkthrough, pricing — 60s vertical for TikTok/Reels"
```

## How It Works

### Phase C — Design Direction (Key Integration Point)

**Agents MUST use these skills during Phase C:**

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **svg-creator** | Create SVG background props (circles, geometric shapes, gradient meshes, grid patterns) | `VARIANCE > 5` for background props, `MOTION > 4` for animated props |
| **pixabay-fetcher** | Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots | Hero backgrounds, section backgrounds, texture overlays |
| **agent-spawner** | Spawn specialized sub-agents (design-agent, svg-agent, image-agent) for parallel execution | Automatic during Phase C — reduces tokens ~47% |

**Phase C now includes:**
- **Section 10**: SVG Asset Creation & Background Props (svg-creator skill)
- **Section 11**: Pixabay Image Fetching (pixabay-fetcher skill)  
- **Section 12**: Agent Spawning Architecture (agent-spawner skill)
- **Section 13**: Updated checklist with SVG props, Pixabay images, agent spawning
- **Section 14**: Quick reference commands for asset creation

### Hard Gates (You Must Approve)

1. **Design Doc** (Phase A) — After brainstorming, you approve the design doc before any code.
2. **Animation Review** (Phase G) — `review-animations` must return **Approve**.
3. **Browser QA = SHIP** (Phase I) — Playwright audit verdict must be SHIP.
4. **Verification Loop = PASS** (Phase J) — All automated checks green.

### Phase M — Video Creation (Optional)

For video projects, Phase M runs after Phase L or in parallel with G/H:
- **HyperFrames** pipeline: compose → assets → design → animate → preview → render
- **Remotion** pipeline: init → compose → animate → audio → render
- **Asset Resolution**: `media-use` for BGM, voiceover, images, SFX
- **Captioning**: HyperFrames `<hf-captions>` + Remotion `remotion-captions`
- **Platform Export**: TikTok/Reels/Shorts (9:16), YouTube (16:9), LinkedIn, Twitter/X, Web

## Configuration

### Environment Variables

```bash
# Required for validation
export MASTER_DESIGN_ROOT="D:\Master Design"

# Optional for Pixabay
export PIXABAY_API_KEY="your-api-key-here"

# Optional dials (defaults in dials.json)
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

## Resource Library

The skill requires the **OpenDesign Master Design** library at `D:\Master Design\` (or `MASTER_DESIGN_ROOT` env var):

```
D:\Master Design\
├── craft/                 # Token schema, anti-ai-slop, typography
├── design-systems/        # 152 systems (default, editorial, brutalist, luxury, shadcn, vercel, ...)
├── design-templates/      # 115 templates (web-prototype, saas-landing, open-design-landing, html-ppt, ...)
├── frames/                # Device mockups (iPhone, iPad, MacBook, Android, Browser)
├── skills/                # 169 skill stubs (catalogue entries pointing to upstreams)
└── references/            # Phase guides, guides, catalogs, audit data
```

**Never modified** — all originals preserved verbatim. Working copies made to output directory.

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

## Graphify Integration

Graphify is installed as an OpenCode skill + hook:

```bash
# Built code graph of Master Design library
cd "D:\Master Design" && graphify . --code-only --no-viz

# Query during Phase B:
/graphify query "design templates for saas landing"
/graphify query "design systems with cobalt accent"
/graphify path "web-prototype" "default"
```

## Attribution & Licensing

Delivered sites include `ATTRIBUTION.md` with full provenance. Key sources:

| Source | License | Upstream |
|--------|---------|----------|
| OpenDesign library | Apache-2.0 | https://github.com/nexu-io/open-design |
| Superpowers (brainstorming) | Apache-2.0 | https://github.com/obra/superpowers |
| Taste Skill | Apache-2.0 | https://github.com/Leonxlnx/taste-skill |
| Emil Kowalski Skills | MIT | https://github.com/emilkowalski/skills |
| Vercel Web Interface Guidelines | MIT | https://github.com/vercel-labs/web-interface-guidelines |
| HTML PPT | MIT | https://github.com/lewislulu/html-ppt-skill |
| Graphify | MIT | https://github.com/Graphify-Labs/graphify |
| SVG Creator | Apache-2.0 | https://github.com/upbrew-tech/svg-creator-skill |
| Pixabay API | Free commercial | https://pixabay.com/api/docs/ |

**Original library preserved** — `D:\Master Design\` never modified (verified via `source-inventory.jsonl` SHA-256 checksums).

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| "Graphify not found" | `uv tool install graphifyy && graphify install --platform opencode` |
| "Master Design library not found" | Set `MASTER_DESIGN_ROOT` env var or ensure `D:\Master Design\` exists |
| "Playwright browsers missing" | `npx playwright install chromium` |
| "Skill not found" | Ensure OpenCode skills installed at `~/.config/opencode/skills/` |
| "Design doc not approved" | Review the generated design doc in `docs/superpowers/specs/` and confirm |
| "Animation review blocked" | Check `review-animations` output; fix per remedial hierarchy (delete → reduce → fix easing → ...) |
| "Browser QA = DO-NOT-SHIP" | Open `BROWSER_QA_REPORT.md`, fix P0 findings, re-run |
| "Pixabay API key missing" | Set `PIXABAY_API_KEY` env var or add to `.opencode/master-website.config.json` |

## Advanced: Smoke Test Scenarios

The skill includes validation scenarios:

1. **Marketing/Brand Website** — `/master-website "Build a premium site for a design agency"`
2. **Multi-Route Web App** — `/master-website "Create a dashboard with auth, settings, data tables"`
3. **Template Reuse** — `/master-website "SaaS landing using saas-landing template + default design system"`
4. **No Template Match** — `/master-website "Real-time collaborative whiteboard with WebGL"` → custom build
5. **Video Project** — `/master-website "Product launch video for SaaS tool with hero demo"`

## Support

- **Skill Issues**: Check `.opencode/skills/master-website/SKILL.md` for phase details
- **Template Selection**: See `references/template-selection-guide.md`
- **Source Attribution**: See `references/source-attribution.md`
- **Integration Map**: See `references/skill-integration-map.md`
- **SVG Creator**: See `references/skills/svg-creator/SKILL.md`
- **Pixabay Fetcher**: See `references/skills/pixabay-fetcher/SKILL.md`
- **Agent Spawner**: See `references/skills/agent-spawner/SKILL.md`

## License

Apache-2.0. Bundles references to upstream Apache-2.0/MIT resources; see `source-attribution.md` for full registry.