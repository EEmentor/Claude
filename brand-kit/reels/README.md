# EEMENTOR ENERGY reels kit

Reels are built in the workspace with the brand kit, Playwright, ffmpeg and an offline voice. No Krea or Higgsfield in automatic runs.

## Formats
- 9:16 1080x1920, 30 fps, H.264 + AAC: Instagram Reel, Facebook Reel, YouTube Short.
- 4:5 1080x1350 version of the same reel for the LinkedIn feed.
- Encoding: H.264 High, yuv420p, 30 fps, keyframe every 2 s, CRF ~16, +faststart; audio AAC stereo 48 kHz (never higher, Instagram rejects it), 192 kbps. Check with ffprobe before publishing.
- 18–40 seconds. Hook in the first 2 seconds. End card with the logo, a red button (e.g. "Get a quote") and the most specific energy.eementor.co URL.

## Brand rules (same as images)
White logo header strip with red rule on every frame (brand-kit/logo_energy.png, unmodified), Dark Blue #1B3A7B, Red #DE544A, Poppins, uppercase captions with key words in red, gradient bar at the bottom. Captions must never cover the product.

## Two reel types
1. Animated brand explainer (example_animated_gen.py + render_frames.py): scenes are HTML/SVG with CSS keyframe animations; render_frames.py pauses all animations and screenshots each frame at 30 fps (deterministic), then ffmpeg encodes. Good for specs, comparisons, how-it-works.
2. Real product photo reel (example_photo_reel_build.py): the real product photo (fetched via fetch/urls.txt) on brand backgrounds with slow camera moves (scale/pan), captions and spec chips per scene, end card. Never let AI redraw a product.

## Voice-over (dialogue standard, set by Osama 30 Oct 2026)
Single-narrator voice-overs sounded like someone reading a script, so every reel is now a short two-voice conversation with music.
- pip install --break-system-packages kokoro-onnx soundfile
- Model files (GitHub releases): https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx and .../voices-v1.0.bin
- Builder: brand-kit/reels/build2.py (photo reels). In the specs file each scene's `vo` is a list of (voice, text, speed) lines; helpers `H_(text)` = host af_heart at 1.12 and `E_(text)` = expert am_puck at 1.2, and `_dlg(...)` (see photo_reel_specs_2026-10.py, REELS climate2/cells2/process2/robots2/ess2).
- Host asks or reacts, expert answers. Lines of 2–8 words, questions to the viewer, "you" language, quick reactions ("Wait, really?", "Nice."). 1–3 lines per scene; the scene lasts as long as its lines (min 2.2 s).
- End with a comment question (e.g. "LiFePO4 or Li-ion for your robot? Vote in the comments."). Use the same question as the end-card note and as a paragraph in every caption, just before the CTA.
- Music bed: brand-kit/reels/music_bed.wav (synthesised by music.py, 112 BPM, royalty-free), looped, ducked under the voices (sidechaincompress), faded out over the last 1.2 s; whoosh.wav on every cut. Final loudnorm I=-14.
- Spell acronyms ("B M S"). Never speak the URL. Facts stay exactly as on the website.
- File names: eementor-reel-<name>-v4-1080x<H>.mp4 (new names each time, Metricool copies media at scheduling).

## Facts
Only facts on energy.eementor.co (product pages, articles). No invented specs, certifications, results or customers. Mock UI numbers must not be presented as real data.

## Publishing
Commit the MP4s to social/YYYY-MM/reels/ and use the raw.githubusercontent.com URL in Metricool.
