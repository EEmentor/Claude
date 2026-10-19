import random, subprocess
from playwright.sync_api import sync_playwright
def sky(lit, cars, bulb=False):
    random.seed(7); W=1080; H=1080
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1A3D"/><stop offset="1" stop-color="{"#1B3A7B" if lit else "#0E1D40"}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#g)"/>'
    for i in range(70):
        s+=f'<circle cx="{random.randint(0,W)}" cy="{random.randint(0,520)}" r="{random.choice([1.5,2,2.5])}" fill="#fff" opacity="{random.uniform(.3,.9):.2f}"/>'
    s+='<circle cx="860" cy="170" r="62" fill="#F3EFE0"/><circle cx="884" cy="152" r="58" fill="url(#g)"/>'
    x=0
    while x<W:
        w=random.randint(90,170); h=random.randint(260,620); y=H-h
        s+=f'<rect x="{x}" y="{y}" width="{w-8}" height="{h}" fill="#081430"/>'
        for wy in range(y+24,H-30,46):
            for wx in range(x+16,x+w-30,34):
                on = lit and random.random()<.62
                s+=f'<rect x="{wx}" y="{wy}" width="18" height="24" rx="2" fill="{"#FFD27A" if on else "#16264D"}" opacity="{0.95 if on else 1}"/>'
        x+=w
    for cx,cy,sc in cars:
        s+=f'''<g transform="translate({cx},{cy}) scale({sc})"><path d="M-60 0 Q-55 -22 -25 -26 L20 -26 Q45 -24 58 -6 L64 2 Q64 10 56 12 L-56 12 Q-64 10 -60 0Z" fill="#DE544A"/>
<path d="M-22 -24 L-8 -40 L22 -40 L36 -24Z" fill="#C6C6C6"/><circle cx="-34" cy="14" r="9" fill="#111"/><circle cx="36" cy="14" r="9" fill="#111"/>
<path d="M-42 22 L-34 50 L-26 22Z" fill="#FFB347"/><path d="M28 22 L36 50 L44 22Z" fill="#FFB347"/></g>'''
    if bulb:
        s+='''<g transform="translate(540,470)"><circle r="150" fill="#000" opacity=".35"/><path d="M-55 10 A70 70 0 1 1 55 10 Q40 30 38 58 L-38 58 Q-40 30 -55 10Z" fill="#2A3557" stroke="#C6C6C6" stroke-width="6"/>
<rect x="-34" y="66" width="68" height="14" rx="4" fill="#C6C6C6"/><rect x="-28" y="86" width="56" height="12" rx="4" fill="#C6C6C6"/>
<line x1="-95" y1="-95" x2="95" y2="95" stroke="#DE544A" stroke-width="14" stroke-linecap="round"/></g>'''
    return s+'</svg>'
imgs={'sky_lit.png':sky(True,[(300,330,1.3),(720,250,0.9),(520,420,0.7)]),'sky_dark.png':sky(False,[(300,330,1.3),(720,250,0.9)],bulb=True)}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1080})
    for n,svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.screenshot(path=f'/home/claude/claude/fetch/out/fly_{n}')
    b.close()
print('ok')
