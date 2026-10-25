# Phase K — Fix & Refine

## Purpose
Address all issues from verification, apply final polish, handle code review feedback. Output: **Release Candidate** (zero critical bugs, polished, reviewed).

## Workflow

### Step 1: Systematic Debugging (from `systematic-debugging`)

For every issue from Phase I/J:

1. **Reproduce** — Minimal reproduction, documented steps, environment captured
2. **Isolate** — Identify affected component, check related, verify not data/race
3. **Diagnose** — Read error fully, check call stack, review recent changes
4. **Fix** — Minimal change, test reproduction, verify no regressions
5. **Verify** — Full test suite, related features, browser check, confirm fix

**Bug Classification**:
| Severity | Response Time | Examples |
|----------|---------------|----------|
| Critical | Immediate | Data loss, security, crash, payment failure |
| High | 4 hours | Broken feature, major CWV regression |
| Medium | 24 hours | Visual inconsistency, minor a11y |
| Low | Next sprint | Polish, enhancement |

### Step 2: Design Polish Workflow (from `impeccable-design-polish` — 6 Modes)

Apply to all affected pages/components:

| Mode | Action | Checklist |
|------|--------|-----------|
| **Audit** | Visual inspection | Contrast, spacing, typography, motion timing |
| **Tighten** | Fix rhythm | Alignment, scale, visual weight balance |
| **Harden** | Add states | Hover, focus, active, loading, error, empty |
| **Animate** | Motion pass | Entrance, exit, micro-interactions, reduced-motion |
| **Live** | Real device test | Mobile, tablet, desktop, different browsers |
| **Ship** | Final approval | Stakeholder sign-off |

### Step 3: Code Review Feedback Handling (from `receiving-code-review`, `requesting-code-review`, `click-path-audit`)

**Review Categories**:
1. **Correctness** — Bugs, logic errors → **Must fix**
2. **Performance** — Render issues, bundle size → **Must fix**
3. **Security** — Vulnerabilities, exposed secrets → **Must fix**
4. **Accessibility** — WCAG violations → **Must fix**
5. **Design** — Visual consistency → Discuss, align with Design Direction Doc
6. **Maintainability** — Structure, naming, comments → Discuss

**Response Protocol**:
- Acknowledge every item
- Categorize: **Fix** / **Discuss** / **Won't Fix** (with reason)
- Fix all Correctness/Security/Accessibility/Performance
- Document design decisions in ADR (`references/decision-record-template.md`)

### Step 4: Animation-Specific Fixes (from `improve-animations`, `review-animations`)

If animation issues found:
- Re-run `review-animations` on affected elements
- Apply remedial hierarchy: Re-order → Rewrite → Remove → Restructure
- Re-verify performance budget

### Step 5: Ponytail Audit (from `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`)

- **Delete**: Reinvented stdlib, needless deps, speculative abstractions
- **Simplify**: Replace with stdlib/native equivalents
- **Debt Log**: Track deferrals in `PONYTAIL_DEBT.md`
- **Gain Scoreboard**: Measure impact (less code, faster, cheaper)

## Hard Gate
> **Zero critical/high bugs + all polish applied + code review addressed** → Proceed to Phase L
> If any remain → Fix before proceeding

## Cross-References
- Consumes: Phase J (Verification Report), Phase I (QA failures)
- Produces: Release Candidate → Phase L
- Skills: `systematic-debugging`, `impeccable-design-polish`, `receiving-code-review`, `click-path-audit`, `improve-animations`, `ponytail-*`