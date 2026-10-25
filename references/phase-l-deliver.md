# Phase L — Ship & Deliver

## Purpose
End-to-end delivery pipeline: final checks, deployment, monitoring, handoff. Output: **Live Production Site** + **Handoff Package**.

## Workflow

### Step 1: Ship-It Pipeline (from `ship-it` — 7 Stages)

| Stage | Action | Verification |
|-------|--------|--------------|
| **1. Decide** | Define success criteria, acceptance criteria, blockers | Stakeholder sign-off |
| **2. Plan** | Break into independent steps, order by dependency, estimate | Plan doc approved |
| **3. Build** | Implement each step, verify incrementally, commit | CI green per commit |
| **4. Verify** | Full verification loop (Phase J) | All 6 phases PASS |
| **5. Secure** | Security scan, fix vulns, verify no secrets | Clean audit |
| **6. Perform** | Performance audit, optimize, verify CWV | All CWV Good |
| **7. Ship** | Deploy to production, verify, monitor | Live + healthy |

### Step 2: Pre-Ship Checklist (from `ship-it`, `release-director`)

#### Content
- [ ] All copy reviewed for clarity, tone, legal
- [ ] All links verified (internal, external, anchors)
- [ ] Images optimized (WebP/AVIF, responsive, alt text)
- [ ] Meta tags: title, description, OG, Twitter, canonical
- [ ] Sitemap.xml, robots.txt generated

#### Technical
- [ ] Build clean (no errors/warnings)
- [ ] No console errors in production
- [ ] No TypeScript errors
- [ ] No lint errors
- [ ] Source maps uploaded (for error tracking)

#### Performance
- [ ] LCP < 2.5s
- [ ] INP < 200ms
- [ ] CLS < 0.1
- [ ] Bundle < 200KB gzipped
- [ ] Lighthouse score ≥ 90 all categories

#### Accessibility
- [ ] WCAG 2.2 AA compliant (Phase H audit)
- [ ] Keyboard navigation tested
- [ ] Screen reader tested (NVDA/VoiceOver)
- [ ] Color contrast verified

#### Security
- [ ] No secrets in code/repo
- [ ] Dependencies audited (no critical/high)
- [ ] CSP headers configured
- [ ] HTTPS enforced (HSTS)
- [ ] Rate limiting active

#### Analytics
- [ ] Tracking code deployed (GA4, Plausible, etc.)
- [ ] Events configured (CTA, form submit, purchase)
- [ ] Goals/funnels defined

### Step 3: Deployment (from `deployment-patterns`, `deployment-patterns`)

#### Vercel (Recommended)
```bash
# Connect repo → Vercel
# Enable automatic deployments on main
# Configure preview deployments on PRs
# Set production environment variables
vercel --prod
```

#### GitHub Pages / Netlify / Cloudflare Pages
```bash
npm run build
# Deploy dist/ or .output/
# Configure custom domain, SSL
```

#### Manual/Container
```bash
npm run build
docker build -t app .
# Deploy to K8s/ECS/Cloud Run
# Health checks, rolling updates
```

### Step 4: Post-Launch Monitoring (from `canary-watch`, `canary-watch`)

**Immediate (0–30 min)**:
- [ ] Error tracking alerts (Sentry, etc.)
- [ ] Performance monitoring (Web Vitals, Lighthouse CI)
- [ ] Uptime monitoring (Pingdom, UptimeRobot)
- [ ] Analytics real-time verification

**Short-term (24–48 hrs)**:
- [ ] CWV trends (no regression)
- [ ] Error rate < 0.1%
- [ ] Conversion funnels working
- [ ] User feedback channel monitored

**Ongoing**:
- [ ] Weekly performance review
- [ ] Monthly security audit
- [ ] Quarterly dependency updates

### Step 5: Handoff Package (from `release-director`, `docs-governance`, `living-docs-governance`)

**Deliverables**:
```
handoff/
├── ARCHITECTURE.md          # System overview, data flow, decisions
├── DEPLOYMENT.md            # Deploy commands, env vars, rollback
├── RUNBOOK.md               # Common issues, debugging, contacts
├── DESIGN_SYSTEM.md         # Tokens, components, usage
├── CONTENT_GUIDE.md         # CMS guide, tone, workflow
├── TESTING.md               # Test commands, coverage, E2E scenarios
├── SECURITY.md              # Threat model, incident response
├── CHANGELOG.md             # Version history, breaking changes
└── ADRs/                    # Architecture Decision Records
```

**Knowledge Transfer**:
- [ ] Walkthrough with receiving team
- [ ] Access granted (repo, deploy, monitoring, analytics)
- [ ] On-call rotation documented
- [ ] Support escalation path defined

### Step 6: Maintenance Planning (from `automation-audit-ops`, `config-gc`, `docs-governance`)

- [ ] Dependency update schedule (monthly/quarterly)
- [ ] Security scan schedule (weekly)
- [ ] Performance budget review (monthly)
- [ ] Content audit schedule (quarterly)
- [ ] Design system versioning (semver)

## Hard Gate
> **All pre-ship checks PASS + deployment successful + monitoring green + handoff complete** → DONE
> If any blocker → Address before closing

## Cross-References
- Consumes: Phase K (Release Candidate)
- Produces: Live Site + Handoff Package
- Skills: `ship-it`, `release-director`, `deployment-patterns`, `verification-loop`, `canary-watch`, `continuous-agent-loop`, `autonomous-agent-harness`, `agent-*`, `configure-ecc`, `config-gc`, `docs-governance`, `living-docs-governance`, `wiki-*`, `git-workflow`, `github-ops`