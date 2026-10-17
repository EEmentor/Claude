import os,math
from PIL import Image,ImageFilter,ImageEnhance
PH='/home/claude/claude/fetch/out'; S=os.path.dirname(os.path.abspath(__file__))
R='#DE544A'; G='#C6C6C6'; C='#26558C'
kw=lambda t:f'<span style="text-transform:none">{t}</span>'
def soc(s):
    st=f'width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"'
    return (f'<svg {st}><circle cx="12" cy="12" r="10"/><path d="M13.5 8.5h1.8V6h-2.1c-2 0-3 1.2-3 3.1V11H8.5v2.4h1.7V19h2.6v-5.6h2.1l.4-2.4h-2.5V9.4c0-.6.3-.9.7-.9z" fill="#fff" stroke="none"/></svg>'
     f'<svg {st}><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="#fff" stroke="none"/></svg>'
     f'<svg width="{s}" height="{s}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#fff"/><text x="12" y="16.4" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1B3A7B">in</text></svg>')
def prep(img,w,h,name):
    im=Image.open(f'{PH}/{img}')
    if im.mode in ('RGBA','LA','P'):
        im=im.convert('RGBA'); b=Image.new('RGBA',im.size,(233,236,242,255)); b.alpha_composite(im); im=b.convert('RGB')
    else: im=im.convert('RGB')
    tw,th=w*2,h*2
    sc=max(tw/im.width,th/im.height); bg=im.resize((int(im.width*sc)+1,int(im.height*sc)+1),Image.LANCZOS)
    l=(bg.width-tw)//2;t=(bg.height-th)//2; bg=bg.crop((l,t,l+tw,t+th)).filter(ImageFilter.GaussianBlur(40)); bg=ImageEnhance.Brightness(bg).enhance(.9)
    sc=min(tw/im.width,th/im.height)*(0.94 if abs(math.log((im.width/im.height)/(tw/th)))>0.05 else 1); fg=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS)
    bg.paste(fg,((tw-fg.width)//2,(th-fg.height)//2)); bg.save(f'{S}/{name}'); return name
def post(name,H,k,h,sub,img=None,visual=None):
    HD=132; PHh=762 if H==1440 else 682
    top=f'<img src="{prep(img,1080,PHh,name+"_ph.jpg")}" style="width:1080px;height:{PHh}px;display:block">' if img else f'<div style="width:1080px;height:{PHh}px;background:#EEF1F6;display:flex;align-items:center;justify-content:center">{visual}</div>'
    html=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
<div class="frame" data-size="1080x{H}" style="width:1080px;height:{H}px"><div class="arcs" style="top:{HD+PHh-200}px"></div>
<div style="position:absolute;left:0;right:0;top:0;height:{HD}px;background:#fff;display:flex;align-items:center;padding-left:84px;border-bottom:6px solid {R}"><img src="logo_energy.png" style="height:84px"></div>
<div style="position:absolute;top:{HD+6}px;left:0">{top}</div>
<div style="position:absolute;left:84px;right:84px;top:{HD+6+PHh+40}px;bottom:46px;display:flex;flex-direction:column">
<div class="kicker" style="font-size:24px">{k}</div><h1 style="font-size:{62 if H==1440 else 58}px;margin-top:14px">{h}</h1>
<p style="font-size:27px;margin-top:18px">{sub}</p><div style="flex:1"></div>
<div class="foot" style="font-size:22px"><div class="soc">{soc(30)}<span class="sep"></span><span>energy.eementor.co</span></div></div></div>
<div class="bar"></div></div></body></html>'''
    open(f'{S}/{name}.html','w').write(html); return name+'.html'
def bat(x,v,ah,kwh,w,label):
    hgt=int(110+w*0.0); 
    return f'''<g transform="translate({x},0)"><rect x="0" y="{300-w}" width="200" height="{w}" rx="14" fill="#1B3A7B"/><rect x="60" y="{300-w-16}" width="80" height="16" rx="4" fill="#1B3A7B"/>
<text x="100" y="{300-w/2+4}" text-anchor="middle" font-size="30" font-weight="600" fill="#fff">{v}</text><text x="100" y="{300-w/2+40}" text-anchor="middle" font-size="24" fill="{G}">{ah}</text>
<text x="100" y="350" text-anchor="middle" font-size="40" font-weight="600" fill="{R}">{kwh}</text><text x="100" y="384" text-anchor="middle" font-size="21" fill="#1B3A7B">{label}</text></g>'''
ahwh=f'''<svg width="900" height="600" viewBox="0 0 900 600">
<text x="450" y="70" text-anchor="middle" font-size="46" font-weight="600" fill="#1B3A7B">Wh = V × Ah</text>
<text x="450" y="112" text-anchor="middle" font-size="24" fill="#26558C">energy = voltage × capacity</text>
<g transform="translate(110,150)">{bat(0,'12.8V','100Ah','1.28 kWh',120,'12.8V × 100Ah')}{bat(480,'51.2V','100Ah','5.12 kWh',270,'51.2V × 100Ah')}</g>
<text x="450" y="585" text-anchor="middle" font-size="28" font-weight="500" fill="#1B3A7B">Same 100Ah. <tspan fill="{R}">Four times the energy.</tspan></text></svg>'''
P=[('ig-rack',1440,f'Rack-mounted {kw("LiFePO4")}','Add modules,<br><em>not a new system</em>','Stackable 48V / 51.2V modules, 2.5 to 20 kWh, up to 15 in parallel.','ig_rack_src.jpeg'),
   ('ig-safety',1440,'Battery safety','Store and charge<br><em>lithium safely</em>','Five practical rules from our engineering team.','ig_safety_src.png'),
   ('aio',None,'All-in-one ESS','Battery and inverter<br><em>in one system</em>',f'5–20 kWh LiFePO4 stack · 5 kW inverter · MPPT solar input','ess_aio.webp'),
   ('ah-wh',None,'Battery basics',f'{kw("Ah")} or {kw("Wh")}?<br>Compare <em>energy</em>','Amp-hours alone don\'t tell you how much energy a battery stores.',None),
   ('wall',None,'Wall-mounted powerwall','Storage that<br><em>hangs on the wall</em>','2.4 to 10.24 kWh LiFePO4 units, with or without a built-in inverter.','ess_wall.webp'),
   ('portable',None,'Portable power','Keep routers and<br><em>cameras running</em>','Compact 12V and 24V packs, 62 to 80 Wh, with DC and USB outputs.','ess_portable.webp')]
files=[]
for n,H,k,h,s,img in P:
    for HH in ([H] if H else [1440,1350]):
        files.append(post(f'ee-{n}-1080x{HH}',HH,k,h,s,img,None if img else ahwh))
print(' '.join(files))
