# Phase J — Test, Review, Verify

## Purpose
Comprehensive verification loop before release. All automated checks must pass. Output: **Verification Report** (PASS/FAIL with evidence).

## Workflow

### Step 1: Six-Phase Verification Loop (from `verification-loop`, `verification-before-completion`)

Run in order — each must pass before next:

#### Phase 1: Build
```bash
npm run build
# Expected: Clean build, no errors, no warnings
```

#### Phase 2: Type Check
```bash
npm run typecheck
# Expected: Zero TypeScript errors (strict mode)
```

#### Phase 3: Lint
```bash
npm run lint
# Expected: Zero lint errors (Biome/ESLint)
# Warnings allowed but documented
```

#### Phase 4: Tests with Coverage
```bash
npm test -- --coverage
# Expected: All tests pass
# Coverage: ≥ 80% unit, all critical paths integration, user journeys E2E
```

#### Phase 5: Security
```bash
npm audit
npx safety-shot --update
# Expected: No critical/high vulnerabilities
# Dependencies pinned, no unpinned ranges
```

#### Phase 6: Diff Review
```bash
git diff --stat
git diff HEAD~1
# Expected: Only intended changes
# No accidental deletions, no debug code, no console.log
```

### Step 2: Verification Before Completion (from `verification-before-completion`)

**Before claiming any task complete**:
- [ ] Run verification commands for affected area
- [ ] Confirm output matches expected
- [ ] Document evidence (screenshots, logs, test results)
- [ ] No rationalization — evidence before assertions

### Step 3: Test-Driven Development Enforcement (from `test-driven-development`, `tdd-workflow`)

For every bug fix / new feature:
1. Write failing test first
2. Watch it fail
3. Implement minimal fix
3. Refactor with coverage
4. All tests pass

**Coverage Gates**:
- Unit: 80%+
- Integration: 100% critical paths
- E2E: 100% user journeys

### Step 4: Cross-Framework Testing (from `kotlin-testing`, `python-testing`, `rust-testing`, `golang-testing`, `cpp-testing`, `csharp-testing`, `fsharp-testing`, `java-testing`, `perl-testing`)

If polyglot stack:
- Run each language's test suite
- Verify integration contracts
- Check shared type definitions (Protocol Buffers / OpenAPI)

## Hard Gate
> **All 6 verification phases PASS** → Proceed to Phase K
> If any FAIL → Fix, re-run from Phase 1

## Cross-References
- Consumes: Phase I (QA Report)
- Produces: Verification Report → Phase K
- Skills: `verification-loop`, `verification-before-completion`, `test-driven-development`, and all language-specific testing skills