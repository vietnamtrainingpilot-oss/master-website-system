# Phase E — Select & Prepare Template

## Purpose
Choose the right template for the project, prepare content structure, and configure template with Design System tokens. Output: **Template Package** (initialized project with content placeholders, Design System integrated).

## Workflow

### Step 1: Template Selection (from `web-prototype`, `saas-landing`, `open-design-landing`, `frontend-design-direction`)

Reference `references/design-templates/AGENTS.md` — 115 cataloged templates. Each has:
- Section library (8–12 sections)
- Responsive breakpoints
- Motion integration points
- Content placeholder structure

**Selection Matrix**:

| Project Type | Recommended Templates | Sections |
|--------------|----------------------|----------|
| SaaS Landing | `web-prototype`, `saas-landing` | Hero, Features, Pricing, Testimonials, FAQ, CTA, Footer |
| Marketing Site | `open-design-landing`, `scroll-craft` | Hero, Value Props, Social Proof, Blog, Contact |
| Portfolio | `minimalist-ui`, `scroll-craft` | Hero, Work, About, Process, Contact |
| Agency/Creative | `industrial-brutalist-ui`, `ptfs-va-website-builder` | Hero, Services, Case Studies, Team, Contact |
| E-commerce | `web-prototype`, `saas-landing` | Hero, Products, Categories, Cart, Checkout |
| Documentation | `html-ppt`, `slides` | Hero, TOC, Content, Search, Sidebar |

**From `template-selection-guide.md`**: Match template to:
- Dial settings (VARIANCE/MOTION/DENSITY)
- Content structure (from Design Read)
- Brand personality (from Phase A/C)

### Step 2: Presentation-Specific Templates (from `pptx-guide.md`)

If deliverable includes presentations:
- `html-ppt` — 36 themes, 15 templates, presenter mode
- `html-ppt-presenter-mode-reveal` — Magnetic cards, keyboard nav
- `slides` — Strategic HTML presentations with Chart.js
- `frontend-slides` — Convert PPT/PPTX to web
- `wowerpoint` — Kawaii NotebookLM slide-deck PDF
- `pptx-html-fidelity-audit` — Audit python-pptx vs HTML
- Variants: `html-ppt-taste-brutalist`, `html-ppt-taste-editorial`, `deck-swiss-international`, `deck-guizang-editorial`, `deck-open-slide-canvas`, `nanobanana-ppt`, `ppt-keynote`

### Step 3: Initialize Template with Design System

```bash
# Clone template
git clone [template-repo] [project-name]
cd [project-name]

# Install Design System tokens
cp [design-system]/tokens.css src/styles/tokens.css
cp [design-system]/components/* src/components/

# Configure Tailwind (if applicable)
# Update tailwind.config.js with design tokens
```

**Token Injection Checklist**:
- [ ] All CSS variables from tokens.css available
- [ ] Tailwind theme extended with design tokens
- [ ] Component library imports working
- [ ] Motion tokens available to animation library
- [ ] Typography scale applied globally

### Step 4: Content Preparation (from `web-prototype`, `writing-plans`)

Map Design Read content to template sections:

| Template Section | Content Source | Status |
|-----------------|----------------|--------|
| Hero | Design Read: Primary goal, key message | ☐ Draft / ☐ Ready |
| Value Props | Design Read: Key differentiators | ☐ Draft / ☐ Ready |
| Features | Design Read: User needs, pain points | ☐ Draft / ☐ Ready |
| Social Proof | Research: Testimonials, logos, metrics | ☐ Draft / ☐ Ready |
| Pricing | Business: Plans, features, CTAs | ☐ Draft / ☐ Ready |
| FAQ | Research: Common objections | ☐ Draft / ☐ Ready |
| CTA | Design Read: Primary action | ☐ Draft / ☐ Ready |
| Footer | Brand: Links, legal, contact | ☐ Draft / ☐ Ready |

**From `writing-plans`**: Each section gets a self-contained context brief:
- File path
- Current state
- Desired state
- Key context (imports, props, related files)
- Constraints
- Verification method

### Step 5: Asset Integration (from Phase B Source Package)

- Replace placeholder images with harvested/approved assets
- Apply color palette to SVGs/illustrations
- Generate missing assets via `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`
- Optimize all images (WebP, AVIF, responsive sizes)

## Hard Gate
> **Template Package ready** (initialized, tokens integrated, content mapped, assets placed) → Proceed to Phase F
> If gaps → Complete content/asset preparation

## Cross-References
- Consumes: Phase C (Design Direction), Phase D (Design System), Phase B (Assets)
- Produces: Template Package → Phase F
- Catalog: `references/design-templates/AGENTS.md` (115 templates)
- Specialty: `references/pptx-guide.md` for presentations