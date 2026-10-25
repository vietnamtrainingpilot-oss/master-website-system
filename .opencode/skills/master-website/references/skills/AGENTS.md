# skills

This directory holds **functional skills** — capabilities the agent invokes mid-task to do work on user input. Each skill is a folder with a `SKILL.md` (frontmatter + body) and any side files (`assets/`, `references/`, scripts, etc.) the workflow needs.

If the entry primarily *renders* a design artifact (deck, prototype, image/video/audio template) it belongs under `../design-templates/` instead. See `specs/current/skills-and-design-templates.md` for the full split.

## Daemon plumbing

- Listed under `/api/skills` (functional only). User-imported skills shadow built-in entries with the same frontmatter `name`.
- Asset routes (`/api/skills/:id/example`, `/api/skills/:id/assets/*`) span both functional skills and design templates so existing `srcdoc`-rewritten URLs keep resolving after the split.
- Integrations + Skills surfaces this directory only. Renderable templates are read from the design-templates registry by the New project "Start from" rails; the redesigned home no longer has a top-level Templates tab.

## Adding a skill

1. Create `skills/<my-skill>/SKILL.md` with `name`, `description`, `triggers`, and `od.mode: utility` (or `design-system`) frontmatter.
2. Drop any side files alongside; reference them from the body using the relative-from-skill-root paths the daemon advertises in the skill preamble.
3. The daemon's lazy scanner picks the entry up on the next `/api/skills` request — no rebuild required during local dev.

## Curated design / creative catalogue

This directory also ships a curated catalogue of design and creative skills hand-picked from `VoltAgent/awesome-agent-skills` and `ComposioHQ/awesome-claude-skills`. Each entry is a lightweight stub — frontmatter + a short body that points at the upstream repo — so the Integrations + Skills surfaces a rich, filterable list out of the box without vendoring every upstream workflow.

- `od.category` on these stubs powers the new category filter row in Integrations + Skills (e.g. `image-generation`, `video-generation`, `audio-music`, `slides`, `documents`, `design-systems`, `figma`, `animation-motion`, `3d-shaders`, `diagrams`, `creative-direction`, `marketing-creative`, `screenshots`, `web-artifacts`).
- The seed script lives at `scripts/seed-curated-design-skills.ts` and is **idempotent**: running it again only creates folders that don't already exist, so a hand-edited stub is never overwritten. Delete the folder under `skills/` and re-run the script to refresh an entry.
- Stubs intentionally do not vendor upstream assets. To run an upstream workflow with its original scripts and references, copy the upstream folder into your active agent's skills directory (Claude Code, Codex, Cursor, etc.) — the body of each stub explains how.

---

## Master Website Plugin Skills (172 total)

These are the skills the **master-website** plugin invokes during its 13-phase pipeline. Each is catalogued here so the AI knows what the skill is and can use it properly when directed by the main skill.

| Skill | Category | Purpose | Phase |
|-------|----------|---------|-------|
| `brainstorming` | creative | Design read, dials, approach selection, design doc gate | A |
| `design-taste-frontend` | creative | Taste authority: dials, design-system map, anti-slop rules | C |
| `frontend-design` | stack | Stack defaults (React/Next, Tailwind v4, Motion) | C, F |
| `emil-design-eng` | craft | Component/motion philosophy, animation decision framework | C, G |
| `review-animations` | craft | Hard animation gate (10 standards, Block/Approve) | G, M |
| `animate` | motion | Animation build sequence, recipes | G |
| `browser-qa` | qa | Playwright QA: console, CWV, forms, screenshots, axe | I |
| `verification-loop` | qa | 6-phase verification (build, type, lint, test, security, diff) | J |
| `generic-site-auditor` | audit | 6-phase audit (Visual, Copy, Layout, Motion, Technical) | H, I |
| `frontend-a11y` | a11y | WCAG 2.2 AA patterns for React/Next.js | H |
| `vercel-react-best-practices` | perf | 70+ perf rules from Vercel Engineering | H, J |
| `ultimate-frontend-skills` | fallback | House style fallback, engines (gradient.js, depth.js, etc.) | H, J |
| `impeccable-design-polish` | polish | Post-gen audit, critique, polish, harden | K, L |
| `systematic-debugging` | debug | Bug diagnosis before fixes | K |
| `ship-it` | delivery | End-to-end delivery coordination | L |
| `svg-creator` | svg | SVG asset creation, background props, patterns | C (Sec 10) |
| `pixabay-fetcher` | image | High-quality free image fetching from Pixabay | C (Sec 11) |
| `agent-spawner` | parallel | Sub-agent architecture for parallel execution (~47% token reduction) | C (Sec 12) |

## Design System References

| System | Category | Description |
|--------|----------|-------------|
| `default` | general | Default design system |
| `editorial` | editorial | Editorial aesthetic |
| `brutalist` | brutalist | Industrial-brutalist UI |
| `luxury` | luxury | High-end visual design |
| `shadcn` | component | shadcn/ui components |
| `vercel` | framework | Vercel-style layouts |
| ... | ... | 152 total catalogued in `design-systems/AGENTS.md` |

## Template References

| Template | Category | Description |
|----------|----------|-------------|
| `web-prototype` | prototype | Web prototype scaffold |
| `saas-landing` | landing | SaaS landing page |
| `open-design-landing` | landing | Open design landing |
| `html-ppt` | ppt | HTML presentation |
| ... | ... | 115 total catalogued in `design-templates/AGENTS.md` |

## Skill Category Keys

| Key | Meaning |
|-----|---------|
| `creative` | Design direction, taste, aesthetic decisions |
| `stack` | Technology stack choices (React, Next.js, etc.) |
| `craft` | Universal design rules (typography, color, motion) |
| `motion` | Animation and motion patterns |
| `qa` | Quality assurance and testing |
| `audit` | Site audits and compliance checks |
| `a11y` | Accessibility |
| `perf` | Performance optimization |
| `fallback` | Default/backup patterns |
| `svg` | SVG asset creation |
| `image` | Image sourcing and fetching |
| `parallel` | Sub-agent/spawn architecture |

---

## Source Skill Submodules

| Skill | Repo | Purpose |
|-------|------|---------|
| `svg-creator` | `https://github.com/upbrew-tech/svg-creator-skill` | SVG asset creation, background props, patterns |
| `pixabay-fetcher` | internal | High-quality free image fetching from Pixabay |
| `agent-spawner` | internal | Sub-agent architecture for parallel execution |

---

## Integrations + Skills Surfaces

This directory is surfaced by the Integrations + Skills panel. Each skill's `SKILL.md` frontmatter `name` field must be unique. User-imported skills with the same `name` will shadow built-in entries. Renderable templates are read from the design-templates registry.