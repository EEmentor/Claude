# EEMENTOR ENERGY reels kit

Reels are built in the workspace with the brand kit, Playwright, ffmpeg and an offline voice. No Krea or Higgsfield in automatic runs.

## Formats
- 9:16 1080x1920, 30 fps, H.264 + AAC: Instagram Reel, Facebook Reel, YouTube Short.
- 4:5 1080x1350 version of the same reel for the LinkedIn feed.
- 18–30 seconds. Hook in the first 2 seconds. End card with the logo, a red button (e.g. "Get a quote") and the most specific energy.eementor.co URL.

## Brand rules (same as images)
White logo header strip with red rule on every frame (brand-kit/logo_energy.png, unmodified), Dark Blue #1B3A7B, Red #DE544A, Poppins, uppercase captions with key words in red, gradient bar at the bottom. Captions must never cover the product.

## Two reel types
1. Animated brand explainer (example_animated_gen.py + render_frames.py): scenes are HTML/SVG with CSS keyframe animations; render_frames.py pauses all animations and screenshots each frame at 30 fps (deterministic), then ffmpeg encodes. Good for specs, comparisons, how-it-works.
2. Real product photo reel (example_photo_reel_build.py): the real product photo (fetched via fetch/urls.txt) on brand backgrounds with slow camera moves (scale/pan), captions and spec chips per scene, end card. Never let AI redraw a product.

## Voice-over
- pip install --break-system-packages kokoro-onnx soundfile
- Model files (GitHub releases): https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx and .../voices-v1.0.bin
- Voice am_puck (energetic male, chosen by Osama 17 Oct 2026), speed 1.15, en-us. One line per scene; time scenes to the lines. Spell acronyms ("B M S", "A B S"). Never speak the URL.
- Write like a person talking, not a spec sheet: short punchy lines, questions to the viewer ("Need eleven volts? Twenty-two?"), "you" language, a light reaction ("Yes, really.", "Your call."), and end with a question ("So... what are you building?"). Facts stay exactly as on the website.
- Photo reels: brand-kit/reels/photo_reel_build.py with a specs file like photo_reel_specs_2026-10.py.
- Mix with adelay per line, amix, loudnorm I=-15.

## Facts
Only facts on energy.eementor.co (product pages, articles). No invented specs, certifications, results or customers. Mock UI numbers must not be presented as real data.

## Publishing
Commit the MP4s to social/YYYY-MM/reels/ and use the raw.githubusercontent.com URL in Metricool.
