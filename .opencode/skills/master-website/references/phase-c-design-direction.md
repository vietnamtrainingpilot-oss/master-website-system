---

## 10. SVG ASSET CREATION & BACKGROUND PROPS (from `svg-creator` skill)

### 10.A When to Create SVG Assets
Create custom SVG assets when the design read calls for:
- **Background props**: circles, geometric shapes, decorative elements that add depth
- **Custom icons/logos**: brand marks, monograms, abstract glyphs
- **Illustrations**: abstract art, patterns, diagrams, infographics
- **Animations**: CSS/SMIL animations, GSAP-driven SVG animations
- **Patterns**: repeating tiles, geometric patterns, textures

### 10.B SVG Creator Workflow (from `svg-creator` skill)
Every SVG goes through the mandatory feedback loop:

```
WRITE SVG → RENDER → VIEW PNG → ASSESS → FIX → RENDER → VIEW → ... → DELIVER
```

**Step-by-step:**
1. **Write SVG** to a working file (`draft.svg`)
2. **Render** using the SVG loop script (mandatory)
3. **View** the rendered PNG (mandatory - must visually inspect)
4. **Assess** - check visual quality, composition, colors
5. **Fix** - edit SVG, re-render, re-view
6. **Deliver** - when perfect, deliver final SVG + preview PNG

### 10.C Background Props Library (Reusable SVG Props)
Create a library of reusable SVG background props:

| Prop Type | Use Case | VARIANCE Gate |
|-----------|----------|---------------|
| **Circles/Orbs** | Hero background depth, floating orbs | VARIANCE > 5 |
| **Geometric Shapes** | Angular accents, tech feel | VARIANCE > 6 |
| **Abstract Blobs** | Organic feel, fluid backgrounds | VARIANCE > 5, MOTION > 4 |
| **Grid Patterns** | Tech/enterprise feel, subtle texture | VARIANCE > 4 |
| **Gradient Meshes** | Premium feel, depth | VARIANCE > 7 |
| **Line Patterns** | Editorial/tech feel, rhythm | VARIANCE > 4 |
| **Particle Systems** | Dynamic backgrounds, motion | MOTION > 5 |
| **Gradient Orbs** | Premium hero depth, glow | VARIANCE > 6, MOTION > 4 |

### 10.D SVG Background Props Templates

#### Circle/Orb Background Prop
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <radialGradient id="orb-gradient" fx="0.3" fy="0.3" r="0.7">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1e3a5f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.1"/>
    </radialGradient>
    <filter id="glow" color-interpolation-filters="linearRGB">
      <feGaussianBlur stdDeviation="20" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="400" cy="300" r="300" fill="url(#orb-gradient)" filter="url(#glow)" opacity="0.4"/>
</svg>
```

#### Geometric Grid Pattern
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" patternUnits="userSpaceOnUse" width="100" height="100">
  <pattern id="grid" patternUnits="userSpaceOnUse" width="40" height="40">
    <line x1="0" y1="0" x2="40" y2="0" stroke="currentColor" stroke-width="0.5" opacity="0.1"/>
    <line x1="0" y1="0" x2="0" y2="40" stroke="currentColor" stroke-width="0.5" opacity="0.1"/>
  </pattern>
  <rect width="100" height="100" fill="url(#grid)"/>
</svg>
```

#### Gradient Mesh Background
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <radialGradient id="mesh1" cx="20%" cy="20%" r="60%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#1e3a5f" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="mesh2" cx="80%" cy="80%" r="60%">
      <stop offset="0%" stop-color="#ec4899" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#831843" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="#0f172a"/>
  <ellipse cx="160" cy="120" rx="400" ry="300" fill="url(#mesh1)"/>
  <ellipse cx="640" cy="480" rx="400" ry="300" fill="url(#mesh2)"/>
</svg>
```

### 10.E SVG Creation Checklist
- [ ] Written with proper document structure (defs, groups, semantic IDs)
- [ ] Uses `color-interpolation="linearRGB"` on gradients
- [ ] Uses `color-interpolation-filters="linearRGB"` on filters
- [ ] Uses `transform-box: fill-box; transform-origin: center;` for animations
- [ ] Multi-stop gradients (4+ stops) with hue shifts
- [ ] Shadows use colored blues/purples/teals, never pure black
- [ ] Grain/noise filter on fixed pseudo-elements only
- [ ] Tested in both light and dark mode
- [ ] Accessible: `role="img"` + `aria-labelledby` + `<title>`
- [ ] Rendered and visually verified before delivery

---

## 11. PIXABAY IMAGE FETCHING (from `pixabay-fetcher` skill)

### 11.A When to Use Pixabay Images
Use Pixabay when:
- Need high-quality photography for hero backgrounds
- Need lifestyle/product shots for sections
- Need texture/pattern images for backgrounds
- Need abstract/color-themed images for sections
- Need free commercial-use images with attribution

### 11.B Search Strategy by Section

| Section | Query Strategy | Category | Orientation | Colors |
|---------|---------------|----------|-------------|--------|
| Hero | `[brand] [product] [mood]` | backgrounds | horizontal | brand colors |
| Features | `[feature] [concept]` | technology/business | horizontal | accent color |
| Testimonials | `professional portrait` | people | vertical | neutral |
| Background textures | `abstract texture pattern` | textures/patterns | all | brand colors |
| Team/About | `team collaboration workspace` | people/business | horizontal | warm neutrals |

### 11.C Search Parameters by Design Dials

| Dial Setting | Pixabay Parameters |
|--------------|-------------------|
| **VARIANCE > 7** | `category: backgrounds, orientation: horizontal, colors: brand palette, per_page: 20` |
| **MOTION > 5** | `category: backgrounds, orientation: horizontal, colors: dynamic palette, order: latest` |
| **DENSITY < 4** | `category: backgrounds, orientation: horizontal, per_page: 10, min_width: 2560` |
| **DENSITY > 7** | `category: textures/patterns, per_page: 30, min_width: 1920` |

### 11.C Search Examples

```bash
# Hero background for premium SaaS
pixabay search --query "modern minimalist workspace clean" --category backgrounds --orientation horizontal --colors blue,teal --min-width 2560 --per-page 20

# Abstract background for tech section
pixabay search --query "abstract technology background mesh gradient" --category backgrounds --colors blue,purple --orientation horizontal --per-page 15

# Texture for card backgrounds
pixabay search --query "paper texture grain subtle" --category textures --orientation all --colors gray,white --per-page 20
```

### 11.D Integration with Design System
```css
/* CSS variable for hero background */
:root {
  --hero-bg-image: url('/assets/images/hero-bg.jpg');
  --hero-bg-overlay: linear-gradient(135deg, var(--color-primary) 0%, transparent 100%);
}

/* CSS for section backgrounds */
.section-bg {
  background-image: var(--section-bg-image);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
```

### 11.E Attribution Requirements
All Pixabay images require attribution:
```html
<!-- In footer or image caption -->
<p class="attribution">Image by <a href="https://pixabay.com/users/{photographer}-{id}">{photographer}</a> from <a href="https://pixabay.com">Pixabay</a></p>
```

---

## 12. AGENT SPAWNING ARCHITECTURE (from `agent-spawner` skill)

### 12.A Why Agent Spawning?
- **Token Reduction**: ~47% token reduction vs monolithic agent
- **Quality**: Specialized agents produce higher quality
- **Parallel Execution**: Multiple agents work simultaneously
- **Focus**: Each agent handles one specialized domain

### 12.B Agent Architecture

| Agent Type | Specialization | Token Budget | Skills Referenced |
|------------|----------------|--------------|-------------------|
| **design-agent** | Visual design, UI/UX, color, typography | 3000 | design-taste, svg-creator, pixabay-fetcher |
| **code-agent** | Implementation, components, logic | 4000 | frontend-patterns, react-patterns |
| **research-agent** | Web research, competitive analysis | 2000 | web-clone, exa-search |
| **svg-agent** | SVG creation, icons, illustrations | 3000 | svg-creator |
| **image-agent** | Image fetching, optimization | 2000 | pixabay-fetcher |
| **video-agent** | Video creation, editing | 5000 | hyperframes, remotion, media-use |
| **qa-agent** | Testing, accessibility, performance | 2000 | browser-qa, verification-loop |
| **content-agent** | Copywriting, SEO, content strategy | 2000 | copywriting, seo-audit |

### 12.C Spawning Protocol

**Main Agent (Orchestrator)** decomposes task → spawns sub-agents → aggregates results.

**Spawn Request:**
```json
{
  "agent_type": "design-agent",
  "task": "Create hero section design with SVG background props and Pixabay images",
  "context": {
    "design_system": "tokens.css",
    "dials": {"variance": 60, "motion": 50, "density": 40},
    "references": ["references/skills/svg-creator/", "references/skills/pixabay-fetcher/"]
  },
  "output_format": "design_spec.json",
  "max_tokens": 3000
}
```

### 12.D Phase C Agent Spawning Workflow

**Phase C Agent Spawning:**
```python
# Main agent spawns for Phase C
spawn("design-agent", "Create design direction with SVG props and Pixabay images", context)
spawn("svg-agent", "Create background props: circles, geometric shapes, gradient meshes", context)
spawn("image-agent", "Fetch Pixabay hero images for background textures", context)
```

**Expected Outputs:**
- `design_spec.json` - Complete design direction
- `svg_props/` - Generated SVG background props
- `pixabay_images/` - Downloaded hero/section images
- `design_direction.md` - Complete design direction document

### 12.E Token Optimization Results

| Approach | Tokens | Quality |
|----------|--------|---------|
| Monolithic Agent | ~15,000 | Lower (divided attention) |
| Agent Swarm | ~8,000 | Higher (specialization) |
| **Savings** | **~47%** | **Higher quality** |

---

## 13. PHASE C EXECUTION CHECKLIST (Updated)

- [ ] **Design Read** completed (Section 0)
- [ ] **Dials Set** (VARIANCE/MOTION/DENSITY)
- [ ] **Design System Selected** (Section 2)
- [ ] **SVG Props Created** (Section 10)
- [ ] **Pixabay Images Fetched** (Section 11)
- [ ] **Agent Spawning Executed** (Section 12)
- [ ] **Design Direction Doc** generated
- [ ] **Anti-Default Decisions** documented (min 5)
- [ ] **Design Direction Doc** approved → Proceed to Phase D

---

## 14. QUICK REFERENCE: ASSET CREATION COMMANDS

```bash
# Create SVG background prop
svg-creator create --type background-prop --type circle --output ./assets/svg/circle-bg.svg

# Create geometric pattern
svg-creator create --type pattern --type grid --output ./assets/svg/grid-pattern.svg

# Create gradient mesh
svg-creator create --type mesh --colors "#3b82f6,#ec4899" --output ./assets/svg/gradient-mesh.svg

# Search Pixabay for hero images
pixabay search --query "modern minimalist workspace" --category backgrounds --orientation horizontal --colors blue,teal --min-width 2560 --per-page 20 --output hero-images.json

# Download hero images
pixabay download --urls-file hero-images.json --output-dir ./assets/images/hero --size largeImageURL

# Spawn design agent for Phase C
agent-spawner spawn --type design-agent --task "Create design direction with SVG props" --context context.json

# Spawn SVG agent for background props
agent-spawner spawn --type svg-agent --task "Create background props: circles, geometric shapes, gradient meshes" --context context.json

# Spawn image agent for Pixabay images
agent-spawner spawn --type image-agent --task "Fetch Pixabay hero images for background textures" --context context.json
"

## Credits & Attribution