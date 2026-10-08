import os,sys
S=sys.argv[1]
def soc(s):
    st=f'width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"'
    fb=f'<svg {st}><circle cx="12" cy="12" r="10"/><path d="M13.5 8.5h1.8V6h-2.1c-2 0-3 1.2-3 3.1V11H8.5v2.4h1.7V19h2.6v-5.6h2.1l.4-2.4h-2.5V9.4c0-.6.3-.9.7-.9z" fill="#fff" stroke="none"/></svg>'
    ig=f'<svg {st}><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="#fff" stroke="none"/></svg>'
    li=f'<svg width="{s}" height="{s}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#fff"/><text x="12" y="16.4" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1B3A7B">in</text></svg>'
    return fb+ig+li
def foot(fs,page=''):
    return f'<div class="foot" style="font-size:{fs}px"><div class="soc">{soc(int(fs*1.35))}<span class="sep"></span><span>energy.eementor.co</span></div><div style="font-weight:500">{page}</div></div>'
def page(name,w,h,body,pad,logo_h):
    html=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
<div class="frame" data-size="{w}x{h}" style="width:{w}px;height:{h}px"><div class="arcs"></div><div class="inner" style="padding:{pad}">
<img class="logo" src="logo.png" style="height:{logo_h}px;width:auto;align-self:flex-start">
{body}</div><div class="bar"></div></div></body></html>'''
    open(os.path.join(S,name),'w').write(html)
B='#1B3A7B';R='#DE544A';C='#26558C';G='#C6C6C6'
def cells(x0,y0,n=4,w=110,h=200,gap=34):
    s=''
    for i in range(n):
        x=x0+i*(w+gap)
        s+=f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="14" fill="{C}" stroke="#fff" stroke-width="3"/><rect x="{x+w/2-18}" y="{y0-14}" width="36" height="14" rx="3" fill="#fff"/>'
        s+=f'<text x="{x+w/2}" y="{y0+h/2+12}" text-anchor="middle" font-size="34" font-weight="600" fill="#fff">{i+1}</text>'
        if i<n-1: s+=f'<line x1="{x+w}" y1="{y0+40}" x2="{x+w+gap}" y2="{y0+40}" stroke="{G}" stroke-width="5"/>'
    return s
P='88px 84px 64px'
def slide(name,n,body):
    page(name,1080,1350,body+'<div style="flex:1"></div>'+foot(22,f'{n} / 5'+(' &nbsp;·&nbsp; SWIPE &rarr;' if n<5 else '')),P,54)
# 1
cov=f'''<svg width="912" height="400" viewBox="0 0 912 400">{cells(70,30)}
<g stroke="{R}" stroke-width="3" fill="none">'''+''.join(f'<path d="M{125+i*144} 230 V280 H{140+i*150} V310"/>' for i in range(4))+f'''</g>
<rect x="110" y="310" width="560" height="84" rx="8" fill="{B}" stroke="{R}" stroke-width="3"/>
<rect x="138" y="331" width="64" height="42" rx="4" fill="{R}"/><text x="228" y="364" font-size="32" font-weight="600" fill="#fff">BMS</text>
<text x="320" y="363" font-size="22" fill="{G}">battery management system</text>
<path d="M670 352 H790" stroke="#fff" stroke-width="4" stroke-dasharray="10 8"/>
<rect x="790" y="314" width="110" height="76" rx="8" fill="{C}" stroke="#fff" stroke-width="3"/><text x="845" y="361" text-anchor="middle" font-size="24" font-weight="500" fill="#fff">Host</text></svg>'''
chips=''.join(f'<span class="chip"><b style="color:{R};font-weight:600">0{i+1}</b>{t}</span>' for i,t in enumerate(['Monitoring','Protection','Balancing','State estimation','Communication']))
slide('bms1.html',1,f'''<div class="kicker" style="font-size:26px;margin-top:70px">Battery engineering</div>
<h1 style="font-size:96px;margin-top:22px">What a <em>BMS</em><br>actually does</h1>
<p style="font-size:33px;margin-top:30px;max-width:880px">It's not just an on/off switch. Here are the five jobs an engineered lithium pack relies on.</p>
<div style="margin-top:46px">{cov}</div>
<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:34px;font-size:25px">{chips}</div>''')
# 2
mon=f'''<svg width="912" height="520" viewBox="0 0 912 520">{cells(150,50)}'''+''.join(f'<line x1="{205+i*144}" y1="250" x2="{205+i*144}" y2="400" stroke="{R}" stroke-width="3"/><rect x="{169+i*144}" y="288" width="72" height="44" rx="6" fill="{B}" stroke="{R}" stroke-width="2.5"/><text x="{205+i*144}" y="319" text-anchor="middle" font-size="24" font-weight="600" fill="#fff">V{i+1}</text>' for i in range(4))+f'''
<rect x="40" y="95" width="70" height="44" rx="6" fill="{B}" stroke="#fff" stroke-width="2.5"/><text x="75" y="126" text-anchor="middle" font-size="24" font-weight="600" fill="#fff">T</text>
<line x1="110" y1="117" x2="150" y2="117" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/><path d="M75 139 V450 H120" stroke="#fff" stroke-width="3" fill="none"/>
<rect x="756" y="95" width="116" height="44" rx="6" fill="{B}" stroke="#fff" stroke-width="2.5"/><text x="814" y="126" text-anchor="middle" font-size="22" font-weight="600" fill="#fff">I shunt</text>
<line x1="726" y1="117" x2="756" y2="117" stroke="{G}" stroke-width="5"/><path d="M814 139 V450 H770" stroke="#fff" stroke-width="3" fill="none"/>
<rect x="120" y="400" width="650" height="96" rx="8" fill="{R}"/><text x="445" y="459" text-anchor="middle" font-size="30" font-weight="600" fill="#fff">BMS measures V · I · T</text></svg>'''
slide('bms2.html',2,f'''<div class="kicker" style="font-size:26px;margin-top:70px">01 · Monitoring</div>
<h2 style="font-size:82px;margin-top:22px">It watches every<br><em>cell group</em></h2>
<p style="font-size:33px;margin-top:28px;max-width:890px">The BMS continuously measures the voltage of each series cell group, the pack current and the temperature at key points in the pack.</p>
<div style="margin-top:54px">{mon}</div>''')
# 3
items=[('Over-charge','Cell voltage too high'),('Over-discharge','Cell voltage too low'),('Over-current','Load above its limit'),('Short circuit','Fault on the output'),('Over-temperature','Pack too hot'),('Cold charging','Charging below the safe temperature')]
warn=f'<svg width="32" height="32" viewBox="0 0 34 34"><path d="M17 3 L31 29 H3 Z" fill="{R}"/><line x1="17" y1="13" x2="17" y2="20" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/><circle cx="17" cy="24.5" r="1.9" fill="#fff"/></svg>'
tiles=''.join(f'<div class="tile" style="padding:22px 24px"><div style="display:flex;align-items:center;gap:14px">{warn}<div style="font-size:29px;font-weight:600">{a}</div></div><p style="font-size:24px;margin-top:8px">{b}</p></div>' for a,b in items)
sw=f'''<svg width="912" height="140" viewBox="0 0 912 140"><rect x="0" y="25" width="200" height="86" rx="8" fill="{C}" stroke="#fff" stroke-width="3"/><text x="100" y="78" text-anchor="middle" font-size="28" font-weight="500" fill="#fff">Cells</text>
<line x1="200" y1="68" x2="360" y2="68" stroke="{G}" stroke-width="5"/><circle cx="360" cy="68" r="8" fill="{G}"/><line x1="360" y1="68" x2="450" y2="22" stroke="{R}" stroke-width="7" stroke-linecap="round"/><circle cx="470" cy="68" r="8" fill="{G}"/>
<text x="415" y="134" text-anchor="middle" font-size="21" font-weight="500" fill="#fff">MOSFETs / contactor open</text>
<line x1="470" y1="68" x2="680" y2="68" stroke="{G}" stroke-width="5" stroke-dasharray="12 10"/><rect x="680" y="25" width="232" height="86" rx="8" fill="none" stroke="{G}" stroke-width="3"/><text x="796" y="78" text-anchor="middle" font-size="24" font-weight="500" fill="{G}">Load / charger</text></svg>'''
slide('bms3.html',3,f'''<div class="kicker" style="font-size:26px;margin-top:70px">02 · Protection</div>
<h2 style="font-size:82px;margin-top:22px">It cuts the power<br><em>before damage</em></h2>
<p style="font-size:31px;margin-top:24px;max-width:900px">When a limit is crossed, the BMS opens the charge or discharge path, usually through MOSFETs or a contactor.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px">{tiles}</div>
<div style="margin-top:26px">{sw}</div>''')
# 4
def bars(x0,vals,col): return ''.join(f'<rect x="{x0+i*78}" y="{320-v}" width="54" height="{v}" rx="4" fill="{col}"/>' for i,v in enumerate(vals))
bal=f'''<svg width="912" height="400" viewBox="0 0 912 400"><text x="160" y="34" text-anchor="middle" font-size="27" font-weight="500" fill="#fff">BEFORE</text><text x="700" y="34" text-anchor="middle" font-size="27" font-weight="500" fill="#fff">AFTER BALANCING</text>
{bars(10,[250,205,270,180],R)}<line x1="0" y1="140" x2="320" y2="140" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>
<path d="M370 200 H520" stroke="#fff" stroke-width="6" stroke-linecap="round"/><path d="M500 180 L525 200 L500 220" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
{bars(550,[240,240,240,240],'#fff')}<line x1="540" y1="80" x2="870" y2="80" stroke="{R}" stroke-width="3" stroke-dasharray="10 8"/>
<line x1="0" y1="322" x2="320" y2="322" stroke="{G}" stroke-width="2"/><line x1="540" y1="322" x2="870" y2="322" stroke="{G}" stroke-width="2"/>
<text x="160" y="368" text-anchor="middle" font-size="22" fill="{G}">Lowest group limits capacity</text><text x="700" y="368" text-anchor="middle" font-size="22" fill="{G}">Groups at the same level</text></svg>'''
slide('bms4.html',4,f'''<div class="kicker" style="font-size:26px;margin-top:70px">03 · Balancing</div>
<h2 style="font-size:82px;margin-top:22px">It keeps cell groups<br><em>in step</em></h2>
<p style="font-size:31px;margin-top:24px;max-width:900px">Small differences between cells grow over many cycles. Balancing brings every cell group back to the same state of charge, so the pack keeps its usable capacity.</p>
<div style="margin-top:44px">{bal}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:26px">
<div class="tile" style="padding:24px"><div style="font-size:28px;font-weight:600">Passive</div><p style="font-size:23px;margin-top:6px">Bleeds extra charge from the highest groups as heat</p></div>
<div class="tile" style="padding:24px"><div style="font-size:28px;font-weight:600">Active</div><p style="font-size:23px;margin-top:6px">Moves charge from higher groups to lower ones</p></div></div>''')
# 5
protos=''.join(f'<span class="chip" style="font-size:28px">{p}</span>' for p in ['CAN','RS485','UART','SMBus'])
slide('bms5.html',5,f'''<div class="kicker" style="font-size:26px;margin-top:70px">04 · State estimation &nbsp; 05 · Communication</div>
<h2 style="font-size:74px;margin-top:22px">It tracks charge and<br><em>talks to your system</em></h2>
<div class="tile" style="padding:30px 32px;margin-top:40px"><div style="font-size:32px;font-weight:600"><span style="color:{R}">SoC</span> &nbsp;State of charge</div><p style="font-size:26px;margin-top:8px">How much energy is left, estimated from voltage, current and history. Many BMS also track <b style="color:#fff;font-weight:600">SoH</b>, state of health.</p>
<div style="margin-top:22px;height:26px;border-radius:3px;background:rgba(255,255,255,.12);overflow:hidden"><div style="width:68%;height:100%;background:linear-gradient(90deg,#fff,{R})"></div></div></div>
<div class="tile" style="padding:30px 32px;margin-top:20px"><div style="font-size:32px;font-weight:600">Talks to the host</div><p style="font-size:26px;margin-top:8px">Shares data and alarms with your controller, charger, inverter or display.</p>
<div style="display:flex;gap:12px;margin-top:22px;flex-wrap:wrap">{protos}</div></div>
<div style="margin-top:30px;padding:28px 34px;background:{R}">
<div style="font-size:34px;font-weight:600;line-height:1.15;text-transform:uppercase">Choose the BMS around the application, not at the end.</div>
<div style="font-size:24px;margin-top:10px">energy.eementor.co/pages/custom-battery-packs</div></div>''')
print('ok')
