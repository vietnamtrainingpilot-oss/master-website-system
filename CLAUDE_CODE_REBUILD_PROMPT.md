# MASTER-WEBSITE PLUGIN — CLAUDE CODE REBUILD PROMPT

## ONE-LINER
Build a global OpenCode skill master-website that autonomously produces production websites from a brief via a 13-phase gated pipeline (A–M), with 3 mandatory Phase C skills, 3 taste dials, 30+ banned defaults, WCAG 2.2 AA, and CWV targets.

---

## ARCHITECTURE AT A GLANCE

`
┌─────────────────────────────────────────────────────────────────┐
│  GLOBAL SKILLS (~/.config/opencode/skills/)                      │
│  ├── master-website/          # Main orchestrator (this build)   │
│  ├── svg-creator/             # Phase C Sec 10: SVG props        │
│  ├── pixabay-fetcher/         # Phase C Sec 11: Hero images      │
│  └── agent-spawner/           # Phase C Sec 12: Parallel agents  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  DESIGN LIBRARY (MASTER_DESIGN_ROOT — read-only)                │
│  ├── craft/              # 12 universal rules (typography, etc)  │
│  ├── design-systems/     # 152 systems (manifest, DESIGN.md,    │
│  │                         tokens.css, components.html, USAGE)  │
│  ├── design-templates/   # 115 templates (SKILL.md, example.html)│
│  ├── frames/             # Device mockups                        │
│  └── skills/             # 169 upstream skill stubs              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT (website-output/)                                       │
│  index.html, tokens.css, styles.css, scripts/, assets/,        │
│  ATTRIBUTION.md, DECISION_RECORD.md, VERIFICATION_REPORT.md    │
└─────────────────────────────────────────────────────────────────┘
`

---

## THE 13 PHASES (Sequential, Hard Gates)

| Phase | Name | Gate | Key Output |
|-------|------|------|------------|
| A | Design Read & Dials | Design Read + dials set | dials.json, Design Read |
| B | Research & Discovery | Source Package verified | Attribution, refs |
| **C** | **Design Direction** | **Anti-defaults, dials justified, system selected** | **Direction Doc** |
| D | Design System Setup | tokens.css + specs + DESIGN.md + a11y | Design system |
| E | Template Selection | Template Package ready | Initialized template |
| F | Plan & Implement | Tests pass + polish | Code |
| **G** | **Animation** | **review-animations = Approve** | Motion |
| H | Engineering & A11y | AA + CWV + Security + Lint | Hardened |
| I | Browser QA | **SHIP** verdict | QA report |
| J | Verify | 6-phase green | Verification |
| K | Fix & Refine | Zero critical + polish | Refined |
| L | Deliver | Deploy + monitoring | Live |
| **M** | **Video (opt)** | **Anim + QA + captions + specs** | Video |

**Phase C MANDATORY SKILLS** (invoke during C):
- svg-creator — when VARIANCE>5 or MOTION>4 → ssets/svg-props/
- pixabay-fetcher — needs PIXABAY_API_KEY → ssets/pixabay/
- gent-spawner — spawns design-agent+svg-agent+image-agent (~47% tokens)

**Phase M OPTIONAL** — skip if not video. Uses HyperFrames or Remotion.

---

## TASTE DIALS (Baseline: V=50, M=40, D=30)

| Signal | V | M | D |
|--------|---|---|---|
| minimalist/clean/editorial | 5-6 | 3-4 | 2-3 |
| premium/Apple/luxury | 7-8 | 5-7 | 3-4 |
| playful/Awwwards/agency | 9-10 | 8-10 | 3-4 |
| landing default | 7-9 | 6-8 | 3-5 |
| trust-first/public-sector | 3-4 | 2-3 | 4-5 |
| redesign preserve | match | +1 | match |
| redesign overhaul | +2 | +2 | match |

**Anti-Default Discipline**: Never default to AI-purple gradients, centered hero/dark mesh, 3 equal cards, generic glassmorphism, infinite micro-loops, Inter+slate-900. Reach past deliberately.

---

## DESIGN SYSTEM SELECTION (Official Packages Only)

| Brief | System | Package |
|-------|--------|---------|
| Microsoft/Enterprise | Fluent | @fluentui/react-components |
| Google/Material | Material 3 | @material/web |
| IBM/Analytics | Carbon | @carbon/react |
| Shopify | Polaris | polaris.js |
| Atlassian/Jira | Atlassian | @atlaskit/* |
| UK Public Sector | GOV.UK | govuk-frontend |
| US Public Sector | USWDS | uswds |
| Fast MVP | Bootstrap | ootstrap |
| Accessible React Base | Radix | @radix-ui/themes |
| Own Components | shadcn/ui | 
px shadcn@latest add ... |
| Indie SaaS | Tailwind v4 | 	ailwindcss |

**Rule**: One system/project. Copy :root verbatim from 	okens.css. Never invent hex.

---

## HARD GATES (Absolute — No Exceptions)

1. **A**: Design Read complete + dials recorded
2. **B**: Source Package verified (all assets attributed)
3. **C**: Direction Doc approved (anti-defaults applied, system chosen)
4. **D**: 	okens.css + DESIGN.md + component specs + a11y baseline
5. **E**: Template initialized with tokens, content, assets mapped
6. **F**: All impl steps done, tests pass (80%+ coverage), polish applied
7. **G**: eview-animations returns **Approve** on every element
8. **H**: WCAG 2.2 AA (47 POUR items) + CWV Good + Security clean + Lint/Typecheck clean
9. **I**: Playwright SHIP (1440/768/375, axe, CWV, visual regression)
10. **J**: 6-phase verification green (build→type→lint→test→security→diff)
11. **K**: Zero critical/high, 6-mode polish (Audit→Tighten→Harden→Animate→Live→Ship)
12. **L**: Deploy success + monitoring green
13. **M**: Anim approve + QA + caption accuracy >95% + platform specs

---

## FILES TO CREATE (Skill Structure)

`
~/.config/opencode/skills/master-website/
├── SKILL.md              # System prompt + phase guide (this file's essence)
├── README.md             # Install, usage, catalogs
├── AGENTS.md             # 13 non-negotiable rules (from repo)
├── validate.py           # 39 checks (37 must pass)
├── references/
│   ├── phase-a-intake.md           # Design Read template
│   ├── phase-b-research.md         # Research workflow
│   ├── phase-c-design-direction.md # CORE: taste-skill + Sec 10-14
│   ├── phase-d-design-system.md    # Tokenize, DESIGN.md
│   ├── phase-e-template.md         # Template selection (10-step)
│   ├── phase-f-implement.md        # Phased impl, TDD, React patterns
│   ├── phase-g-animation.md        # CORE: 6-step + 10 standards
│   ├── phase-h-engineering.md      # A11y, perf, security, quality
│   ├── phase-i-browser.md          # Playwright QA
│   ├── phase-j-test.md             # 6-phase verification
│   ├── phase-k-fix.md              # Systematic debug + 6-mode polish
│   ├── phase-l-deliver.md          # ship-it pipeline
│   ├── phase-m-video.md            # HyperFrames/Remotion pipelines
│   ├── pptx-guide.md               # Slides/presentations
│   ├── docs-guide.md               # Docs/content
│   ├── brand-guide.md              # Brand/visual systems
│   ├── animation-guide.md          # Motion reference
│   ├── video-guide.md              # Video creation
│   ├── craft/                      # 12 files (typography, color, anti-ai-slop...)
│   ├── design-systems/AGENTS.md    # 152 systems catalog
│   ├── design-templates/AGENTS.md  # 115 templates catalog
│   ├── skills/AGENTS.md            # 172 skills catalog
│   ├── dials.json                  # V/M/D defaults
│   ├── hard-gates.md               # Gate definitions
│   ├── template-selection-guide.md # 10-step process
│   ├── skill-integration-map.md    # Skill→Phase mapping
│   ├── source-attribution.md       # License/upstream tracking
│   ├── design-read-template.md     # Phase A template
│   ├── decision-record-template.md # Decision logging
│   └── prompt-examples.md          # 8 test prompts
└── (no .opencode/ in skill — global only)
`

---

## 3 MANDATORY PHASE C SKILLS (Separate Global Skills)

### 1. svg-creator (~/.config/opencode/skills/svg-creator/SKILL.md)
`yaml
name: svg-creator
description: "SVG background props (grid, gradient-mesh, circles, geometric, noise). Phase C when VARIANCE>5 or MOTION>4."
triggers: ["svg background", "gradient mesh", "grid pattern"]
od: {mode: utility, category: svg}
`
**Types**: grid (--color, --opacity, --size), gradient-mesh (--colors, --blur), circles (--count, --variance), geometric (--shape), 
oise (--opacity)
**Output**: ssets/images/svg-props/*.svg

### 2. pixabay-fetcher (~/.config/opencode/skills/pixabay-fetcher/SKILL.md)
`yaml
name: pixabay-fetcher
description: "Fetch Pixabay images for hero/texture. Phase C Sec 11. Needs PIXABAY_API_KEY."
triggers: ["hero background", "stock photo", "texture"]
od: {mode: utility, category: image}
`
**Params**: --query, --orientation, --min-width, --category, --count, --output-dir
**Output**: ssets/images/pixabay/ + ATTRIBUTION.md entries

### 3. agent-spawner (~/.config/opencode/skills/agent-spawner/SKILL.md)
`yaml
name: agent-spawner
description: "Spawn design-agent/svg-agent/image-agent for parallel Phase C. ~47% token reduction."
triggers: ["spawn agent", "parallel execution"]
od: {mode: utility, category: parallel}
`
**Protocol**: Main creates task specs → 3 sub-agents execute parallel (no shared state) → Main collects/validates

---

## INSTALLATION (User Runs Once)

`ash
# 1. Prerequisites
winget install OpenJS.NodeJS Python.Python.3.11 astral-sh.uv
uv tool install graphifyy && graphify install --platform opencode
npx playwright install chromium

# 2. Env vars (add to shell profile)
export MASTER_DESIGN_ROOT="D:\Master Design"   # or user's path
export PIXABAY_API_KEY="your-key"              # optional

# 3. Global skills (Claude Code creates these at ~/.config/opencode/skills/)
#    svg-creator/, pixabay-fetcher/, agent-spawner/, master-website/
`

---

## USAGE (After Install)

`ash
# Basic
/master-website "Build a premium SaaS landing for dev analytics tool with dark mode, scroll-reveal, pricing"

# With options
/master-website "Portfolio site" --design_system editorial --template web-prototype-taste-editorial --framework nextjs

# Video (runs Phase M)
/master-website "60s vertical launch video for SaaS — hero demo, features, pricing. Beat-synced, captions."
`

---

## UPSTREAM REFERENCES (Claude Code Can Fetch)

| Skill | Repo | Key Content |
|-------|------|-------------|
| taste-skill | Leonxlnx/taste-skill | 87KB: dials, anti-defaults, system map |
| emil-design-eng | emilkowalski/skills | Motion philosophy, spring presets |
| review-animations | emilkowalski/skills | 10 standards, Block/Approve |
| svg-creator | upbrew-tech/svg-creator-skill | SVG props generator |
| html-ppt | lewislulu/html-ppt-skill | 36 themes, presenter mode |
| vercel-guidelines | ercel-labs/web-interface-guidelines | 70+ perf rules |
| graphify | Graphify-Labs/graphify | Code graph |
| superpowers | obra/superpowers | brainstorming |

---

## VALIDATION

`ash
python validate.py
# Must output: 37 PASS, 2 FAIL (install.ps1, command file — both optional)
`

---

## TEST PROMPTS (Verify Build)

`ash
# 1. Smoke (<5KB, all gates)
/master-website "Hello world page: title, paragraph, button. Dark mode. No animations."

# 2. Full SaaS
/master-website "SaaS 'DevPulse': real-time API monitoring. Hero+live demo, 5 features, 3-tier pricing, testimonials carousel, GitHub/Discord footer. Dark, cobalt. LCP<2.5s."

# 3. Editorial Portfolio
/master-website "Designer Maya Chen portfolio: editorial, warm paper, italic serif (Atelier Zero), collage grid case studies, generous whitespace. MOTION=30, DENSITY=25."

# 4. Video (Phase M)
/master-website "60s vertical (9:16) launch video for DevPulse: hero demo 15s, features 30s, pricing/CTA 15s. Beat-synced, kinetic type, captions>95%. HyperFrames."
`

---

## CRITICAL CONSTRAINTS (Do Not Violate)

1. **GLOBAL ONLY** — Skills at ~/.config/opencode/skills/, never .opencode/ in project
2. **PHASE C MANDATORY** — Must invoke all 3 skills during C
3. **OFFICIAL PKGS** — Design systems = official npm packages, :root copied verbatim
4. **HARD GATES ABSOLUTE** — No proceeding without pass
5. **PHASE M OPTIONAL** — Skip entirely for non-video
6. **VALIDATION** — python validate.py → 37 PASS minimum
7. **ATTRIBUTION** — Every asset tracked in ATTRIBUTION.md
8. **READ-ONLY LIBRARY** — MASTER_DESIGN_ROOT never modified
9. **TOKEN EFFICIENCY** — Agent spawner for Phase C; load only needed craft via od.craft.requires
10. **NO AI DEFAULTS** — Every design decision justified by design read + dials

---

## REFERENCE REPO
https://github.com/vietnamtrainingpilot-oss/master-website-system (working implementation)

---

## DELIVERABLE
A working master-website skill at ~/.config/opencode/skills/master-website/ that passes validation and produces production websites from briefs. All 13 phases, 3 mandatory Phase C skills, 3 taste dials, hard gates, optional Phase M video.
