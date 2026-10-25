# Phase F — Plan & Implement

## Purpose
Build the production codebase from Template Package using Design System tokens. Output: **Working Implementation** (all pages, components, interactions, data fetching, state management).

## Workflow

### Step 1: Phased Implementation Planning (from `writing-plans`, `orch-pipeline`, `orch-add-feature`, `orch-build-mvp`, `orch-change-feature`, `orch-refine-code`)

Create self-contained context briefs for each implementation step:

```markdown
## Step: [Name]

### File Path
src/components/[Component].tsx

### Current Behavior
[What exists now — 1-2 sentences]

### Desired Behavior
[What it should do — 1-2 sentences]

### Context Brief
- Imports: [list]
- Props: [interface]
- Related Files: [list]
- Design Tokens Used: [list from tokens.css]

### Constraints
- [Rules from _must-use-rules.md]
- [Dial alignment: VARIANCE/MOTION/DENSITY]
- [Accessibility: WCAG 2.2 AA]

### Verification
- [ ] Unit test passes
- [ ] Visual matches design
- [ ] Responsive at all breakpoints
- [ ] Motion tokens applied
- [ ] No console errors
```

**Dependency Graph**: Order steps by dependency. Mark parallelizable steps.

### Step 2: React/Framework Patterns (from `frontend-patterns`, `react-patterns`, `nextjs-turbopack`, `vue-patterns`, `nuxt4-patterns`, `angular-developer`, `svelte-patterns`)

**Server Components (Default)**:
```tsx
// app/page.tsx — Server Component by default
async function Page() {
  const data = await fetchData(); // Direct DB/API call
  return <Layout><Content data={data} /></Layout>;
}
```

**Client Components (Explicit)**:
```tsx
// components/Interactive.tsx
'use client';
import { useState } from 'react';

export function Interactive() {
  const [state, setState] = useState(initial);
  return <button onClick={() => setState(new)}>{state}</button>;
}
```

**Data Fetching — Parallel, Not Waterfall**:
```tsx
// Bad: Sequential
const user = await getUser();
const posts = await getPosts(user.id);

// Good: Parallel
const [user, posts, comments] = await Promise.all([
  getUser(),
  getPosts(),
  getComments()
]);
```

**State Management Decision Tree** (from `frontend-patterns`):

| Need | Solution |
|------|----------|
| Local UI state | `useState`, `useReducer` |
| Form state | `react-hook-form` + `zod` |
| Server data | `TanStack Query` / `SWR` |
| Global UI state | Context (small), Zustand (large) |
| URL state | `useSearchParams`, router |
| Complex forms | `react-hook-form` + `zod` |

### Step 3: Backend & Infrastructure Patterns (from all backend skills)

**API Layer** (from `fastapi-patterns`, `nestjs-patterns`, `springboot-patterns`, `rails-patterns`, `laravel-patterns`, `django-patterns`, `django-patterns`):
- Contract-first with `contract-first` skill
- Pydantic v2 / Zod schemas
- Dependency injection
- Auth: JWT/OIDC via `security` patterns

**Database** (from `prisma-patterns`, `postgres-patterns`, `mysql-patterns`, `redis-patterns`, `database-migrations`):
- Prisma schema with proper indexes
- Migrations: expand-contract for zero-downtime
- Connection pooling (PgBouncer/Prisma)

**Infrastructure** (from `docker-patterns`, `kubernetes-patterns`, `deployment-patterns`):
- Multi-stage Dockerfiles
- Health checks, readiness probes
- Horizontal pod autoscaling

### Step 4: Performance Budgets (from `react-performance`, `vercel-react-best-practices`, `web-design`, `benchmark`)

| Metric | Target | Tool |
|--------|--------|------|
| LCP | < 2.5s | Lighthouse, Web Vitals |
| INP | < 200ms | INP Debugger |
| CLS | < 0.1 | Layout Shift Debugger |
| Bundle (gzipped) | < 200KB | `@next/bundle-analyzer` |
| JS Main Thread | < 16ms/frame | Chrome DevTools |

**Optimization Checklist** (from `vercel-react-best-practices` 70+ rules):
- [ ] No waterfall data fetching
- [ ] Code-split by route (`next/dynamic`)
- [ ] Lazy-load heavy components
- [ ] Images optimized (`next/image`)
- [ ] Fonts self-hosted, preloaded
- [ ] Third-party scripts deferred
- [ ] Memoize expensive components (`React.memo`)
- [ ] Virtualize long lists (`react-window`)

### Step 5: Implementation Loop (from `tdd-workflow`, `test-driven-development`, `impeccable-design-polish`)

For each step:
1. **Write failing test** (unit/integration/E2E)
2. **Watch it fail**
3. **Implement minimal code** to pass
4. **Refactor** with Design System tokens
5. **Apply 6-mode polish** (from `impeccable-design-polish`):
   1. **Audit** — Visual inspection, contrast, spacing, typography
   2. **Tighten** — Fix rhythm, alignment, scale
   3. **Harden** — Add hover/focus/active/loading/error states
   4. **Animate** — Entrance, exit, micro-interactions (Phase G tokens)
   5. **Live** — Test in real browser, real device
   6. **Ship** — Final verification

**Coverage Requirements**:
- Unit: 80%+
- Integration: All critical paths
- E2E: User journeys

## Hard Gate
> **All steps complete + tests passing + polish applied** → Proceed to Phase G
> If failing → Fix before proceeding

## Cross-References
- Consumes: Phase E (Template Package), Phase D (Design System)
- Produces: Working Implementation → Phase G, H
- Skills: 65+ pattern skills (frontend, backend, database, infra)
"@
Set-Content -Path (Join-Path $phaseDir "phase-f-implement.md") -Value $phaseF -Encoding UTF8
Write-Host "Phase F: $([math]::Round((Get-Item (Join-Path $phaseDir 'phase-f-implement.md')).Length/1KB,1)) KB"