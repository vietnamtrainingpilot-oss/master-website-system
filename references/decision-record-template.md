# Master Website — Resource Selection Decision Record Template

Used by Phase E (Template Selection) to document the canonical starter choice.

## Template

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
- **Token File**: `tokens.css` (56 standard tokens, paste `:root` into `<style>`)
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

## Required Fields

| Field | Required | Description |
|-------|----------|-------------|
| `target.type` | Yes | Output type (landing, portfolio, dashboard, etc.) |
| `target.framework` | Yes | html, react, nextjs, astro |
| `primary_template.name` | Yes | Template folder name |
| `primary_template.canonical_entry` | Yes | Relative path to starter file |
| `design_system.name` | Yes | Design system folder name |
| `design_system.token_file` | Yes | Path to tokens.css |
| `candidates_examined` | Yes | Array of evaluated alternatives |
| `selection_rationale` | Yes | Why this combination |
| `license_attribution` | Yes | License + upstream URL |