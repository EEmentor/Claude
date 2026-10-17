# EEMENTOR brand kit for social images

Follows the EEmentor Brand Guideline (rev. 01-06-2026).

- Colors: Dark Blue `#1B3A7B` (background), Red `#DE544A` (accents, highlighted words, buttons), White, grays `#EAEAEA` / `#C6C6C6`. Gradient bar blue → white → red.
- Font: Poppins (Regular 400 for body, Medium 500 for headlines, SemiBold 600 for labels). Files included (SIL Open Font License).
- Headlines: UPPERCASE, key words in red. Tight leading on big type.
- Logo: ALWAYS `logo_energy.png` (the EEMENTOR ENERGY lock-up, full colour). It sits on a white header strip at the top of every image, with a red rule under the strip, because its dark blue letters need a white background. Never stretch, recolor, rotate, add effects or rearrange it.
- Layout: white header strip with the logo, left-aligned; red kicker; headline; short body; red rectangular button; footer with Facebook / Instagram / LinkedIn icons | energy.eementor.co; gradient bar at the bottom.
- Sizes: Instagram, Facebook and LinkedIn 1080x1350 (4:5); LinkedIn also 1200x627. Never 3:4 (1080x1440) for Instagram: its publishing API only accepts 4:5 to 1.91:1. Keep text and product 60+ px from the side edges (the profile grid trims ~34 px each side). Photo posts: template_photo_post.py.

## Make images
1. Copy a template (`template_*.py`), edit the text and diagrams. Each page is an HTML file with `data-size="WxH"`.
2. `python3 template_x.py <outdir>` writes HTML into `<outdir>` (copy style.css, logo_energy.png and the .woff2 files there first, and create `<outdir>/out`).
3. `python3 render.py <outdir> file1.html file2.html` renders PNGs into `<outdir>/out/` (needs Playwright + Chromium).
4. Put finished PNGs in `social/YYYY-MM/` and push. Public link: `https://raw.githubusercontent.com/EEmentor/Claude/main/social/YYYY-MM/<file>.png`
