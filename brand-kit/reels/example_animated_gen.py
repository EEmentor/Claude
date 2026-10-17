import sys
H=int(sys.argv[1]); out=sys.argv[2]
tall=H>1500
S=[0,3.2,9.6,14.0,18.3,21.6,25.7]; END=29.2
HD=150 if tall else 118
SC=1.15 if tall else 0.74   # stage scale
CY=HD+(70 if tall else 36)
FS=78 if tall else 60
STAGE_Y=HD+(470 if tall else 330)
STAGE_H=1000
B='#1B3A7B';R='#DE544A'
def scene(i,inner,last=False):
    d=(END if last else S[i+1])-S[i]
    anim='sceneLast' if last else 'scene'
    return f'<div class="sc" style="animation:{anim} {d}s linear {S[i]}s both">{inner}</div>'
def cap(k,h,sub=''):
    s=f'<div style="position:absolute;left:64px;right:64px;top:{CY}px"><div class="kicker" style="font-size:{int(FS*.42)}px;margin-bottom:10px">{k}</div><h2 style="font-size:{FS}px">{h}</h2>'
    if sub: s+=f'<p style="font-size:{int(FS*.42)}px;margin-top:16px;color:#EAEAEA">{sub}</p>'
    return s+'</div>'
def stage(svg): return f'<div style="position:absolute;left:0;right:0;top:{STAGE_Y}px;height:{STAGE_H}px;display:flex;justify-content:center;transform:scale({SC});transform-origin:top center">{svg}</div>'
def a(name,dur,delay,extra=''): return f'animation:{name} {dur}s ease-out {delay}s both {extra}'
def unit(x,y,mods=4,anim_base=None,glow=False):
    # all-in-one: inverter head + module stack
    s=f'<g transform="translate({x},{y})">'
    s+=f'<rect x="0" y="0" width="300" height="190" rx="18" fill="#F4F6FB" stroke="#C6C6C6" stroke-width="3"/>'
    s+=f'<rect x="30" y="34" width="120" height="64" rx="8" fill="#0E1E44"/><rect x="42" y="46" width="60" height="10" rx="3" fill="#6FE3A6"/><rect x="42" y="64" width="90" height="8" rx="3" fill="#8C9BCB"/><rect x="42" y="78" width="70" height="8" rx="3" fill="#8C9BCB"/>'
    s+=f'<circle cx="250" cy="66" r="12" fill="{R}"/><text x="150" y="160" text-anchor="middle" font-size="22" font-weight="600" fill="{B}">INVERTER 5 kW</text>'
    for m in range(mods):
        st=f'style="{a("slideIn",.6,anim_base+0.5+m*1.1)}"' if anim_base is not None else ''
        s+=f'<g {st}><rect x="0" y="{205+m*118}" width="300" height="108" rx="14" fill="#fff" stroke="#C6C6C6" stroke-width="3"/><rect x="24" y="{205+m*118+44}" width="150" height="20" rx="6" fill="#EAEAEA"/><rect x="24" y="{205+m*118+44}" width="150" height="20" rx="6" fill="#4CC38A" style="transform-box:fill-box;transform-origin:left;{a("fillBar",.8,(anim_base or 0)+1.0+m*1.1)}"/><text x="276" y="{205+m*118+64}" text-anchor="end" font-size="22" font-weight="600" fill="{B}">5.12 kWh</text></g>'
    return s+'</g>'
house=lambda x,y,win_anim: f'''<g transform="translate({x},{y})"><path d="M0 170 L170 30 L340 170 V400 H0 Z" fill="#26558C" stroke="#fff" stroke-width="4"/>
<rect x="40" y="200" width="90" height="80" rx="6" fill="#FFD36A" style="{win_anim}"/><rect x="210" y="200" width="90" height="80" rx="6" fill="#FFD36A" style="{win_anim}"/>
<rect x="135" y="290" width="70" height="110" rx="6" fill="#1B3A7B" stroke="#fff" stroke-width="3"/></g>'''
# scenes
s1=cap('Home energy storage','<span style="'+a('fadeUp',.5,S[0]+0.3)+';display:inline-block">Power cut?</span><br><span style="'+a('fadeUp',.5,S[0]+1.6)+';display:inline-block">Your home <em>keeps running</em></span>')+stage(f'''<svg width="900" height="900" viewBox="0 0 900 900">
<circle cx="760" cy="120" r="60" fill="#EAEAEA" opacity=".25"/>
<g stroke="#C6C6C6" stroke-width="5"><line x1="80" y1="760" x2="80" y2="300"/><line x1="40" y1="330" x2="120" y2="330"/></g>
<path d="M80 330 Q180 360 250 460" stroke="#C6C6C6" stroke-width="4" fill="none" style="{a('lineCut',1.2,S[0]+0.6)}"/>
{house(200,380,a('flicker',1.6,S[0]+0.5))}
<g transform="translate(610,470) scale(.9)">{unit(0,0,2)}</g>
<line x1="560" y1="660" x2="610" y2="660" stroke="{R}" stroke-width="6" style="{a('fadeIn',.3,S[0]+1.5)}"/>
<path d="M560 560 l-30 60 h30 l-20 60 l60 -80 h-30 l20 -40 z" fill="{R}" style="{a('fadeIn',.3,S[0]+0.9)}"/>
</svg>''')
counter=''.join(f'<text x="450" y="80" text-anchor="middle" font-size="110" font-weight="600" fill="#fff" style="{a("countStep",1.1,S[1]+0.5+i*1.1)}">{v} kWh</text>' for i,v in enumerate(['5','10','15','20']))
s2=cap('All-in-One ESS with inverter','Plug-in modules,<br><em>5–20 <span style="text-transform:none">kWh</span></em>','Battery modules of 51.2 V · 100 Ah · 5.12 kWh each')+stage(f'''<svg width="900" height="1100" viewBox="0 0 900 1100">{counter}{unit(300,150,4,S[1])}</svg>''')
flow=lambda d,delay: f'<path d="{d}" stroke="#FFD36A" stroke-width="8" fill="none" stroke-dasharray="18 16" style="{a("flow",1.2,delay,"infinite linear")}"/>'
s3=cap('Solar ready','Built-in <em>5 <span style="text-transform:none">kW</span></em><br>inverter','Solar input up to 5200 W · 230 V pure sine wave output')+stage(f'''<svg width="900" height="1100" viewBox="0 0 900 1100">
<g style="{a('fadeIn',.5,S[2]+0.2)}"><circle cx="140" cy="120" r="70" fill="#FFD36A"/>{''.join(f'<line x1="{140+95*__import__("math").cos(t)}" y1="{120+95*__import__("math").sin(t)}" x2="{140+125*__import__("math").cos(t)}" y2="{120+125*__import__("math").sin(t)}" stroke="#FFD36A" stroke-width="8" stroke-linecap="round"/>' for t in [i*0.785 for i in range(8)])}</g>
<g transform="translate(330,90) skewX(-12)" style="{a('fadeIn',.5,S[2]+0.5)}"><rect width="420" height="200" fill="#0E2A66" stroke="#fff" stroke-width="4"/>{''.join(f'<line x1="{i*84}" y1="0" x2="{i*84}" y2="200" stroke="#8C9BCB" stroke-width="2"/>' for i in range(1,5))}<line x1="0" y1="100" x2="420" y2="100" stroke="#8C9BCB" stroke-width="2"/></g>
{flow('M560 300 V420 H450 V470',S[2]+1.0)}
{unit(300,470,3)}
{flow('M600 700 H760',S[2]+1.8)}
<text x="760" y="680" font-size="28" fill="#fff" font-weight="500" style="{a('fadeIn',.4,S[2]+1.8)}">230 V AC</text>
</svg>''')
s4=cap('Seamless backup','Switches over in<br>about <em>10 <span style="text-transform:none">ms</span></em>','Your lights and devices stay on')+stage(f'''<svg width="900" height="1100" viewBox="0 0 900 1100">
<g stroke="#C6C6C6" stroke-width="5" fill="none"><path d="M60 620 L110 300 L160 620 M80 420 H140 M70 500 H150"/></g>
<line x1="160" y1="330" x2="420" y2="430" stroke="#C6C6C6" stroke-width="5" style="{a('lineCut',1,S[3]+0.6)}"/>
<text x="290" y="300" text-anchor="middle" font-size="80" fill="{R}" font-weight="700" style="{a('popX',.4,S[3]+0.9)}">✕</text>
{house(420,300,'')}
<text x="450" y="150" text-anchor="middle" font-size="150" font-weight="700" fill="#fff" style="{a('fadeUp',.5,S[3]+1.4)}">10 <tspan fill="{R}">ms</tspan></text>
<path d="M590 780 V860" stroke="{R}" stroke-width="8" style="{a('fadeIn',.3,S[3]+1.6)}"/>
<g transform="translate(450,860)"><rect x="0" y="0" width="300" height="110" rx="14" fill="#F4F6FB" stroke="#C6C6C6" stroke-width="3"/><text x="150" y="68" text-anchor="middle" font-size="30" font-weight="600" fill="{B}">ESS ON</text></g>
</svg>''')
circ=2*3.14159*150
s5=cap('Smart control','<em>Cloud</em> monitoring','Check your system from your phone')+stage(f'''<svg width="900" height="1100" viewBox="0 0 900 1100">
<rect x="270" y="20" width="360" height="720" rx="50" fill="#0E1E44" stroke="#fff" stroke-width="6"/><rect x="390" y="44" width="120" height="16" rx="8" fill="#26558C"/>
<circle cx="450" cy="300" r="150" fill="none" stroke="#26558C" stroke-width="26"/>
<circle cx="450" cy="300" r="150" fill="none" stroke="#4CC38A" stroke-width="26" stroke-linecap="round" stroke-dasharray="{circ}" transform="rotate(-90 450 300)" style="--c:{circ};{a('ring',1.6,S[4]+0.4)}"/>
<text x="450" y="290" text-anchor="middle" font-size="34" fill="#C6C6C6">Battery</text><text x="450" y="345" text-anchor="middle" font-size="64" font-weight="600" fill="#fff" style="{a('fadeIn',.4,S[4]+1.4)}">86%</text>
{''.join(f'<rect x="310" y="{500+i*70}" width="280" height="50" rx="12" fill="#1B3A7B"/><text x="330" y="{533+i*70}" font-size="24" fill="#fff">{t}</text><circle cx="565" cy="{525+i*70}" r="9" fill="#4CC38A"/>' for i,t in enumerate(['Solar','Grid','Home load']))}
</svg>''')
def tile(icon,label,i):
    return f'<div class="tile" style="width:860px;padding:34px 40px;display:flex;align-items:center;gap:36px;margin-top:26px;{a("fadeUp",.5,S[5]+0.4+i*0.8)}"><svg width="110" height="110" viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{icon}</svg><div style="width:6px;height:70px;background:{R}"></div><div style="font-size:46px;font-weight:500">{label}</div></div>'
icons=['<path d="M8 30 L32 10 L56 30 V56 H8 Z"/><path d="M34 26 l-8 14 h8 l-4 12 l12 -16 h-8 l4 -10 z" fill="#DE544A" stroke="none"/>',
'<circle cx="18" cy="16" r="7"/><path d="M18 3v3M18 26v3M5 16h3M28 16h3"/><path d="M26 40 L44 26 L62 40 V60 H26 Z"/>',
'<path d="M6 34 L26 18 L46 34 V58 H6 Z"/><path d="M54 58 V40 M54 22 l-8 18 h16 z"/>']
s6=cap('Built for','Your home, <em>your power</em>')+f'<div style="position:absolute;left:0;right:0;top:{STAGE_Y}px;display:flex;flex-direction:column;align-items:center;transform:scale({SC});transform-origin:top center">'+''.join(tile(ic,l,i) for i,(ic,l) in enumerate(zip(icons,['Home backup','Solar self-consumption','Off-grid homes']))) +'</div>'
efs=92 if tall else 72
s7=f'''<div style="position:absolute;left:0;right:0;top:{HD}px;bottom:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 60px">
<div class="kicker" style="font-size:{int(efs*.36)}px">LiFePO4 energy storage</div>
<h1 style="font-size:{efs}px;margin-top:16px">All-in-One ESS<br>with <em>inverter</em></h1>
<svg width="{360 if tall else 260}" height="{600 if tall else 430}" viewBox="0 0 300 700" style="margin-top:{40 if tall else 20}px">{unit(0,0,4)}</svg>
<div style="margin-top:{40 if tall else 22}px"><span class="btn" style="font-size:{int(efs*.36)}px;padding:22px 52px">Get a quote</span></div>
<div style="margin-top:{36 if tall else 20}px;font-size:{int(efs*.3)}px">energy.eementor.co/pages/energy-storage</div></div>'''
html=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>
body{{margin:0}} .sc{{position:absolute;inset:0}}
@keyframes scene{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes sceneLast{{0%{{opacity:0}}8%{{opacity:1}}100%{{opacity:1}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(30px)}}to{{opacity:1;transform:none}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes slideIn{{from{{opacity:0;transform:translateX(320px)}}to{{opacity:1;transform:none}}}}
@keyframes fillBar{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes flicker{{0%{{opacity:1}}20%{{opacity:.1}}30%{{opacity:.8}}40%{{opacity:.05}}75%{{opacity:.05}}100%{{opacity:1}}}}
@keyframes lineCut{{0%{{opacity:1;stroke:#C6C6C6}}40%{{stroke:#DE544A;opacity:1}}100%{{stroke:#DE544A;opacity:.15}}}}
@keyframes popX{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:none}}}}
@keyframes countStep{{0%{{opacity:0}}10%{{opacity:1}}90%{{opacity:1}}100%{{opacity:0}}}}
@keyframes flow{{from{{stroke-dashoffset:68}}to{{stroke-dashoffset:0}}}}
@keyframes ring{{from{{stroke-dashoffset:var(--c)}}to{{stroke-dashoffset:calc(var(--c)*.14)}}}}
svg text{{font-family:Poppins}}
</style></head><body><div class="frame" style="width:1080px;height:{H}px"><div class="arcs"></div>
{scene(0,s1)}{scene(1,s2)}{scene(2,s3)}{scene(3,s4)}{scene(4,s5)}{scene(5,s6)}{scene(6,s7,True)}
<div style="position:absolute;left:0;right:0;top:0;height:{HD-6}px;background:#fff;display:flex;align-items:center;padding-left:64px;border-bottom:6px solid #DE544A;z-index:5"><img src="logo_energy.png" style="height:{int(HD*.58)}px"></div>
<div class="bar" style="z-index:5"></div></div></body></html>'''
# last-scene count text: keep final 20 kWh visible -> override last counter
html=html.replace(f'style="animation:countStep 1.1s ease-out {S[1]+0.5+3*1.1}s both ">20 kWh',f'style="animation:fadeIn .3s ease-out {S[1]+0.5+3*1.1}s both ">20 kWh')
open(out,'w').write(html); print(END)
