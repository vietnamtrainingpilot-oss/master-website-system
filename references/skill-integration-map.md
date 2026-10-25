# Master Website Skill — Integration Map

This document maps every relevant supplied skill to the website-production workflow phases. It records source, completeness, callability, and how its instructions are applied when the skill is not directly callable in OpenCode.

## Classification Key

| Tag | Meaning |
|-----|---------|
| **local-full** | Complete skill folder present in live OpenCode (`~/.config/opencode/skills/`) with full workflow, scripts, and references |
| **local-stub** | Catalogue entry in Master Design (`skills/`) pointing to upstream; requires upstream copy to run |
| **design-system** | Design system package under `design-systems/` with `DESIGN.md`, `manifest.json`, `tokens.css`, `components.html` |
| **design-template** | Renderable template under `design-templates/` with `SKILL.md`, `assets/`, `references/` |
| **reference-only** | Inspected for rules/patterns; not directly invoked |

---

## Phase A — Intake & Project Discovery

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **brainstorming** | `~/.config/opencode/skills/brainstorming/` (upstream: `obra/superpowers`) | local-full | A.1 Brief understanding, A.2 Design read, A.3 Approach selection | Directly invoked. Runs visual-companion server for mockups. Hard-gate: design doc must be approved before build. |
| **design-brief** | `D:\Master Design\skills\design-brief\SKILL.md` | local-stub | A.1 Structured brief capture | Read its `SKILL.md` for brief schema; adapt questions into intake. Upstream not vendored — use as reference. |
| **design-consultation** | `D:\Master Design\skills\design-consultation\SKILL.md` | local-stub | A.1 Stakeholder interview pattern | Reference for structured discovery questions. |

---

## Phase B — Research & Source Discovery

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **web-clone** | `D:\Master Design\skills\web-clone\SKILL.md` | local-full (scripts vendored) | B.1 Reference site recon, B.2 Asset harvest, B.3 Tech stack detection | Scripts (`recon-site.mjs`, `asset-harvest.mjs`, `network-capture.mjs`, `route-crawl.mjs`, `interaction-probe.mjs`) invoked via Node. Requires system Chrome/Edge. |
| **image-to-code** | `D:\Master Design\skills\image-to-code-skill\SKILL.md` | local-full | B.2 Visual reference generation, B.3 Design extraction | Image-first workflow: generate section images → deep analysis → extract tokens → implement. Mandates one image per section in Codex. |
| **visual-research** | `~/.config/opencode/skills/visual-research/` | local-full | B.1 Competitor visual audit, B.2 Moodboard | Direct invocation for live site screenshots and design reference gathering. |
| **research-ops** | `~/.config/opencode/skills/research-ops/` | local-full | B.1 Evidence-first research | Direct invocation for current public evidence, comparisons, enrichment. |
| **deep-research** | `~/.config/opencode/skills/deep-research/` | local-full | B.1 Multi-source cited reports | Direct invocation for deep competitive/technical research with inline citations. |
| **Graphify** | `graphify` CLI + OpenCode skill | installed | B.2 Resource library navigation | `graphify . --code-only` built code graph of Master Design. Query via `/graphify query "..."` for cross-file relationships. |

---

## Phase C — Design Direction & Taste

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **design-taste-frontend** (taste-skill) | `~/.config/opencode/skills/design-taste-frontend/` (upstream: `Leonxlnx/taste-skill`) | local-full | C.1 Design read, C.2 Dial setting (VARIANCE/MOTION/DENSITY), C.3 Design system selection, C.4 Bias correction rules | **Primary taste authority.** Directly invoked. Outputs one-line "Design Read". Enforces three dials, design-system map, typography/color/layout hard rules, anti-AI-slop patterns. |
| **taste-skill-v1** | `~/.config/opencode/skills/taste-skill-v1/` | local-full | C.1 Legacy taste reference | Reference only; v2 is default. |
| **frontend-design** | `~/.config/opencode/skills/frontend-design/` (upstream: `anthropics/skills`) | local-full | C.2 Aesthetic commitment, C.3 Real interface design, C.4 Production-grade code, C.5 Craft refinement | Directly invoked. Complements taste-skill: stack defaults (React/Next, Tailwind v4, Motion), RSC safety, icon library priority, responsiveness rules. |
| **emil-design-eng** | `~/.config/opencode/skills/emil-design-eng/` (upstream: `emilkowalski/skills`) | local-full | C.4 Invisible details, C.5 Animation philosophy, C.6 Component principles | Directly invoked for review/polish. Core philosophy: "unseen details compound", "beauty is leverage". Animation decision framework (should it animate? purpose? easing? speed?). Component rules: buttons responsive, no scale(0), popover origin-aware, tooltip instant-on-subsequent, CSS transitions over keyframes, blur for crossfade, @starting-style. |
| **emilkowalski-motion** | `~/.config/opencode/skills/emilkowalski-motion/` | local-full | C.5 Follow-up motion polish | Directly invoked after artifact exists. Adds restrained micro-interactions, reduced-motion fallbacks. |
| **impeccable-design-polish** | `~/.config/opencode/skills/impeccable-design-polish/` (upstream: `pbakaus/impeccable`) | local-full | C.6 Post-generation audit, critique, polish, animate, harden | Directly invoked as follow-up. Modes: Audit/Critique/Polish/Animate/Harden/Live. Removes AI tells, tightens copy, adds restrained motion, fixes a11y/responsive. |
| **ultimate-frontend-skills** | `~/.config/opencode/skills/ultimate-frontend-skills/` (upstream: bitwize-music plugin) | local-full | C.2 House style fallback, C.6 Section library, scaffolder, audit, engines | Directly invoked. Pipeline (`references/pipeline.md`) = 9 stages with gates. House style: editorial serif (Newsreader), warm neutrals, cinematic imagery, layered parallax, exploded views. Assets: `core.css`, `motion.js`, section library, `gradient.js`/`depth.js`/`sky.js`/`exploded.js` engines. Commands: `webdesign.mjs new/audit/look/verify`. |
| **generic-site-auditor** | `~/.config/opencode/skills/generic-site-auditor/` | local-full | C.6 Visual/UX/technical audit | Directly invoked. 6-phase workflow: Inspect → Diagnose (5 categories) → Prioritize (P0-P3) → Plan → Fix → Verify. Produces actionable remediation plan. |
| **web-design-guidelines** | `~/.config/opencode/skills/web-design-guidelines/` (upstream: `vercel-labs/web-interface-guidelines`) | local-full | C.6 Vercel Web Interface Guidelines compliance | Directly invoked. Pinned guidelines at `references/guidelines.md`. Checks layout, typography, color, motion, accessibility. |

---

## Phase D — Establish Design System

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **design-md** | `D:\Master Design\skills\design-md\SKILL.md` (upstream: `google-labs-code/skills`) | local-stub | D.1 Generate/update DESIGN.md | Catalogue entry. Read upstream for full workflow. Local stub documents the DESIGN.md format. |
| **design-system** | `~/.config/opencode/skills/design-system/` | local-full | D.1 Token architecture, component specs, slide generation | Directly invoked. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales. |
| **stitch-design-taste** | `~/.config/opencode/skills/stitch-design-taste/` | local-full | D.1 Semantic DESIGN.md generation for Google Stitch | Directly invoked. Generates agent-friendly DESIGN.md enforcing premium anti-generic standards. |
| **Default Design System** | `D:\Master Design\design-systems\default\` (DESIGN.md, manifest.json, tokens.css, components.html, USAGE.md, design-tokens.json) | design-system | D.2 Default starter system | **Primary fallback.** Machine-readable tokens in `tokens.css` (56 tokens, standard names: --bg/--surface/--fg/--muted/--border/--accent/--success/--warn/--danger, --font-display/--font-body/--font-mono, --text-*, --space-*, --radius-*, --elev-*, --focus-ring, --motion-*, --ease-standard, --container-*). `components.html` = paste-ready reference components using only var(--*). `manifest.json` = schema v1, preview pages, source evidence. |
| **110+ Design Systems** | `D:\Master Design\design-systems\<name>\` | design-system | D.2 Brand-specific systems | Each has `DESIGN.md`, `manifest.json`, `tokens.css`, `components.html`, `preview/`, `system/artifacts/`, `source/`. Selection via `template-selection-guide.md`. |
| **craft contracts** | `D:\Master Design\craft\` | reference | D.3 Cross-system constraints | Shared token schema (`craft/color.md`), anti-ai-slop (`craft/anti-ai-slop.md`), typography (`craft/typography.md`), accessibility-baseline. Lint enforces: raw hex >12 outside :root → P1; indigo laundering → P0. |

---

## Phase E — Select & Prepare Template

| Skill / Template | Source | Type | Workflow Stage | How Applied |
|------------------|--------|------|----------------|-------------|
| **web-prototype** | `D:\Master Design\design-templates\web-prototype\SKILL.md` | design-template | E.1 Primary general-purpose prototype | **Primary template.** Workflow: read `assets/template.html` (seed) → read `references/layouts.md` (8 section skeletons) → read active DESIGN.md → map tokens → compose sections → self-check via `references/checklist.md`. Outputs single `index.html`. |
| **saas-landing** | `D:\Master Design\design-templates\saas-landing\SKILL.md` | design-template | E.1 SaaS-specific landing | Inputs: product_name, tagline, has_pricing, proof_count. Parameters: hero_density, accent_strength. Outputs self-contained `index.html`. |
| **web-prototype-taste-brutalist** | `D:\Master Design\design-templates\web-prototype-taste-brutalist\SKILL.md` | design-template | E.1 Brutalist/Swiss-print aesthetic | Hard rules: newsprint substrate, carbon ink, hazard red accent, Archivo Black display, zero border-radius, 1px grid dividers, ASCII syntax. Pre-flight checklist. |
| **web-prototype-taste-editorial** | `D:\Master Design\design-templates\web-prototype-taste-editorial\SKILL.md` | design-template | E.1 Editorial-minimalist aesthetic | Warm off-white, serif display + grotesque body, 1px hairlines, pastel chips, asymmetric bento, subtle scroll-reveal. Pre-flight checklist. |
| **web-prototype-taste-soft** | `D:\Master Design\design-templates\web-prototype-taste-soft\SKILL.md` | design-template | E.1 Soft aesthetic variant | Reference for softer direction. |
| **open-design-landing** | `D:\Master Design\design-templates\open-design-landing\SKILL.md` | design-template | E.1 Atelier Zero editorial collage | Parameterized: typed `inputs.json` → `scripts/compose.ts` + `styles.css` → standalone HTML. 16 collage slots, scroll-reveal, Headroom nav. Image strategy: generate/placeholder/bring-your-own. |
| **html-ppt** | `D:\Master Design\design-templates\html-ppt\SKILL.md` | design-template | E.1 Presentation/slide deck | 36 themes, 15 full-deck templates, 31 layouts, 27 CSS animations, 20 canvas FX, presenter mode (S key). |
| **Other Templates** | `D:\Master Design\design-templates\<name>\` (100+) | design-template | E.1 Niche/page-specific | See `template-selection-guide.md` for selection procedure. |

---

## Phase F — Plan & Implement

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **writing-plans** | `~/.config/opencode/skills/writing-plans/` | local-full | F.1 Implementation plan creation | Directly invoked after design doc approved. Produces phased plan with self-contained context briefs. |
| **tdd-workflow** | `~/.config/opencode/skills/tdd-workflow/` | local-full | F.2 Test-first implementation | Directly invoked. Red→Green→Refactor with 80%+ coverage across unit/integration/E2E. |
| **test-driven-development** | `~/.config/opencode/skills/test-driven-development/` | local-full | F.2 TDD discipline | Directly invoked. Write failing test first, watch fail, minimal change to green. |
| **frontend-patterns** | `~/.config/opencode/skills/frontend-patterns/` | local-full | F.2 React/Next.js patterns | Directly invoked. Hooks discipline, server/client boundaries, Suspense+error boundaries, form actions, data fetching, state management decision trees. |
| **react-patterns** | `~/.config/opencode\skills\react-patterns\` | local-full | F.2 React 18/19 patterns | Directly invoked. |
| **vercel-react-best-practices** | `~/.config\opencode\skills\vercel-react-best-practices\` | local-full | F.2 Performance patterns | Directly invoked. 70+ rules across 8 priority categories (waterfalls, bundle, SSR, client fetching, re-render, rendering, JS micro-perf, advanced). |
| **react-performance** | `~/.config\opencode\skills\react-performance\` | local-full | F.2 Performance optimization | Directly invoked. Adapted from Vercel Engineering React Best Practices. |
| **motion-foundations** | `~/.config\opencode\skills\motion-foundations\` | local-full | F.2 Motion tokens, springs, performance | Directly invoked. Foundation layer for all motion skills. |
| **motion-patterns** | `~/.config\opencode\skills\motion-patterns\` | local-full | F.2 Production animation patterns | Directly invoked. Button, modal, toast, stagger, page transitions, exit, scroll, layout. |
| **animate** | `~/.config\opencode\skills\animate\` (upstream: emilkowalski) | local-full | F.2 Animation implementation | Directly invoked. Build sequence: should animate? purpose? tool? properties? easing/duration/spring? interruption? reduced-motion? Recipes for button, dropdown, tooltip, modal, drawer, toast, accordion, stagger, hold-to-confirm, tab indicator, scroll reveal, drag-to-dismiss. |
| **gsap-core / gsap-react / gsap-scrolltrigger** | `~/.config\opencode\skills\gsap-*\` | local-full | F.2 GSAP scroll choreography | Directly invoked. Core API, React hooks, ScrollTrigger pinning/scrub. |
| **web-clone** (scripts) | `D:\Master Design\skills\web-clone\scripts\` | local-full | F.2 Clone & adapt reference | `init-clone.mjs`, `recon-site.mjs`, `asset-harvest.mjs`, `mirror-site.mjs`, `route-crawl.mjs`, `interaction-probe.mjs`, `sourcemap-hunt.mjs`, `compare-recon.mjs`, `visual-diff.mjs`, `audit-clone.mjs`, `od-preview-rewrite.mjs`, `dna-scaffold.mjs`. |

---

## Phase G — Animation & Interaction Engineering

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **review-animations** | `~/.config\opencode\skills\review-animations\` (upstream: emilkowalski) | local-full | G.1 Animation craft review | **Primary review gate.** Ten non-negotiable standards. Aggressive escalation triggers. Remedial hierarchy (delete → reduce → fix easing → fix origin → interruptible → GPU → asymmetric → polish → a11y/cohesion). Output: Before/After/Why table + tiered verdict → Block/Approve. |
| **ui-animation** | `~/.config\opencode\skills\ui-animation\` (upstream: mblode/agent-skills) | local-full | G.1 Implementation, measurement, reverse-engineer | Directly invoked. Decision framework, spring animations, component patterns, clip-path, gesture/drag, scroll animations, performance deep-dive, debugging symptoms, SVG animation, review format, contextual animations, transition recipes, measurement guide, curve-fitting, code-output, choreography, vocabulary, interface SFX. |
| **emilkowalski-motion** | `~/.config\opencode\skills\emilkowalski-motion\` | local-full | G.2 Follow-up polish | Directly invoked. |
| **animate** | `~/.config\opencode\skills\animate\` | local-full | G.2 Build animations | Directly invoked. |
| **motion-lab** | `D:\Master Design\skills\motion-lab\SKILL.md` (upstream: yangxu128/Motion.Lab) | local-stub | G.2 160 case reference | Catalogue of 160 HTML/CSS/JS cases (basic, text, interaction, advanced). Reference via `references/index.md` → category files. Adapt to current DOM. |
| **cinematic-gsap-lenis-motion-system** | `~/.config\opencode\skills\cinematic-gsap-lenis-motion-system\` | local-full | G.2 Premium cinematic motion | Directly invoked. GSAP + ScrollTrigger + Lenis. Smooth scroll reveals, staggered text, parallax, pinned sections, magnetic hover, custom cursors. |
| **awwwards-animations** | `~/.config\opencode\skills\awwwards-animations\` | local-full | G.2 Award-level React animations | Directly invoked. GSAP ScrollTrigger, Motion, Anime.js, Lenis. Premium scroll, custom cursors, page transitions, text animations, parallax, micro-interactions, Three.js/WebGL integration. |
| **animation-vocabulary** | `~/.config\opencode\skills\animation-vocabulary\` | local-full | G.1 Reverse-lookup naming | Directly invoked. Turns vague descriptions into exact terms. |
| **find-animation-opportunities** | `~/.config\opencode\skills\find-animation-opportunities\` | local-full | G.1 Read-only opportunity scan | Directly invoked. Proposes motion with exact values; does not implement. |

---

## Phase H — Engineering & Accessibility Standards

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **frontend-a11y** | `~/.config\opencode\skills\frontend-a11y\` | local-full | H.1 Semantic HTML, ARIA, forms, keyboard, focus, screen reader | Directly invoked. Form labeling, modal/dropdown/tab patterns, focus management. |
| **accessibility** | `~/.config\opencode\skills\accessibility\` | local-full | H.1 WCAG 2.2 AA across Web/iOS/Android | Directly invoked. Semantic ARIA roles/labels, accessibility traits/hints, focus management, contrast, target size, screen-reader support. |
| **vercel-react-best-practices** | `~/.config\opencode\skills\vercel-react-best-practices\` | local-full | H.2 Performance, bundle, SSR, re-render | Directly invoked. |
| **react-performance** | `~/.config\opencode\skills\react-performance\` | local-full | H.2 70+ perf rules | Directly invoked. |
| **coding-standards** | `~/.config\opencode\skills\coding-standards\` | local-full | H.3 Cross-project conventions | Directly invoked. Naming, readability, immutability, code-quality review. |
| **design-is** | `~/.config\opencode\skills\design-is\` | local-full | H.3 Dieter Rams audit → plan | Directly invoked. Audits against 10 principles, hands off `/make-plan` for new/refine/redesign. |

---

## Phase I — Run & Inspect (Browser Automation)

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **browser-qa** | `~/.config\opencode\skills\browser-qa\` | local-full | I.1 Post-deploy UI verification | Directly invoked. Playwright: console errors, Core Web Vitals, form/auth flows, 3-breakpoint screenshots, axe-core a11y. SHIP/DO-NOT-SHIP verdict. |
| **ui-demo** | `~/.config\opencode\skills\ui-demo\` | local-full | I.1 Polished demo recording | Directly invoked. Playwright: visible cursor, natural pacing, WebM output. |
| **playwright** (MCP) | `playwright` MCP server | installed | I.1 Browser automation | Direct tool calls: navigate, snapshot, click, fill, evaluate, screenshot, network requests, console messages. |

---

## Phase J — Test, Review, Verify

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **verification-loop** | `~/.config\opencode\skills\verification-loop\` | local-full | J.1 Six-phase verification | Directly invoked. Build → type check → lint → tests with coverage → security grep → diff review → PASS/FAIL report. |
| **verification-before-completion** | `~/.config\opencode\skills\verification-before-completion\` | local-full | J.1 Evidence before assertions | Directly invoked. Runs verification commands, confirms output before success claims. |
| **lint-check** | tool | built-in | J.2 Linting | Auto-detects linter (Biome, ESLint, Ruff, etc.). |
| **format-code** | tool | built-in | J.2 Formatting | Auto-detects formatter (Biome, Prettier, Black, etc.). |
| **run-tests** | tool | built-in | J.2 Test suite | Auto-detects package manager + test framework. |
| **check-coverage** | tool | built-in | J.2 Coverage threshold | Reads coverage reports. |
| **security-audit** | `~/.config\opencode\skills\security-audit\` | local-full | J.3 Security scan | Directly invoked. Dependencies, secrets, code. |
| **codehealth-mcp** | `~/.config\opencode\skills\codehealth-mcp\` | local-full | J.3 CodeScene structural health | Directly invoked. Review before edits, verify score deltas, gate commits/PRs. |
| **ponytail-review** | `~/.config\opencode\skills\ponytail-review\` | local-full | J.3 YAGNI code review | Directly invoked. Finds reinvented stdlib, needless deps, speculative abstractions. One line per finding. |

---

## Phase K — Fix & Refine

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **systematic-debugging** | `~/.config\opencode\skills\systematic-debugging\` | local-full | K.1 Bug diagnosis before fixes | Directly invoked. Use on any bug/test failure/unexpected behavior. |
| **receiving-code-review** | `~/.config\opencode\skills\receiving-code-review\` | local-full | K.2 Review feedback processing | Directly invoked. Technical rigor, verification, not performative agreement. |
| **impeccable-design-polish** | `~/.config\opencode\skills\impeccable-design-polish\` | local-full | K.3 Polish/Harden/Live modes | Directly invoked. Fixes mobile overflow, text clipping, contrast, missing states, broken links, fragile layouts. |

---

## Phase L — Deliver

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **ship-it** | `~/.config\opencode\skills\ship-it\` | local-full | L.1 End-to-end delivery | Directly invoked. Process-to-result: decide, plan, build, verify, secure, perform, ship. |
| **conventional-commit-review** | `~/.config\opencode\skills\conventional-commit-review\` | local-full | L.2 Commit message | Directly invoked. Drafts Conventional Commits message. |
| **finishing-a-development-branch** | `~/.config\opencode\skills\finishing-a-development-branch\` | local-full | L.3 Integration decision | Directly invoked. When implementation complete, tests pass, decide how to integrate. |

---

## Cross-Phase / Infrastructure

| Skill | Source | Type | Workflow Stage | How Applied |
|-------|--------|------|----------------|-------------|
| **Graphify** | `graphify` CLI + OpenCode skill | installed | All (navigation) | Code graph of Master Design + project. Query via `/graphify query`. |
| **superpowers:writing-plans** | `~/.config\opencode\skills\writing-plans\` | local-full | F.1 | Directly invoked. |
| **superpowers:executing-plans** | `~/.config\opencode\skills\executing-plans\` | local-full | F.2 | Directly invoked. |
| **subagent-driven-development** | `~/.config\opencode\skills\subagent-driven-development\` | local-full | F.2 Parallel execution | Directly invoked. |
| **dispatching-parallel-agents** | `~/.config\opencode\skills\dispatching-parallel-agents\` | local-full | F.2 Independent tasks | Directly invoked. |
| **using-git-worktrees** | `~/.config\opencode\skills\using-git-worktrees\` | local-full | F.2 Isolation | Directly invoked. |
| **agent-architecture-audit** | `~/.config\opencode\skills\agent-architecture-audit\` | local-full | Meta | Audits 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures. |
| **agent-self-evaluation** | `~/.config\opencode\skills\agent-self-evaluation\` | local-full | Meta | Self-rates output on 5 axes. |
| **continuous-learning-v2** | `~/.config\opencode\skills\continuous-learning-v2\` | local-full | Meta | Instinct-based learning via hooks. |

---

## Conflict Resolution Rules

1. **Taste authority**: `design-taste-frontend` (taste-skill) is primary for aesthetic decisions. `frontend-design` provides stack defaults. `emil-design-eng` provides component/motion philosophy. `ultimate-frontend-skills` is fallback house style.
2. **Animation review**: `review-animations` is the hard gate. `animate` and `ui-animation` implement; `review-animations` approves/blocks.
3. **Design system**: Active DESIGN.md (from selected design system) is the single source of truth for tokens. `design-md`/`stitch-design-taste` generate it; `design-system` manages it.
4. **Template**: `web-prototype` is primary general template. Specialized templates (`saas-landing`, `open-design-landing`, taste variants) selected via `template-selection-guide.md`.
5. **Accessibility**: `frontend-a11y` + `accessibility` + `vercel-react-best-practices` + `web-design-guidelines` all apply. Most restrictive wins.
6. **Verification**: `verification-loop` + `verification-before-completion` are mandatory gates. `browser-qa` for deployed preview.
7. **Source preservation**: Never modify files under `D:\Master Design\`. Copy to working directory, rename, adapt there.
8. **Attribution**: Preserve all LICENSE, SOURCES.md, upstream URLs, manifest `source` fields. Record in `source-attribution.md`.

---

## Upstream Sources Requiring Manual Install

| Skill | Upstream URL | Install Instruction |
|-------|--------------|---------------------|
| brainstorming (full) | https://github.com/obra/superpowers | Copy upstream `skills/brainstorming/` to active agent skills dir |
| design-md | https://github.com/google-labs-code/skills | Copy upstream to active agent skills dir |
| design-taste-frontend | https://github.com/Leonxlnx/taste-skill | Already installed as local-full |
| emil-design-eng | https://github.com/emilkowalski/skills | Already installed as local-full |
| web-clone | https://github.com/Jane-xiaoer/claude-skill-web-clone | Already adapted in Master Design |
| image-to-code | https://github.com/Leonxlnx/taste-skill | Already installed as local-full |
| html-ppt | https://github.com/lewislulu/html-ppt-skill | `npx skills add https://github.com/lewislulu/html-ppt-skill` |
| motion-lab | https://github.com/yangxu128/Motion.Lab | Catalogue only; reference files in Master Design |
| web-design-guidelines | https://github.com/vercel-labs/web-interface-guidelines | Already installed as local-full (pinned) |

---

## Live OpenCode Skills Not in Master Design (Supplemental)

These are available in the live environment and should be invoked where relevant:

- `agent-architecture-audit`, `agent-eval`, `agent-harness-construction`, `agent-introspection-debugging`, `agent-payment-x402`, `agent-runtime-gateway-smoke-test`, `agent-security-hardening`, `agent-self-evaluation`, `agent-sort`
- `autonomous-agent-harness`, `autonomous-loops`, `autoresearch`, `awwwards-animations`
- `backend`, `backend-patterns`, `benchmark`, `benchmark-methodology`, `benchmark-optimization-loop`
- `bengali-nlp`, `blender-motion-state-inspection`, `blueprint`, `brand`, `brand-discovery`, `brand-voice`, `brandkit`
- `canary-watch`, `canvas`, `carrier-relationship-management`, `ccs-align`, `change-impact`
- `claude-devfleet`, `claude-mem-install`, `claude-security`, `click-path-audit`, `clickhouse-io`
- `cloud-sync`, `cloud-uploader`, `config-gc`, `configure`, `configure-ecc`, `connections-optimizer`
- `content-engine`, `content-hash-cache-pattern`, `context-and-decisions`, `context-budget`
- `continuous-agent-loop`, `continuous-learning-v2`, `contract-first`, `conventional-commit-review`
- `cpp-coding-standards`, `cpp-testing`, `counterparty-channel-discipline`, `customize-opencode`
- `customs-trade-compliance`, `dart-flutter-patterns`, `dashboard-builder`, `data-scraper-agent`
- `data-throughput-accelerator`, `database-migrations`, `deep-research`, `deepseek-harness-setup`
- `defi-amm-security`, `defuddle`, `delivery-gate`, `deployment-patterns`, `docker-patterns`
- `docs-governance`, `document-hunter`, `documentation-lookup`, `dotnet-patterns`
- `e2e-testing`, `ecc-guide`, `ecc-recipes`, `ecc-tools-cost-audit`, `email-ops`
- `energy-procurement`, `enhance-prompt`, `enterprise-agent-ops`, `error-handling`
- `esign-field-placement`, `eval-harness`, `evm-token-decimals`, `exa-search`, `executing-plans`
- `explicit-checker`, `faceless-explainer`, `fal-ai-media`, `fastapi-patterns`
- `figma`, `finance-billing-ops`, `find-animation-opportunities`, `finishing-a-development-branch`
- `fixing-motion-performance`, `flox-environments`, `flutter-dart-code-review`
- `foundation-models-on-device`, `frontend-a11y`, `frontend-design-direction`, `frontend-patterns`
- `frontend-slides`, `fsharp-testing`, `full-output-enforcement`, `gan-style-harness`
- `gateguard`, `general-video`, `generating-python-installer`, `generic-site-auditor`
- `golang-patterns`, `golang-testing`, `google-workspace-ops`, `growth-log`
- `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `health-check`, `healthcare-cdss-patterns`
- `healthcare-emr-patterns`, `healthcare-eval-harness`, `healthcare-phi-compliance`
- `help`, `hermes-imports`, `hexagonal-architecture`, `high-end-visual-design`
- `hipaa-compliance`, `homelab-network-readiness`, `homelab-network-setup`, `homelab-pihole-dns`
- `homelab-vlan-segmentation`, `homelab-wireguard-vpn`, `hookify-rules`, `host-observer`
- `how-it-works`, `hyperframes`, `hyperframes-animation`, `hyperframes-audio`, `hyperframes-cli`
- `hyperframes-core`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-registry`
- `hyperframes-studio`, `i18n-sync`, `image-to-code`, `imagegen-frontend-mobile`, `imagegen-frontend-web`
- `img2threejs`, `impeccable`, `impeccable-design-polish`, `import-art`, `import-audio`, `import-track`
- `improve-animations`, `industrial-brutalist-ui`, `inherit-legacy-style`, `intent-driven-development`
- `inventory-demand-planning`, `investor-materials`, `investor-outreach`, `ios-icon-gen`
- `iterative-retrieval`, `ito-baskets`, `ito-compute`, `ito-inference`, `ito-training`
- `java-coding-standards`, `jira-integration`, `jpa-patterns`, `knowledge-agent`, `knowledge-ops`
- `kotlin-coroutines-flows`, `kotlin-exposed-patterns`, `kotlin-ktor-patterns`, `kotlin-patterns`
- `kotlin-testing`, `kubernetes-patterns`, `laravel-patterns`, `laravel-plugin-discovery`
- `laravel-security`, `laravel-tdd`, `laravel-verification`, `latency-critical-systems`
- `lead-intelligence`, `learn-codebase`, `link-prospecting`, `liquid-glass-design`
- `living-docs-governance`, `llm-trading-agent-security`, `local-seo`, `logistics-exception-management`
- `make-interfaces-feel-better`, `make-plan`, `manim-video`, `market-research`
- `marketing-campaign`, `master-agreement-generator`, `mastering-engineer`
- `mcp-dependency-review`, `mcp-server-patterns`, `media-use`, `mem-search`, `mem-setup`
- `messages-ops`, `minimalist-ui`, `mix-engineer`, `ml-adoption-playbook`, `mle-workflow`
- `mode-creator`, `module-regression`, `motion-advanced`, `motion-foundations`, `motion-graphics`
- `motion-patterns`, `music-to-video`, `mybatis-patterns`, `mysql-patterns`
- `nanoclaw-repl`, `nasiko-control-plane`, `nestjs-patterns`, `netmiko-ssh-automation`
- `network-bgp-diagnostics`, `network-config-validation`, `network-interface-health`
- `new-album`, `next-step`, `nextjs-turbopack`, `nodejs-keccak256`
- `nutrient-document-processing`, `nuxt4-patterns`, `obsidian-bases`, `obsidian-cli`
- `obsidian-markdown`, `oh-my-issues`, `openclaw-persona-forge`, `opensource-pipeline`
- `operator-approval-loop`, `orch-add-feature`, `orch-build-mvp`, `orch-change-feature`
- `orch-fix-defect`, `orch-pipeline`, `orch-refine-code`, `osint-investigation`
- `parallel-execution-optimizer`, `pathfinder`, `payments`, `perl-patterns`, `perl-security`
- `perl-testing`, `pick-ui-library`, `plagiarism-checker`, `plan-canvas`, `plan-orchestrate`
- `plankton-code-quality`, `ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`
- `ponytail-help`, `ponytail-review`, `postgres-patterns`, `prediction-market-oracle-research`
- `prediction-market-risk-review`, `prisma-patterns`, `product-capability`, `product-launch-video`
- `product-lens`, `production-audit`, `production-scheduling`, `project-flow-ops`
- `promo-director`, `promo-reviewer`, `promo-writer`, `promote-idea`, `prompt-caching-strategy`
- `prompt-engineering-patterns`, `prompt-optimizer`, `pronunciation-specialist`, `prototype`
- `ptfs-va-website-builder`, `python-patterns`, `python-testing`, `pytorch-patterns`
- `quality-nonconformance`, `quarkus-patterns`, `quarkus-security`, `quarkus-tdd`
- `quarkus-verification`, `rails-patterns`, `ralphinho-rfc-pipeline`
- `react-native-patterns`, `react-patterns`, `react-performance`, `react-testing`
- `recsys-pipeline-architect`, `recursive-decision-ledger`, `redesign-existing-projects`
- `redis-patterns`, `regex-vs-llm-structured-text`, `release-director`, `remotion-*`
- `rename`, `repo-scan`, `requesting-code-review`, `research-ops`, `researcher`
- `researchers-*`, `resume`, `returns-reverse-logistics`, `review-animations`, `rules-distill`
- `rust-patterns`, `rust-testing`, `safety-guard`, `santa-method`, `save`
- `scientific-db-pubmed-database`, `scientific-db-uspto-database`, `scientific-pkg-gget`
- `scientific-thinking-literature-review`, `scientific-thinking-scholar-evaluation`
- `scroll-craft`, `search-first`, `security`, `security-bounty-hunter`, `security-review`
- `security-scan`, `seo`, `seo-audit`, `seo-coach`, `seo-project-setup`, `seo-report`
- `session-start`, `setup`, `sheet-music-publisher`, `ship-it`, `skill-comply`
- `skill-host-compat`, `skill-scout`, `skill-stocktake`, `slides`, `slideshow`
- `smart-explore`, `social-graph-ranker`, `social-publisher`, `springboot-patterns`
- `springboot-security`, `springboot-tdd`, `springboot-verification`, `standup`
- `stitch-design-taste`, `story-lifecycle`, `strategic-compact`, `subagent-driven-development`
- `suno-engineer`, `swift-actor-persistence`, `swift-concurrency-6-2`, `swift-protocol-di-testing`
- `swiftui-patterns`, `systematic-debugging`, `talking-head-recut`, `taste`, `taste-application`
- `taste-distillation`, `tasteforge-video`, `tdd-workflow`, `team-agent-orchestration`
- `team-builder`, `terminal-opener`, `terminal-ops`, `test`, `test-collaboration`
- `test-driven-development`, `think`, `timeline-report`, `tinystruct-patterns`
- `token-budget-advisor`, `token-card`, `tutorial`, `ui-demo`, `ui-styling`, `ui-to-vue`
- `ui-ux-pro-max`, `uncloud`, `unified-memory`, `unified-notifications-ops`
- `using-git-worktrees`, `using-superpowers`, `validate-album`, `vercel-react-best-practices`
- `verification-loop`, `verification-before-completion`, `verify-sources`, `version-bump`
- `vibe-code`, `video-editing`, `video-production`, `videodb`, `visa-doc-translate`
- `visual-research`, `vite-patterns`, `voice-checker`, `vue-patterns`, `watch`
- `web-design`, `weekly-digests`, `what-the`, `wiki`, `wiki-cli`, `wiki-fold`, `wiki-ingest`
- `wiki-lint`, `wiki-mode`, `wiki-query`, `wiki-retrieve`, `windows-desktop-e2e`
- `workspace-surface-audit`, `wowerpoint`, `write-swift`, `writing-plans`, `writing-skills`
- `x-api`

(These are listed for completeness; the master-website skill invokes only the subset mapped above.)