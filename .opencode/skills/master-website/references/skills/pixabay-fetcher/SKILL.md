---
name: pixabay-fetcher
description: Fetch high-quality free images from Pixabay API for use in website designs. Search by keywords, categories, colors, orientation, and more. Returns high-resolution images with proper attribution.
---

# Pixabay Image Fetcher Skill

## Purpose
Fetch high-quality, royalty-free images from Pixabay for use in website designs, backgrounds, hero sections, and content. All images are free for commercial use with attribution.

## API Setup
```bash
# Get your free API key from https://pixabay.com/api/docs/
export PIXABAY_API_KEY="your-api-key-here"
```

## Usage
```bash
# Search for images
python scripts/pixabay_fetcher.py search --query "modern office workspace" --category backgrounds --orientation horizontal --min-width 1920 --min-height 1080 --per-page 10

# Download images
python scripts/pixabay_fetcher.py download --urls-file urls.json --output-dir ./assets/images

# Search by color
python scripts/pixabay_fetcher.py search --query "abstract background" --colors blue,teal --orientation horizontal --per-page 20
```

## Search Parameters
| Parameter | Description | Options |
|-----------|-------------|---------|
| `query` | Search keywords | Any text |
| `category` | Image category | backgrounds, textures, patterns, business, technology, nature, education, people, places, transportation, animals, fashion, sports, science, health, computer, food, music |
| `orientation` | Image orientation | horizontal, vertical, all |
| `colors` | Dominant colors | red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown |
| `orientation` | Image orientation | horizontal, vertical, all |
| `min_width` | Minimum width in pixels | integer |
| `min_height` | Minimum height in pixels | integer |
| `per_page` | Results per page | 3-200 (default 20) |
| `page` | Page number | integer (default 1) |
| `order` | Sort order | popular, latest |
| `safe_search` | Safe search | true/false (default true) |

## Output
Returns JSON with:
- Image URLs (multiple sizes)
- Photographer info
- Tags
- Image stats (views, downloads, likes)
- Direct download URLs

## Integration with Design System
Images fetched can be:
- Used as hero backgrounds
- Section backgrounds with CSS `background-image`
- Inline images in content
- Hero image placeholders in templates
- Background props for SVG compositions

## Attribution
All images require attribution: "Image by [photographer] from Pixabay"
Include in footer or image caption.

## Scripts
- `scripts/pixabay_fetcher.py` - Main CLI
- `scripts/pixabay_search.py` - Search module
- `scripts/pixabay_download.py` - Download module