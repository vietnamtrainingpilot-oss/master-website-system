# Master Website — Source Attribution & License Registry

This document records the provenance, license, and attribution requirements for every source resource integrated into the master-website skill system. It connects the original resources to the **Skill Integration Map** (`skill-integration-map.md`) and **Template Selection Guide** (`template-selection-guide.md`).

**Principle:** Keep the supplied `Master Design/` library unchanged. Preserve verbatim copies where practicable. Preserve all original license and attribution notices. Record original paths, upstream URLs, versions/commits, and license terms.

---

## 1. Master Design Resource Library (Supplied Archive)

**Root:** `D:\Master Design\`  
**Inventory:** 5,243 files / 1,185 directories (reconciled against brief's "≈5,243 files / 1,186 dirs")  
**Extraction Date:** 2026-10-25  
**SHA-256 Manifest:** See `source-inventory.jsonl` (one line per file with hash)

### 1.1 Top-Level Structure
```
D:\Master Design\
├── craft/                    # Cross-system constraints (token schema, anti-ai-slop, typography)
├── design-systems/           # 110+ design system packages
├── design-templates/         # 100+ renderable templates
├── frames/                   # Device mockup wrappers (5 HTML files)
├── skills/                   # 200+ functional skill stubs (catalogue entries)
└── docs/                     # Upstream documentation (skills-protocol, skills-contributing)
```

### 1.2 License Summary
| Directory | License | Notes |
|-----------|---------|-------|
| `skills/` | Apache-2.0 (default) | Per `skills/README.md`; `web-clone/` adapted from Jane-xiaoer/claude-skill-web-clone (MIT); `guizang-ppt` template MIT |
| `design-systems/` | Varies per system | Each has `manifest.json` `source.license` or `LICENSE` file |
| `design-templates/` | Varies per template | Each has `SKILL.md` `license` field or `LICENSE` file |
| `craft/` | Apache-2.0 (assumed) | Part of OpenDesign curated bundle |
| `frames/` | Apache-2.0 (assumed) | Simple device wrapper HTML |

**Do not assume** the repository license applies to every bundled template, skill, font, image, or external asset. Check each item's own `LICENSE`, `manifest.json`, or `SKILL.md` frontmatter.

---

## 2. Design Systems (110+ Packages)

Each design system under `design-systems/<name>/` follows a standard structure:

```
design-systems/<name>/
├── DESIGN.md              # Human-readable visual spec
├── manifest.json          # Schema v1: id, name, category, files, preview, sourceFiles, craft
├── tokens.css             # Machine-readable :root token bindings (standard names)
├── components.html        # Paste-ready reference components using var(--*)
├── USAGE.md               # Usage guide for agents
├── design-tokens.json     # Structured token registry with sources, layers, confidence
├── preview/               # Visual sanity pages (colors, typography, spacing, buttons, inputs, app)
├── system/artifacts/      # Additional system assets
└── source/                # Evidence: tokens.source.json, token-contract.report.json, evidence.md
```

### 2.1 Primary Fallback: `default` (Neutral Modern)

| Field | Value |
|-------|-------|
| **Path** | `D:\Master Design\design-systems\default\` |
| **Category** | Starter |
| **Manifest** | `manifest.json` (schema v1, `od-design-system-project/v1`) |
| **Token Count** | 56 tokens (all source-backed, grade: excellent) |
| **Standard Tokens** | `--bg`, `--surface`, `--fg`, `--muted`, `--border`, `--accent` (#2F6FEB), `--success`, `--warn`, `--danger`, `--font-display` (Inter), `--font-body` (Inter), `--font-mono` (JetBrains Mono), `--text-xs`..`--text-4xl`, `--space-1`..`--space-20`, `--radius-sm`..`--radius-pill`, `--elev-flat/ring/raised`, `--focus-ring`, `--motion-fast/base`, `--ease-standard`, `--container-max/gutter-*` |
| **License** | Bundled fixture (Apache-2.0 assumed) |
| **Upstream** | OpenDesign curated bundle (no external upstream) |
| **Attribution** | Preserve `manifest.json` `source` field, `USAGE.md`, `LICENSE` if present |

### 2.2 Other Notable Design Systems (Sample)

| Name | Category | Key Tokens / Aesthetic | License / Source |
|------|----------|------------------------|------------------|
| `editorial` | Editorial | Serif display, asymmetric grid, generous whitespace | Bundled |
| `brutalist` | Brutalism | Monospace, raw borders, zero radius | Bundled |
| `minimal` | Minimal | Clean, reduced, whitespace-first | Bundled |
| `luxury` | Luxury | High-contrast, refined, premium | Bundled |
| `shadcn` | Component | shadcn/ui compatible tokens | Bundled |
| `vercel` | Vercel-style | Vercel design language | Bundled |
| `linear-app` | Linear-style | Minimal, technical, dark | Bundled |
| `notion` | Notion-style | Clean, functional, warm | Bundled |
| `github` | GitHub Primer | Primer-compatible | Bundled |
| `stripe` | Stripe | Stripe design language | Bundled |
| `atlas` | ... | ... | ... |

**Full list:** See `source-inventory.jsonl` filtered by `dir` starting with `design-systems/`.

### 2.3 Attribution Requirements for Design Systems
When using a design system in a generated website:
1. Copy `tokens.css` `:root` block verbatim into the artifact's `<style>` (first block).
2. Reference component classes from `components.html` — do not redefine tokens.
3. Preserve `manifest.json` `source` object in the working copy's metadata.
4. If the system has a `LICENSE` file, include it in the deliverable's attribution.
5. Record the design system name, path, and token commit/hash in the project's decision record.

---

## 3. Design Templates (100+ Packages)

Each template under `design-templates/<name>/` follows:

```
design-templates/<name>/
├── SKILL.md                 # Frontmatter + workflow (same shape as functional skills)
├── assets/
│   └── template.html        # Canonical starter (or example.html)
├── example.html             # Demo rendering (reference only)
├── references/
│   ├── layouts.md           # Section skeletons
│   ├── checklist.md         # P0/P1/P2 self-review
│   ├── animations.md        # Animation catalog
│   └── themes.md            # Theme catalog
├── scripts/                 # Composers, generators, validators
├── styles.css               # Inlined stylesheet (for parameterized templates)
├── inputs.example.json      # Worked example inputs
├── schema.ts                # Typed input schema (TypeScript)
├── README.md                # Quick-start
└── LICENSE                  # Template-specific license
```

### 3.1 Primary Templates (Referenced in Integration Map)

| Template | Canonical Starter | Output Type | License | Upstream |
|----------|-------------------|-------------|---------|----------|
| `web-prototype` | `assets/template.html` | Single-page HTML prototype | MIT (assumed) | OpenDesign |
| `saas-landing` | *Skill generates* `index.html` | SaaS landing page | MIT (assumed) | OpenDesign |
| `open-design-landing` | `scripts/compose.ts` + `inputs.json` | Editorial collage landing | MIT (assumed) | OpenDesign (Atelier Zero) |
| `html-ppt` | `templates/deck.html` (via `new-deck.sh`) | HTML presentation deck | MIT (Lewis) | https://github.com/lewislulu/html-ppt-skill |
| `web-prototype-taste-brutalist` | *Rules in SKILL.md* | Brutalist web prototype | MIT (assumed) | Distilled from Leonxlnx/taste-skill |
| `web-prototype-taste-editorial` | *Rules in SKILL.md* | Editorial minimalist prototype | MIT (assumed) | Distilled from Leonxlnx/taste-skill |
| `open-design-landing-deck` | `scripts/compose.ts` + `inputs.json` | Slide deck | MIT (assumed) | OpenDesign |

### 3.2 Template License & Attribution
| Template | License File | Upstream URL | Attribution Required |
|----------|--------------|--------------|---------------------|
| `web-prototype` | None found (Apache-2.0 assumed) | OpenDesign curated | Preserve `SKILL.md` upstream reference |
| `saas-landing` | None found (Apache-2.0 assumed) | OpenDesign curated | Preserve `SKILL.md` upstream reference |
| `open-design-landing` | None found (Apache-2.0 assumed) | OpenDesign curated | Preserve `SKILL.md` upstream reference |
| `html-ppt` | MIT (in `SKILL.md` footer) | https://github.com/lewislulu/html-ppt-skill | **Must** preserve MIT copyright: `Copyright (c) 2026 lewis <sudolewis@gmail.com>` |
| `web-prototype-taste-brutalist` | None found | Distilled from Leonxlnx/taste-skill | Credit: "Distilled from Leonxlnx/taste-skill brutalist-skill" |
| `web-prototype-taste-editorial` | None found | Distilled from Leonxlnx/taste-skill | Credit: "Distilled from Leonxlnx/taste-skill minimalist-skill" |

---

## 4. Functional Skills (200+ Stubs + Live OpenCode Skills)

### 4.1 Master Design Skills (Catalogue Stubs)

Located at `D:\Master Design\skills\<name>\SKILL.md`. These are **catalogue entries** — frontmatter + short body pointing to upstream. They do **not** vendor upstream assets.

| Skill | Upstream | Upstream URL | License | Notes |
|-------|----------|--------------|---------|-------|
| `brainstorming` | Superpowers | https://github.com/obra/superpowers | Apache-2.0 | Full workflow installed in live OpenCode |
| `design-md` | Google Labs | https://github.com/google-labs-code/skills | Apache-2.0 | Catalogue stub only |
| `design-taste-frontend` | Taste Skill | https://github.com/Leonxlnx/taste-skill | Apache-2.0 | Full workflow installed in live OpenCode |
| `emil-design-eng` | Emil Kowalski | https://github.com/emilkowalski/skills | MIT | Full workflow installed in live OpenCode |
| `emilkowalski-motion` | Emil Kowalski | https://emilkowal.ski/skill | MIT | Full workflow installed in live OpenCode |
| `web-clone` | Jane-xiaoer | https://github.com/Jane-xiaoer/claude-skill-web-clone | MIT | Adapted in Master Design (scripts vendored) |
| `image-to-code` | Taste Skill | https://github.com/Leonxlnx/taste-skill | Apache-2.0 | Full workflow installed in live OpenCode |
| `motion-lab` | Motion.Lab | https://github.com/yangxu128/Motion.Lab | MIT | 160 case catalogue (references only) |
| `html-ppt` | Lewis | https://github.com/lewislulu/html-ppt-skill | MIT | Full skill in `design-templates/html-ppt/` |
| `web-design-guidelines` | Vercel Labs | https://github.com/vercel-labs/web-interface-guidelines | MIT | Pinned snapshot in live OpenCode |

### 4.2 Live OpenCode Skills (Installed & Callable)

Located at `C:\Users\Admin\.config\opencode\skills\<name>\`. These are **full, callable skills** with scripts, references, and complete workflows.

**Key Skills Used by Master-Website (see Integration Map):**
- `brainstorming`, `design-taste-frontend`, `frontend-design`, `emil-design-eng`, `emilkowalski-motion`, `review-animations`, `animate`, `ui-animation`, `motion-foundations`, `motion-patterns`, `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `cinematic-gsap-lenis-motion-system`, `awwwards-animations`, `frontend-a11y`, `accessibility`, `vercel-react-best-practices`, `react-performance`, `verification-loop`, `verification-before-completion`, `browser-qa`, `systematic-debugging`, `ship-it`, `conventional-commit-review`, `generic-site-auditor`, `ultimate-frontend-skills`, `impeccable-design-polish`, `design-system`, `stitch-design-taste`, `writing-plans`, `tdd-workflow`, `test-driven-development`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `Graphify` (CLI + skill).

**License:** Each skill's `SKILL.md` frontmatter or `LICENSE` file. Most are Apache-2.0 or MIT per upstream.

**Attribution:** When a skill's workflow is executed, the master-website skill logs the skill name and version in the project's decision record. No additional runtime attribution needed (skills are development-time tools).

---

## 5. Upstream Repositories & External Sources

| Source | URL | Purpose | License | Version/Commit |
|--------|-----|---------|---------|----------------|
| OpenDesign | https://github.com/nexu-io/open-design | Primary resource library | Apache-2.0 | Main branch (2026) |
| Superpowers | https://github.com/obra/superpowers | Brainstorming, planning, TDD, verification | Apache-2.0 | Main branch |
| Taste Skill | https://github.com/Leonxlnx/taste-skill | Design taste, image-to-code, anti-slop | Apache-2.0 | Main branch |
| Emil Kowalski Skills | https://github.com/emilkowalski/skills | Animation philosophy, component principles | MIT | a47903a (emil-design-eng), e8a175d (animate) |
| Vercel Web Interface Guidelines | https://github.com/vercel-labs/web-interface-guidelines | Product UI standards | MIT | 4e799d4 (pinned) |
| Anthropic Skills | https://github.com/anthropics/skills | Frontend design, React patterns | Apache-2.0 | Main branch |
| Google Labs Skills | https://github.com/google-labs-code/skills | DESIGN.md, Stitch integration | Apache-2.0 | Main branch |
| Motion.Lab | https://github.com/yangxu128/Motion.Lab | 160 animation cases | MIT | fbfda03 |
| HTML PPT | https://github.com/lewislulu/html-ppt-skill | HTML presentations | MIT | Main branch |
| Superpowers (OpenCode) | https://github.com/obra/superpowers | Process discipline, brainstorming | Apache-2.0 | Installed via OpenCode |
| bitwize-music plugin | https://github.com/vietnamtrainingpilot-oss/bitwize-music | Ultimate frontend skills, ultimate-frontend-skills | Apache-2.0 | Main branch |

---

## 6. Source Registry (Machine-Readable Index)

This registry connects each integrated resource to its location in the **Integration Map** and **Selection Guide**.

```jsonl
{"resource": "design-systems/default", "type": "design-system", "map_ref": "Phase D — Primary Fallback", "guide_ref": "Section 3.1, Case 2", "license": "Apache-2.0 (bundled)", "upstream": "OpenDesign curated", "attribution": "Preserve manifest.json source, USAGE.md, tokens.css verbatim"}
{"resource": "design-templates/web-prototype", "type": "design-template", "map_ref": "Phase E — Primary Template", "guide_ref": "Section 3.1, Case 2; Section 5 Worked Example", "license": "MIT (assumed)", "upstream": "OpenDesign curated", "attribution": "Preserve SKILL.md upstream reference; copy assets/template.html as index.html"}
{"resource": "design-templates/saas-landing", "type": "design-template", "map_ref": "Phase E — SaaS Template", "guide_ref": "Section 3.1, Case 1", "license": "MIT (assumed)", "upstream": "OpenDesign curated", "attribution": "Skill generates index.html; pair with chosen design system tokens"}
{"resource": "design-templates/open-design-landing", "type": "design-template", "map_ref": "Phase E — Atelier Zero", "guide_ref": "Section 3.1, Case 4", "license": "MIT (assumed)", "upstream": "OpenDesign curated (Atelier Zero)", "attribution": "Run compose.ts; preserve styles.css, image-manifest.json, scripts/"}
{"resource": "design-templates/html-ppt", "type": "design-template", "map_ref": "Phase E — Deck Template", "guide_ref": "Section 5 Case 5", "license": "MIT", "upstream": "https://github.com/lewislulu/html-ppt-skill", "attribution": "MIT copyright (c) 2026 lewis <sudolewis@gmail.com>; preserve in deliverable"}
{"resource": "skills/design-taste-frontend (taste-skill)", "type": "functional-skill", "map_ref": "Phase C — Primary Taste Authority", "guide_ref": "Section 3.1 (dial setting, design-system map)", "license": "Apache-2.0", "upstream": "https://github.com/Leonxlnx/taste-skill", "attribution": "Log skill invocation in decision record"}
{"resource": "skills/emil-design-eng", "type": "functional-skill", "map_ref": "Phase C — Component/Motion Philosophy", "guide_ref": "Animation decision framework, component rules", "license": "MIT", "upstream": "https://github.com/emilkowalski/skills (commit a47903a)", "attribution": "Log skill invocation in decision record"}
{"resource": "skills/review-animations", "type": "functional-skill", "map_ref": "Phase G — Hard Review Gate", "guide_ref": "Ten standards, remedial hierarchy, Block/Approve", "license": "MIT", "upstream": "https://github.com/emilkowalski/skills (commit a47903a)", "attribution": "Log skill invocation; output Before/After/Why table"}
{"resource": "skills/animate", "type": "functional-skill", "map_ref": "Phase F/G — Animation Implementation", "guide_ref": "Build sequence, recipes, never-ship table", "license": "MIT", "upstream": "https://github.com/emilkowalski/skills (commit e8a175d)", "attribution": "Log skill invocation"}
{"resource": "skills/frontend-design", "type": "functional-skill", "map_ref": "Phase C — Stack Defaults, Craft", "guide_ref": "React/Next, Tailwind v4, Motion, RSC safety", "license": "Apache-2.0", "upstream": "https://github.com/anthropics/skills", "attribution": "Log skill invocation"}
{"resource": "skills/web-clone", "type": "functional-skill", "map_ref": "Phase B/F — Reference Recon & Clone", "guide_ref": "Scripts: recon-site, asset-harvest, mirror-site, audit-clone", "license": "MIT", "upstream": "https://github.com/Jane-xiaoer/claude-skill-web-clone", "attribution": "Scripts vendored in Master Design; log invocation"}
{"resource": "skills/image-to-code", "type": "functional-skill", "map_ref": "Phase B — Image-First Workflow", "guide_ref": "Section 5 Case 1; mandates one image per section in Codex", "license": "Apache-2.0", "upstream": "https://github.com/Leonxlnx/taste-skill", "attribution": "Log skill invocation"}
{"resource": "skills/web-design-guidelines", "type": "functional-skill", "map_ref": "Phase C/H — Vercel UI Standards", "guide_ref": "Pinned guidelines at references/guidelines.md", "license": "MIT", "upstream": "https://github.com/vercel-labs/web-interface-guidelines (commit 4e799d4)", "attribution": "Log skill invocation"}
{"resource": "skills/generic-site-auditor", "type": "functional-skill", "map_ref": "Phase C/H — 6-Phase Audit", "guide_ref": "Inspect→Diagnose→Prioritize→Plan→Fix→Verify", "license": "Apache-2.0 (assumed)", "upstream": "OpenCode community", "attribution": "Log skill invocation"}
{"resource": "skills/ultimate-frontend-skills", "type": "functional-skill", "map_ref": "Phase C/F — House Style Fallback + Engines", "guide_ref": "Pipeline (9 stages), core.css, motion.js, gradient.js/depth.js/sky.js/exploded.js", "license": "Apache-2.0 (assumed)", "upstream": "bitwize-music plugin", "attribution": "Log skill invocation; webdesign.mjs commands"}
{"resource": "skills/Graphify", "type": "tool-integration", "map_ref": "Cross-Phase — Navigation Graph", "guide_ref": "Step 2 Graphify queries; code-only graph built", "license": "MIT (graphifyy)", "upstream": "https://github.com/Graphify-Labs/graphify", "attribution": "Graphify CLI installed; skill integrated via hook"}
```

---

## 7. Attribution Checklist for Generated Websites

When the master-website skill delivers a website, the deliverable **must** include:

- [ ] **ATTRIBUTION.md** in the project root listing:
  - Design system used (name, path, token commit)
  - Template used (name, path, canonical starter file)
  - Skills invoked (names, versions)
  - Upstream URLs for all sources
  - License for each source (copy of LICENSE files where required)
- [ ] **Verbatim token block** from `tokens.css` pasted as first `<style>` `:root` block
- [ ] **Component classes** used from `components.html` without redefining tokens
- [ ] **No modified originals** — all `D:\Master Design\` files unchanged (verify via `source-inventory.jsonl` hashes)
- [ ] **Decision record** saved with selection rationale and rejected alternatives
- [ ] **Graphify query log** showing navigation queries used

---

## 8. License Compliance Notes

### 8.1 Permissive Licenses (Safe to Copy/Adapt)
- Apache-2.0: OpenDesign, Superpowers, Taste Skill, Google Labs Skills, Anthropic Skills, OpenCode skills
- MIT: Emil Kowalski, Vercel Guidelines, Motion.Lab, HTML PPT, web-clone (adapted), bitwize-music

### 8.2 Attribution Required
- **MIT licenses** require preserving copyright notice and license text in deliverable.
- **Apache-2.0** requires preserving NOTICE file if present; include license copy.
- **Bundled fixtures** (OpenDesign curated): treat as Apache-2.0; preserve `manifest.json` `source` metadata.

### 8.3 Do Not Redistribute Without Permission
- **Proprietary fonts** (if any design system references commercial fonts)
- **Stock photos** (Unsplash/Pexels via URL only — do not bundle unless license permits)
- **gpt-image-2 generated assets** (fal.ai terms apply; `generate` strategy requires FAL_KEY)

### 8.4 Safe Defaults When License Unclear
- Use `default` design system (bundled, Apache-2.0 assumed)
- Use `web-prototype` template (bundled, MIT assumed)
- Generate images via `picsum.photos` seeded URLs (CC0)
- Use `simple-icons` CDN for brand logos (MIT)

---

## 9. Verification of Source Preservation

The master-website skill includes a **source preservation gate**:

```bash
# Before declaring delivery complete:
cd "D:\Master Design"
# Verify no files modified (compare against source-inventory.jsonl hashes)
python3 -c "
import json, hashlib, sys
with open('source-inventory.jsonl') as f:
    for line in f:
        rec = json.loads(line)
        if rec['sha256'].startswith('ERR'): continue
        import os
        p = os.path.join('D:\\Master Design', rec['path'])
        if os.path.exists(p):
            h = hashlib.sha256(open(p,'rb').read()).hexdigest()
            if h != rec['sha256']:
                print(f'MODIFIED: {rec[\"path\"]}')
                sys.exit(1)
print('All source files preserved.')
"
```

Exit code 0 = gate passes. Any modification to the original library blocks delivery.

---

## 10. Summary: Attribution in One Sentence

> "This website was built using the **master-website** OpenCode skill, which orchestrates the **OpenDesign** resource library (Apache-2.0), the **design-taste-frontend** taste skill (Apache-2.0, Leonxlnx/taste-skill), **Emil Kowalski** animation philosophy (MIT), **Vercel Web Interface Guidelines** (MIT), and the **ultimate-frontend-skills** house style (Apache-2.0, bitwize-music). The **default/Neutral Modern** design system (bundled) and **web-prototype** template (bundled) provided the token and structural foundation. All original sources preserved verbatim under `D:\Master Design\`."