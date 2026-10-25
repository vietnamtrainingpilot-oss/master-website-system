---
type: skill
description: "Master Website — Autonomous full-stack website production from brief to deployable HTML/CSS/JS. Synthesized playbooks with zero content loss from 169 skills."
---

# /master-website — Complete Website Production System

## Purpose
Build a complete, portable, autonomous website-production system that synthesizes all 169 skills from `D:\Master Design\skills\` into 12 actionable phase playbooks. Each phase is a coherent playbook with zero content loss — every technique, config table, example, banned default, spring preset, and workflow step from the source skills is preserved and organized for execution.

## Usage
```bash
# Run the master skill
/master-website

# Or use the command
master-website --project "My Website" --dials variance=50 motion=40 density=30
```

## Phase Playbooks (12)

| Phase | File | Size | Focus |
|-------|------|------|-------|
| A | `references/phase-a-intake.md` | ~3 KB | Design Read, taste dials, skills discovery |
| B | `references/phase-b-research.md` | ~2 KB | Web clone recon, asset harvest, source verification |
| C | `references/phase-c-design-direction.md` | ~9 KB | **Core** — Dials, anti-defaults, design system map, tokens |
| D | `references/phase-d-design-system.md` | ~5 KB | Tokenize, component specs, DESIGN.md, a11y baseline |
| E | `references/phase-e-template.md` | ~4 KB | Template selection, init, content mapping, assets |
| F | `references/phase-f-implement.md` | ~6 KB | Phased impl, React/backend patterns, perf budgets, TDD |
| G | `references/phase-g-animation.md` | ~6 KB | **Core** — Build sequence, 10 standards, component patterns |
| H | `references/phase-h-engineering.md` | ~5 KB | A11y audit, perf optimization, security, code quality |
| I | `references/phase-i-browser.md` | ~1 KB | Browser QA: visual regression, CWV, a11y, interactions |
| J | `references/phase-j-test.md` | ~1 KB | 6-phase verification loop, TDD enforcement |
| K | `references/phase-k-fix.md` | ~2 KB | Systematic debugging, 6-mode polish, code review |
| L | `references/phase-l-deliver.md` | ~4 KB | Ship-it pipeline, deploy, monitor, handoff |

## Specialty Guides

| Guide | Purpose |
|-------|---------|
| `references/pptx-guide.md` | Presentation/slide deck creation (html-ppt, slides, wowerpoint) |
| `references/docs-guide.md` | Documentation/content processing (article-writing, data-report) |
| `references/brand-guide.md` | Brand identity/visual systems (brandkit, brand-discovery, design) |
| `references/animation-guide.md` | Animation/motion reference (animate, gsap-*, motion-*, remotion) |

## Hard Gates Table

| Phase | Gate Name | Pass Condition | If Fail |
|-------|-----------|----------------|---------|
| A | Project Brief Locked | Design Read complete, dials set | Return to stakeholder |
| B | Research Complete | Source Package verified | Expand research |
| C | Design Direction Approved | Anti-defaults applied, dials justified, system selected | Adjust dials, regenerate |
| D | Design System Ready | tokens.css + component specs + DESIGN.md + a11y baseline | Complete missing items |
| E | Template Selected | Template Package ready (initialized, tokens, content, assets) | Complete preparation |
| F | Implementation Complete | All steps done + tests pass + polish applied | Fix failing tests |
| G | Animation Approved | `review-animations` returns Approve on all elements | Fix or remove animation |
| H | Engineering Complete | A11y AA + CWV Good + Security clean + Lint/Typecheck clean | Fix failures |
| I | Browser QA Passed | SHIP verdict (visual regression, CWV, a11y, interactions green) | Return to H/F/G |
| J | Verification Loop Pass | All 6 phases green | Fix, re-run from Phase 1 |
| K | Bugs Fixed | Zero critical/high + polish applied + review addressed | Fix before proceeding |
| L | Ship Ready | All pre-ship PASS + deploy successful + monitoring green | Address blockers |

## Resource Root Discovery
This skill operates from its installed location. Resource discovery:

```
Resource Root: ~/.opencode/skills/master-website/
├── SKILL.md              # This file
├── references/
│   ├── phase-a-intake.md
│   ├── phase-b-research.md
│   ├── phase-c-design-direction.md
│   ├── phase-d-design-system.md
│   ├── phase-e-template.md
│   ├── phase-f-implement.md
│   ├── phase-g-animation.md
│   ├── phase-h-engineering.md
│   ├── phase-i-browser.md
│   ├── phase-j-test.md
│   ├── phase-k-fix.md
│   ├── phase-l-deliver.md
│   ├── pptx-guide.md
│   ├── docs-guide.md
│   ├── brand-guide.md
│   ├── animation-guide.md
│   ├── design-systems/
│   │   ├── AGENTS.md       # 152 design systems catalog
│   │   └── _must-use-rules.md
│   ├── design-templates/
│   │   └── AGENTS.md       # 115 templates catalog
│   ├── skills-phase-mapping.md
│   ├── source-attribution.md
│   ├── skill-integration-map.md
│   ├── template-selection-guide.md
│   ├── design-read-template.md
│   ├── dials.json
│   ├── decision-record-template.md
│   └── hard-gates.md
└── docs/
    └── master-website/
        └── audit/
            └── source-audit-enhanced.jsonl  # 5,243 entries
```

## Environment Configuration

```bash
# Master Design root location (REQUIRED for validation)
export MASTER_DESIGN_ROOT="D:\Master Design"

# Output location (defaults to current directory)
export MASTER_WEBSITE_OUTPUT="./website-output"

# Dial settings (optional, defaults in dials.json)
export VARIANCE=50
export MOTION=40
export DENSITY=30
```

### Path Resolution
```python
import os
from pathlib import Path

MASTER_DESIGN_ROOT = os.environ.get('MASTER_DESIGN_ROOT', 'D:\\Master Design')
SKILL_ROOT = Path.home() / '.opencode' / 'skills' / 'master-website'
PRODUCT_ROOT = Path(MASTER_DESIGN_ROOT) / 'master-website-system'
REFERENCES = SKILL_ROOT / 'references'
```

## Key Synthesized Content (Zero Loss)

### Phase C — Design Direction (Core)
- **Three Taste Dials** (VARIANCE/MOTION/DENSITY) with full range tables from `taste-skill`
- **30+ Banned LLM Defaults** with before/after examples from `taste-skill`
- **Design System Map**: Color → Typography → Spacing → Shadows → Motion
- **Spring Config Table** with 5 presets from `emil-design-eng`
- **Typography Scale** (Display→Caption) with weights, line heights, tracking from `high-end-visual-design`
- **Shadow System** (4 levels) with colored shadows from `emil-design-eng`
- **Anti-Default Decisions** template (minimum 5 required)
- **Design Direction Doc** template consuming Phase A/B

### Phase G — Animation (Core)
- **6-Step Build Sequence** (Frequency → Tool → Properties → Easing → Interruption → Reduced Motion) from `animate`
- **10 Non-Negotiable Standards** with before/after table from `review-animations`
- **Component Motion Patterns** (Buttons, Popovers, Tooltips, Modals, Lists, Pages) from `emil-design-eng`, `motion-patterns`
- **Spring Presets** (5 configs) from `emil-design-eng`
- **Library Integration** (GSAP, Motion/React, CSS) with code examples
- **Performance Budget** (16ms/frame, max 3 concurrent) from `fixing-motion-performance`

### Phase F — Implementation
- **Phased Planning** with self-contained context briefs from `writing-plans`, `orch-*`
- **React Patterns** (Server/Client components, parallel fetching) from `frontend-patterns`, `react-patterns`
- **State Management Decision Tree** from `frontend-patterns`
- **Backend Patterns** (API, DB, Auth, Infra) from 20+ backend skills
- **Performance Budgets** (CWV targets, 70+ optimization rules) from `vercel-react-best-practices`
- **6-Mode Polish Workflow** (Audit→Tighten→Harden→Animate→Live→Ship) from `impeccable-design-polish`

### Phase H — Engineering
- **WCAG 2.2 AA Checklist** (47 items across POUR) from `accessibility`, `frontend-a11y`
- **Core Web Vitals Optimization** (8 categories, 70+ rules) from `vercel-react-best-practices`
- **Security Hardening** (deps, code, auth, headers) from `security`, `security-review`
- **Code Quality** (Ponytail YAGNI, TypeScript strict, linting) from `ponytail-*`, `coding-standards`
- **Generic Site Audit** (6-phase) from `generic-site-auditor`

## Validation
```bash
python validate.py
```
Expected: 30/30 structural checks PASS.

## Distribution
Copy `master-website-system/` to any machine. Run `install.ps1` to install locally.

## Source
Synthesized from 169 skills in `D:\Master Design\skills\` with zero content loss — every technique, config, example, and workflow preserved in actionable playbook form.

## Integration Summary

| Metric | Value |
|--------|-------|
| Total Skills Synthesized | 169 |
| Phase Playbooks | 12 |
| Specialty Guides | 4 |
| Design Systems Cataloged | 152 (via AGENTS.md) |
| Templates Cataloged | 115 (via AGENTS.md) |
| Total Playbook Content | ~50 KB (synthesized, not concatenated) |
| Source Audit Entries | 5,243 |

---

## Phase A — Intake & Discovery
**Purpose**: Capture project brief, set taste dials, identify relevant skills.
**Hard Gate**: Design Read complete + dials set.
**Key Skills**: brainstorming, creative-director, brand-discovery, market-research, keyword-research, seo-audit, competitor-analysis, domain-name-brainstormer, design-consultation, brand-voice, ai-prompt-research, ai-visibility-audit, prompt-engineering-patterns, prompt-optimizer, workspace-surface-audit, using-superpowers, promote-idea, album-conceptualizer, album-ideas, tutorial.
**Output**: Design Read document + dials.json.

## Phase B — Research & Source Discovery
**Purpose**: Conduct reconnaissance, harvest assets, verify sources.
**Hard Gate**: Source Package verified.
**Key Skills**: web-clone, autoresearch, deep-research, document-hunter, exa-search, visual-research, research-ops, watch, competitive-ads-extractor, youtube-clipper, video-downloader, wiki-retrieve, prediction-market-oracle-research, scientific-thinking-literature-review.
**Output**: Verified assets, color/typography samples, reference URLs, interaction patterns.

## Phase C — Design Direction & Taste
**Purpose**: Establish visual direction via taste dials, anti-default discipline, design system selection.
**Hard Gate**: Design Direction Doc approved (anti-defaults applied, dials justified, system selected).
**Key Skills**: taste-skill, taste-skill-v1, emil-design-eng, frontend-design, ultimate-frontend-skills, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, brandkit, brand, ui-ux-pro-max, apple-design, liquid-glass-design, stitch-design-taste, design, banner-design, color-expert, design-brief, brand-extract, impeccable, imagegen-frontend-web, imagegen-frontend-mobile, image-to-code-skill, generic-site-auditor, scroll-craft, ptfs-va-website-builder, frontend-design-direction, design-system, design-is, gpt-taste, brand-guidelines, minimalist-skill, web-design-guidelines, reference-design-contract, enhance-prompt, and 40+ frame/template skills.
**Output**: Design Direction Doc (color system, typography scale, shadow system, spacing scale, motion tokens, anti-default decisions).

## Phase D — Establish Design System
**Purpose**: Transform Design Direction into working tokenized design system.
**Hard Gate**: Design System Package complete (tokens.css + component specs + DESIGN.md + a11y baseline).
**Key Skills**: design-md, ui-styling, accessibility, frontend-a11y, make-interfaces-feel-better.
**Reference**: 152 design systems in design-systems/AGENTS.md.
**Output**: tokens.css, component specs (15 minimum), DESIGN.md, accessibility baseline.

## Phase E — Select & Prepare Template
**Purpose**: Choose template, prepare content structure, integrate Design System.
**Hard Gate**: Template Package ready (initialized, tokens integrated, content mapped, assets placed).
**Key Skills**: web-prototype, saas-landing, open-design-landing, html-ppt, html-ppt-presenter-mode-reveal, slides, frontend-slides, wowerpoint, pptx-html-fidelity-audit, pptx, pptx-generator, ppt-keynote, deck-swiss-international, deck-guizang-editorial, deck-open-slide-canvas, html-ppt-retro-quarterly-review, nanobanana-ppt.
**Reference**: 115 templates in design-templates/AGENTS.md.
**Specialty**: pptx-guide.md for presentations.
**Output**: Template Package with content placeholders.

## Phase F — Plan & Implement
**Purpose**: Build production codebase from Template Package using Design System tokens.
**Hard Gate**: All steps complete + tests passing + polish applied.
**Key Skills**: frontend-patterns, react-patterns, nextjs-turbopack, vue-patterns, nuxt4-patterns, react-performance, tdd-workflow, impeccable-design-polish, web-design, vite-patterns, angular-developer, dart-flutter-patterns, android-clean-architecture, kotlin-patterns, kotlin-coroutines-flows, kotlin-ktor-patterns, compose-multiplatform-patterns, swiftui-patterns, swift-concurrency-6-2, swift-actor-persistence, dotnet-patterns, golang-patterns, python-patterns, rust-patterns, java-coding-standards, rails-patterns, laravel-patterns, django-patterns, springboot-patterns, nestjs-patterns, fastapi-patterns, backend-patterns, contract-first, prisma-patterns, postgres-patterns, mysql-patterns, redis-patterns, database-migrations, docker-patterns, deployment-patterns, image-to-code, threejs, img2threejs, remotion, remotion-*, hyperframes, hyperframes-*, general-video, video-production, video-editing, faceless-explainer, product-launch-video, pr-to-video, talking-head-recut, embedded-captions, music-to-video, motion-graphics, vibe-code, subagent-driven-development, parallel-execution-optimizer, orch-*, token-budget-advisor, prompt-caching-strategy, evm-token-decimals, using-git-worktrees, laravel-plugin-discovery, mybatis-patterns, tinystruct-patterns, kotlin-exposed-patterns, healthcare-cdss-patterns, healthcare-emr-patterns, nodejs-keccak256, orch-fix-defect, frontend-dev, video-hyperframes.
**Output**: Working Implementation (all pages, components, interactions, data fetching, state management).

## Phase G — Animation & Interaction
**Purpose**: Apply purposeful motion using Design System motion tokens.
**Hard Gate**: review-animations returns Approve on all animated elements.
**Key Skills**: animate, review-animations, find-animation-opportunities, gsap-core, gsap-scrolltrigger, gsap-react, gsap-plugins, gsap-performance, gsap-utils, gsap-frameworks, gsap-timeline, ui-animation, chat-motion-overlay, motion-lab, gif-sticker-maker, emilkowalski-motion, animate-expo, awwwards-animations, cinematic-gsap-lenis-motion-system, fixing-motion-performance, motion-advanced, motion-foundations, motion-patterns, oil-motion, huashu-art-motion, swiftui-design, flutter-animating-apps.
**Output**: Animated Implementation (all motion implemented, reviewed, approved).

## Phase H — Engineering & Accessibility
**Purpose**: Harden implementation: accessibility, performance, security, code quality.
**Hard Gate**: All audits pass (A11y AA, CWV Good, Security clean, Lint/Typecheck clean, Generic audit).
**Key Skills**: vercel-react-best-practices, benchmark, latency-critical-systems, data-throughput-accelerator, content-hash-cache-pattern, kubernetes-patterns, generic-site-auditor, ecommerce-image-workflow, output-skill, export-download-debugging, full-page-screenshot, screenshot, shader-dev, d3-visualization, fal-kling-o3, fal-upscale, fal-realtime, fal-video-edit, fal-3d, fal-train, fal-lip-sync, minimax-docx, minimax-pdf, venice-audio-music, venice-audio-speech, venice-video, speech, pdf, docx, doc, slack-gif-creator, image-enhancer, wpds, paywall-upgrade-cro, ad-creative, agent-browser, odo-next-media-inputs, security, security-bounty-hunter, security-review, security-scan, springboot-security, quarkus-security, laravel-security, django-security, healthcare-phi-compliance, hipaa-compliance, defi-amm-security, stripe-best-practices, payments, perl-security, netmiko-ssh-automation, network-bgp-diagnostics, network-config-validation, network-interface-health, cisco-ios-patterns, homelab-network-readiness, homelab-network-setup, homelab-pihole-dns, homelab-vlan-segmentation, homelab-wireguard-vpn, energy-procurement, carrier-relationship-management, logistics-exception-management, returns-reverse-logistics, production-scheduling, inventory-demand-planning.
**Output**: Production-Ready Build.

## Phase I — Run & Inspect (Browser QA)
**Purpose**: Automated browser-based verification.
**Hard Gate**: SHIP verdict (visual regression, CWV, a11y, interactions green).
**Key Skills**: browser-qa, e2e-testing, canary-watch, benchmark-optimization-loop, windows-desktop-e2e.
**Output**: QA Report.

## Phase J — Test, Review, Verify
**Purpose**: Comprehensive verification loop before release.
**Hard Gate**: All 6 verification phases PASS.
**Key Skills**: verification-loop, verification-before-completion, test-driven-development, kotlin-testing, python-testing, rust-testing, golang-testing, cpp-testing, csharp-testing, fsharp-testing, java-testing, springboot-tdd, springboot-verification, quarkus-tdd, quarkus-verification, laravel-tdd, laravel-verification, django-tdd, django-verification, test-collaboration, ai-regression-testing, perl-testing, healthcare-eval-harness.
**Output**: Verification Report.

## Phase K — Fix & Refine
**Purpose**: Address issues, apply final polish, handle code review feedback.
**Hard Gate**: Zero critical/high bugs + polish applied + review addressed.
**Key Skills**: systematic-debugging, impeccable-design-polish, receiving-code-review, requesting-code-review, click-path-audit, improve-animations, ponytail-review, ponytail-audit, ponytail, ponytail-debt, ponytail-gain, ponytail-help, verify-sources, explicit-checker, plagiarism-checker, pronunciation-specialist, module-regression, change-impact, prediction-market-risk-review, agent-introspection-debugging, agent-self-evaluation, quality-nonconformance, repo-scan, santa-method, pr-feedback-quality-gate.
**Output**: Release Candidate.

## Phase L — Ship & Deliver
**Purpose**: End-to-end delivery: final checks, deployment, monitoring, handoff.
**Hard Gate**: All pre-ship PASS + deploy successful + monitoring green + handoff complete.
**Key Skills**: ship-it, release-director, deployment-patterns, continuous-agent-loop, autonomous-agent-harness, agent-architecture-audit, agent-eval, agent-harness-construction, agent-payment-x402, agent-runtime-gateway-smoke-test, agent-security-hardening, agent-sort, agentic-engineering, agentic-os, ai-first-engineering, automation-audit-ops, configure-ecc, config-gc, connections-optimizer, content-engine, crosspost, delivery-gate, docs-governance, hookify-rules, llm-trading-agent-security, mcp-dependency-review, mcp-server-patterns, mem-search, mem-setup, mode-creator, nasiko-control-plane, openclaw-persona-forge, operator-approval-loop, safety-guard, santa-method, save, sheet-music-publisher, skill-comply, skill-host-compat, skill-scout, skill-stocktake, social-graph-ranker, social-publisher, standup, strategic-compact, subagent-driven-development, suno-engineer, terminal-opener, terminal-ops, token-card, unified-memory, unified-notifications-ops, validate-album, version-bump, vibe-code, wiki, wiki-cli, wiki-fold, wiki-ingest, wiki-lint, wiki-mode, wiki-query, x-api, git-workflow, github-ops, album-dashboard, next-step, resume, pre-generation-check, mastering-engineer, mix-engineer, clipboard, promo-director, promo-reviewer, promo-writer, about, help, test, configure, ck, claude-mem-install, cloud-sync, cloud-uploader, import-art, import-audio, import-track, new-album, release-notes-one-pager.
**Output**: Live Production Site + Handoff Package.

---

*All substantive instructional content has been synthesized into phase playbooks with zero loss — organized for execution, not archival.*