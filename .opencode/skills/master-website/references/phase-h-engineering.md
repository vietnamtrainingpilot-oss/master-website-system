# Phase H — Engineering & Accessibility

## Purpose
Hardening the implementation: accessibility compliance, performance optimization, security, code quality. Output: **Production-Ready Build** (all audits pass, no critical issues).

## Workflow

### Step 1: Accessibility Audit (from `accessibility`, `frontend-a11y`, `wcag-compliance`)

**WCAG 2.2 Level AA Checklist**:

#### Perceivable
- [ ] **1.1.1** Non-text content: Alt text on all images, ARIA labels on icon buttons
- [ ] **1.3.1** Info and relationships: Semantic HTML, proper heading hierarchy (h1→h6)
- [ ] **1.4.3** Contrast (Minimum): 4.5:1 text, 3:1 large text/UI components
- [ ] **1.4.4** Resize text: Up to 200% without loss of function
- [ ] **1.4.11** Non-text contrast: 3:1 on UI components, graphical objects
- [ ] **1.4.12** Text spacing: No loss of function with user spacing overrides

#### Operable
- [ ] **2.1.1** Keyboard: All functionality operable via keyboard
- [ ] **2.1.2** No keyboard trap: Focus can move away from any component
- [ ] **2.4.3** Focus order: Logical tab order
- [ ] **2.4.7** Focus visible: Clear focus indicator (use `--shadow-colored`)
- [ ] **2.5.1** Pointer gestures: No multipoint/path-based gestures required
- [ ] **2.5.2** Pointer cancellation: Down-event not used for execution
- [ ] **2.5.3** Label in name: Accessible name contains visible label
- [ ] **2.5.4** Motion actuation: Alternative for motion-triggered actions
- [ ] **2.5.8** Target size (minimum): 44×44px touch targets

#### Understandable
- [ ] **3.1.2** Language of parts: `lang` attributes on language changes
- [ ] **3.2.1** On focus: No unexpected context changes on focus
- [ ] **3.2.2** On input: No unexpected context changes on input
- [ ] **3.3.2** Labels/instructions: Clear labels on all inputs

#### Robust
- [ ] **4.1.2** Name, role, value: ARIA roles on custom components
- [ ] **4.1.3** Status messages: Live regions for dynamic updates

**Tools**: `axe-core` (via `browser-qa`), manual keyboard testing, screen reader (NVDA/VoiceOver)

### Step 2: Performance Optimization (from `vercel-react-best-practices`, `react-performance`, `benchmark`, `benchmark-optimization-loop`)

**Core Web Vitals Targets**:
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | ≤ 2.5s | 2.5–4s | > 4s |
| INP | ≤ 200ms | 200–500ms | > 500ms |
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |

**Optimization Categories** (from `vercel-react-best-practices` 70+ rules):

#### 1. Waterfall Elimination
- [ ] All data fetching parallelized (`Promise.all`)
- [ ] No component-level fetch in render path
- [ ] Server Components for data fetching where possible

#### 2. Bundle Size
- [ ] Code-split by route (`next/dynamic`, `React.lazy`)
- [ ] Tree-shake unused imports
- [ ] Analyze with `@next/bundle-analyzer`
- [ ] Target: < 200KB gzipped initial JS

#### 3. Server-Side
- [ ] Static generation where possible (`getStaticProps`)
- [ ] ISR for semi-dynamic content
- [ ] Edge runtime for low-latency responses
- [ ] Streaming with `Suspense`

#### 4. Client Fetching
- [ ] `TanStack Query` / `SWR` with stale-while-revalidate
- [ ] Prefetch on hover/intent
- [ ] Deduplicate requests

#### 5. Re-render Reduction
- [ ] `React.memo` on expensive components
- [ ] `useMemo`/`useCallback` for stable references
- [ ] Avoid inline object/function creation in render
- [ ] Virtualize long lists (`@tanstack/react-virtual`)

#### 6. Rendering
- [ ] Minimize layout shifts (reserve space for images/ads)
- [ ] `next/image` with `width`/`height`/`blur` placeholder
- [ ] Font optimization: self-host, `preload`, `font-display: swap`

#### 7. JS Micro-Perf
- [ ] Debounce/throttle event handlers
- [ ] Web Workers for heavy computation
- [ ] `requestIdleCallback` for non-critical work

#### 8. Advanced
- [ ] Partial hydration (`islands` architecture)
- [ ] Streaming SSR with `Suspense` boundaries
- [ ] Service Worker for offline/caching

### Step 3: Security Hardening (from `security`, `security-review`, `security-scan`, `security-bounty-hunter`)

**Dependency Audit**:
```bash
npm audit
npx safety-shot --update
```
- [ ] No critical/high vulnerabilities
- [ ] All dependencies pinned (no `^`/`~` in production)
- [ ] `package-lock.json` committed

**Code Security**:
- [ ] No secrets in code (use `security-scan` on repo)
- [ ] Input validation on all API routes (Zod schemas)
- [ ] SQL injection prevention (parameterized queries/ORM)
- [ ] XSS prevention (auto-escaping, CSP headers)
- [ ] CSRF protection (SameSite cookies, CSRF tokens)
- [ ] Rate limiting on auth endpoints
- [ ] Security headers: CSP, HSTS, X-Frame-Options, Referrer-Policy

**Authentication/Authorization** (from `springboot-security`, `django-security`, `laravel-security`, `nextjs-patterns`):
- [ ] JWT/OIDC with short expiry, refresh rotation
- [ ] Role-based access control (RBAC)
- [ ] Session management (secure, httpOnly, SameSite)

### Step 4: Code Quality (from `coding-standards`, `ponytail-review`, `ponytail-audit`, `impeccable-design-polish`)

**Ponytail Principles** (YAGNI, stdlib first, no unrequested abstractions):
- [ ] No reinvented stdlib (use `date-fns`, not custom date utils)
- [ ] No needless dependencies (audit with `ponytail-audit`)
- [ ] No speculative abstractions (delete unused code)
- [ ] Delete commented code

**TypeScript** (from `frontend-patterns`, `typescript-patterns`):
- [ ] `strict: true` in tsconfig
- [ ] No `any` (use `unknown` + type guards)
- [ ] Proper generics on components/hooks
- [ ] Discriminated unions for state

**Linting**:
```bash
npm run lint    # Biome/ESLint - zero errors
npm run typecheck  # tsc --noEmit - zero errors
```

### Step 5: Generic Site Audit (from `generic-site-auditor` — 6-Phase Workflow)

1. **Visual Design** — Typography, color, spacing, hierarchy
2. **Typography** — Scale, contrast, line length, font loading
3. **Layout** — Grid, whitespace, responsive, alignment
4. **Branding** — Logo, voice, consistency, differentiation
5. **Copywriting** — Clarity, tone, hierarchy, CTAs
6. **UX/Animation** — Motion standards, interaction feedback, performance

**Output**: Remediation plan with priority scores.

## Hard Gate
> **All audits pass** (A11y AA, CWV Good, Security clean, Lint/Typecheck clean, Generic audit) → Proceed to Phase I
> If any fail → Fix before proceeding

## Cross-References
- Consumes: Phase F (Implementation), Phase G (Animated Implementation)
- Produces: Production-Ready Build → Phase I, J
- Skills: 45+ engineering/security/accessibility skills