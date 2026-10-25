# Master Website — Template Selection Guide

This guide teaches the agent how to identify, select, inspect, reuse, copy, rename, and validate design systems, template bundles, example files, HTML starters, components, and animation resources from the supplied `Master Design/` library.

**Golden Rule:** Never change the original source file when the goal is to create a modified working copy. Preserve originals; copy to the new website's working directory and adapt there.

---

## 1. Selection Procedure (Mandatory)

Before choosing any resource, the agent **must** execute these steps in order:

### Step 1 — Understand the Output Requirements
- Target output type: marketing site, SaaS landing, portfolio, dashboard, editorial, presentation, web app, etc.
- Required functionality: pages/routes, forms, auth, data fetching, animations, CMS, etc.
- Brand constraints: existing logo, colors, type, photography, voice.
- Technical constraints: framework, existing styles, accessibility level, performance budget, export target.
- Acceptance criteria: what "done" looks like.

### Step 2 — Search the Resource Library
Use recursive search, manifests, the complete inventory (`source-inventory.jsonl`), Graphify queries, and source instructions to discover candidates in:
- `design-templates/` — renderable starters (websites, decks, dashboards, prototypes)
- `design-systems/` — visual/implementation contracts (tokens, components, previews)
- `skills/` — functional workflows (some contain templates/assets)
- `craft/` — cross-system constraints (token schema, anti-ai-slop, typography)
- `frames/` — device mockup wrappers

**Graphify queries that help:**
```
/graphify query "design templates for saas landing"
/graphify query "design systems with cobalt accent"
/graphify query "templates with scroll reveal motion"
/graphify path "web-prototype" "saas-landing"
```

### Step 3 — Identify Purpose of Each Candidate
For each promising candidate, determine:
- Is it a **functional skill** (does work), **design system** (defines look), **design template** (starter), or **example file** (demo only)?
- What output type does it produce? (HTML page, React app, deck, dashboard, etc.)
- What are its declared triggers, inputs, parameters, outputs?

### Step 4 — Read Complete Instructions
Read the candidate's **full** relevant files:
- `SKILL.md` (frontmatter + body)
- `README.md`, `USAGE.md`, `AGENTS.md`
- `manifest.json` (design systems)
- `DESIGN.md` (design systems)
- `references/checklist.md`, `references/layouts.md`, `references/animations.md` (templates)
- `LICENSE`, `SOURCES.md`, upstream URLs

### Step 5 — Inspect Actual Implementation
Open and inspect:
- `assets/template.html` or `example.html` — the **canonical starter**
- `components.html` — reference components using only `var(--token)`
- `tokens.css` — machine-readable token bindings
- `preview/*.html` — visual sanity checks
- `scripts/*.ts/.mjs/.py` — composers, generators, validators
- `styles.css` — inlined stylesheet for templates

### Step 6 — Determine Canonical Starter vs Examples
**Critical distinction:**
| File Role | How to Identify | Action |
|-----------|----------------|--------|
| **Canonical starter** | Referenced in `SKILL.md` as seed/entry; `manifest.json` `files.design` or `preview.entry`; `assets/template.html` | **Copy & rename** to working dir (e.g., `index.html`) |
| **Example/preview** | Named `example.html`, `preview/*.html`, `examples/*.html`; demo data | **Reference only** — do not copy as starter |
| **Component/effect** | Partial snippet in `components.html`, `references/layouts.md`, `assets/*.html` | **Copy selectively** into working copy |
| **Asset** | `assets/*.png`, `assets/fonts/`, `assets/images/` | **Copy preserving relative paths** |

### Step 7 — Verify Licensing, Compatibility, Suitability
- License: `LICENSE` file, `manifest.json` `source.license`, `SKILL.md` `license` field
- Technical compatibility: framework, CSS approach, token schema, motion library
- Functionality: does the template actually implement the routes/components needed?
- Dependencies: declared in `capabilities_required`, `package.json`, `scripts/` imports

### Step 8 — Compare Candidates (Decision Table)
When multiple credible options exist, use a weighted scoring table:

| Criterion | Weight | Candidate A | Candidate B | Candidate C |
|-----------|--------|-------------|-------------|-------------|
| Output type match | 30% | | | |
| Design system compatibility | 25% | | | |
| Functional completeness | 20% | | | |
| License permissiveness | 10% | | | |
| Motion/animation support | 10% | | | |
| Maintenance burden | 5% | | | |
| **Total** | **100%** | | | |

### Step 9 — Choose Primary Starter & Supporting Systems
- Select **one** primary template as the canonical starter
- Identify compatible design system(s) for tokens/components
- List companion files that must be copied together
- Record selection rationale and rejected alternatives

### Step 10 — Record Decision
Create a **Resource Selection Decision Record** (see Section 2) for the project.

---

## 2. Resource Selection Decision Record (Per Project)

For each website project, document:

```markdown
# Resource Selection Decision Record

## Target Output & Essential Requirements
- Type: [e.g., SaaS marketing landing, 5 sections, hero + features + pricing + testimonial + CTA]
- Framework: [e.g., plain HTML/CSS/JS, React/Next.js, Astro]
- Brand: [existing assets or "new"]
- Motion: [e.g., scroll-reveal, stagger, reduced-motion required]
- A11y: [WCAG 2.2 AA target]

## Primary Template
- **Name**: [e.g., web-prototype]
- **Source Path**: `D:\Master Design\design-templates\web-prototype\`
- **Canonical Entry**: `assets/template.html` → copy as `index.html`
- **Companion Files**: `assets/template.html` (seed), `references/layouts.md` (8 section skeletons), `references/checklist.md` (P0/P1/P2), `styles.css` (if separate)

## Design System
- **Name**: [e.g., default / Neutral Modern]
- **Source Path**: `D:\Master Design\design-systems\default\`
- **Token File**: `tokens.css` (56 standard tokens, paste `:root` block verbatim)
- **Component Ref**: `components.html` (paste-ready classes)
- **Manifest**: `manifest.json` (schema v1, preview pages)

## Candidate Examples Examined
| Candidate | Type | Why Rejected |
|-----------|------|--------------|
| saas-landing | design-template | Too opinionated for generic brief; requires product_name/tagline inputs |
| web-prototype-taste-editorial | design-template | Aesthetic too specific (serif display, pastel chips) without brief justification |
| open-design-landing | design-template | Requires typed inputs.json + 16 collage assets; overkill for simple landing |
| html-ppt | design-template | Output is deck, not website |

## Canonical Entry File
- `D:\Master Design\design-templates\web-prototype\assets\template.html` → copy to `./index.html`

## Companion Files to Copy
| Source | Destination | Purpose |
|--------|-------------|---------|
| `design-templates/web-prototype/assets/template.html` | `./index.html` | Seed HTML (tokens + class system + chrome) |
| `design-systems/default/tokens.css` | `./tokens.css` | Machine-readable token bindings (paste `:root` into `<style>`) |
| `design-systems/default/components.html` | `./references/components.html` | Component class reference |
| `design-templates/web-prototype/references/layouts.md` | `./references/layouts.md` | 8 section skeletons |
| `design-templates/web-prototype/references/checklist.md` | `./references/checklist.md` | P0/P1/P2 self-review |

## Dependencies & Asset Relationships
- Template expects `tokens.css` `:root` variables pasted into `<style>` before component classes
- `layouts.md` sections use classes defined in `template.html` `<style>` — keep in sync
- `checklist.md` references DESIGN.md rules (accent budget, type scale, responsive breakpoints)
- No external JS required (vanilla CSS/IntersectionObserver only)

## Applicable License & Attribution
- Template: MIT (see `design-templates/web-prototype/LICENSE` or upstream)
- Design System: Apache-2.0 (bundled fixture, `manifest.json` source.type=bundle)
- Preserve `LICENSE`, `SOURCES.md`, `manifest.json` `source` fields in working copy

## Technical Compatibility & Limitations
- Template: vanilla HTML/CSS/JS — works in any framework or static host
- Tokens: standard names (`--bg`, `--surface`, `--fg`, `--muted`, `--border`, `--accent`, `--font-display`, `--font-body`, `--font-mono`, `--text-*`, `--space-*`, `--radius-*`, `--elev-*`, `--focus-ring`, `--motion-*`, `--ease-standard`, `--container-*`)
- Motion: CSS `@starting-style` + IntersectionObserver reveals (no library)
- Responsive: media queries at 1024px/639px breakpoints (matches DESIGN.md)
- Dark mode: not built-in; add `dark:` variants or CSS variable swap if needed

## Selection Rationale
`web-prototype` chosen because:
1. General-purpose, minimal opinions — adapts to any brief via DESIGN.md tokens
2. Seed (`template.html`) encodes good defaults (typography, spacing, accent budget)
3. Layout library (`layouts.md`) provides 8 paste-ready section skeletons
4. Self-check (`checklist.md`) enforces P0/P1/P2 quality gates
5. Zero external dependencies — plain HTML/CSS/JS
6. Explicit `data-od-id` tagging for comment mode compatibility

## Changes Made to Working Copy
- [ ] Pasted DESIGN.md tokens into `index.html` `<style>` `:root` block
- [ ] Replaced page `<title>` and topnav brand
- [ ] Composed sections from `layouts.md` into `<main id="content">`
- [ ] Replaced `[REPLACE]` placeholders with real copy
- [ ] Swapped `.ph-img` scaffolding for real images (or labeled placeholders)
- [ ] Ran `checklist.md` P0 items — all pass
- [ ] Verified responsive at 1440w, 768w, 375w
```

---

## 3. Copy & Rename Procedure (Canonical)

When a suitable template/example is selected:

1. **Identify the canonical source file** from its actual instructions (`SKILL.md`, `manifest.json`, `USAGE.md`).
2. **Preserve the original file and its filename unchanged.**
3. **Copy the source file to the new website's working directory.**
4. **Rename the copied file** to suit the deliverable (`index.html`, route file, component filename).
5. **Copy required companion files** (stylesheets, scripts, images, fonts, data, config) preserving relative-path relationships.
6. **Verify the initial copy** against the original (diff or checksum).
7. **Record the source→destination mapping and required attribution.**
8. **Customize the working copy** to satisfy the actual brief.
9. **Validate the resulting site** (every asset path, dependency, route, interaction).

### Worked Example: `web-prototype` → New Site

**Source:** `D:\Master Design\design-templates\web-prototype\assets\template.html`
**Confirmed by:** `SKILL.md` Step 1 ("Read `assets/template.html` end-to-end"), `manifest.json` would list it as seed.

```bash
# 1. Create working directory
mkdir -p ./my-site
cd ./my-site

# 2. Copy canonical starter
cp "D:\Master Design\design-templates\web-prototype\assets\template.html" ./index.html

# 3. Copy design system tokens
cp "D:\Master Design\design-systems\default\tokens.css" ./tokens.css

# 4. Copy layout library & checklist
cp -r "D:\Master Design\design-templates\web-prototype\references" ./references

# 5. (Optional) Copy design system component reference
cp "D:\Master Design\design-systems\default\components.html" ./references/components.html

# 6. Verify copy
diff "D:\Master Design\design-templates\web-prototype\assets\template.html" ./index.html
# Should show no differences
```

**Now adapt `index.html`:**
- Paste `:root` block from `tokens.css` into `<style>` (replaces seed's hardcoded tokens)
- Replace `<title>` and topnav brand
- Plan section list (Step 2 of template workflow)
- For each section: copy `<section>` block from `references/layouts.md` into `<main id="content">`
- Replace `[REPLACE]` strings with real copy
- Replace `.ph-img` blocks with real `<img class="content-img">` (or labeled placeholders)
- Run `references/checklist.md` P0 items

---

## 4. Validation Checklist for Selection

Before declaring selection complete, verify:

- [ ] **Canonical starter identified** from template's own instructions (not guessed from filename)
- [ ] **Original source unchanged** — no modifications to files under `D:\Master Design\`
- [ ] **All companion files copied** with relative paths preserved
- [ ] **License & attribution recorded** — `LICENSE`, `SOURCES.md`, upstream URL, manifest `source`
- [ ] **Technical compatibility confirmed** — framework, CSS approach, token schema, motion lib
- [ ] **Functional completeness checked** — template actually implements needed routes/components
- [ ] **Decision record created** with rationale and rejected alternatives
- [ ] **Graphify query cross-checked** — no better candidate missed

---

## 5. Worked Cases from Actual Inspected Files

### Case 1: SaaS Landing Page → `saas-landing`

**Brief:** "Build a SaaS landing page for a dev tool with hero, features, pricing, testimonials."

**Inspection:**
- `design-templates/saas-landing/SKILL.md` declares: inputs `product_name`, `tagline`, `has_pricing`, `proof_count`; parameters `hero_density`, `accent_strength`; output `index.html`; requires DESIGN.md.
- No `assets/template.html` — skill generates from scratch per workflow.
- Workflow: read DESIGN.md → plan sections (hero, features, social proof, pricing, footer CTA, footer) → apply tokens → write self-contained HTML.

**Decision:** Use `saas-landing` **as the generating skill**, not as a template to copy. The skill *is* the generator. Pair with selected design system (e.g., `default`).

**Copy/Rename:** N/A — skill writes `index.html` directly. Design system tokens copied from `design-systems/default/tokens.css`.

### Case 2: General Marketing Site → `web-prototype`

**Brief:** "Build a marketing site for a design agency with portfolio, services, about, contact."

**Inspection:**
- `design-templates/web-prototype/SKILL.md` Step 1: "Read `assets/template.html` end-to-end" — this is the seed.
- `assets/template.html` exists (523 lines), contains full `:root` tokens, class system, hero-grid, features-grid, form-row, form, cards, buttons, inputs, badges, links, kbd.
- `references/layouts.md` has 8 section skeletons (hero, features, stats/quote, split, log list, comparison table, cta, footer).
- `references/checklist.md` has P0/P1/P2 items.
- `USAGE.md` says: read SKILL.md → DESIGN.md → paste tokens.css → use components.manifest.json → components.html → preview pages.

**Decision:** `web-prototype` is the **primary general template**. Copy `assets/template.html` → `index.html`, paste DESIGN.md tokens, compose sections from `layouts.md`.

### Case 3: Brutalist Portfolio → `web-prototype-taste-brutalist`

**Brief:** "Build a brutalist portfolio for a designer — Swiss print, raw borders, hazard red."

**Inspection:**
- `design-templates/web-prototype-taste-brutalist/SKILL.md` has hard rules: newsprint `#F4F4F0`/`#EAE8E3`, carbon ink `#050505`, hazard red `#E61919`, Archivo Black display, `border-radius: 0`, 1px grid dividers, ASCII syntax.
- Pre-flight checklist: 7 items.
- No separate `assets/template.html` — skill defines aesthetic directly in SKILL.md.
- Source: distilled from `Leonxlnx/taste-skill` brutalist-skill §2.1.

**Decision:** Use this skill **as the aesthetic director**. It does not provide a starter HTML file; the agent must implement from the hard rules. Pair with `web-prototype` seed for structure, or build from scratch per rules.

**Copy/Rename:** No starter to copy. Create `index.html` implementing the hard rules. Design system = custom tokens from SKILL.md.

### Case 4: Editorial Collage Landing → `open-design-landing`

**Brief:** "Build an editorial landing page like open-design's own site with collage assets."

**Inspection:**
- `design-templates/open-design-landing/SKILL.md`: parameterized workflow — `inputs.json` + `styles.css` → `scripts/compose.ts` → standalone HTML.
- 16 collage slots, scroll-reveal, Headroom nav.
- Image strategy: `generate` (fal.ai gpt-image-2), `placeholder` (SVG frames), `bring-your-own`.
- `inputs.example.json` = OpenDesign worked example.
- `scripts/compose.ts` reads typed `inputs.json` and inlines `styles.css`.
- `scripts/placeholder.ts` generates 16 SVG paper-textured frames.
- `scripts/imagegen.ts` calls fal.ai for gpt-image-2.

**Decision:** Use this **full pipeline** when brief wants Atelier Zero aesthetic + collage assets. Requires Node/tsx runtime, fal.ai key for generation.

**Copy/Rename:**
```bash
cp -r "D:\Master Design\design-templates\open-design-landing" ./my-landing
cd ./my-landing
# Fill inputs.json from brief
# Choose image_strategy: placeholder (fast, free) or generate (needs FAL_KEY)
npx tsx scripts/placeholder.ts ./assets/   # or npx tsx scripts/imagegen.ts inputs.json --out=./assets/
npx tsx scripts/compose.ts inputs.json ./index.html
# Verify: open ./index.html, check 16 images load, scroll-reveal works, responsive
```

### Case 5: Presentation/Deck → `html-ppt`

**Brief:** "Create a consulting-style slide deck for a client pitch."

**Inspection:**
- `design-templates/html-ppt/SKILL.md`: 36 themes, 15 full-deck templates, 31 layouts, 27 CSS animations, 20 canvas FX, presenter mode (S key).
- `scripts/new-deck.sh` scaffolds from `templates/deck.html`.
- `scripts/render.sh` uses managed Chromium for PNG export.
- Presenter mode: magnetic cards (CURRENT/NEXT/SCRIPT/TIMER) via `runtime.js`.
- Full-deck templates: `pitch-deck`, `product-launch`, `tech-sharing`, `weekly-report`, `course-module`, `presenter-mode-reveal`, etc.

**Decision:** Use `html-ppt` when output is a **deck**, not a website. Different `od.mode: deck`.

**Copy/Rename:**
```bash
cd "D:\Master Design\design-templates\html-ppt"
./scripts/new-deck.sh my-pitch
# Edit examples/my-pitch/index.html: pick theme (T key), copy layouts from templates/single-page/, add notes in <div class="notes">
./scripts/render.sh examples/my-pitch/index.html 12  # export 12 slides to PNG
```

### Case 6: No Suitable Template Found → Custom Build

**Brief:** "Build a real-time collaborative whiteboard with WebGL rendering."

**Inspection:**
- No template in `design-templates/` matches "collaborative whiteboard WebGL".
- `design-templates/webgl-experience` exists but is a demo, not a starter.
- `skills/threejs` exists but is a functional skill, not a template.

**Decision:** No appropriate template. Build custom:
1. Select design system (e.g., `default` or `dark-tech`).
2. Use `ultimate-frontend-skills` house style + `threejs` skill for WebGL.
3. Scaffold minimal HTML + `core.css` + `motion.js` + `exploded.js`/`depth.js` engines.
4. Implement canvas/WebGL layer separately.

**Record:** "No template matched output type (WebGL app). Custom build from design system + engine skills."

---

## 6. Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Correct Approach |
|--------------|----------------|------------------|
| Copy `example.html` instead of `assets/template.html` | `example.html` has demo data; not the seed | Read `SKILL.md`/`manifest.json` to find canonical starter |
| Copy only HTML, omit CSS/JS/assets | Broken relative paths, missing tokens, components | Copy entire companion set preserving structure |
| Modify original source in `D:\Master Design\` | Pollutes library for future projects | Always copy to working dir first |
| Treat design system `DESIGN.md` as complete implementation | It's a spec, not code | Use `tokens.css` + `components.html` for implementation |
| Mix tokens from multiple design systems | Token name collisions, visual inconsistency | One design system per project (enforced by `design-taste-frontend`) |
| Skip `checklist.md` / pre-flight | Ships broken work (P0 failures) | Run all P0 checks before delivery |
| Use `example.html` assets (images/fonts) in production | Placeholder assets, wrong licenses | Generate real assets or use licensed sources |
| Assume `html-ppt` works for websites | `od.mode: deck` — different runtime, navigation | Use `web-prototype`/`saas-landing` for websites |

---

## 7. Quick Reference: Template → Canonical Starter Mapping

| Template/Skill | Canonical Starter File | Copy As | Key Companion Files |
|----------------|------------------------|---------|---------------------|
| `web-prototype` | `assets/template.html` | `index.html` | `references/layouts.md`, `references/checklist.md`, `design-systems/default/tokens.css` |
| `saas-landing` | *Skill generates* | `index.html` | `design-systems/<chosen>/tokens.css`, active `DESIGN.md` |
| `open-design-landing` | `scripts/compose.ts` + `inputs.json` | `index.html` | `styles.css`, `assets/image-manifest.json`, `scripts/placeholder.ts` or `imagegen.ts` |
| `html-ppt` | `templates/deck.html` (via `new-deck.sh`) | `examples/<name>/index.html` | `assets/base.css`, `assets/themes/*.css`, `assets/runtime.js`, `templates/full-decks/` |
| `web-prototype-taste-brutalist` | *No starter — rules in SKILL.md* | `index.html` (new) | Custom tokens from SKILL.md |
| `web-prototype-taste-editorial` | *No starter — rules in SKILL.md* | `index.html` (new) | Custom tokens from SKILL.md |
| `design-systems/<name>` | `tokens.css` + `components.html` | Paste `:root` into `<style>`; copy classes | `manifest.json`, `preview/*.html`, `USAGE.md` |

---

## 8. Graphify-Assisted Selection Queries

Use these Graphify queries during Step 2 to discover candidates:

```bash
# Find all design templates with "landing" in name or description
/graphify query "design templates for landing page marketing site"

# Find design systems with specific token (e.g., cobalt accent)
/graphify query "design systems with accent color #2F6FEB"

# Find templates that use GSAP ScrollTrigger
/graphify query "templates with GSAP scroll animations"

# Find skills that generate HTML prototypes
/graphify query "skills that produce standalone HTML prototypes"

# Trace dependency: which templates depend on which design systems
/graphify path "web-prototype" "default"

# Find all templates with "brutalist" aesthetic
/graphify query "brutalist design templates"
```

---

## 9. Enforcement in Master-Website Skill

The `master-website` skill encodes this guide as a **hard gate**:

1. Before any template selection, the skill runs the 10-step procedure.
2. The agent must output the **Resource Selection Decision Record** (Section 2) to the working directory.
3. The skill verifies the canonical starter was identified from the template's own instructions (not guessed).
4. The skill verifies original sources are unchanged (checksum comparison).
5. The skill verifies all companion files copied with relative paths preserved.
6. Only after gate passes does the skill proceed to Phase F (Plan & Implement).

This guide is also copied to `.opencode/skills/master-website/references/template-selection-guide.md` so the installed skill can use it directly at runtime.