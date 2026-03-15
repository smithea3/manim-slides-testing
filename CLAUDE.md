# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a [manim-slides](https://github.com/jeertmans/manim-slides) + [manim-voiceover](https://github.com/ManimCommunity/manim-voiceover) project for creating interactive mathematical presentations with narration. Slides are Python classes rendered to MP4 segments by manim, then presented interactively via manim-slides.

## Environment

Uses a local `.venv`. Activate before running any commands:
```bash
.venv/Scripts/activate   # Windows
```

## Workflow Commands

**Render a slide class:**
```bash
manim <file>.py ClassName
```

**Present slides interactively:**
```bash
manim-slides present ClassName
```

**Export to HTML:**
```bash
manim-slides convert ClassName output.html
```

## Architecture

### Slide classes

All slide classes live in `.py` files in the project root. A class can extend:
- `Slide` (from `manim_slides`) — interactive slides only
- `VoiceoverScene` + `Slide` — slides with narration (use multiple inheritance in that order)

`self.pause()` defines slide advance points. `with self.voiceover("text"):` wraps animations so they sync to the audio — manim-voiceover automatically waits for the audio to finish if the animation ends first.

### Speech backends

The default backend used here is **gTTS** (Google Text-to-Speech, free, requires internet). Set it in `construct()`:
```python
from manim_voiceover.services.gtts import GTTSService
self.set_speech_service(GTTSService())
```

Other available backends (require API keys): `AzureService`, `ElevenLabsService`, `OpenAIService`. Store keys in a `.env` file — `python-dotenv` is included.

### Build output
- `media/` — manim's raw render output (auto-generated, gitignored)
- `slides/` — manim-slides output JSON + MP4 segments (auto-generated, gitignored)
- Audio cache for voiceover is stored under `media/voiceover/`

## Key Pattern

```python
class MySlide(VoiceoverScene, Slide):
    def construct(self):
        self.set_speech_service(GTTSService())

        with self.voiceover("Narration text here."):
            self.play(Write(some_mobject))

        self.pause()  # slide advance point
```
