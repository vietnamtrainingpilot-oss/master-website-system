---
name: svg-creator
description: "Create SVG background props (circles, geometric shapes, gradient meshes, grid patterns) for web backgrounds and animated props. Used in Phase C when VARIANCE > 5 or MOTION > 4."
triggers:
  - "svg background"
  - "svg props"
  - "gradient mesh"
  - "grid pattern"
  - "geometric shapes"
od:
  mode: utility
  category: svg
---
# svg-creator — SVG Background Props Generator

## Purpose
Generate SVG background props for web projects: circles, geometric shapes, gradient meshes, grid patterns, noise textures. Used during Phase C (Design Direction) when taste dials indicate need for custom background assets.

## Usage
```bash
# In OpenCode:
/svg-creator --type grid --color "#2F6FEB" --opacity 0.06 --size 40
/svg-creator --type gradient-mesh --colors "#2F6FEB,#10B981" --blur 40 --aspect 16:9
/svg-creator --type circles --count 12 --size-variance 0.4 --color var(--accent)
```

## Types

| Type | Parameters | Use Case |
|------|------------|----------|
| `grid` | --color, --opacity, --size, --stroke-width | Technical backgrounds, developer sites |
| `gradient-mesh` | --colors (comma-separated), --blur, --aspect | Hero backgrounds, premium feel |
| `circles` | --count, --size-variance, --color, --opacity | Playful, organic backgrounds |
| `geometric` | --shape (triangle|hex|diamond), --color, --opacity | Brutalist, Swiss-style |
| `noise` | --opacity, --color, --grain | Textured overlays |

## Phase C Integration
- **Trigger**: VARIANCE > 5 (background props) or MOTION > 4 (animated props)
- **Output**: SVG files to `website-output/assets/images/svg-props/`
- **Reference**: Copied into `tokens.css` as background-image or inline SVG

## Example Output
```svg
<!-- Grid pattern -->
<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg">
  <path d="M40 0H0V40" fill="none" stroke="#2F6FEB" stroke-width="0.5" opacity="0.06"/>
</svg>

<!-- Gradient mesh -->
<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="blur"><feGaussianBlur stdDeviation="40"/></filter>
  </defs>
  <circle cx="400" cy="200" r="300" fill="#2F6FEB" filter="url(#blur)"/>
  <circle cx="1500" cy="800" r="400" fill="#10B981" filter="url(#blur)"/>
</svg>
```

## Installation
Installed globally at `~/.config/opencode/skills/svg-creator/`
