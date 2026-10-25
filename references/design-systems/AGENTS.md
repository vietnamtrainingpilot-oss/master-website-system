# Design-Systems Catalog — AGENTS.md

> **Authoritative catalog of all 152 curated/template design systems** under `D:/Master Design/design-systems/`.
> Generated from machine-enumeration + human inspection of `manifest.json` and `DESIGN.md`.
> Source of truth: `audit/source-audit.jsonl`.

## Schema Contract

Every design-system folder follows the v1 project contract (`/_schema/manifest.schema.ts`):

| File | Required? | Purpose |
|---|---|---|
| `manifest.json` | Yes (for manifest-guarded systems) | Machine-readable entry: id, name, category, source, files, craft, preview, importMode |
| `DESIGN.md` | Yes | Canonical design prose (colors, typography, components, rules) |
| `tokens.css` | Yes | Compiled CSS custom properties (`:root` token block) |
| `components.html` | Optional | Standalone component fixture |
| `USAGE.md` | Optional | Agent-facing package guide |
| `source/` | Optional | Importer evidence |
| `preview/` | Optional | Static preview pages |
| `assets/` | Optional | Brand assets, webfonts |
| `fonts/` | Optional | Webfont files |

### Token Layer Model

Every token answers two questions:
1. **Who decides the value?** — brand author (Layer A) or schema author (Layer B-slot).
2. **What happens if omitted?** — required, fallback, or alias.

| Layer | Who decides | If omitted | Examples |
|---|---|---|---|
| **A1-identity** | brand | guard fails | `--bg`, `--fg`, `--accent`, `--font-display` |
| **A1-structure** | brand | guard fails | type scale, `--container-max`, `--section-y-*` |
| **A2** | brand (with fallback) | guard fails today | `--motion-fast`, `--success`, `--space-4` |
| **B-slot** | brand or schema-suggested alias | guard fails | `--fg-2 → var(--fg)`, `--surface-warm → var(--surface)` |

**Rule:** Every brand's `:root` must declare every shared slot. Do not invent hex values — map to tokens.

## Tier Classification

- **CURATED (100+ lines of DESIGN.md):** Brand systems with source-derived, detailed specifications including color palettes, typography hierarchies, component specs, responsive behavior, and agent prompt guides. ~95 systems.
- **TEMPLATE (50–98 lines):** Systems generated from style-parameter templates with a standard structure (Theme > Color > Typography > Spacing > Layout > Components > Motion > Voice > Anti-patterns). ~57 systems.

The `default` system is special: it's the neutral modern starter with 6 `:root` variables, 12-col grid, and two-level elevation.

## Quick-Pick Guide

| Use case | Recommended systems |
|---|---|
| No specific brand → default starter | `default` (neutral modern) |
| Bespoke editorial / warm | `atelier-zero`, `kami`, `urdu` |
| Premium brand / tech product | `stripe`, `apple`, `vercel`, `linear-app`, `figma` |
| Fintech / crypto | `stripe`, `coinbase`, `binance`, `revolut`, `wise`, `mastercard` |
| Developer tools | `cursor`, `cloudflare-kumo`, `superhuman`, `github`, `warp` |
| AI / LLM product | `openai`, `claude`, `cohere`, `mistral-ai`, `ollama` |
| E-commerce | `shopify`, `nike`, `airbnb`, `meta` (store) |
| SaaS / productivity | `notion`, `linear-app`, `slack`, `cal`, `mintlify` |
| Bold / expressive | `brutalism`, `bold`, `dramatic`, `colorful`, `neobrutalism` |
| Dark / gaming / tech | `nike`, `bmw-m`, `ferrari`, `playstation`, `tetris` |
| Glassmorphism / modern | `glassmorphism`, `neumorphism`, `sleek` |

## Full Catalog

### AI & LLM (15)

- **claude** `Claude (Anthropic)` — *CURATED (260 lines)*. Anthropic's design language for AI interfaces: conversational layouts, clear outcomes, agentic workflow support.
- **cohere** `Cohere` — *CURATED (217 lines)*. AI platform UI: developer-first controls, API-focused workflows, technical documentation styling.
- **elevenlabs** `ElevenLabs` — *CURATED (219 lines)*. Voice/AI audio interface: waveform visuals, play controls, audio-centric design patterns.
- **huggingface** `Hugging Face` — *CURATED (122 lines)*. ML model hub: model cards, gradient-themed accents, dataset browsing patterns.
- **minimax** `MiniMax` — *CURATED (213 lines)*. Chinese AI platform: clean tech aesthetic, model showcase layouts.
- **mistral-ai** `Mistral AI` — *CURATED (212 lines)*. European AI lab: minimalist, research-focused, technical documentation styling.
- **ollama** `Ollama` — *CURATED (217 lines)*. Local LLM tooling: terminal-inspired, dark mode, code-first interface.
- **openai** `OpenAI` — *CURATED (115 lines)*. OpenAI product aesthetic: clean, research-forward, GPT UI patterns.
- **opencode-ai** `OpenCode` — *CURATED (227 lines)*. Code-generation IDE interface patterns, agent workflow UI, multi-panel layouts.
- **perplexity** `Perplexity AI` — *CURATED (217 lines)*. AI search/conversational research tool: answer-focused layouts, source attribution display.
- **replicate** `Reprolate` — *CURATED (213 lines)*. ML model inference UI: model galleries, inference output displays, API demo patterns.
- **runwayml** `Runway` — *CURATED (200 lines)*. Creative AI tooling: video editing UI, media-first interaction patterns.
- **together-ai** `Together AI` — *CURATED (214 lines)*. LLM API platform: dashboard-style, rate-limiting displays, model comparison UI.
- **voltagent** `VoltAgent` — *CURATED (271 lines)*. AI agent framework UI: agent workflow visualization, tool call displays, conversational interfaces.
- **x-ai** `xAI` — *CURATED (214 lines)*. Grok/xAI brand aesthetic: dark theme, futuristic tech styling.

### Automotive (7)

- **bmw** `BMW` — *CURATED (144 lines)*. Premium automotive: black/white minimalism, geometric grids, bold typography.
- **bmw-m** `BMM M` — *CURATED (186 lines)*. Performance variant: high-contrast, red accent, aggressive typography.
- **bugatti** `Bugatti` — *CURATED (217 lines)*. Ultra-luxury automotive: deep blacks, metallic accents, precision typography.
- **ferrari** `Ferrari` — *CURATED (262 lines)*. Supercar brand: Rosso Corsa red, black, racing heritage typography.
- **lamborghini** `Lamboborghini` — *CURATED (240 lines)*. Extreme performance: aggressive angles, bright accents, cyberpunk-influenced.
- **renault** `Renault` — *CURATED (260 lines)*. French automotive: bright accent colors, geometric forms, tech-forward.
- **tesla** `Tesla` — *CURATED (237 lines)*. Electric vehicle: minimal dark theme, sleek grids, product-focused photography.

### Backend & Data (9)

- **cisco** `Cisco` — *CURATED (160 lines)*. Enterprise networking: blue/white professional, B2B-focused, technical diagrams.
- **clickhouse** `ClickHouse` — *CURATED (233 lines)*. Database/analytics: dark theme, green accent, data-dense grids.
- **composio** `Composio` — *CURATED (255 lines)*. Developer tools: API-focused, tool listings, integration patterns.
- **hashicorp** `HashiCorp` — *CURATED (232 lines)*. DevOps tooling: orange accent, technical precision, infrastructure-focused.
- **mongodb** `MongoDB` — *CURATED (221 lines)*. Database: green accent, developer docs styling, data visualization.
- **posthog** `PostHog` — *CURATED (213 lines)*. Product analytics: data-dense dashboards, chart-heavy layouts.
- **sanity** `Sanity` — *CURATED (294 lines)*. Headless CMS: clean, content-editing focused, real-time collaboration UI.
- **sentry** `Sentry` — *CURATED (218 lines)*. Error monitoring: red/orange alerts, technical dashboard patterns.
- **supabase** `Supabase` — *CURATED (211 lines)*. Firebase alternative: green accent, developer-first, dashboard patterns.

### Bold & Expressive (9)

- **bold** `Bold` — *TEMPLATE (50 lines)*. High-contrast, saturated colors, dramatic typography.
- **brutalism** `Brutalism` — *TEMPLATE (51 lines)*. Raw anti-design: unadorned elements, jarring layouts, concrete-inspired.
- **colorful** `Colorful` — *TEMPLATE (50 lines)*. Vibrant multi-color palette, playful layouts.
- **dramatic** `Dramatic` — *TEMPLATE (50 lines)*. High contrast, bold visuals, cinematic feel.
- **energetic** `Energetic` — *TEMPLATE (51 lines)*. Dynamic layouts, motion-focused, vibrant energy.
- **expressive** `Expressive` — *TEMPLATE (50 lines)*. Creative layouts, expressive typography, artistic flair.
- **neobrutalism** `Neobrutalism` — *TEMPLATE (50 lines)*. Modern brutalist revival: raw, unpolished, high-contrast.
- **vibrant** `Vibrant` — *TEMPLATE (50 lines)*. Bright, saturated colors, energetic layouts.

### Creative & Artistic (9)

- **artistic** `Artistic` — *TEMPLATE (50 lines)*. Hand-crafted feel, creative layouts, artistic expression.
- **cafe** `Cadfe` — *TEMPLATE (50 lines)*. Warm, inviting, café-inspired color palette and layout.
- **cosmic** `Cosmic` — *TEMPLATE (50 lines)*. Space-themed, dark, cosmic color palette, celestial elements.
- **creative** `Creative` — *TEMPLATE (50 lines)*. Artistic layouts, creative expression, unconventional designs.
- **doodle** `Doodle` — *TEMPLATE (50 lines)*. Hand-drawn aesthetic, sketch-like elements, informal.
- **editorial** `Editorial` — *TEMPLATE (50 lines)*. Magazine/newspaper aesthetic, editorial typography.
- **fantasy** `Fantasy` — *TEMPLATE (50 lines)*. Mythical themes, fantasy-inspired colors and imagery.
- **friendly** `Friendly` — *TEMPLATE (50 lines)*. Warm, welcoming, approachable design elements.
- **lingo** `Lingo` — *TEMPLATE (50 lines)*. Language-focused, communication-centric design.
- **publication** `Publication` — *TEMPLATE (50 lines)*. Editorial/print publication styling, newspaper-like grids.
- **storytelling** `Storytelling` — *TEMPLATE (50 lines)*. Narrative-focused, sequential story layouts.

### Design & Creative (7)

- **airtable** `Airtable` — *TEMPLATE (71 lines)*. Database meets spreadsheet UI: pastel colors, grid-based, card-centric.
- **canva** `Canva` — *CURATED (130 lines)*. Design tool: colorful, creative, drag-and-drop interface patterns.
- **clay** `Clay` — *CURATED (249 lines)*. 3D clay-style design: organic shapes, soft 3D-inspired elements.
- **figma** `Figma` — *CURATED (177 lines)*. Design tool: dark theme, plugin UI, real-time collaboration patterns.
- **framer** `Framer` — *CURATED (203 lines)*. Interactive design tool: motion-focused, prototyping UI.
- **miro** `Miro` — *TEMPLATE (89 lines)*. Whiteboard/collaboration tool: infinite canvas, sticky notes, diagramming.
- **webflow** `Webflow` — *TEMPLATE (75 lines)*. No-code design tool: visual editor patterns, design-to-code workflows.

### Developer Tools (8)

- **cloudflare-kumo** `Cloudflare Kumo UI` — *TEMPLATE (90 lines)*. Cloudflare's UI framework: technical, code-focused, open-source oriented.
- **cursor** `Cursor` — *CURATED (256 lines)*. AI code editor: dark theme, multi-panel layout, code-focused.
- **expo** `Expo` — *CURATED (232 lines)*. React Native tooling: mobile-focused, developer docs styling.
- **github** `GitHub` — *CURATED (128 lines)*. Code repository: Primer design system, dark/light themes, issue/PR UI.
- **lovable** `Lovable` — *CURATED (248 lines)*. AI coding tool: chat-first interface, real-time code preview.
- **mission-control** `Mission Control Design System` — *CURATED (383 lines)*. NASA-inspired, mission-critical interfaces, data visualization.
- **raycast** `Raycast` — *CURATED (224 lines)*. Mac productivity launcher: command palette, extension UI, dark theme.
- **superhuman** `Superhuman` — *CURATED (209 lines)*. Email client: speed-focused, keyboard shortcuts, dark theme.
- **vercel** `Vercel` — *CURATED (259 lines)*. Frontend platform: clean, code-focused, deployment dashboards.
- **warp** `Warp` — *CURATED (210 lines)*. Terminal-based: command-line aesthetic, blocks layout, dark theme.

### E-Commerce & Retail (5)

- **airbnb** `Airbnb` — *CURATED (317 lines)*. Travel marketplace: warm, friendly, community-focused, bold typography.
- **meta** `Meta (Store)` — *CURATED (288 lines)*. Meta's store: product-focused, clean, social-commerce patterns.
- **nike** `Nike` — *CURATED (282 lines)*. Athleisure: bold, high-contrast, product imagery-first, athletic aesthetic.
- **shopify** `Shopify` — *CURATED (274 lines)*. E-commerce platform: Shopify Polar design system patterns.
- **starbucks** `Starbucks` — *CURATED (452 lines)*. Coffee retail: warm, earthy tones, brand-consistent, retail-focused.

### Editorial & Print (2)

- **atelier-zero** `Atelier Zero` — *CURATED (253 lines)*. Warm-paper editorial aesthetic: italic serif, collage-on-grid, magazine-style.
- **kami** `kami (紙/纸,)` — *CURATED (335 lines)*. Paper-based design system with Japanese typography influence.

### Fintech & Crypto (7)

- **binance** `Binance.US` — *CURATED (269 lines)*. Cryptocurrency exchange: technical, data-dense, dark theme.
- **coinbase** `Coinbase` — *CURATED (100 lines)*. Crypto trading: blue accent, clean trading UI.
- **kraken** `Kraken` — *TEMPLATE (98 lines)*. Crypto exchange: orange accent, trading-focused, technical.
- **mastercard** `Mastercard` — *CURATED (301 lines)*. Financial brand: red/yellow brand colors, payment-centric.
- **revolut** `Revolut` — *CURATED (149 lines)*. Digital banking: green accent, mobile-first, financial data display.
- **stripe** `Stripe` — *CURATED (272 lines)*. Payment infrastructure: purple accent, shadow-tinted elevation, clean technical aesthetic.
- **wise** `Wise` — *CURATED (140 lines)*. International money transfer: green accent, borderless, value-focused.

### Layout & Structure (4)

- **bento** `Bento` — *TEMPLATE (50 lines)*. Card-based grid layouts, bento-box style.
- **levels** `Levels` — *TEMPLATE (50 lines)*. Hierarchical layouts, layered composition.
- **perspective** `Perspective` — *TEMPLATE (50 lines)*. Visual depth, layered elements, modern 3D feel.
- **spacious** `Spacious` — *TEMPLATE (50 lines)*. Generous whitespace, minimal, airy layouts.

### Media & Consumer (12)

- **apple** `Apple` — *CURATED (202 lines)*. Consumer electronics: precision editorial, black/white alternating chapters, SF Pro typography, cinematic product photography.
- **ibm** `IBM` — *CURATED (282 lines)*. Enterprise tech: IBM Plex, professional, technical documentation.
- **nvidia** `NVIDIA` — *CURATED (243 lines)*. GPU/AI hardware: dark theme, green accent, technical product focus.
- **pinterest** `Pinterest` — *CURATED (188 lines)*. Visual discovery: pin-based grid, red accent, image-first.
- **playstation** `PlayStation` — *CURATED (305 lines)*. Gaming: dark theme, blue accent, gaming-focused UI.
- **spacex** `SpaceX` — *CURATED (155 lines)*. Aerospace: dark theme, mission-focused, rocket imagery.
- **spotify** `Spotify` — *CURATED (204 lines)*. Music streaming: green accent, dark theme, media controls.
- **theverge** `The Verge` — *CURATED (241 lines)*. Tech media: editorial, Verge design system, article-focused.
- **uber** `Uber` — *CURATED (244 lines)*. Ride-sharing: uber black, mobility-focused, maps integration.
- **vodafone** `Vodafone` — *CURATED (324 lines)*. Telecom: red accent, global brand, network-focused.
- **wired** `WIRED` — *CURATED (225 lines)*. Tech media: editorial, dark theme, magazine-style layouts.
- **xiaohongshu** `Xiaohongshu` — *CURATED (300 lines)*. Social commerce: pink/red accent, lifestyle-focused, Chinese market.

### Morphism & Effects (6)

- **claymorphism** `Claymorphism` — *TEMPLATE (50 lines)*. Clay-like 3D elements, soft shadows, rounded forms.
- **glassmorphism** `Glassmorphism` — *TEMPLATE (50 lines)*. Glass-like blur effects, transparency, light borders.
- **gradient** `Gradient` — *TEMPLATE (50 lines)*. Gradient-based color schemes, smooth transitions.
- **neon** `Neon` — *TEMPLATE (50 lines)*. Neon-inspired, dark backgrounds, glowing effects.
- **neumorphism** `Neumorphism` — *TEMPLATE (50 lines)*. Soft extruded elements, subtle shadows, minimal.
- **skeumorphism** `Skeuomorphism` — *TEMPLATE (50 lines)*. Real-world texture mimicry, leather/wood/grain.

### Modern & Minimal (10)

- **clean** `Clean` — *TEMPLATE (50 lines)*. Minimal, uncluttered, functional.
- **contemporary** `Contemporary` — *TEMPLATE (50 lines)*. Modern, up-to-date styling.
- **flat** `Flat` — *TEMPLATE (50 lines)*. Flat design, no gradients, solid colors.
- **minimal** `Minimal` — *TEMPLATE (50 lines)*. Extreme minimalism, maximum whitespace.
- **modern** `Modern` — *TEMPLATE (50 lines)*. Contemporary modern aesthetic.
- **mono** `Mono` — *TEMPLATE (50 lines)*. Monochromatic, single-color palette.
- **refined** `Refined` — *TEMPLATE (50 lines)*. Polished, sophisticated, clean.
- **shadcn** `Shadcn` — *TEMPLATE (50 lines)*. Shadcn/ui component patterns: Radix-based, modern React.
- **simple** `Simple` — *TEMPLATE (50 lines)*. Simple, clean, no-frills.
- **sleek** `Sleek` — *TEMPLATE (50 lines)*. Smooth, polished, professional.

### Productivity & SaaS (11)

- **arc** `Arc Browser` — *CURATED (126 lines)*. Browser UI: sidebar-centric, space-based navigation.
- **cal** `Cal.com` — *CURATED (217 lines)*. Scheduling: calendar-focused, booking flows, date/time inputs.
- **discord** `Discord` — *CURATED (133 lines)*. Communication: dark theme, community channels, chat-centric.
- **duolingo** `Duolingo` — *CURATED (127 lines)*. Gamified learning: green accent, fun, progress-focused.
- **intercom** `Intercom` — *CURATED (118 lines)*. Customer communication: chat UI, messenger, help center.
- **linear-app** `Linear` — *CURATED (312 lines)*. Issue tracking: clean, linear design language, dark mode.
- **mintlify** `Mintlify` — *CURATED (271 lines)*. Developer docs: MDX-focused, clean, technical documentation.
- **notion** `Notion` — *CURATED (258 lines)*. All-in-one workspace: block-based, clean, versatile.
- **resend** `Resend` — *CURATED (251 lines)*. Email infrastructure: clean, developer-focused, technical.
- **slack** `Slack` — *CURATED (305 lines)*. Team communication: purple accent, channel-based UI, message-focused.
- **webex** `Webex` — *CURATED (164 lines)*. Video conferencing: Cisco's design, meeting-focused UI.
- **zapier** `Zapier` — *CURATED (276 lines)*. Automation: workflow-focused, integration listing, Zap patterns.

### Professional & Corporate (10)

- **ant** `Ant` — *TEMPLATE (50 lines)*. Professional, enterprise-focused.
- **application** `Application` — *TEMPLATE (50 lines)*. Business application styling, enterprise-ready.
- **corporate** `Corporate` — *TEMPLATE (50 lines)*. Corporate identity, professional, business-focused.
- **dashboard** `Dashboard` — *TEMPLATE (50 lines)*. Data dashboard patterns, business metrics, charts.
- **elegant** `Elegant` — *TEMPLATE (50 lines)*. Sophisticated, refined, professional.
- **enterprise** `Enterprise` — *TEMPLATE (50 lines)*. Large-scale enterprise styling, B2B-focused.
- **luxury** `Luxury` — *TEMPLATE (50 lines)*. High-end, premium aesthetic, dark, bold typography.
- **material** `Material` — *TEMPLATE (50 lines)*. Google's Material Design patterns, elevation, motion.
- **premium** `Premium` — *TEMPLATE (50 lines)*. Premium feel, high-quality, sophisticated.
- **professional** `Professional` — *TEMPLATE (50 lines)*. Professional, business-appropriate, clean.

### Retro & Nostalgic (4)

- **dithered** `Dithered` — *TEMPLATE (50 lines)*. Dithered/pixel art aesthetic, retro color palettes.
- **paper** `Paper` — *TEMPLATE (50 lines)*. Paper-like textures, print-inspired, tactile feel.
- **retro** `Retro` — *TEMPLATE (50 lines)*. Retro/vintage styling, nostalgia-focused.
- **vintage** `Vintage` — *TEMPLATE (50 lines)*. Vintage aesthetic, aged, old-school styling.

### Social & Messaging (1)

- **wechat** `WeChat` — *CURATED (243 lines)*. Chinese super-app: WeChat Design System patterns, social/commerce hybrid.

### Starter (3)

- **default** `Neutral Modern` — *TEMPLATE (62 lines)*. **Default fallback.** Clean, product-oriented, content-first. Neutral palette (FAFAFA/#111111), cobalt accent (#2F6FEB). 12-col grid, 1200px max-width.
- **tom-modern** `Tom Modern Design` — *CURATED (268 lines)*. Modern starter with refined defaults, design-token-based.
- **warm-editorial** `Warm Editorial` — *TEMPLATE (55 lines)*. Warm, editorial-focused, serif typography.

### Themed & Unique (8)

- **agentic** `Agentic` — *TEMPLATE (51 lines)*. Conversational AI agent interfaces, minimal controls, clear outcomes.
- **futuristic** `Futuristic` — *TEMPLATE (50 lines)*. Sci-fi inspired, futuristic aesthetic, technology-focused.
- **hud** `HUD Design System` — *CURATED (131 lines)*. Heads-up display patterns, overlay interfaces, real-time data.
- **loom** `Loom Design System` — *CURATED (163 lines)*. Video messaging interface, play controls, video-centric UI.
- **pacman** `Pacman` — *TEMPLATE (50 lines)*. Gaming nostalgia, arcade-inspired, playful.
- **tetris** `Tetris` — *TEMPLATE (50 lines)*. Puzzle-game inspired, block-based layouts, grid-focused.
- **totality-festival** `Totality Festival` — *CURATED (182 lines)*. Event/festival design: energetic, colorful, social.
- **trading-terminal** `Trading Terminal Design System` — *CURATED (142 lines)*. Financial trading UI: data-dense, real-time feeds, dark theme.

## Selection Algorithm

1. If the brief names a specific brand → use that system directly (e.g., "Stripe" → `stripe/`).
2. If the brief names a style category → pick the matching Tier-2 template (e.g., "brutalist" → `brutalism/`).
3. If the brief names a genre → consult the category quick-pick above.
4. If no match → use `default` (Neutral Modern) as the universal fallback.
5. Always read `DESIGN.md` + `USAGE.md` of the selected system before implementation.
6. Always copy `tokens.css` `:root` block into the artifact's `<style>` — never invent new hex values.
7. For brand systems (100+ lines), also read `components.html` and `components.manifest.json` for the component inventory.

## Catalog Summary

| Metric | Count |
|---|---|
| Total design systems | 152 |
| Curated (detailed brand specs) | 95 |
| Template-generated | 57 |
| Have manifest.json | 152 |
| Have DESIGN.md | 152 |
| Have tokens.css | 152 |
| Have components.html | 152 |
| Have USAGE.md | 151 (all except `tom-modern`) |
| Categories represented | 16 |

---

*This catalog was generated by automated filesystem enumeration + manual inspection of `manifest.json` and `DESIGN.md` (first-section summary) for each folder. For full design prose, read the source `DESIGN.md`. Source of truth: `audit/source-audit.jsonl`.*