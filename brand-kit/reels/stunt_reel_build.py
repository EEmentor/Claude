"""Stunt reel: the real All-in-One ESS photo slides, lifts off, flips and flies.
python3 stunt.py <H>   (H = 1920 or 1350)"""
import sys, os, math, random, subprocess, json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from playwright.sync_api import sync_playwright

H = int(sys.argv[1]); W = 1080; tall = H > 1500
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = '/home/claude/claude/brand-kit'
TTS = '/tmp/claude-0/-home-claude-claude/597a0b6c-e239-5cf6-a538-974de408a6fe/scratchpad/tts'
OUTDIR = '/home/claude/claude/social/2026-10/reels'
B = f'{HERE}/b{H}'; os.makedirs(B, exist_ok=True)
for f in ['logo_energy.png', 'style.css'] + [x for x in os.listdir(KIT) if x.endswith('.woff2')]:
    subprocess.run(['cp', f'{KIT}/{f}', B])
FPS = 30
HD = 150 if tall else 118           # header height
AY0 = HD                             # animation area top
AY1 = 1340 if tall else 900          # animation area bottom / caption panel top
AH = AY1 - AY0
FS = 80 if tall else 60

kw = lambda t: f'<span style="text-transform:none">{t}</span>'
SC = [
 dict(k='POV', h="Everyone's car<br><em>can fly now</em>", s='', vo="Okay, so... everyone's car can fly now.", kind='city_cars', min=2.6),
 dict(k='Meanwhile', h='Our battery<br><em>saw the videos</em>', s='', vo='And our battery? It saw the videos.', kind='idle', min=2.6),
 dict(k='Step 1', h='<em>The slide</em>', s='', vo='Step one... the slide.', kind='slide', min=3.0),
 dict(k='Step 2', h='<em>Lift-off</em>', s='', vo='Step two... lift-off!', kind='liftoff', min=3.4),
 dict(k='Step 3', h='Keep the<br><em>lights on</em>', s='Backup power while the grid is down', vo='Step three... keep the lights on.', kind='fly_city', min=3.8),
 dict(k='All-in-one ESS', h=f'<em>{kw("10 ms")}</em> switch-over', s='5 kW inverter · 5–20 kWh LiFePO4 · MPPT solar input up to 5,200 W', vo='Ten millisecond switch-over. Five kilowatt inverter. Up to twenty kilowatt-hours.', kind='land', min=3.6),
]
END = dict(vo="Okay, it doesn't really fly. But it really does keep your power on. Link below!")

def ff(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)

# ---------- voice-over ----------
vo_dir = f'{HERE}/vo'; os.makedirs(vo_dir, exist_ok=True)
lines = [s['vo'] for s in SC] + [END['vo']]
import soundfile as sf
if any(not os.path.exists(f'{vo_dir}/{i}.wav') for i in range(len(lines))):
    from kokoro_onnx import Kokoro
    k = Kokoro(f'{TTS}/kokoro-v1.0.onnx', f'{TTS}/voices-v1.0.bin')
    for i, t in enumerate(lines):
        a, sr = k.create(t, voice='am_puck', speed=1.15, lang='en-us'); sf.write(f'{vo_dir}/{i}.wav', a, sr)
vd = [sf.info(f'{vo_dir}/{i}.wav').frames / sf.info(f'{vo_dir}/{i}.wav').samplerate for i in range(len(lines))]
dur = [max(SC[i]['min'], round(vd[i] + 0.55, 2)) for i in range(len(SC))] + [max(4.2, vd[-1] + 1.0)]
starts = [0]
for d in dur[:-1]: starts.append(starts[-1] + d)
TOTAL = sum(dur)

# ---------- HTML overlays (header + caption panel; animation area transparent) ----------
def header(): return f'<div style="position:absolute;left:0;right:0;top:0;height:{HD-6}px;background:#fff;display:flex;align-items:center;padding-left:64px;border-bottom:6px solid #DE544A"><img src="logo_energy.png" style="height:{int(HD*.58)}px"></div>'
def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>html,body{{background:transparent}}</style></head><body><div style="position:relative;width:{W}px;height:{H}px;overflow:hidden">{body}<div class="bar"></div></div></body></html>'
def overlay(sc, i):
    sub = f'<p style="font-size:{int(FS*.42)}px;margin-top:16px;color:#EAEAEA">{sc["s"]}</p>' if sc['s'] else ''
    return page(f'''{header()}
<div class="frame" style="position:absolute;left:0;right:0;top:{AY1}px;bottom:0"><div class="arcs" style="top:-300px"></div></div>
<div style="position:absolute;left:0;right:0;top:{AY1}px;height:6px;background:#DE544A"></div>
<div style="position:absolute;left:64px;right:64px;top:{AY1+(54 if tall else 30)}px">
<div style="display:flex;justify-content:space-between;align-items:center"><div class="kicker" style="font-size:{30 if tall else 24}px">{sc["k"]}</div><div style="font-size:{24 if tall else 20}px;color:#C6C6C6;font-weight:500">{i+1}/{len(SC)}</div></div>
<h2 style="font-size:{FS}px;margin-top:10px">{sc["h"]}</h2>{sub}</div>''')
def end_card():
    chips = ''.join(f'<span class="chip" style="font-size:{26 if tall else 21}px;margin:6px">{c}</span>' for c in ['Home backup', 'Solar', 'Off-grid'])
    ih = 600 if tall else 380
    return page(f'''<div class="frame" style="position:absolute;inset:0"><div class="arcs" style="top:-200px"></div></div>{header()}
<div style="position:absolute;left:0;right:0;top:{HD}px;bottom:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 60px">
<div class="kicker" style="font-size:{28 if tall else 22}px">All-in-one ESS</div>
<h2 style="font-size:{70 if tall else 52}px;margin-top:12px">It doesn't really fly.<br><em>It keeps the power on.</em></h2>
<img src="prod.png" style="height:{ih}px;margin-top:{36 if tall else 18}px">
<div style="margin-top:{24 if tall else 14}px">{chips}</div>
<span class="btn" style="font-size:{30 if tall else 24}px;padding:18px 40px;margin-top:{28 if tall else 16}px">See the ESS</span>
<div style="font-size:{26 if tall else 21}px;margin-top:20px;color:#fff">energy.eementor.co/pages/energy-storage</div></div>''')
prod = Image.open('/home/claude/claude/fetch/out/aio_cut.png').convert('RGBA')
prod = prod.crop(prod.getchannel('A').getbbox())
prod.save(f'{B}/prod.png')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    for i, sc in enumerate(SC):
        open(f'{B}/ov{i}.html', 'w').write(overlay(sc, i)); pg.goto(f'file://{B}/ov{i}.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
        pg.screenshot(path=f'{B}/ov{i}.png', omit_background=True)
    open(f'{B}/end.html', 'w').write(end_card()); pg.goto(f'file://{B}/end.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    pg.screenshot(path=f'{B}/end.png'); b.close()
OV = [Image.open(f'{B}/ov{i}.png').convert('RGBA') for i in range(len(SC))]
ENDIMG = Image.open(f'{B}/end.png').convert('RGB')

# ---------- scene art ----------
def city(lit_frac):
    """returns (lit, dark) skyline images of size W x AH with identical layout"""
    random.seed(11)
    im_l = Image.new('RGB', (W, AH)); im_d = Image.new('RGB', (W, AH))
    for img, top, bot in [(im_l, (11, 26, 61), (27, 58, 123)), (im_d, (8, 18, 44), (14, 29, 64))]:
        d = ImageDraw.Draw(img)
        for y in range(AH):
            t = y / AH; d.line([(0, y), (W, y)], fill=tuple(int(top[c] + (bot[c] - top[c]) * t) for c in range(3)))
    dl, dd = ImageDraw.Draw(im_l), ImageDraw.Draw(im_d)
    for _ in range(80):
        x, y, r = random.randint(0, W), random.randint(0, int(AH * .45)), random.choice([1.5, 2, 2.5])
        for d in (dl, dd): d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))
    for d, bg in ((dl, (11, 26, 61)), (dd, (8, 18, 44))):
        d.ellipse([820, 90, 940, 210], fill=(243, 239, 224)); d.ellipse([846, 72, 962, 188], fill=bg)
    wins = []
    x = 0
    while x < W:
        w = random.randint(90, 170); h = random.randint(int(AH * .28), int(AH * .56)); y = AH - h
        for d in (dl, dd): d.rectangle([x, y, x + w - 8, AH], fill=(8, 20, 48))
        for wy in range(y + 24, AH - 30, 46):
            for wx in range(x + 16, x + w - 30, 34):
                on = random.random() < lit_frac
                wins.append((wx, wy, on))
        x += w
    for wx, wy, on in wins:
        dd.rounded_rectangle([wx, wy, wx + 18, wy + 24], 2, fill=(22, 38, 77))
        dl.rounded_rectangle([wx, wy, wx + 18, wy + 24], 2, fill=(255, 210, 122) if on else (22, 38, 77))
    return im_l, im_d
CITY_L, CITY_D = city(0.62)

def car_sprite(sc):
    s = Image.new('RGBA', (200, 140), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    d.polygon([(40, 70), (50, 44), (80, 40), (125, 40), (150, 44), (163, 64), (169, 72), (161, 82), (44, 82)], fill=(222, 84, 74))
    d.polygon([(83, 42), (97, 26), (127, 26), (141, 42)], fill=(198, 198, 198))
    d.ellipse([62, 75, 80, 93], fill=(17, 17, 17)); d.ellipse([132, 75, 150, 93], fill=(17, 17, 17))
    return s.resize((int(200 * sc), int(140 * sc)), Image.LANCZOS)

def showroom():
    im = Image.new('RGB', (W, AH)); d = ImageDraw.Draw(im)
    fy = int(AH * .74)
    for y in range(AH):
        if y < fy:
            t = y / fy; c = tuple(int(a + (b - a) * t) for a, b in zip((236, 239, 245), (214, 220, 230)))
        else:
            t = (y - fy) / (AH - fy); c = tuple(int(a + (b - a) * t) for a, b in zip((196, 203, 215), (170, 178, 192)))
        d.line([(0, y), (W, y)], fill=c)
    d.line([(0, fy), (W, fy)], fill=(160, 168, 182), width=3)
    for x in range(-200, W + 200, 160):  # floor perspective lines
        d.line([(W / 2 + (x - W / 2) * 0.35, fy), (x, AH)], fill=(185, 192, 205), width=2)
    return im, fy
ROOM, FLOOR = showroom()

PH_ = int(AH * (0.46 if tall else 0.50))      # product height on screen
PROD = prod.resize((int(prod.width * PH_ / prod.height), PH_), Image.LANCZOS)
PW_ = PROD.width
REFL = PROD.transpose(Image.FLIP_TOP_BOTTOM)
ra = REFL.getchannel('A').point(lambda v: int(v * 0.16)); REFL.putalpha(ra)
REFL = REFL.crop((0, 0, PW_, int(PH_ * 0.35)))

def flames(t, power):
    """flame sprite to sit under the product; power 0..1"""
    fw, fh = PW_, int(PH_ * 0.55)
    s = Image.new('RGBA', (fw, fh), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    for cx in (fw * 0.28, fw * 0.72):
        L = fh * (0.55 + 0.35 * power) * (0.85 + 0.15 * math.sin(t * 47 + cx))
        wid = fw * 0.11
        d.polygon([(cx - wid, 0), (cx + wid, 0), (cx, L)], fill=(255, 140, 50, 230))
        d.polygon([(cx - wid * .55, 0), (cx + wid * .55, 0), (cx, L * .62)], fill=(255, 220, 120, 245))
        d.polygon([(cx - wid * .25, 0), (cx + wid * .25, 0), (cx, L * .3)], fill=(255, 255, 230, 255))
    glow = s.filter(ImageFilter.GaussianBlur(18))
    return Image.alpha_composite(glow, s)

def sprite(t, power):
    """product with optional flames below, as one RGBA sprite (for rotation)"""
    if power <= 0: return PROD.copy(), 0
    fl = flames(t, power)
    sp = Image.new('RGBA', (PW_, PH_ + fl.height - 10), (0, 0, 0, 0))
    sp.alpha_composite(fl, (0, PH_ - 10)); sp.alpha_composite(PROD, (0, 0))
    return sp, fl.height - 10

def paste_rot(base, sp, cx, cy, ang):
    r = sp.rotate(ang, resample=Image.BICUBIC, expand=True)
    base.alpha_composite(r, (int(cx - r.width / 2), int(cy - r.height / 2)))

def shadow(base, cx, y, scale, alpha):
    sh = Image.new('RGBA', (W, AH), (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    w = PW_ * 0.62 * scale; h = 26 * scale
    d.ellipse([cx - w, y - h, cx + w, y + h], fill=(20, 30, 50, int(alpha)))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))

ease = lambda x: 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, x)))
def frame(si, t, T):
    kind = SC[si]['kind']; u = t / T
    if kind == 'city_cars':
        base = CITY_L.copy().convert('RGBA')
        for k, (y, sc, sp) in enumerate([(0.22, 1.2, 300), (0.12, 0.8, 220), (0.32, 0.6, 170)]):
            c = car_sprite(sc); x = (-c.width + (t * sp + k * 420)) % (W + c.width * 2) - c.width
            fl = Image.new('RGBA', (c.width, int(c.height * .7)), (0, 0, 0, 0)); d = ImageDraw.Draw(fl)
            for fx in (0.33, 0.73):
                L = c.height * .55 * (0.8 + 0.2 * math.sin(t * 40 + k + fx * 9))
                d.polygon([(c.width * fx - 8 * sc, 0), (c.width * fx + 8 * sc, 0), (c.width * fx, L)], fill=(255, 179, 71, 240))
            yy = int(AH * y + 6 * math.sin(t * 3 + k))
            base.alpha_composite(fl, (int(x), yy + int(c.height * .62))); base.alpha_composite(c, (int(x), yy))
        return base.convert('RGB')
    base = ROOM.copy().convert('RGBA')
    if kind == 'idle':
        cx = W * 0.5; wob = 2.5 * math.sin(t * 6) if u > 0.45 else 0
        base.alpha_composite(REFL, (int(cx - PW_ / 2), FLOOR + 4))
        shadow(base, cx, FLOOR + 6, 1, 110)
        paste_rot(base, PROD, cx, FLOOR - PH_ / 2, wob)
        if u > 0.45:  # "!" pop
            d = ImageDraw.Draw(base); s = min(1, (u - 0.45) * 6)
            x0, y0 = cx + PW_ * 0.5, FLOOR - PH_ - 40
            d.ellipse([x0 - 46 * s, y0 - 46 * s, x0 + 46 * s, y0 + 46 * s], fill=(222, 84, 74))
            if s > .6:
                d.rectangle([x0 - 7, y0 - 28, x0 + 7, y0 + 8], fill=(255, 255, 255)); d.ellipse([x0 - 8, y0 + 16, x0 + 8, y0 + 32], fill=(255, 255, 255))
        return base.convert('RGB')
    if kind == 'slide':
        p = ease(min(1, u / 0.8)); x = -PW_ + p * (W * 0.5 + PW_)
        ang = -10 * math.sin(math.pi * p) if p < 1 else 0
        d = ImageDraw.Draw(base)
        if p < 0.98:
            random.seed(int(t * 20))
            for _ in range(9):
                yy = FLOOR - random.uniform(0.05, 0.95) * PH_; L = random.uniform(120, 320)
                d.line([(x - PW_ / 2 - L - 30, yy), (x - PW_ / 2 - 30, yy)], fill=(150, 160, 178), width=random.choice([3, 4, 6]))
            for k in range(5):  # dust
                r = 18 + k * 9 + p * 40
                dx = x - PW_ * 0.45 - k * 50
                d.ellipse([dx - r, FLOOR - r * .6, dx + r, FLOOR + r * .4], fill=(205, 210, 220))
        shadow(base, x, FLOOR + 6, 1, 110)
        paste_rot(base, PROD, x, FLOOR - PH_ / 2, ang)
        return base.convert('RGB')
    if kind == 'liftoff':
        cx = W * 0.5
        power = min(1, u / 0.18)
        rise = ease((u - 0.18) / 0.82) if u > 0.18 else 0
        cy = FLOOR - PH_ / 2 - rise * (AH * 1.15)
        jit = 3 * math.sin(t * 80) if u < 0.18 else 0
        ang = -360 * ease((u - 0.38) / 0.4) if u > 0.38 else 0
        shadow(base, cx, FLOOR + 6, max(0.3, 1 - rise), 110 * max(0.2, 1 - rise))
        if rise < 0.2:  # floor glow
            g = Image.new('RGBA', (W, AH), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse([cx - 260, FLOOR - 30, cx + 260, FLOOR + 50], fill=(255, 170, 80, int(140 * power)))
            base.alpha_composite(g.filter(ImageFilter.GaussianBlur(30)))
        sp, fh = sprite(t, power)
        paste_rot(base, sp, cx + jit, cy + fh / 2, ang)
        return base.convert('RGB')
    if kind == 'fly_city':
        p = u; x = -PW_ + p * (W + 2 * PW_ * 0.8); y = AH * 0.30 + 30 * math.sin(t * 2.5)
        base = CITY_D.copy()
        mask = Image.new('L', (W, AH), 0); ImageDraw.Draw(mask).rectangle([0, 0, max(0, int(x)), AH], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(40))
        base = Image.composite(CITY_L, base, mask).convert('RGBA')
        sc = 0.62
        sp, fh = sprite(t, 0.9)
        sp = sp.resize((int(sp.width * sc), int(sp.height * sc)), Image.LANCZOS)
        paste_rot(base, sp, x, y, -12)
        return base.convert('RGB')
    if kind == 'land':
        cx = W * 0.5
        dropu = min(1, u / 0.35)
        yb = (FLOOR - PH_ / 2)
        if dropu < 1:
            cy = -PH_ + (yb + PH_) * (dropu ** 2); power = 0.8
        else:
            b2 = (u - 0.35) / 0.15; cy = yb - (18 * math.sin(math.pi * b2) if b2 < 1 else 0); power = 0
        shadow(base, cx, FLOOR + 6, 0.4 + 0.6 * dropu, 110 * dropu)
        if power == 0: base.alpha_composite(REFL, (int(cx - PW_ / 2), FLOOR + 4))
        sp, fh = sprite(t, power)
        paste_rot(base, sp, cx, cy + fh / 2, 0)
        if 0.35 < u < 0.55:  # landing dust
            d = ImageDraw.Draw(base); s = (u - 0.35) / 0.2
            for side in (-1, 1):
                for k in range(4):
                    r = 20 + 30 * s + k * 6; dx = cx + side * (PW_ * 0.5 + 30 + k * 40 * s)
                    d.ellipse([dx - r, FLOOR - r * .6, dx + r, FLOOR + r * .3], fill=(205, 210, 220, int(220 * (1 - s))))
        return base.convert('RGB')

# ---------- render ----------
silent = f'{B}/silent.mp4'
proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                         '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p', '-g', '60', silent], stdin=subprocess.PIPE)
CANVAS_BG = (27, 58, 123)
for si in range(len(SC)):
    n = int(round(dur[si] * FPS))
    for f in range(n):
        t = f / FPS
        art = frame(si, t, dur[si])
        fr = Image.new('RGBA', (W, H), CANVAS_BG + (255,))
        fr.paste(art, (0, AY0))
        fr.alpha_composite(OV[si])
        fade = min(1, f / 6, (n - 1 - f) / 6)
        out = fr.convert('RGB')
        if fade < 1: out = Image.blend(Image.new('RGB', (W, H), CANVAS_BG), out, max(0, fade))
        proc.stdin.write(out.tobytes())
n = int(round(dur[-1] * FPS))
for f in range(n):
    fade = min(1, f / 9)
    out = Image.blend(Image.new('RGB', (W, H), CANVAS_BG), ENDIMG, fade) if fade < 1 else ENDIMG
    proc.stdin.write(out.tobytes())
proc.stdin.close(); proc.wait()

# ---------- audio: voice + whooshes + thruster rumble ----------
SR = 48000; N = int(TOTAL * SR) + SR
mix = np.zeros(N)
import scipy.signal as sg
def put(sig, at): i = int(at * SR); mix[i:i + len(sig)] += sig[:max(0, N - i)]
rng = np.random.default_rng(3)
def whoosh(d, f0, f1, g):
    n = int(d * SR); noise = rng.standard_normal(n); out = np.zeros(n); blk = 1024
    for s in range(0, n, blk):
        fc = f0 + (f1 - f0) * (s / n); b, a = sg.butter(2, [max(80, fc * 0.6) / (SR / 2), min(fc * 1.6, 20000) / (SR / 2)], 'band')
        out[s:s + blk] = sg.lfilter(b, a, noise[s:s + blk])
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    return out * env * g
def rumble(d, g):
    n = int(d * SR); b, a = sg.butter(2, 220 / (SR / 2)); out = sg.lfilter(b, a, rng.standard_normal(n))
    env = np.minimum(1, np.linspace(0, 6, n)) * np.minimum(1, np.linspace(6, 0, n))
    return out * env * g
ks = [s['kind'] for s in SC]
put(whoosh(1.2, 400, 2500, 0.10), starts[ks.index('slide')] + 0.2)
put(rumble(dur[ks.index('liftoff')] - 0.2, 0.25), starts[ks.index('liftoff')] + 0.1)
put(whoosh(1.0, 600, 3500, 0.12), starts[ks.index('liftoff')] + dur[ks.index('liftoff')] * 0.35)
put(rumble(dur[ks.index('fly_city')], 0.15), starts[ks.index('fly_city')])
put(whoosh(1.5, 3000, 500, 0.08), starts[ks.index('fly_city')] + 0.5)
put(whoosh(0.8, 2500, 300, 0.10), starts[ks.index('land')])
sfx = f'{B}/sfx.wav'; sf.write(sfx, (mix / max(1e-9, np.abs(mix).max()) * 0.5).astype(np.float32), SR)
starts_all = starts + [starts[-1] + dur[-2]]
ins = []; fc = ''; tags = ''
for i in range(len(lines)):
    ins += ['-i', f'{vo_dir}/{i}.wav']; ms = int((starts_all[i] + 0.25) * 1000)
    fc += f'[{i+2}:a]aresample=48000,adelay={ms}|{ms}[a{i}];'; tags += f'[a{i}]'
fc += f'[1:a]volume=0.55[s];{tags}[s]amix=inputs={len(lines)+1}:normalize=0,pan=stereo|c0=c0|c1=c0,loudnorm=I=-15:TP=-1.5,aresample=48000[a]'
out = f'{OUTDIR}/eementor-reel-flystunt-v3-1080x{H}.mp4'
ff(['-i', silent, '-i', sfx] + ins + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-t', f'{TOTAL:.2f}', '-c:v', 'copy', '-c:a', 'aac', '-ar', '48000', '-b:a', '192k', '-movflags', '+faststart', out])
json.dump({'durations': dur, 'starts': starts_all, 'end': TOTAL}, open(f'{B}/timing.json', 'w'))
print(out, round(TOTAL, 2))
