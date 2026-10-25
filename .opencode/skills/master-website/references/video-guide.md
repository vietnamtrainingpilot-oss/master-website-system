# Video Creation & Editing Guide

This guide covers all video creation and editing capabilities in the master-website-system.

## Overview

The video pipeline integrates 20+ video skills into a coherent workflow. The router `video-production` selects the right tool based on the task:

| Task | Primary Tool | Workflow |
|------|--------------|----------|
| Product launch / promo from URL | `product-launch-video` → HyperFrames | Brief → Compose → Assets → Animate → Render |
| PR to video | `pr-to-video` → HyperFrames | Diff → Script → Compose → Render |
| Talking-head + graphics | `talking-head-recut` → HyperFrames | Footage → Transcribe → Graphics → Compose |
| Captioning | `embedded-captions` → HyperFrames | Footage → Transcribe → Style → Embed |
| Music-driven video | `music-to-video` → HyperFrames | Audio → Beat grid → Visuals → Sync |
| Motion graphics | `motion-graphics` → Remotion/HyperFrames | Design → Animate → Export |
| Raw footage editing | `video-editing` → FFmpeg/Remotion | Import → Cut → Assemble → Export |

---

## HyperFrames Pipeline (Primary)

### 1. Install & Setup
```bash
# HyperFrames is included in the skill
# CLI available via: npx hyperframes
```

### 2. Compose (index.html)
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Your Video</title>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="clip" data-start="0" data-end="5">
    <!-- Scene 1 -->
  </div>
  <div class="clip" data-start="5" data-end="10">
    <!-- Scene 2 -->
  </div>
</body>
</html>
```

### 3. Assets (media-use)
```bash
# BGM
media-use resolve --type bgm --mood "cinematic, tension" --duration 30

# Voiceover
media-use resolve --type voice --text "Your script here" --voice "en-US-Neural2-A"

# Images
media-use resolve --type image --prompt "cinematic hero shot" --style "hyperrealistic"
```

### 4. Animate (hyperframes-animation)
```javascript
// GSAP (default)
gsap.to('.element', { opacity: 1, y: 0, duration: 1, ease: 'out-expo' });

// Scroll-triggered
gsap.from('.reveal', {
  scrollTrigger: { trigger: '.reveal', start: 'top 80%' },
  y: 50, opacity: 0, duration: 0.8, ease: 'out-expo', stagger: 0.1
});
```

### 5. Preview & Render
```bash
# Preview in browser
npx hyperframes preview

# Render locally
npx hyperframes render --format mp4 --output video.mp4

# Render to cloud
npx hyperframes cloud --project my-video
```

---

## Remotion Pipeline (React Alternative)

### 1. Init
```bash
npx create-video my-video
cd my-video
npm install
```

### 2. Compose (React)
```tsx
// src/Root.tsx
import { Sequence, Composition } from 'remotion';

export const Root = () => (
  <>
    <Sequence from={0} durationInFrames={150}>
      <Scene1 />
    </Sequence>
    <Sequence from={150} durationInFrames={150}>
      <Scene2 />
    </Sequence>
  </>
);

export const Composition = ({ width, height, fps }) => (
  <Composition
    width={width}
    height={height}
    fps={fps}
    durationInFrames={300}
    component={Root}
  />
);
```

### 3. Animate (remotion-video-creation)
```tsx
import { motion, useSpring } from 'remotion';

<motion.div
  style={{
    opacity: useSpring(0, { stiffness: 300, damping: 20 }),
    x: useSpring(-50, { stiffness: 300, damping: 20 })
  }}
/>
```

### 4. Audio & Captions
```tsx
import { Audio } from 'remotion';
import { Caption } from 'remotion-captions';

<Audio src="voiceover.mp3" />
<Caption transcript={transcript} />
```

### 5. Render
```bash
# Local
npx remotion render src/Root.tsx Video out/video.mp4

# Cloud (Lambda)
npx remotion lambda render src/Root.tsx Video out/video.mp4

# Cloud Run
npx remotion cloudrun render src/Root.tsx Video out/video.mp4
```

---

## Captioning

### HyperFrames
```html
<hf-captions src="captions.vtt" style="custom" />
<!-- or inline -->
<hf-captions>
  <span data-start="0" data-end="2">Hello world</span>
  <span data-start="2" data-end="4">This is a caption</span>
</hf-captions>
```

### Remotion
```bash
# Auto-transcribe
npx remotion-captions transcribe audio.mp3 --output captions.json

# Render with captions
<Caption transcript={captions} style={captionStyle} />
```

---

## Asset Resolution (media-use)

```bash
# BGM
media-use resolve --type bgm --mood "cinematic, tension" --duration 30

# Voiceover (TTS)
media-use resolve --type voice --text "Your script here" --voice "en-US-Neural2-A"

# Sound effects
media-use resolve --type sfx --prompt "whoosh transition"

# Images
media-use resolve --type image --prompt "cinematic hero shot" --style "hyperrealistic"

# Video clips
media-use resolve --type video --prompt "slow motion water" --duration 5
```

---

## Platform Export Specs

| Platform | Aspect | Resolution | Max Duration | Codec |
|----------|--------|------------|--------------|-------|
| TikTok | 9:16 | 1080×1920 | 60s (3min max) | H.264 MP4 |
| Reels | 9:16 | 1080×1920 | 90s | H.264 MP4 |
| Shorts | 9:16 | 1080×1920 | 60s | H.264 MP4 |
| YouTube | 16:9 | 1920×1080 / 4K | 12h | H.264/VP9 |
| LinkedIn | 1:1 / 16:9 | 1080×1080 / 1920×1080 | 10min | H.264 MP4 |
| Twitter/X | 16:9 | 1280×720 | 140s | H.264 MP4 |
| Web embed | 16:9/9:16 | Responsive | Any | WebM + MP4 |

### HyperFrames Render Presets
```bash
npx hyperframes render --preset tiktok --output video.mp4
npx hyperframes render --preset reels --output video.mp4
npx hyperframes render --preset youtube --output video.mp4
npx hyperframes render --preset linkedin --output video.mp4
npx hyperframes render --preset twitter --output video.mp4
npx hyperframes render --preset web --format webm,mp4
```

---

## Hard Gates (Video)

| Gate | Check | Tool |
|------|-------|------|
| Animation Quality | `review-animations` returns Approve | `review-animations` |
| Visual Regression | Browser QA passes | `browser-qa` |
| Caption Accuracy | 99%+ word accuracy | Manual spot-check |
| Audio Sync | <50ms drift | `hyperframes-cli preview` |
| File Specs | Platform requirements met | `ffprobe` |
| Performance | <100MB web, <50MB social | File check |

---

## Template Pulling

From `references/design-templates/design-templates/`:

| Template | Use For |
|----------|---------|
| `hyperframes/` | Base project, house style, patterns, palettes, scripts |
| `video-shortform/` | TikTok/Reels/Shorts vertical format |
| `video-hyperframes/` | Continuous animation / ambient video |
| `video-production/` | General video project scaffold |
| `web-prototype/` | Video embeds in website |
| `saas-landing/` | Video hero on landing page |

---

## Skills Reference

All video skills available in `references/skills/`:

**HyperFrames**: `hyperframes`, `hyperframes-animation`, `hyperframes-audio`, `hyperframes-cli`, `hyperframes-core`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-registry`, `hyperframes-studio`

**Remotion**: `remotion`, `remotion-best-practices`, `remotion-captions`, `remotion-create`, `remotion-docs`, `remotion-interactivity`, `remotion-maps`, `remotion-markup`, `remotion-multimedia`, `remotion-render`, `remotion-saas`, `remotion-studio`, `remotion-upgrade`, `remotion-video-creation`, `remotion-to-hyperframes`

**Video Production**: `video-production`, `video-editing`, `product-launch-video`, `pr-to-video`, `talking-head-recut`, `embedded-captions`, `music-to-video`, `motion-graphics`, `faceless-explainer`, `general-video`

**Asset/Audio**: `media-use`, `fal-ai-media`

**Animation**: `animate`, `review-animations`, `gsap-*`, `motion-*`

---

*This guide extends the 12-phase pipeline with Phase M (Video). For non-video projects, skip Phase M. For video projects, execute after Phase L or in parallel with Phase G/H.*