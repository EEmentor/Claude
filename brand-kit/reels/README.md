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

## Voice-over (standard since 27 Nov 2026, chosen by Osama)
One narrator: the ElevenLabs voice "Will" (voice_id bIHbv24MWmeRgasZH58o, model eleven_v3, stability 0.5, similarity 0.75), energetic, natural American delivery. The Kokoro two-voice dialogue (30 Oct to 27 Nov) is retired: Osama found it robotic, cheesy and badly paced.
- Script: one or two short, punchy sentences per scene in "you" language; questions and quick reactions are fine; v3 audio tags such as [excited], [laughs], [gasps] where they fit. End with a comment question that is also the end-card note and a caption paragraph before the CTA.
- Generate: commit tts/requests/will_<reel>.json ({"voice_id","model_id","settings","lines":[{"id":"s1","text":...},...,{"id":"end",...}]}). The GitHub Action "elevenlabs-tts" (.github/workflows/tts.yml) reads the ELEVENLABS_API_KEY repository secret (the workspace itself cannot reach ElevenLabs) and commits tts/out/will_<reel>/<id>.mp3; existing files are skipped.
- Build: in the specs set each scene's vo to [('file', '/home/claude/claude/tts/out/will_<reel>/sN.mp3', 1.0)] and end_vo to [('file', '.../end.mp3', 1.0)]; build2.py treats voice 'file' as a recorded line. Music bed ducked under the voice, whoosh on cuts, loudnorm I=-14.
- Spell acronyms in the script ("B M S"). Never speak the URL. Facts stay exactly as on the website.
- File names: eementor-reel-<name>-v5-1080x<H>.mp4 (new names each time, Metricool copies media at scheduling).
- Free fallback (not chosen): Chatterbox open-source TTS via .github/workflows/chatterbox.yml.

## Facts
Only facts on energy.eementor.co (product pages, articles). No invented specs, certifications, results or customers. Mock UI numbers must not be presented as real data.

## Publishing
Commit the MP4s to social/YYYY-MM/reels/ and use the raw.githubusercontent.com URL in Metricool.
