---
name: pixabay-fetcher
description: "Fetch high-quality free images from Pixabay for hero backgrounds, textures, lifestyle shots. Used in Phase C Section 11. Requires PIXABAY_API_KEY env var."
triggers:
  - "pixabay"
  - "hero background"
  - "stock photo"
  - "texture overlay"
od:
  mode: utility
  category: image
---
# pixabay-fetcher — Pixabay Image Fetcher

## Purpose
Fetch high-quality, royalty-free images from Pixabay API for hero backgrounds, section backgrounds, texture overlays. Used during Phase C (Design Direction) Section 11.

## Prerequisites
```bash
# Set API key (get from https://pixabay.com/api/docs/)
export PIXABAY_API_KEY="your-key-here"
# Or add to .opencode/master-website.config.json
```

## Usage
```bash
# In OpenCode:
/pixabay-fetcher --query "abstract technology dark" --orientation horizontal --min-width 1920 --count 5
/pixabay-fetcher --query "paper texture" --orientation horizontal --min-width 2000 --category textures
/pixabay-fetcher --query "developer workspace" --orientation horizontal --min-width 1920 --quality high
```

## Parameters
| Param | Required | Default | Description |
|-------|----------|---------|-------------|
| --query | Yes | - | Search terms |
| --orientation | No | horizontal | horizontal, vertical, all |
| --min-width | No | 1920 | Minimum image width |
| --min-height | No | 1080 | Minimum image height |
| --category | No | all | backgrounds, textures, nature, technology, etc. |
| --quality | No | high | high, medium |
| --count | No | 5 | Number of results to fetch |
| --output-dir | No | ./assets/images/pixabay | Output directory |

## Phase C Integration
- **Trigger**: Hero background needed, texture overlays, lifestyle shots
- **Output**: Downloaded images to `website-output/assets/images/pixabay/`
- **Attribution**: Auto-generated in `ATTRIBUTION.md` with Pixabay URLs and author credits

## Example Queries by Use Case
| Use Case | Query |
|----------|-------|
| SaaS hero | "abstract technology dark gradient", "neural network visualization" |
| Portfolio | "designer workspace minimal", "creative studio interior" |
| Docs site | "code screen dark mode", "developer terminal" |
| Texture | "paper texture white", "concrete wall", "fabric linen" |

## Installation
Installed globally at `~/.config/opencode/skills/pixabay-fetcher/`
