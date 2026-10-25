# Design-Templates Catalog — AGENTS.md

> **Authoritative catalog of all 115 design templates** under `D:/Master Design/design-templates/`.
> Generated from machine-enumeration + human inspection of `SKILL.md`, `README.md`, and `example.html`.
> Source of truth: `audit/source-audit.jsonl`.

## Template Classification by Mode

| Mode | Count | Purpose |
|---|---|---|
| `prototype` | 82 | Single-page web prototypes (landing, marketing, SaaS, dashboards) |
| `deck` | 27 | HTML slide presentations (consulting, strategy, product launch) |
| `image` | 4 | Static visual compositions (posters, carousels, infographics) |
| `video` | 2 | Video generation workflows (short-form, hyperframes compositions) |

## Quick-Pick Guide

| Use case | Recommended template(s) |
|---|---|
| General landing / marketing / docs / SaaS page | `web-prototype` (canonical starter) |
| Editorial / warm newspaper-style page | `web-prototype-taste-editorial` |
| Brutalist / Swiss print industrial page | `web-prototype-taste-brutalist` |
| Soft / gentle editorial page | `web-prototype-taste-soft` |
| Consulting final deck / decision-grade B2B deck | `html-ppt` + full-deck templates |
| Client presentation with speaker notes | `html-ppt-presenter-mode-reveal` |
| Product launch deck | `html-ppt-product-launch` |
| Technical sharing / engineering deck | `html-ppt-tech-sharing` |
| Weekly / recurring report deck | `html-ppt-weekly-report` |
| Pitch deck / VC presentation | `html-ppt-pitch-deck` |
| Course module / training deck | `html-ppt-course-module` |
| Annual report / studio annual | `open-design-landing` (8-section editorial) |
| OpenDesign ecosystem landing page | `open-design-landing` / `open-design-landing-deck` |
| GitHub activity daily briefing | `orbit-github` |
| Multi-connector daily digest | `orbit-general` |
| Social media carousel (3×1080) | `social-carousel` |
| Short-form video (3-10s) | `video-shortform` |
| HyperFrames composition (HTML→video) | `hyperframes` |
| Blog post / article page | `blog-post` |
| Waitlist / coming soon page | `waitlist-page` |
| Pricing page | `pricing-page` |
| Contact widget / form | `contact-widget` |
| Dashboard / data visualization | `dashboard`, `flowai-live-dashboard-template`, `trading-analysis-dashboard-template` |
| Mobile app screen in iPhone frame | `mobile-app` |
| Wireframes (annotated, greybox, mobile flow) | `wireframe-annotated`, `wireframe-greybox`, `wireframe-mobile-flow` |

## Template Mode Reference

### `prototype` — Single-Page Web Prototypes

The canonical seed-and-compose workflow: copy `assets/template.html` → paste section skeletons from `references/layouts.md` → fill with real copy → self-check via `references/checklist.md`.

#### Core Starter Templates

| Template | Description | Assets | References | Best For |
|---|---|---|---|---|
| **web-prototype** | General-purpose desktop web prototype. 8 paste-ready section layouts, self-contained HTML. | `assets/template.html` (seed), `references/layouts.md`, `references/checklist.md` | Any landing / marketing / docs / SaaS page when no specific skill matches |
| **web-prototype-taste-brutalist** | Swiss industrial-print: newsprint canvas, monolithic grotesque, viewport-bleeding numerals, hazard-red accent. | Distilled from Leonxlnx/taste-skill `brutalist-skill` | Editorial, newspaper, agency portfolio, manifesto sites |
| **web-prototype-taste-editorial** | Warm-paper editorial: italic serif, collage-on-grid, generous whitespace, Atelier Zero language. | Distilled from Leonxlnx/taste-skill `editorial-skill` | Magazine-style, literary, warm editorial pages |
| **web-prototype-taste-soft** | Soft editorial variant: gentle serif, muted palette, calm rhythm. | Distilled from taste-skill | Gentle editorial, personal blogs, quiet pages |

#### Specialized Prototypes (single-purpose, `example.html` + `SKILL.md`)

| Template | Purpose |
|---|---|
| `saas-landing` | SaaS landing page with hero, features, pricing, testimonials, CTA |
| `pricing-page` | Dedicated pricing/comparison page |
| `waitlist-page` | Coming-soon / waitlist with email capture |
| `blog-post` | Single article/blog post layout |
| `docs-page` | Documentation page with sidebar navigation |
| `dashboard` | Data dashboard with KPIs, charts, tables |
| `flowai-live-dashboard-template` | Real-time AI dashboard with live data feeds |
| `trading-analysis-dashboard-template` | Financial trading analysis dashboard |
| `social-media-dashboard` | Social media metrics dashboard |
| `social-media-matrix-tracker-template` | Social media tracking matrix |
| `mobile-app` | Mobile screen inside iPhone 15 Pro frame |
| `mobile-onboarding` | Mobile onboarding flow screens |
| `contact-widget` | Contact form / widget component |
| `email-marketing` | Email campaign layout |
| `magazine-poster` | Magazine-style poster/visual |
| `social-carousel` | 3-card Instagram/TikTok carousel (1080×1080) |
| `image-poster` | Static image poster generation |
| `invoice` | Invoice/billing document layout |
| `digital-eguide` | Two-spread digital guide preview |
| `critique` | 5-dimension design review generator (scores 0-10) |
| `gamified-app` | Gamified app UI patterns |
| `github-dashboard` | GitHub-style developer dashboard |
| `aster-atelier` | Atelier-style portfolio/artist page |
| `clinical-case-report` | Medical/clinical case report format |
| `hr-onboarding` | HR onboarding page |
| `eng-runbook` | Engineering runbook/playbook |
| `finance-report` | Financial report layout |
| `dcf-valuation` | DCF valuation model page |
| `team-okrs` | Team OKR tracking page |
| `weekly-update` | Weekly update/standup page |
| `meeting-notes` | Meeting minutes/notes layout |
| `kanban-board` | Kanban board UI |
| `last30days` | 30-day trend research summary |
| `live-dashboard` | Live data dashboard |
| `live-artifact` | Live artifact viewer |
| `video-shortform` | Short-form video generation (also video mode) |
| `webgl-experience` | WebGL/3D experience prototype |
| `sprite-animation` | Sprite animation demo |
| `motion-frames` | Motion/animation frames prototype |
| `tweaks` | UI tweak/polish examples |
| `audio-jingle` | Audio jingle/short audio component |
| `x-research` | Research/exploration page |
| `ib-pitch-book` | Investment banking pitch book layout |
| `pricing-page` | Pricing page layout |
| `replit-deck` | Replit-style interactive deck |
| `kami-deck` | Kami-styled slide deck |
| `kami-landing` | Kami-styled landing page |
| `guizang-ppt` | Magazine web PPT / editorial slide deck |
| `simple-deck` | Simple slide deck |
| `schedule` | Schedule/timeline page |

#### Wireframe Templates

| Template | Purpose |
|---|---|
| `wireframe-annotated` | Annotated wireframes with notes |
| `wireframe-greybox` | Greybox/low-fidelity wireframes |
| `wireframe-mobile-flow` | Mobile user flow wireframes |
| `wireframe-sketch` | Hand-sketched style wireframes |

---

### `deck` — HTML Slide Presentations

All `deck` mode templates share the **html-ppt** runtime: 36 themes, 31 layouts, 27 CSS animations, 20 canvas FX, presenter mode (S key), keyboard navigation.

#### Master Template: `html-ppt`

**Upstream:** `https://github.com/lewislulu/html-ppt-skill` (MIT)

| Asset | Count | Description |
|---|---|---|
| Themes | 36 | `assets/themes/*.css` — minimal-white, editorial-serif, tokyo-night, dracula, cyberpunk-neon, pitch-deck-vc, etc. |
| Full-deck templates | 15 | `templates/full-decks/<name>/` — complete multi-slide decks with scoped CSS |
| Single-page layouts | 31 | `templates/single-page/*.html` — realistic demo data, copy/paste |
| CSS animations | 27 | `assets/animations/animations.css` — `data-anim="fade-up"`, `anim-stagger-list` |
| Canvas FX | 20 | `assets/animations/fx/*.js` — particle-burst, knowledge-graph, neural-net, etc. |
| Runtime | 2 | `assets/runtime.js` (keyboard/presenter) + `fx-runtime.js` (auto-init FX) |

**Presenter Mode (S key):** Opens 4 magnetic cards — CURRENT (pixel-perfect iframe), NEXT, SPEAKER SCRIPT (scrollable notes), TIMER. Notes must be in `<aside class="notes">` inside each slide.

**Key full-deck templates:**

| Template | Scenario | Slides | Best For |
|---|---|---|---|
| `presenter-mode-reveal` | Consulting/tech sharing | 15+ | Any deck needing speaker notes + presenter view |
| `pitch-deck` | VC pitch / fundraising | 12-15 | Investor presentations |
| `product-launch` | Product launch / reveal | 10-15 | Product announcements |
| `tech-sharing` | Technical talk / conference | 15+ | Engineering presentations |
| `weekly-report` | Recurring team update | 8-12 | Weekly standups |
| `course-module` | Training / education | 10-20 | Course modules |
| `xhs-post` | Xiaohongshu 3:4 social | 6-8 | Social media decks |
| `xhs-white-editorial` | Editorial social | 8-10 | Editorial-style social |
| `xhs-pastel-card` | Pastel card social | 8-10 | Card-style social |
| `knowledge-arch-blueprint` | Architecture/docs | 12+ | Knowledge architecture |
| `hermes-cyber-terminal` | Cyber/tech aesthetic | 10+ | Technical deep-dives |
| `obsidian-claude-gradient` | Gradient aesthetic | 10+ | Modern gradient themes |
| `graphify-dark-graph` | Dark graph visualization | 10+ | Data visualization |
| `testing-safety-alert` | Security/testing | 8+ | Safety/security decks |

**Theme selection by audience:**

| Audience | Recommended Themes |
|---|---|
| Business / investor | `pitch-deck-vc`, `corporate-clean`, `swiss-grid` |
| Tech / engineering | `tokyo-night`, `dracula`, `catppuccin-mocha`, `terminal-green`, `blueprint` |
| Xiaohongshu / social | `xiaohongshu-white`, `soft-pastel`, `rainbow-gradient`, `magazine-bold` |
| Academic / report | `academic-paper`, `editorial-serif`, `minimal-white` |
| Edgy / cyber / launch | `cyberpunk-neon`, `vaporwave`, `y2k-chrome`, `neo-brutalism` |

#### Orbit Templates (Live Connector Briefings)

| Template | Connector | Description |
|---|---|---|
| `orbit-general` | Multi-connector | Daily digest from all connected sources (GitHub, Slack, Linear, Notion, Gmail, etc.) |
| `orbit-github` | GitHub only | GitHub PRs, reviews, issues, CI runs — mirrors GitHub Notifications + PR-diff UI |
| `orbit-slack` | Slack only | Slack messages, threads, mentions |
| `orbit-gmail` | Gmail only | Email digest, threads |
| `orbit-linear` | Linear only | Linear issues, cycles, projects |
| `orbit-notion` | Notion only | Notion pages, databases |

**Hard constraint:** Orbit templates **ignore** any attached design system. They ship their own baked visual language (GitHub Primer, etc.) and must reproduce `example.html` 1:1.

#### Zhangzara Cobalt Grid Family (32 templates, MIT-licensed from upstream)

All share: light scheme, high formality, medium density, electric cobalt italic serifs on graph-paper canvas, stair-stepped pixel-glitch decorations.

| Template | Scenario |
|---|---|
| `cobalt-grid` (base) | B2B sales / renewal & expansion business case |
| `biennale-yellow` | Art/biennale exhibition review |
| `block-frame` | Structured block-frame layouts |
| `blue-professional` | Professional blue-themed |
| `bold-poster` | Bold poster-style |
| `broadside` | Broadside/editorial broadsheet |
| `capsule` | Capsule/pill-shaped elements |
| `cartesian` | Cartesian/grid-based academic |
| `cobalt-grid` | Cobalt grid base |
| `coral` | Coral/warm accent |
| `creative-mode` | Creative/expressive mode |
| `daisy-days` | Light/playful daisy theme |
| `editorial-tri-tone` | Three-tone editorial |
| `grove` | Nature/grove themed |
| `long-table` | Long table/data format |
| `mat` | Mat/flat material |
| `monochrome` | Monochrome only |
| `neo-grid-bold` | Neo-grid bold |
| `peoples-platform` | People/platform community |
| `pin-and-paper` | Pin-and-paper aesthetic |
| `pink-script` | Pink/script handwriting |
| `playful` | Playful/casual |
| `raw-grid` | Raw grid |
| `retro-windows` | Retro Windows 95/98 aesthetic |
| `retro-zine` | Retro zine/magazine |
| `sakura-chroma` | Sakura/cherry blossom chromatic |
| `scatterbrain` | Scattered/brainstorm layout |
| `signal` | Signal/communication |
| `soft-editorial` | Soft editorial |
| `stencil-tablet` | Stencil/tablet aesthetic |
| `studio` | Studio/creative workspace |
| `vellum` | Vellum/paper texture |

**Workflow:** Clone `example.html` → replace content → preserve design system → adjust length by duplicating layouts → never mix with other templates.

#### Other Deck Templates

| Template | Purpose |
|---|---|
| `html-ppt-taste-brutalist` | Brutalist taste deck (dark CRT mode) |
| `html-ppt-taste-editorial` | Editorial taste deck |
| `open-design-landing-deck` | OpenDesign landing page as slide deck |

---

### `image` — Static Visual Compositions

| Template | Purpose | Output |
|---|---|---|
| `image-poster` | Magazine-style poster | Single HTML→screenshot |
| `magazine-poster` | Editorial magazine poster | Single HTML→screenshot |
| `social-carousel` | 3-card social carousel (1080×1080) | HTML→screenshot |
| `invoice` | Invoice/document visual | HTML→screenshot |

---

### `video` — Video Generation

| Template | Purpose | Backend |
|---|---|---|
| `hyperframes` | HTML→video composition engine (HyperFrames) | HyperFrames CLI + renderer (local/HeyGen/Cloud Run/Lambda) |
| `video-shortform` | 3-10 second short-form clips (product reveals, teasers) | Seedance 2 / Kling 3 / 4 / Veo 3 / Sora 2 (via fal.ai) |

**HyperFrames:** For any video work — building, editing, packaging, rendering videos, motion graphics, explainers, promos, captions, talking-head recuts. Uses HTML-to-video rendering (HyperFrames) or React video (Remotion).

---

## Template Selection Algorithm

1. **If brief names a specific template** → use it directly.
2. **If brief asks for a slide deck / presentation** → route to `html-ppt` ecosystem:
   - Consulting/B2B → `html-ppt` + full-deck templates
   - Speaker notes needed → `presenter-mode-reveal`
   - Product launch → `product-launch`
   - Social media deck → `xhs-*` variants
   - Architecture/technical → `knowledge-arch-blueprint` / `hermes-cyber-terminal`
3. **If brief asks for a web page / landing page** → route to `web-prototype` ecosystem:
   - No specific style → `web-prototype` (canonical starter)
   - Editorial / warm → `web-prototype-taste-editorial`
   - Brutalist / Swiss → `web-prototype-taste-brutalist`
   - Soft / gentle → `web-prototype-taste-soft`
4. **If brief asks for daily briefing / connector digest** → route to Orbit:
   - GitHub only → `orbit-github`
   - Multi-connector → `orbit-general`
5. **If brief asks for video / motion** → route to `hyperframes` or `video-shortform`.
6. **If brief asks for static visual / poster / carousel** → route to `image` templates.
7. **If no match** → ask clarifying question with 2-3 recommended options.

---

## Template File Structure Reference

Every template folder contains at minimum:

```
<template-name>/
├── SKILL.md              # Agent contract (read first) — name, description, triggers, od.mode, workflow
├── example.html          # Canonical rendering (baked, regenerable)
└── [optional side files]
    ├── assets/           # Images, fonts, placeholders
    ├── references/       # layouts.md, checklist.md, themes.md, etc.
    ├── scripts/          # Compose/imagegen/placeholder scripts (TypeScript)
    ├── styles.css        # Standalone stylesheet (open-design-landing)
    ├── schema.ts         # Typed inputs schema (open-design-landing)
    ├── inputs.example.json # Worked example inputs (open-design-landing)
    ├── README.md         # Human quick-start
    ├── LICENSE           # License file (MIT for upstream-vendored)
    └── template.json     # Upstream metadata snapshot (zhangzara family)
```

---

## Catalog Summary

| Metric | Count |
|---|---|
| Total templates | 115 |
| `prototype` mode | 82 |
| `deck` mode | 27 |
| `image` mode | 4 |
| `video` mode | 2 |
| Have `SKILL.md` | 115 |
| Have `example.html` | 110 |
| Have `README.md` | 18 |
| Upstream-vendored (MIT) | 35 (zhangzara family + html-ppt) |

---

*This catalog was generated by automated filesystem enumeration + manual inspection of `SKILL.md` (frontmatter + workflow) and `README.md` for each folder. For full agent contracts, read the source `SKILL.md`. Source of truth: `audit/source-audit.jsonl`.*