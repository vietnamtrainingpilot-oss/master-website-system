# Master Website — Hard Gates (Validation Scripts)

Each gate is a non-negotiable checkpoint. The skill stops and asks for resolution if a gate fails.

## Gate 1: Design Doc Approved (Phase A)

**Condition:** Human approved the design doc produced by `brainstorming`.

**Check:**
```bash
# Design doc exists at:
docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md
# User confirmed approval in conversation
```

**Failure:** Stop; ask for approval. No implementation before approval.

---

## Gate 2: Design System Tokens Ready (Phase D)

**Condition:** `tokens.css` `:root` block pasted as first `<style>` in HTML.

**Check:**
```bash
# In output_dir/index.html (or framework entry):
grep -q ':root' index.html && head -50 index.html | grep -A 60 ':root' | grep -q 'var(--'
# Or for frameworks: tokens imported in global CSS
```

**Failure:** Stop; complete Phase D (copy tokens.css, paste :root block).

---

## Gate 3: Template Decision Recorded (Phase E)

**Condition:** `DECISION_RECORD.md` written with all required fields.

**Check:**
```bash
test -f DECISION_RECORD.md && grep -q "primary_template" DECISION_RECORD.md && grep -q "design_system" DECISION_RECORD.md
```

**Failure:** Stop; run template-selection-guide.md 10-step procedure.

---

## Gate 4: Animation Approved (Phase G)

**Condition:** `review-animations` skill returns **Approve** verdict.

**Check:**
```bash
# Run review-animations on output_dir/
# Parse output for explicit "Approve" verdict (not "Block")
# No feel-breaking regressions, durations ≤300ms, interruptibility handled, reduced-motion respected
```

**Failure:** Fix per remedial hierarchy (delete → reduce → fix easing → fix origin → interruptible → GPU → asymmetric → polish → a11y/cohesion); re-run review.

---

## Gate 5: P0 Findings Resolved (Phase H)

**Condition:** `generic-site-auditor` reports 0 P0 findings.

**Check:**
```bash
# Run generic-site-auditor on output_dir/
# Parse findings: P0 count must be 0
# P1 should be 0 or documented as accepted risk
```

**Failure:** Fix P0 findings; re-audit.

---

## Gate 6: Browser QA = SHIP (Phase I)

**Condition:** `browser-qa` verdict = SHIP.

**Check:**
```bash
# Run browser-qa on deployed/preview URL
# Parse verdict: must be "SHIP"
# No console errors, CWV pass, forms work, 3 breakpoints clean, axe 0 violations
```

**Failure:** Fix findings; re-run QA.

---

## Gate 7: Verification Loop = PASS (Phase J)

**Condition:** `verification-loop` exit code 0 (PASS).

**Check:**
```bash
# Run verification-loop in output_dir/
# All 6 phases pass: build, type check, lint, tests+coverage, security, diff review
# Coverage ≥80%, Lighthouse ≥90
```

**Failure:** Fix failures; re-verify.

---

## Gate 8: Source Library Unchanged (Phase L)

**Condition:** `D:\Master Design\` unchanged per `source-inventory.jsonl` checksums.

**Check:**
```bash
cd "D:\Master Design"
python3 -c "
import json, hashlib, sys, os
with open('C:\\Users\\Admin\\.local\\share\\opencode\\tool-output\\source-inventory.jsonl') as f:
    for line in f:
        rec = json.loads(line)
        if rec['sha256'].startswith('ERR'): continue
        p = os.path.join('D:\\Master Design', rec['path'])
        if os.path.exists(p):
            h = hashlib.sha256(open(p,'rb').read()).hexdigest()
            if h != rec['sha256']:
                print(f'MODIFIED: {rec[\"path\"]}')
                sys.exit(1)
print('All source files preserved.')
"
```

**Failure:** Abort delivery; investigate modification.

---

## Automation

Each gate check is a callable bash function. The skill runs them in sequence:

```bash
check_gate_1_design_doc_approved
check_gate_2_tokens_ready
check_gate_3_decision_record
check_gate_4_animation_approved
check_gate_5_p0_resolved
check_gate_6_browser_qa_ship
check_gate_7_verification_pass
check_gate_8_source_preserved
```

Any failure → immediate stop with actionable message.