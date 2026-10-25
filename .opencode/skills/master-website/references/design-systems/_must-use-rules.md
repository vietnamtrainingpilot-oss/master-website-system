# Must-Use Rules — Every Design Project

These rules apply to EVERY project built with the Master Website System. They are the non-negotiable baseline derived from the complete source ecosystem.

## 1. Design System Foundation (MANDATORY)

Every project MUST start with one of the following:

| When | Use |
|---|---|
| No brand specified, or brief is generic | `default` (Neutral Modern) — 6 `:root` variables, 12-col grid, content-first |
| Brand explicitly named (Apple, Stripe, Vercel, etc.) | The named brand system from `design-systems/` |
| Aesthetic category named (brutalist, minimal, luxury, etc.) | The matching Tier-2 template from `design-systems/` |
| Redesign/preserve existing brand | Audit existing brand tokens, use that system |

**Never invent new `:root` variables.** Copy the selected system's `tokens.css` `:root` block verbatim into the project `<style>` element.

## 2. Anti-Default Discipline (MANDATORY)

These are the LLM defaults that are **automatically banned** unless the brief explicitly requests them:

| Banned Pattern | Replacement |
|---|---|
| `transition: all` | Name exact properties: `transition: transform 200ms ease-out` |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` |
| `ease-in` on UI | `ease-out` + custom cubic-bezier curve |
| `transform-origin: center` on popovers/dropdowns | `var(--transform-origin)` (Base UI) / centered for modals only |
| `background: linear-gradient(... purple ...)` | Neutral base + single accent color |
| Three equal feature cards | 2-column zig-zag, asymmetric grid, or scroll-pinned |
| `Inter` as default display font | `Geist`, `Outfit`, `Cabinet Grotesk`, or brand-appropriate serif |
| `90%` / `50%` / round numbers in data | Organic, messy data (`47.2%`, `+1 (312) 847-1928`) |
| Generic names "John Doe", "Acme", "Nexus" | Realistic, locale-appropriate names |
| Version labels in hero (V0.6, BETA, ALPHA) | Only if brief explicitly about launch preview |
| Em-dash `—` anywhere visible | Regular hyphen `-` only |
| "Quietly in use at" / "Quietly trusted by" social-proof | "Trusted by", "Used at", "Customers include" or skip |
| Hero version footers (v1.4.2, Build 0048) | Banned on marketing pages |
| `border-t` + `border-b` on every row of long lists | Pick one (bottom-border between rows OR top-border above group) |
| Scoring/progress bars with filled background tracks | Number + small icon, or tiny inline bar WITHOUT track |
| Locale/city-name/time/weather strips | Only if brief is genuinely globally-distributed or place-focused |
| Scroll cues (`Scroll`, `↓ scroll`, animated mouse-wheel icons) | Simple "Scroll" arrow or none |
| Decorative status dots by default | Only for real semantic state (server status, availability flag) |
| Section-numbering eyebrows (`00 / INDEX`, `001 · Capabilities`) | Plain language section names |
| `01 / 4`-style pagination on images/bento tiles | No labels needed |
| `Scroll · 001 Capabilities`-style scroll cues | Simple arrow or "Scroll" |
| Emoji as default | Use icon libraries (Phosphor / HugeIcons / Radix / Tabler) |
| Div-based fake screenshots | Real images, generated images, or skip with labeled placeholders |
| `border-t` + `border-b` on every row of spec tables | Use alternatives from Section 4.9 |
| Generic step labels (`Stage 1 / Stage 2 / Stage 3`) | Verb-noun labels ("Install", "Configure", "Ship") |
| Pills/labels/tags overlaid on images | Let the image speak alone, or caption below |
| Photo-credit captions as decoration | Skip caption or functional one-line caption only |
| "Reservation 412 of 800"-style live-stock counters | Only if brief is explicitly limited-run waitlist with real data |
| Decoration text strip at hero bottom (`BRAND. MOTION. SPATIAL.`) | Drop it or make it navigable links |
| Floating top-right sub-text in section headings | Put sub-text directly under headline, or 2-column header |
| Scoring/progress bars with filled background tracks as comparison visuals | Number + small icon, or tiny inline bar without track |
| `transition: all` with unbounded property animation | Flag on sight (aggressive escalation trigger) |
| `scale(0)` or pure-fade entrances with no initial transform | Flag on sight |
| `ease-in` on any UI interaction; weak built-in easing on deliberate animation | Flag on sight |
| Animation on keyboard shortcut, command-palette toggle, 100+/day action | Flag on site - **No animation** |
| UI duration > 300ms with no stated reason | Flag on site - **reduce to 150-250ms** |
| `transform-origin: center` on trigger-anchored popover/dropdown/tooltip | Flag on site |
| Keyframes on toasts, toggles, rapidly-triggered elements | Flag on site - **use CSS transitions** |
| Animating layout properties (`width`/`height`/`margin`/`padding`/`top`/`left`) | Flag on site - **use `transform`/`opacity`** |
| Framer Motion `x`/`y`/`scale` props under load | Flag on site - **use full `transform: "translateX()"`** |
| Updating CSS variable on parent to drive child transform (style recalc storm) | Flag on site - **set `transform` directly on element** |
| Missing `prefers-reduced-motion` handling on movement | Flag on site - **gentler variant, not zero** |
| Ungated `:hover` motion | Flag on site - **add `@media (hover: hover) and (pointer: fine)`** |
| Symmetric enter/exit timing on press-and-release or hold interaction | Flag on site - **asymmetric: slow deliberate, fast response** |
| Everything-at-once entrance where 30-80ms stagger belongs | Flag on site - **max one per page** |

## 3. Taste Dials (Every Project Sets These)

Every project MUST set three dials from `design-taste-frontend` §1:

| Dial | Range | Default | Description |
|---|---|---|---|
| `DESIGN_VARIANCE` | 1–10 | 8 | 1 = Perfect Symmetry, 10 = Artsy Chaos |
| `MOTION_INTENSITY` | 1–10 | 6 | 1 = Static, 10 = Cinematic / Physics |
| `VISUAL_DENSITY` | 1–10 | 4 | 1 = Art Gallery / Airy, 10 = Cockpit / Packed Data |

**Baseline:** `8 / 6 / 4`. Override conversationally from the brief. These dials gate EVERY layout, motion, and density decision in the project.

### Dial Inference from Brief Signals

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "minimalist / clean / calm / editorial / Linear-style" | 5–6 | 3–4 | 2–3 |
| "premium consumer / Apple-y / luxury / brand" | 7–8 | 5–7 | 3–4 |
| "playful / wild / Dribbble / Awwwards / experimental / agency" | 9–10 | 8–10 | 3–4 |
| "landing page / portfolio / marketing site (default)" | 7–9 | 6–8 | 3–5 |
| "trust-first / public-sector / regulated / a11y-critical" | 3–4 | 2–3 | 4–5 |
| "redesign - preserve" | match existing | +1 | match existing |
| "redesign - overhaul" | +2 | +2 | match existing |

## 4. Accessibility (MANDATORY — WCAG 2.2 AA)

Every project MUST pass these non-negotiable checks:

| Check | Requirement |
|---|---|
| Contrast | ≥4.5:1 for body text, ≥7:1 for AAA; ≥3:1 for large text (≥18px) |
| Focus states | Visible focus ring on all interactive elements |
| Keyboard navigation | Tab order is logical, no keyboard traps |
| Touch targets | Minimum 44×44px |
| Reduced motion | Honored — animations degrade to static/gentler, not zero |
| ARIA | Proper labeling, role attributes where needed |
| Skip links | For keyboard users, if page has significant content |
| Landmark regions | Header, main, navigation, complementary, footer |

## 5. Core Web Vitals (MANDATORY)

| Metric | Target |
|---|---|
| LCP | <2.5s |
| INP | <200ms |
| CLS | <0.1 |
| Hero image | `next/image` priority or preloaded |

## 6. Motion (MANDATORY — review-animations Gate)

Every animated element must pass the **review-animations gate**:

| Gate | Condition |
|---|---|
| Justified motion | Answers "why does this animate?" in one sentence |
| Frequency-appropriate | Matches how often users see it |
| Responsive easing | `ease-out` / custom curve; `ease-in` is a block |
| Sub-300ms UI | UI animations stay under 300ms |
| Origin & physical correctness | Scales from trigger, not center (modals exempt) |
| Interruptibility | CSS transitions / springs retarget from current state |
| GPU-only properties | `transform` and `opacity` only |
| Accessibility | `prefers-reduced-motion` honored (gentler, not zero) |
| Asymmetric enter/exit | Deliberate actions slower; system responses snap |
| Cohesion | Motion matches component personality / product voice |

**Failure action:** Fix per remedial hierarchy; re-review. The agent MUST run the full review-animations gate on every animated element before proceeding.

## 6. Source Preservation (MANDATORY)

| Rule | Requirement |
|---|---|
| Originals unchanged | `D:\Master Design\` must remain verbatim — SHA-256 verified |
| Source attribution | `ATTRIBUTION.md` included in deliverables with full provenance |
| License compliance | All upstream licenses preserved; restricted material not redistributed |

---

# Project-Specific Rules — When to Apply

These rules apply only when the brief signals the corresponding condition:

| Brief Signal | When to Apply | How |
|---|---|---|
| "Stripe-like", "fintech", "payment infrastructure" | Use `stripe` design system from `design-systems/` | Copy `tokens.css` `:root`, follow Stripe token names |
| "Apple-like", "premium consumer", "consumer electronics" | Use `apple` design system | Follow SF Pro typography, black/white chapters, cinematic imagery |
| "Brutalist", "Swiss industrial", "raw aesthetic" | Use `brutalism` / `bold` design systems | Follow rigid grids, `border-radius: 0`, hazard red accent |
| "Editorial", "warm newspaper-style", "Atelier Zero" | Use `atelier-zero` / `kami` design systems | Follow italic serif, collage-on-grid, warm paper aesthetic |
| "Dark", "gaming", "cyber", "tech" | Use appropriate system (nike, bmw-m, tetris, etc.) | Follow dark theme, relevant accent colors |
| "SaaS", "landing page", "marketing site" | Use `web-prototype` as canonical starter | Copy `assets/template.html`, follow layout library |
| "Consulting deck", "presentation", "slide show" | Use `html-ppt` ecosystem | Follow 36 themes, 15 full-deck templates, presenter mode |
| "GitHub daily briefing" | Use `orbit-github` | Follow GitHub Primer UI, hard constraint: ignore attached design system |
| "Short-form video (3-10s)" | Use `video-shortform` | Seedance 2 / Kling 3 / 4 / Veo 3 / Sora 2 via fal.ai |
| "HyperFrames video composition" | Use `hyperframes` | HTML-to-video via HyperFrames CLI |
| "Social media carousel (3×1080)" | Use `social-carousel` | 3-card carousel, 1080×1080 |
| "OpenDesign landing page" | Use `open-design-landing` | 8-section editorial, Atelier Zero aesthetic |
| "Over 100 keywords / data-dense" | Use `vercel` / `linear-app` / `sanity` systems | Follow data-density patterns |
| "Voice / audio content" | Use appropriate audio skills | Follow structure from `audio-jingle`, `music-to-video` |
| "Accessibility-first", "public-sector", "regulated" | Apply a11y-first dials (3-4, 2-3, 4-5) | Reduce variance, reduce motion, increase density |

---

# Integration Reference

This file is embedded in the main `master-website` `SKILL.md` at Phase C (§2) and referenced in all subsequent phases. It is **not optional** — every project must abide by the Must-Use Rules.

*Source: Derived from complete inspection of:*
- `design-taste-frontend` (1,206 lines) — taste dials, anti-default discipline
- `review-animations` (120 lines) — 10 non-negotiable standards
- `emil-design-eng` (674 lines) — design engineering philosophy
- `web-design-guidelines` (200+ lines) — Vercel guidelines
- `generic-site-auditor` (341 lines) — 6-phase audit
- `frontend-a11y` (443 lines) — WCAG 2.2 AA
- `accessibility` (146 lines) — a11y patterns
- `vercel-react-best-practices` (149 lines) — performance
- `react-performance` (575 lines) — React performance
- `web-clone` (293 lines) — recon/asset-harvest
- `image-to-code-skill` (1,253 lines) — image-first workflow
- `web-clone` skills collection (full Superpowers brainstorming)
- Design systems (152 folders, manifest + DESIGN.md)
- Design templates (115 folders, SKILL.md + example.html)

---