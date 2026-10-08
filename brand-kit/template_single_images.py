import os,sys
exec(open(os.path.join(os.path.dirname(__file__),'gen.py')).read().split("B='#1B3A7B'")[0])
B='#1B3A7B';R='#DE544A';C='#26558C';G='#C6C6C6'
chart=f'''<svg viewBox="0 0 720 414" style="width:100%;height:auto">
<line x1="60" y1="20" x2="60" y2="350" stroke="{G}" stroke-width="2.5"/><line x1="60" y1="350" x2="710" y2="350" stroke="{G}" stroke-width="2.5"/>
<text x="28" y="190" transform="rotate(-90 28 190)" text-anchor="middle" font-size="20" font-weight="500" fill="{G}">Current</text>
<text x="704" y="378" text-anchor="end" font-size="20" font-weight="500" fill="{G}">Time</text>
<line x1="60" y1="90" x2="710" y2="90" stroke="{R}" stroke-width="2" stroke-dasharray="8 7"/>
<line x1="60" y1="240" x2="710" y2="240" stroke="#fff" stroke-width="2" stroke-dasharray="8 7" opacity=".7"/>
<path d="M60 320 H120 V240 H220 V90 H265 V240 H400 V90 H445 V240 H550 V320 H620 V240 H710 V350 H60 Z" fill="rgba(255,255,255,.08)"/>
<path d="M60 320 H120 V240 H220 V90 H265 V240 H400 V90 H445 V240 H550 V320 H620 V240 H710" fill="none" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>
<text x="470" y="80" font-size="21" font-weight="600" fill="{R}">Peak current</text>
<text x="456" y="228" font-size="21" font-weight="600" fill="#fff">Continuous current</text>
<path d="M220 52 V44 H265 V52" stroke="#fff" stroke-width="2.5" fill="none"/><text x="242" y="34" text-anchor="middle" font-size="19" font-weight="500" fill="#fff">Pulse duration</text>
<path d="M220 372 V380 H400 V372" stroke="#fff" stroke-width="2.5" fill="none"/><text x="310" y="402" text-anchor="middle" font-size="19" font-weight="500" fill="#fff">One load cycle</text>
<text x="585" y="312" text-anchor="middle" font-size="19" font-weight="500" fill="{G}">Rest</text></svg>'''
def decides(fs):
    it=['Which cell you choose','How many cells go in parallel','How the BMS is sized','How the pack handles heat']
    return ''.join(f'<div style="display:flex;gap:14px;align-items:flex-start;margin-top:{int(fs*.5)}px"><span style="flex:none;width:{int(fs*.42)}px;height:{int(fs*.42)}px;margin-top:{int(fs*.36)}px;background:{R}"></span><span style="font-size:{fs}px;font-weight:500">{t}</span></div>' for t in it)
def btn(fs,t='Learn more'): return f'<span class="btn" style="font-size:{fs}px;padding:{int(fs*.5)}px {int(fs*1.1)}px">{t}</span>'
LP='40px 52px 34px'
page('load_li.html',1200,627,f'''<div style="display:flex;gap:40px;flex:1;margin-top:18px">
<div style="flex:1.25;display:flex;flex-direction:column"><div class="kicker" style="font-size:16px">Battery sizing</div>
<h1 style="font-size:44px;margin-top:6px">Start with the <em>load profile</em></h1><div style="margin-top:14px">{chart}</div></div>
<div style="flex:.8;display:flex;flex-direction:column;justify-content:center"><p style="font-size:20px;color:#fff;font-weight:500">Same voltage and capacity can still need a different battery. The load decides:</p>{decides(20)}
<div style="margin-top:26px">{btn(17,'Send us your load profile')}</div></div></div>
{foot(16)}''',LP,34)
page('load_sq.html',1080,1350,f'''<div class="kicker" style="font-size:26px;margin-top:64px">Battery sizing</div>
<h1 style="font-size:74px;margin-top:16px">Start with the<br><em>load profile</em></h1>
<p style="font-size:31px;margin-top:24px;max-width:880px">Two products can need the same voltage and capacity, and still need completely different batteries.</p>
<div class="tile" style="margin-top:28px;padding:20px 26px 10px">{chart}</div>
<p style="font-size:30px;color:#fff;font-weight:600;margin-top:22px;text-transform:uppercase">The load decides:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:30px">{decides(26)}</div>
<div style="flex:1;min-height:24px"></div>{foot(22)}''','88px 84px 64px',54)
icons={
'Logistics robots':'<rect x="8" y="22" width="48" height="20" rx="4"/><circle cx="18" cy="48" r="5"/><circle cx="46" cy="48" r="5"/><rect x="25" y="12" width="14" height="10" rx="2"/><line x1="16" y1="32" x2="30" y2="32"/>',
'Drones':'<rect x="24" y="27" width="16" height="10" rx="3"/><line x1="24" y1="28" x2="13" y2="18"/><line x1="40" y1="28" x2="51" y2="18"/><line x1="24" y1="36" x2="13" y2="46"/><line x1="40" y1="36" x2="51" y2="46"/><ellipse cx="13" cy="16" rx="9" ry="3"/><ellipse cx="51" cy="16" rx="9" ry="3"/><ellipse cx="13" cy="48" rx="9" ry="3"/><ellipse cx="51" cy="48" rx="9" ry="3"/>',
'Medical equipment':'<rect x="8" y="14" width="48" height="36" rx="6"/><polyline points="13,33 22,33 26,24 32,43 36,29 40,33 51,33"/>',
'Industrial power tools':'<rect x="8" y="16" width="34" height="14" rx="4"/><line x1="42" y1="23" x2="58" y2="23"/><path d="M18 30 V46 H30 V30"/><rect x="13" y="46" width="22" height="7" rx="2"/>',
'E-mobility':'<circle cx="14" cy="46" r="7"/><circle cx="50" cy="46" r="7"/><line x1="14" y1="46" x2="43" y2="46"/><line x1="44" y1="46" x2="39" y2="14"/><line x1="33" y1="14" x2="46" y2="14"/>',
'IoT & security cameras':'<path d="M8 22 L44 15 L48 29 L12 36 Z"/><circle cx="40" cy="24" r="3.5"/><path d="M24 33 V48 H12"/><path d="M50 10 a8 8 0 0 1 6 6"/><path d="M50 4 a14 14 0 0 1 12 12"/>'}
def tile(n,sz,fs,pad):
    return f'<div class="tile" style="padding:{pad}px;display:flex;flex-direction:column;align-items:flex-start;justify-content:center"><svg width="{sz}" height="{sz}" viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{icons[n]}</svg><div style="width:{int(sz*.45)}px;height:4px;background:{R};margin-top:{int(pad*.5)}px"></div><div style="font-size:{fs}px;font-weight:500;margin-top:{int(pad*.5)}px;line-height:1.2">{n}</div></div>'
page('apps_li.html',1200,627,f'''<div style="display:flex;gap:40px;flex:1;margin-top:10px">
<div style="flex:.85;display:flex;flex-direction:column;justify-content:center"><div class="kicker" style="font-size:16px">Applications</div>
<h1 style="font-size:46px;margin-top:8px">Where custom battery packs <em>matter</em></h1>
<p style="font-size:19px;margin-top:16px">Limited space, unusual voltage, high pulse current, specific connectors or a fixed mechanical envelope.</p>
<div style="margin-top:22px">{btn(16)}</div></div>
<div style="flex:1.15;display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;align-content:center">{''.join(tile(n,48,19,18) for n in icons)}</div></div>
<div style="height:14px"></div>{foot(16)}''',LP,34)
page('apps_sq.html',1080,1350,f'''<div class="kicker" style="font-size:26px;margin-top:64px">Applications</div>
<h1 style="font-size:70px;margin-top:16px">Where custom<br>battery packs <em>matter</em></h1>
<p style="font-size:29px;margin-top:20px;max-width:880px">When a product has limited space, an unusual voltage, high pulse current, specific connectors or a fixed mechanical envelope.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:32px">{''.join(tile(n,58,27,22) for n in icons)}</div>
<div style="flex:1;min-height:24px"></div>{foot(22)}''','88px 84px 64px',54)
print('ok2')
