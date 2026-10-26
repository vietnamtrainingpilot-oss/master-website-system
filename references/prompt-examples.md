# Master Website — Prompt Examples

Ready-to-use prompts for generating the master-website plugin website and testing.

---

## 🎯 Main Prompt — Plugin Website

Copy-paste this into OpenCode to generate the plugin's own website:

```bash
/master-website "Build a premium developer landing page for 'master-website' — an OpenCode skill that autonomously produces production-ready websites from a brief through a 13-phase pipeline (A–M). 

**Audience**: Developers, DevOps engineers, AI-assisted coding teams, OpenCode users.

**Value Proposition**: 
- One command: /master-website "your brief" → complete website
- 13-phase pipeline with hard gates (design doc → research → design direction → design system → template → implement → animation → engineering → browser QA → verification → fix → deliver → optional video)
- 169 skills synthesized, 152 design systems, 115 templates catalogued
- WCAG 2.2 AA, Core Web Vitals, anti-AI-slop defaults, review-animations hard gate
- Optional video pipeline (Phase M) with HyperFrames/Remotion

**Key Features to Highlight**:
- Phase C mandatory skills: svg-creator (SVG background props), pixabay-fetcher (hero images), agent-spawner (parallel sub-agents, ~47% token reduction)
- Three taste dials: VARIANCE (deviation), MOTION (animation), DENSITY (information)
- 30+ banned LLM defaults with before/after examples
- Real design systems (official packages only): @fluentui, @material/web, @carbon/react, polaris.js, govuk-frontend, uswds, shadcn/ui, Tailwind v4
- Never invent hex values — copy tokens.css :root verbatim

**Design Direction**:
- Developer-focused, technical credibility, not marketing fluff
- Clean, high-density (DENSITY ~50), moderate motion (MOTION ~40), low variance (VARIANCE ~30)
- Code-first aesthetic: monospace, syntax highlighting, terminal blocks
- Dark mode default, reduced-motion respect
- Live validation badges: 37/39 checks PASS

**Sections Required**:
1. Hero with one-liner, live demo link, install command
2. What You Get (output tree)
3. Installation prerequisites table (Node 18+, Python 3.10+, uv, Graphify, Playwright, OpenCode)
4. Usage examples (SaaS landing, portfolio, docs site, video project)
5. 13-phase pipeline table with hard gates
6. Phase C deep-dive (svg-creator, pixabay-fetcher, agent-spawner)
6. Live skills table (17 skills with purpose)
7. Design systems & templates catalog counts
8. Validation results (37 PASS / 2 FAIL optional)
9. GitHub link, license (Apache-2.0)

**Technical Stack**: vanilla HTML/CSS/JS (framework: html), self-contained, deployable to GitHub Pages
**Output Dir**: ./website-output/master-website-landing
```

---

## 🧪 Testing & Example Prompts

### 1. Minimal Smoke Test
```bash
/master-website "Simple hello world page with title, paragraph, and button. Dark mode. No animations. Output vanilla HTML."
```
**Expected**: Single HTML file, < 5KB, loads in < 100ms, passes all hard gates.

### 2. SaaS Landing (Full Pipeline)
```bash
/master-website "SaaS landing for 'DevPulse' — real-time API monitoring. Hero with live metrics demo, features grid (5 items), pricing table (3 tiers), testimonials carousel, footer with GitHub/Discord links. Dark mode default, cobalt accent. LCP < 2.5s."
```

### 3. Portfolio (Editorial Aesthetic)
```bash
/master-website "Designer portfolio for Maya Chen — editorial aesthetic, warm paper tones, italic serif display (Atelier Zero), collage-on-grid case studies, generous whitespace. Minimal motion (MOTION 30), low density (DENSITY 25). Case studies: 3 projects with process shots."
```

### 4. Documentation Site
```bash
/master-website "Documentation site for 'GraphQL Mesh' — search (Algolia), dark mode, versioned sidebar (v0.1–v1.2), code playground with live query editor, copy-to-clipboard, edit-on-GitHub links. High density (DENSITY 60), low motion (MOTION 20)."
```

### 5. Video Project (Phase M)
```bash
/master-website "Product launch video for 'DevPulse' SaaS — 60s vertical (9:16) for TikTok/Reels/Shorts. Hero demo (15s), feature walkthrough (30s), pricing + CTA (15s). Beat-synced cuts, kinetic typography, caption accuracy > 95%. HyperFrames pipeline."
```

### 6. Brutalist / Swiss Style
```bash
/master-website "Agency manifesto site — brutalist/Swiss print: newsprint canvas, monolithic grotesque (Space Grotesk), viewport-bleeding numerals, hazard-red accent (#FF001F). High variance (VARIANCE 90), anti-default maximal. No rounded corners, no shadows."
```

### 7. Template Reuse Test
```bash
/master-website "SaaS landing using saas-landing template + default design system. Custom: hero copy, 3 features, 2 pricing tiers, client logos. Override only tokens.css accent color to emerald (#10B981)."
```

### 8. Edge Case — No Template Match
```bash
/master-website "Real-time collaborative whiteboard with WebGL canvas, multi-user cursors, sticky notes, infinite zoom. Custom build — no template matches."
```

---

## ⚡ Quick Validation Commands

```bash
# Validate skill structure
python validate.py

# Check all 13 phase files exist
ls references/phase-*.md | wc -l  # Should be 13

# Check skill catalog
ls references/skills/ | wc -l    # Should be 169

# Verify dials.json
cat references/dials.json

# Check design systems catalog
grep -c "## " references/design-systems/AGENTS.md  # Should show 152

# Check templates catalog
grep -c "## " references/design-templates/AGENTS.md  # Should show 115
```

---

## 📋 Expected Output Structure

```
website-output/master-website-landing/
├── index.html              # Entry point
├── tokens.css              # Design system :root block (verbatim)
├── styles.css              # Project styles
├── scripts/
│   ├── motion.js           # IntersectionObserver reveals, reduced-motion
│   └── interactions.js     # Smooth scroll, copy buttons, theme toggle
├── assets/
│   ├── images/             # SVG props (from svg-creator), Pixabay hero
│   └── fonts/              # Self-hosted (Space Grotesk, Geist, etc.)
├── ATTRIBUTION.md          # Full source registry
├── DECISION_RECORD.md      # Template choice, dials, rationale
├── VERIFICATION_REPORT.md  # Browser QA, verification-loop, audit
└── README.md               # Run/deploy instructions
```

---

## 🎨 Design System Selection Guide

| Brief Reads As… | Use System | Package |
|----------------|-----------|---------|
| Dev tool / technical | `default` | Native CSS + Tailwind v4 |
| Microsoft / enterprise | Fluent UI | `@fluentui/react-components` |
| Google / Material | Material 3 | `@material/web` |
| IBM / analytics | Carbon | `@carbon/react` |
| Shopify app | Polaris | `polaris.js` |
| Atlassian / Jira | Atlassian | `@atlaskit/*` |
| UK public sector | GOV.UK | `govuk-frontend` |
| US public sector | USWDS | `uswds` |
| Fast MVP | Bootstrap 5.3 | `bootstrap` |
| Accessible React base | Radix Themes | `@radix-ui/themes` |
| Own components | shadcn/ui | `npx shadcn@latest add ...` |
| Indie SaaS | Tailwind v4 | `tailwindcss` |

**Rule**: Never mix systems. Install official package, copy `:root` verbatim.

---

## 🔧 Phase C Mandatory Skills Reference

### svg-creator (Section 10)
```bash
# Background props trigger: VARIANCE > 5, MOTION > 4
svg-creator --type grid --color var(--accent) --opacity 0.06
svg-creator --type gradient-mesh --colors var(--accent),var(--fg) --blur 40
svg-creator --type circles --count 12 --size-variance 0.4
```

### pixabay-fetcher (Section 11)
```bash
# Hero background, texture overlays
pixabay-fetcher --query "abstract technology dark" --orientation horizontal --min-width 1920
pixabay-fetcher --query "paper texture" --orientation horizontal --min-width 2000
pixabay-fetcher --query "developer workspace" --orientation horizontal --min-width 1920
```

### agent-spawner (Section 12)
```bash
# Automatic during Phase C — spawns:
# - design-agent: design direction, dials, anti-defaults
# - svg-agent: SVG background props generation
# - image-agent: Pixabay fetching & optimization
# ~47% token reduction vs sequential
```

---

## 🔗 Related Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Root skill with phase guide & hard gates |
| `README.md` | Full installation & usage docs |
| `phase-a-intake.md` | Design Read template |
| `phase-c-design-direction.md` | Phase C with Sections 10-14 |
| `references/dials.json` | Taste dial defaults |
| `references/design-systems/AGENTS.md` | 152 systems catalog |
| `references/design-templates/AGENTS.md` | 115 templates catalog |
| `references/skills/AGENTS.md` | 172 skills catalog |
| `validate.py` | Structural validation |

---

*Generated prompts for master-website plugin v1.0.0 — run via `/master-website` in OpenCode*