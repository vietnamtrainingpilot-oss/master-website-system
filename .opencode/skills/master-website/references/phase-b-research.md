# Phase B — Research & Source Discovery

## Purpose
Conduct reconnaissance, harvest assets, verify sources. Output: **Source Package** (verified assets, color palette candidates, typography samples, reference URLs, interaction patterns).

## Workflow

### Step 1: Web Clone Recon (from web-clone — 6-step methodology)

1. **Scope Definition** — Target URL, pages to crawl, depth limit
2. **Asset Harvest** — Download all images, fonts, CSS, JS, media
3. **Route Crawl** — Map all routes, params, dynamic segments
4. **Interaction Probe** — Click, hover, scroll, form submit on every element
5. **State Capture** — Screenshot every breakpoint (320, 768, 1024, 1440, 1920)
6. **Source Verification** — Hash assets, verify licenses, flag restricted

**Tools**: gent-browser for automation, isual-research for visual analysis, exa-search for neural search.

### Step 2: Competitive Ads Extraction (from competitive-ads-extractor)
- Pull active ads from Meta/Google/TikTok libraries
- Analyze copy, creative, targeting signals
- Map to competitor positioning

### Step 3: Video/Audio Source Mining (from youtube-clipper, ideo-downloader)
- Extract reference motion, transitions, pacing
- Download for frame-by-frame analysis in Phase G

### Step 4: Deep Research (from deep-research, utoresearch, utoresearch)
- Plan sub-questions
- Search + deep-read sources
- Synthesize with inline citations + confidence levels

### Step 5: Document Hunting (from document-hunter)
- Court filings, government reports, public records
- Primary source PDFs → clean markdown via defuddle

### Step 6: Wiki/Vault Retrieval (from wiki-retrieve)
- BM25 + Nomic reranking on local knowledge vault
- Contextual retrieval for brand history, prior decisions

## Hard Gate
> **Source Package verified** → Proceed to Phase C
> If gaps → Expand research

## Cross-References
- Assets → Phase C (design direction), Phase E (template content)
- Color/typography samples → Phase C (dial calibration)
- Interaction patterns → Phase G (animation reference)
