# Classroom AI Studio

A free, offline recording studio for teacher tutorial videos. One 1920×1080 stage with three panels:

| Steps | AI | Sources |
| --- | --- | --- |
| Your step-by-step directions, with tips | A live browser tab with your AI tool | Pictures, PDFs and text cards |

Draw on the stage with a pen, highlighter, spotlight, zoom, callouts and numbered step badges, and record the stage plus your microphone to one video file.

**Use it now:** download `index.html` and open it in Chrome or Edge on a computer. Nothing to install, no account, and it works offline.

## Quick start

1. **Steps tab:** paste your steps, one per line. A line starting with `Tip:` or `Hint:` attaches to the step above.
2. **Sources tab:** drag in pictures or PDFs, or add a text card.
3. **Connect AI tab:** in the share box, choose **Chrome Tab** and pick the tab with your AI tool.
4. **Settings → Turn on mic.** Then press **F9** to record and **F9** again to stop.

## Keyboard shortcuts

| Key | Action |
| --- | --- |
| F9 / F8 | Start or stop recording / pause or resume |
| → / ← | Next or previous step |
| ] / [ | Next or previous source |
| PgDn / PgUp | Next or previous PDF page |
| P, H, S, Z, T, B | Pen, highlighter, spotlight, zoom, callout, step badge |
| V or Esc | No tool; Esc also zooms out and removes the spotlight |
| 1–4 | Pen color |
| Ctrl+Z / C | Undo last mark / clear all marks |

## Privacy

Everything stays on your computer. The app has no server and sends nothing anywhere. Only the stage is recorded, but close email, school accounts and anything with student names before you share a tab.

## For developers

`index.html` is built from `src/studio.html` by `build.py`, which inlines the font and PDF reader so the file works offline:

```
python3 build.py path/to/deps
```

`deps` must contain the unpacked npm packages `pdfjs-dist@3.11.174` and `@fontsource/atkinson-hyperlegible@5.3.0`.

## Credits

- [PDF.js](https://github.com/mozilla/pdf.js) 3.11.174, Apache License 2.0
- [Atkinson Hyperlegible](https://brailleinstitute.org/freefont) font by the Braille Institute, SIL Open Font License 1.1

Version 1.0
