"""Photo reel builder: python3 build.py <reel> <H>  (H=1920 or 1350)"""
import sys, os, subprocess, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from specs import REELS
from PIL import Image
from playwright.sync_api import sync_playwright

NAME, H = sys.argv[1], int(sys.argv[2]); tall = H > 1500
R = REELS[NAME]
HERE = os.path.dirname(os.path.abspath(__file__))
PH = '/home/claude/claude/fetch/out'
KIT = '/home/claude/claude/brand-kit'
TTS = '/tmp/claude-0/-home-claude-claude/597a0b6c-e239-5cf6-a538-974de408a6fe/scratchpad/tts'
B = f'{HERE}/{NAME}_{H}'; os.makedirs(B, exist_ok=True)
for f in ['logo_energy.png', 'style.css'] + [x for x in os.listdir(KIT) if x.endswith('.woff2')]:
    subprocess.run(['cp', f'{KIT}/{f}', B])
HD = 150 if tall else 118
PY, PW, PHh = (HD + 170, 1080, 1080) if tall else (HD, 1080, 800)   # photo window
FS = 76 if tall else 58
FPS = 30

def ff(a): subprocess.run(['ffmpeg', '-v', 'error', '-y'] + a, check=True)

# ---------- voice-over (cached per reel, shared by both sizes) ----------
vo_dir = f'{HERE}/{NAME}_vo'; os.makedirs(vo_dir, exist_ok=True)
lines = [s['vo'] for s in R['scenes']] + [R['end_vo']]
durs = []
need = any(not os.path.exists(f'{vo_dir}/{i}.wav') for i in range(len(lines)))
if need:
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(f'{TTS}/kokoro-v1.0.onnx', f'{TTS}/voices-v1.0.bin')
    for i, t in enumerate(lines):
        a, sr = k.create(t, voice='am_puck', speed=1.15, lang='en-us'); sf.write(f'{vo_dir}/{i}.wav', a, sr)
import soundfile as sf
for i in range(len(lines)):
    d = sf.info(f'{vo_dir}/{i}.wav'); durs.append(d.frames / d.samplerate)
sd = [max(2.6, round(d + 0.7, 2)) for d in durs]; sd[0] = max(sd[0], 2.4)
sd[-1] = max(sd[-1] + 0.6, 3.6)

# ---------- HTML overlays ----------
exec(open(f'{KIT}/template_bms_carousel.py').read().split('def page(')[0].replace('S=sys.argv[1]', ''))
def header(): return f'<div style="position:absolute;left:0;right:0;top:0;height:{HD-6}px;background:#fff;display:flex;align-items:center;padding-left:64px;border-bottom:6px solid #DE544A;z-index:3"><img src="logo_energy.png" style="height:{int(HD*.58)}px"></div>'
def page(body, bg='transparent'):
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>body{{background:{bg}}}</style></head><body><div style="position:relative;width:1080px;height:{H}px;overflow:hidden">{body}<div class="bar" style="z-index:4"></div></div></body></html>'
CAP_TOP = PY + PHh
def bg_scene(sc, idx, n):
    # static frame: blue background, header, top band, caption area (photo window left transparent)
    band = ''
    if tall:
        band = f'<div style="position:absolute;left:64px;right:64px;top:{HD+52}px;display:flex;justify-content:space-between;align-items:center"><div class="kicker" style="font-size:30px">{sc["k"]}</div><div style="font-size:24px;color:#C6C6C6;font-weight:500">{idx}/{n}</div></div>'
    kick = '' if tall else f'<div class="kicker" style="font-size:24px;margin-bottom:8px">{sc["k"]}</div>'
    sub = f'<p style="font-size:{int(FS*.44)}px;margin-top:16px;color:#EAEAEA">{sc["s"]}</p>' if sc['s'] else ''
    cap = f'<div style="position:absolute;left:64px;right:64px;top:{CAP_TOP+(56 if tall else 34)}px">{kick}<h2 style="font-size:{FS}px">{sc["h"]}</h2>{sub}</div>'
    return page(f'<div class="frame" style="position:absolute;inset:0"><div class="arcs" style="top:{H-700}px"></div></div>{header()}{band}<div style="position:absolute;left:0;top:{PY}px;width:{PW}px;height:{PHh}px;background:#000"></div>{cap}')
def end_card():
    chips = ''.join(f'<span class="chip" style="font-size:{26 if tall else 21}px;margin:6px">{c}</span>' for c in R['end_chips'])
    ih = 640 if tall else 400
    return page(f'''<div class="frame" style="position:absolute;inset:0"><div class="arcs" style="top:-200px"></div></div>{header()}
<div style="position:absolute;left:0;right:0;top:{HD}px;bottom:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 60px">
<div class="kicker" style="font-size:{30 if tall else 24}px">{R["end_kicker"]}</div>
<h1 style="font-size:{88 if tall else 66}px;margin-top:14px">{R["end_h"]}</h1>
<img src="end.jpg" style="height:{ih}px;margin-top:{36 if tall else 18}px;border-radius:18px;box-shadow:0 16px 44px rgba(0,0,0,.45)">
<div style="margin-top:{26 if tall else 14}px;display:flex;flex-wrap:wrap;justify-content:center">{chips}</div>
<div style="margin-top:{30 if tall else 16}px"><span class="btn" style="font-size:{32 if tall else 25}px;padding:22px 52px">{R["button"]}</span></div>
<div style="margin-top:{26 if tall else 14}px;font-size:{27 if tall else 22}px">{R["url"]}</div>
{f'<div style="margin-top:12px;font-size:{22 if tall else 18}px;color:#C6C6C6">{R["note"]}</div>' if R.get("note") else ''}</div>''', '#1B3A7B')

im = Image.open(f'{PH}/{R["end_img"]}').convert('RGB')
if abs(im.width/im.height-1) > 0.6:
    from PIL import ImageFilter
    s_ = max(im.size); bgi = im.resize((s_, s_)).filter(ImageFilter.GaussianBlur(40)); bgi.paste(im, ((s_-im.width)//2, (s_-im.height)//2)); im = bgi
if im.width != im.height:
    s_ = min(im.size); im = im.crop(((im.width-s_)//2, (im.height-s_)//2+0, (im.width+s_)//2, (im.height+s_)//2))
im.resize((900, 900), Image.LANCZOS).save(f'{B}/end.jpg', quality=92)

n = len(R['scenes'])
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': H})
    for i, sc in enumerate(R['scenes']):
        open(f'{B}/bg{i}.html', 'w').write(bg_scene(sc, i+1, n))
        pg.goto(f'file://{B}/bg{i}.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(250)
        pg.screenshot(path=f'{B}/bg{i}.png')
    open(f'{B}/end.html', 'w').write(end_card()); pg.goto(f'file://{B}/end.html'); pg.wait_for_timeout(300)
    pg.screenshot(path=f'{B}/end.png')
    b.close()

# ---------- photo windows with slow push / pan ----------
def prep(img):
    im0 = Image.open(f'{PH}/{img}')
    if im0.mode in ('RGBA', 'LA', 'P'):
        im0 = im0.convert('RGBA'); base = Image.new('RGBA', im0.size, (233, 236, 242, 255)); base.alpha_composite(im0); im = base.convert('RGB')
    else:
        im = im0.convert('RGB')
    CROP = {'lipo_unwrapped.jpg': (0, 0, 1, .885), 'li_open_52v.jpg': (0, 0, 1, .89), 'li_exploded_52v.jpg': (0, 0, 1, .89), 'connectors.jpg': (0, .09, 1, 1)}
    if img in CROP:
        a = CROP[img]; im = im.crop((int(a[0]*im.width), int(a[1]*im.height), int(a[2]*im.width), int(a[3]*im.height)))
    tw, th = PW*2, PHh*2
    import math
    from PIL import ImageFilter
    if abs(math.log((im.width/im.height)/(tw/th))) > 0.15:
        sc = max(tw/im.width, th/im.height); bg = im.resize((int(im.width*sc)+1, int(im.height*sc)+1), Image.LANCZOS)
        l = (bg.width-tw)//2; t = (bg.height-th)//2
        bg = bg.crop((l, t, l+tw, t+th)).filter(ImageFilter.GaussianBlur(40))
        from PIL import ImageEnhance
        bg = ImageEnhance.Brightness(bg).enhance(0.85)
        sc = min(tw/im.width, th/im.height)*0.96; fg = im.resize((int(im.width*sc), int(im.height*sc)), Image.LANCZOS)
        bg.paste(fg, ((tw-fg.width)//2, (th-fg.height)//2)); bg.save(f'{B}/win_{img}.png')
    else:
        sc = max(tw/im.width, th/im.height); im = im.resize((int(im.width*sc)+1, int(im.height*sc)+1), Image.LANCZOS)
        l = (im.width-tw)//2; t = (im.height-th)//2
        im.crop((l, t, l+tw, t+th)).save(f'{B}/win_{img}.png')
    return f'{B}/win_{img}.png'
segs = []
for i, sc in enumerate(R['scenes']):
    d = sd[i]; nf = int(d*FPS)
    w = prep(sc['img'])
    moves = ["zoom='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
             "zoom='1.06-0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
             "zoom='1.05':x='(iw-iw/zoom)*on/{n}':y='ih/2-(ih/zoom/2)'"]
    mv = moves[i % 3].format(n=nf)
    ff(['-loop', '1', '-i', w, '-i', f'{B}/bg{i}.png', '-filter_complex',
        f'[0:v]zoompan={mv}:d={nf}:s={PW}x{PHh}:fps={FPS},setsar=1[ph];[1:v][ph]overlay=0:{PY}[o];[o]fade=t=in:d=0.25,fade=t=out:st={d-0.25}:d=0.25[out]',
        '-map', '[out]', '-frames:v', str(nf), '-r', str(FPS), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', f'{B}/s{i}.mp4'])
    segs.append(f'{B}/s{i}.mp4')
de = sd[-1]
ff(['-loop', '1', '-i', f'{B}/end.png', '-vf', 'fade=t=in:d=0.3', '-t', str(de), '-r', str(FPS), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', f'{B}/send.mp4'])
segs.append(f'{B}/send.mp4')
open(f'{B}/list.txt', 'w').write(''.join(f"file '{s}'\n" for s in segs))
ff(['-f', 'concat', '-safe', '0', '-i', f'{B}/list.txt', '-c', 'copy', f'{B}/silent.mp4'])
starts = []; t = 0
for x in sd: starts.append(t); t += x
END = t
ins = []; fc = ''; mix = ''
for i in range(len(lines)):
    ins += ['-i', f'{vo_dir}/{i}.wav']; ms = int((starts[i]+0.25)*1000)
    fc += f'[{i+1}:a]aresample=48000,adelay={ms}|{ms}[a{i}];'; mix += f'[a{i}]'
out = f'{HERE}/eementor-reel-{NAME}-1080x{H}.mp4'
ff(['-i', f'{B}/silent.mp4'] + ins + ['-filter_complex', fc + mix + f'amix=inputs={len(lines)}:normalize=0,pan=stereo|c0=c0|c1=c0,loudnorm=I=-15:TP=-1.5[a]',
    '-map', '0:v', '-map', '[a]', '-t', str(END), '-c:v', 'copy', '-c:a', 'aac', '-ar', '48000', '-b:a', '192k', '-movflags', '+faststart', out])
json.dump({'durations': sd, 'starts': starts, 'end': END}, open(f'{B}/timing.json', 'w'))
print(out, round(END, 2))
