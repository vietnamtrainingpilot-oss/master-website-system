# Master Website — Design Read Template

Used by Phase A (brainstorming) to output the one-line Design Read.

## Format

```
Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <design system or aesthetic family>.
```

## Page Kinds

| Kind | Description |
|------|-------------|
| `landing` | SaaS, consumer, agency, event |
| `portfolio` | Developer, designer, creative studio |
| `redesign` | Preserve vs overhaul |
| `editorial` | Blog, magazine, publication |
| `dashboard` | Data-heavy, operational |
| `docs` | Documentation, knowledge base |
| `web-app` | Multi-route application |

## Audiences

| Audience | Implication |
|----------|-------------|
| `technical buyers` | Linear-style, minimal, trust-first |
| `design-conscious consumers` | Editorial, kinetic, premium |
| `recruiters/hiring managers` | Clean, scannable, skill-forward |
| `general public` | Accessible, clear, mobile-first |
| `procurement panels` | Trust signals, compliance, boring-good |

## Vibes (Taste-Skill Vocabulary)

| Vibe | Taste-Skill Signals | Dial Tendency |
|------|---------------------|---------------|
| `minimalist` / `clean` / `calm` | "Linear-style", "editorial" | VAR 5-6, MOT 3-4, DEN 2-3 |
| `premium consumer` / `Apple-y` / `luxury` | "brand", "premium" | VAR 7-8, MOT 5-7, DEN 3-4 |
| `playful` / `wild` / `experimental` | "Awwwards", "Dribbble", "agency" | VAR 9-10, MOT 8-10, DEN 3-4 |
| `trust-first` / `public-sector` | "accessibility-critical", "regulated" | VAR 3-4, MOT 2-3, DEN 4-5 |
| `brutalist` | "Swiss", "newspaper", "manifesto" | Custom (brutalist-skill) |
| `dark tech` / `hacker` | "terminal", "mono", "neon" | Custom |

## Design System / Aesthetic Family

| Family | When to Choose |
|--------|----------------|
| `Tailwind + Geist + restrained motion` | Modern SaaS, technical buyers |
| `native CSS + scroll-driven animation + custom typography` | Designer portfolio, editorial |
| `GOV.UK Frontend` / `USWDS` | Public sector, accessibility-critical |
| `shadcn/ui` | Modern SaaS where you own components |
| `@radix-ui/themes` | Accessible React foundation |
| `Bootstrap 5.3` | Fast MVP, local business |
| `brutalist-skill` (Swiss Industrial Print) | Agency portfolio, manifesto |
| `minimalist-skill` (Editorial Minimalism) | Premium SaaS, documentation |

## Example Outputs

```
Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion.

Reading this as: solo designer portfolio for hiring managers, with an editorial / kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography.

Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend.
```