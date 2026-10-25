# Phase I — Run & Inspect (Browser QA)

## Purpose
Automated browser-based verification of the production build. Visual regression, accessibility, Core Web Vitals, interaction testing. Output: **QA Report** (SHIP / DO-NOT-SHIP verdict).

## Workflow

### Step 1: Automated QA Suite (from `browser-qa` MCP)

Run Playwright automation against deployed preview/staging URL:

```bash
# Configuration
URL: [preview/staging URL]
Breakpoints: [320, 768, 1024, 1440, 1920]
Browsers: [chromium, firefox, webkit]
```

**Checks Performed**:

1. **Console Error Scan** — Zero errors/warnings allowed
2. **Core Web Vitals** — LCP, INP, CLS measured via Lighthouse
3. **Visual Regression** — Screenshot diff vs. approved baseline at all breakpoints
4. **Accessibility Audit** — `axe-core` full scan, target ≥ 95%
5. **Form/Interaction Tests** — Login, checkout, contact forms, navigation
6. **Auth Flow Tests** — Login, logout, password reset, protected routes

### Step 2: Visual Regression Details (from `browser-qa`, `visual-research`)

- **Baseline**: Approved design screenshots from Phase C/E
- **Threshold**: 0.1% pixel difference (configurable per element)
- **Masking**: Ignore dynamic content (dates, user names, ads)
- **Output**: Side-by-side diff with highlight overlay

### Step 3: Interaction Testing (from `e2e-testing`, `windows-desktop-e2e`)

**Critical User Journeys**:
| Journey | Steps | Verification |
|---------|-------|--------------|
| Homepage → CTA | Load → Click hero CTA → Landing | Correct page, no errors |
| Navigation | All header links → Footer links | All 200, correct content |
| Forms | Fill valid/invalid → Submit | Success/error states work |
| Auth | Login → Protected → Logout | Session management |
| Search | Query → Results → Filter | Correct filtering |
| Cart/Checkout | Add → Cart → Checkout → Confirm | Full flow |

### Step 4: Canary Watch (from `canary-watch`)

Post-deploy monitoring:
- HTTP endpoints (200 OK)
- SSE/WebSocket streams
- Static assets (fonts, images, CSS, JS)
- Console error monitoring
- Performance regression (CWV vs. baseline)

## Hard Gate
> **SHIP verdict** (all checks pass) → Proceed to Phase J
> **DO-NOT-SHIP** → Return to Phase H/F/G with specific failures

## Cross-References
- Consumes: Phase H (Production-Ready Build)
- Produces: QA Report → Phase J
- Skills: `browser-qa`, `e2e-testing`, `canary-watch`, `windows-desktop-e2e`