# Phase G — Animation & Interaction

## Purpose
Apply purposeful motion to the implementation using Design System motion tokens. Every animation must pass the `review-animations` hard gate. Output: **Animated Implementation** (all motion implemented, reviewed, approved).

## Workflow

### Step 1: Animation Build Sequence (from `animate` — 6-Step Decision Framework)

**For every animated element, run this sequence:**

#### 1. Frequency Gate — Should this animate?
- Does motion serve a clear purpose? (communicate state, guide attention, show relationship)
- Is it noticeable and meaningful?
- Does it interrupt existing motion correctly?
- **If NO to any → STOP. Element stays static.**

#### 2. Tool Selection
| Behavior | Tool |
|----------|------|
| Single property tween | GSAP `.to()`, `.from()`, `.fromTo()` |
| Sequenced timing | GSAP Timeline |
| Scroll-driven | GSAP ScrollTrigger |
| Complex choreography | Multiple tweens + Timelines |
| React state-driven | `motion/react` (Framer Motion) |
| Simple hover/focus | CSS Transitions |

#### 3. Properties — Animate Only What Matters
**DO animate**: `transform` (translate, scale, rotate), `opacity`, `clip-path`
**DON'T animate**: `color`, `background-color`, `box-shadow`, `width`, `height`, `top`, `left`, `text-content`

#### 4. Easing & Duration (from `emil-design-eng`, `motion-foundations`, `animate`)

**Never use `linear` for physical motion.**

| Motion Type | Easing | Duration | Spring Config |
|-------------|--------|----------|---------------|
| Micro (press, hover) | `ease-out` / spring | 100–150ms | `stiffness: 400, damping: 20, mass: 0.5` |
| Fast (tooltip, toast) | `ease-out` / spring | 150–250ms | `stiffness: 300, damping: 18, mass: 0.6` |
| Standard (modal, panel) | `ease-in-out` / spring | 300–500ms | `stiffness: 250, damping: 22, mass: 0.8` |
| Slow (page transition) | `ease-in-out` / spring | 500–800ms | `stiffness: 150, damping: 25, mass: 1.0` |
| Cinematic (hero reveal) | Custom / spring | 600–1200ms | `stiffness: 120, damping: 18, mass: 1.5` |

**From `emil-design-eng` Spring Presets**:
```javascript
// Button press
{ type: 'spring', stiffness: 400, damping: 20, mass: 0.5 }

// Modal entrance
{ type: 'spring', stiffness: 250, damping: 22, mass: 0.8 }

// Page transition
{ type: 'spring', stiffness: 150, damping: 25, mass: 1.0 }

// List item entry
{ type: 'spring', stiffness: 300, damping: 18, mass: 0.6 }
```

#### 5. Interruption Handling
- **GSAP**: `invalidate()` on re-trigger, `kill()` old tweens
- **CSS**: `transition` with `animation-fill-mode: both`
- **Motion/React**: `stagger` with `onComplete` cleanup
- **Rule**: New animation always wins gracefully — no jank, no stuck states

#### 6. Reduced Motion (MANDATORY)
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  /* Keep functional motion (loading spinners) but simplify */
}
```
- Hide non-essential motion
- Simplify essential motion (fade instead of slide)
- Never remove functional motion (loading, progress)

### Step 2: The 10 Non-Negotiable Standards (from `review-animations` — HARD GATE)

Every animation must pass all 10. `review-animations` returns **Approve** / **Fix Required** / **Remove Required**.

| # | Standard | Before (❌) | After (✅) |
|---|----------|-------------|------------|
| 1 | **No Linear Easing** for physical motion | `ease: 'linear'` | `ease: 'out-expo'` or spring |
| 2 | **Duration Matches Scale** | All 300ms | Entry 400–600ms, Exit 300–400ms, Micro 150–250ms |
| 3 | **Stagger Groups, Not Individuals** | All cards animate together | `stagger: 0.05` from `start` or `center` |
| 4 | **Origin-Aware Positioning** | Appears at viewport center | Originates from trigger element |
| 5 | **Clip-Path for Reveals** | `opacity: 0→1` | `clip-path: inset(0 100% 0 0) → inset(0 0% 0 0)` |
| 6 | **Gesture Feedback on Press** | Only hover state | `active`: scale(0.97) or translateY(1px), 100–150ms |
| 7 | **Performance Budget** | 10 concurrent transforms | Max 3 concurrent, prefer transform/opacity |
| 8 | **Accessibility Compliance** | Motion required for understanding | Info conveyed without motion |
| 9 | **Sequence, Not Simultaneity** | All fade in together | `stagger: 0.05` from `start`/`center` |
| 10 | **Exit Animations Required** | Disappears instantly | Fade/scale/translate out |

**Remedial Hierarchy** (if Fix Required):
1. Re-order (fix sequence/timing)
2. Rewrite (fix easing/duration/properties)
3. Remove (revert to static)
4. Restructure (change component architecture)

### Step 3: Component Motion Patterns (from `emil-design-eng`, `motion-patterns`, `motion-foundations`, `animate`)

#### Buttons
- **Press**: `scale(0.97)` or `translateY(1px)`, 100–150ms, spring/ease-out
- **Hover**: `scale(1.02)` + subtle shadow, 200ms
- **Focus**: Visible ring (`--shadow-colored`), immediate
- **Disabled**: 50% opacity, no motion

#### Popovers / Dropdowns / Menus
- **Origin**: Must animate from trigger element (not viewport center)
- **Enter**: `scale(0.95) → scale(1)` + `opacity(0→1)`, 200ms, ease-out
- **Exit**: Reverse, 150ms, ease-in
- **Backdrop**: Fade in/out, click closes

#### Tooltips
- **Position**: Near trigger, not cursor
- **Enter**: Fade only (`opacity(0→1)`), 150ms
- **No slide** — feels like lag
- **Respects reduced-motion**: Instant show/hide

#### Modals / Drawers
- **Backdrop**: Fade in 200ms
- **Panel**: `translateY(20px) → translateY(0)` + scale(0.98→1), 300ms, spring
- **Exit**: Reverse, 200ms
- **Focus trap**: Required

#### Lists / Grids (from `animate`, `motion-patterns`)
- **Stagger**: `0.05s` per item
- **Origin**: `start` (top-left), `center`, or `end` based on layout
- **Enter**: `opacity(0→1)` + `translateY(20px→0)`
- **Exit**: Reverse, faster (0.03s stagger)

#### Page Transitions (from `motion-patterns`, `nextjs-turbopack`)
- **Shared Layout**: Animate between shared elements
- **Exit**: Fade + slight scale down, 300ms
- **Enter**: Fade + slight scale up, 400ms
- **Preserve scroll** where appropriate

### Step 4: Motion Library Integration

#### GSAP (Recommended for Scroll/Complex)
```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Scroll reveal
gsap.from('.reveal', {
  scrollTrigger: { trigger: '.reveal', start: 'top 80%' },
  y: 50, opacity: 0, duration: 0.8, ease: 'out-expo', stagger: 0.1
});

// Pin section
gsap.to('.pinned', {
  scrollTrigger: { trigger: '.pinned', pin: true, end: '+=500' }
});
```

#### Motion/React (React State-Driven)
```tsx
import { motion } from 'framer-motion';

<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -20 }}
  transition={{ type: 'spring', stiffness: 250, damping: 22 }}
/>
```

#### CSS Transitions (Simple Only)
```css
.button {
  transition: transform 150ms var(--ease-out), box-shadow 150ms var(--ease-out);
}
.button:hover { transform: scale(1.02); }
.button:active { transform: scale(0.97); }
```

### Step 5: Performance Audit (from `fixing-motion-performance`, `gsap-performance`, `benchmark`)

- [ ] Total animation cost < 16ms/frame (60fps)
- [ ] Max 3 concurrent complex animations per view
- [ ] Only `transform`/`opacity` animated (no layout thrashing)
- [ ] `will-change` used sparingly (only sustained animations)
- [ ] `prefers-reduced-motion` tested and working
- [ ] No layout shift from animations (CLS < 0.1)

## Hard Gate
> **`review-animations` returns Approve** on all animated elements → Proceed to Phase H
> If **Fix Required** → Apply remedial hierarchy
> If **Remove Required** → Revert element to static state

## Cross-References
- Consumes: Phase F (Implementation), Phase C/D (Motion Tokens)
- Produces: Animated Implementation → Phase H
- Specialty: `references/animation-guide.md`
- Skills: 30+ animation skills (GSAP, Motion, CSS, Remotion, etc.)