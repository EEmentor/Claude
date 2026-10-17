import sys,os,subprocess
from playwright.sync_api import sync_playwright
H=int(sys.argv[1]); TAG=f'h{H}'; tall=H>1500
SITE='/tmp/claude-0/-home-claude/597a0b6c-e239-5cf6-a538-974de408a6fe/scratchpad/brand/site'
W='/tmp/claude-0/-home-claude-claude/597a0b6c-e239-5cf6-a538-974de408a6fe/scratchpad/ess1b'; B=f'{W}/{TAG}'; os.makedirs(B,exist_ok=True)
U='/root/.claude/uploads/597a0b6c-e239-5cf6-a538-974de408a6fe'
C1=f'{U}/2c4f1408-Picture-1-clip.mp4'; C3=f'{U}/83d08b5d-Picture-3-clip.mp4'; WC=f'{W}/wall_comp.mp4'
S=[0,3.0,7.5,11.6,14.4,19.0,23.8]; END=26.8
HD=150 if tall else 118; FS=82 if tall else 62; R='#DE544A'
exec(open('/home/claude/claude/brand-kit/template_bms_carousel.py').read().split("def page(")[0].replace("S=sys.argv[1]",""))
def header(): return f'<div style="position:absolute;left:0;right:0;top:0;height:{HD-6}px;background:#fff;display:flex;align-items:center;padding-left:64px;border-bottom:6px solid #DE544A"><img src="logo_energy.png" style="height:{int(HD*.58)}px"></div>'
def html(body,bg='transparent'): return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>body{{background:{bg}}}h2{{text-shadow:0 2px 18px rgba(0,0,0,.45)}}</style></head><body><div style="position:relative;width:1080px;height:{H}px;overflow:hidden">{body}<div class="bar"></div></div></body></html>'
def top(k,h,a=.7):
    return f'<div style="position:absolute;left:0;right:0;top:{HD}px;height:{int(FS*6.5)}px;background:linear-gradient(180deg,rgba(10,18,40,{a}),rgba(10,18,40,{a*.8}) 50%,rgba(10,18,40,0))"></div><div style="position:absolute;left:64px;right:64px;top:{HD+(70 if tall else 40)}px"><div class="kicker" style="font-size:{int(FS*.4)}px;margin-bottom:10px">{k}</div><h2 style="font-size:{FS}px">{h}</h2></div>'
def bottom(k,h,sub='',extra=''):
    sb=f'<p style="font-size:{int(FS*.42)}px;margin-top:14px;color:#fff">{sub}</p>' if sub else ''
    return f'<div style="position:absolute;left:0;right:0;bottom:0;height:{int(H*.42)}px;background:linear-gradient(180deg,rgba(14,28,62,0),rgba(14,28,62,.82) 45%,rgba(20,44,98,.96))"></div><div style="position:absolute;left:64px;right:64px;bottom:{90 if tall else 56}px">{extra}<div class="kicker" style="font-size:{int(FS*.4)}px;margin-bottom:10px">{k}</div><h2 style="font-size:{FS}px">{h}</h2>{sb}</div>'
kw=lambda t:f'<span style="text-transform:none">{t}</span>'
chipcss=f'display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.35);border-radius:8px;padding:{14 if tall else 10}px {22 if tall else 16}px;font-size:{int(FS*.4)}px;font-weight:500;color:#fff'
icons={'sun':'<circle cx="12" cy="12" r="4.5" fill="#FFD36A"/><g stroke="#FFD36A" stroke-width="2" stroke-linecap="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></g>',
'grid':'<path d="M13 2L5 14h6l-1 8 8-12h-6z" fill="#FFD36A"/>',
'bat':'<rect x="3" y="7" width="16" height="10" rx="2" fill="none" stroke="#6FE3A6" stroke-width="2"/><rect x="20" y="10" width="2" height="4" fill="#6FE3A6"/><rect x="5" y="9" width="10" height="6" fill="#6FE3A6"/>'}
isz=int(FS*.5)
def chip(ic,t): return f'<span style="{chipcss}"><svg width="{isz}" height="{isz}" viewBox="0 0 24 24">{icons[ic]}</svg>{t}</span>'
L={}
L['ov1']=html(header()+top('Home energy storage','Power cut?<br>Your home<br><em>keeps running</em>'))
L['ov2']=html(header()+bottom('All-in-One ESS','Battery <em>+ inverter</em><br>in one unit'))
L['ov3']=html(header()+bottom('Battery + inverter',f'Built-in <em>5 {kw("kW")}</em><br>inverter','MPPT solar input · 230 V pure sine wave'))
L['ov4']=html(header()+top('Solar ready','Stores your<br><em>surplus solar</em>',.88))
L['ov5']=html(header()+bottom('Smart power','Runs on <em>solar, grid</em><br>or battery','With grid monitoring'))
for i,(ic,t) in enumerate([('sun','Solar'),('grid','Grid'),('bat','Battery')]):
    x=[64,64+ (300 if tall else 230), 64+(560 if tall else 430)][i]
    L[f'ov5c{i}']=html(f'<div style="position:absolute;left:{x}px;bottom:{(470 if tall else 330)}px">{chip(ic,t)}</div>')
L['ov6']=html(header()+bottom('LiFePO4 battery stack',f'<em>5–20 {kw("kWh")}</em><br>of storage'))
for i,t in enumerate(['5–20 kWh LiFePO4','Plug-in modules','Cloud monitoring','DC/AC surge protection']):
    col=i%2; row=i//2
    x=64+col*(470 if tall else 400); y=(560 if tall else 400)-row*(84 if tall else 62)
    L[f'ov6c{i}']=html(f'<div style="position:absolute;left:{x}px;bottom:{y}px"><span style="{chipcss}"><b style="color:{R}">✓</b>{t}</span></div>')
efs=86 if tall else 66
L['end']=html(f'''<div class="frame" style="position:absolute;inset:0"><div class="arcs" style="top:-200px"></div></div>{header()}
<div style="position:absolute;left:0;right:0;top:{HD}px;bottom:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 60px">
<div class="kicker" style="font-size:{int(efs*.36)}px">Battery + inverter</div>
<h1 style="font-size:{efs}px;margin-top:14px">All-in-One ESS<br>with <em>inverter</em></h1>
<img src="aio_product.png" style="height:{820 if tall else 520}px;margin-top:{40 if tall else 22}px;filter:drop-shadow(0 18px 40px rgba(0,0,0,.45))">
<div style="margin-top:{44 if tall else 24}px"><span class="btn" style="font-size:{int(efs*.36)}px;padding:22px 52px">Order this system</span></div>
<div style="margin-top:{30 if tall else 18}px;font-size:{int(efs*.3)}px">energy.eementor.co/pages/energy-storage</div></div>''','#1B3A7B')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':H})
    for k,v in L.items():
        open(f'{SITE}/aio_{TAG}_{k}.html','w').write(v); pg.goto(f'file://{SITE}/aio_{TAG}_{k}.html'); pg.wait_for_timeout(300); pg.screenshot(path=f'{B}/{k}.png',omit_background=True)
    b.close()
def ff(a): subprocess.run(['ffmpeg','-v','error','-y']+a,check=True)
enc=['-r','30','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-an']
d=[round(S[i+1]-S[i],3) for i in range(6)]+[round(END-S[6],3)]
def crop(yoff): return '' if tall else f',crop=1080:{H}:0:{yoff}'
def seg(n,src_filter,inputs,ovs,dur,yoff):
    # ovs: list of (png, start_offset)
    fc=f'[0:v]{src_filter},scale=1080:1920:flags=lanczos{crop(yoff)},setsar=1,fps=30[v0];'; last='[v0]'
    args=[]+inputs
    for j,(png,t0) in enumerate(ovs):
        args+=['-loop','1','-t',str(dur),'-i',f'{B}/{png}.png']
        fc+=f'[{j+1}:v]format=rgba,fade=t=in:st={t0}:d=0.35:alpha=1[o{j}];{last}[o{j}]overlay=0:0:shortest=1[m{j}];'; last=f'[m{j}]'
    fc+=f'{last}trim=duration={dur},fade=t=in:d=0.25,fade=t=out:st={dur-0.25}:d=0.25[out]'
    ff(args+['-filter_complex',fc,'-map','[out]','-t',str(dur)]+enc+[f'{B}/s{n}.mp4'])
seg(1,'null',['-i',C1],[('ov1',0.2)],d[0],570)
seg(2,f'trim=start_frame=0:end_frame=135,setpts=PTS-STARTPTS',['-i',WC],[('ov2',0.3)],d[1],150)
seg(3,f'trim=start_frame=135:end_frame=254,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=0.5',['-i',WC],[('ov3',0.2)],d[2],150)
seg(4,'null',['-i',C3],[('ov4',0.2)],d[3],250)
seg(5,f'trim=start_frame=116:end_frame=254,setpts=PTS-STARTPTS,reverse',['-i',WC],[('ov5',0.2),('ov5c0',0.8),('ov5c1',1.5),('ov5c2',2.2)],d[4],150)
seg(6,f'trim=start_frame=0:end_frame=145,setpts=PTS-STARTPTS',['-i',WC],[('ov6',0.2)]+[(f'ov6c{i}',0.8+i*0.6) for i in range(4)],d[5],150)
ff(['-loop','1','-i',f'{B}/end.png','-vf','fade=t=in:d=0.3','-t',str(d[6])]+enc+[f'{B}/s7.mp4'])
open(f'{B}/list.txt','w').write(''.join(f"file 's{i}.mp4'\n" for i in range(1,8)))
ff(['-f','concat','-safe','0','-i',f'{B}/list.txt','-c','copy',f'{B}/silent.mp4'])
T='/tmp/claude-0/-home-claude-claude/597a0b6c-e239-5cf6-a538-974de408a6fe/scratchpad/tts'
st=[0.4,S[1]+0.2,S[2]+0.2,S[3]+0.2,S[4]+0.2,S[5]+0.2,S[6]+0.2]
ins=[]; fc=''; mix=''
for i in range(7):
    ins+=['-i',f'{T}/aio_{i}.wav']; ms=int(st[i]*1000); fc+=f'[{i+1}:a]aresample=48000,adelay={ms}|{ms}[a{i}];'; mix+=f'[a{i}]'
ff(['-i',f'{B}/silent.mp4']+ins+['-filter_complex',fc+mix+'amix=inputs=7:normalize=0,pan=stereo|c0=c0|c1=c0,loudnorm=I=-15:TP=-1.5[a]','-map','0:v','-map','[a]','-t',str(END),'-c:v','copy','-c:a','aac','-b:a','160k','-movflags','+faststart',f'{W}/eementor-all-in-one-ess-1080x{H}.mp4'])
print('done',H)
