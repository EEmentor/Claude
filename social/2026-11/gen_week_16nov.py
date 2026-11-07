exec(open('template_photo_post.py').read().split('\ndef bat(')[0])
B='#1B3A7B'
def cellv(x,y,w,h,fill=B):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>'
cells16=''.join(cellv(80+i*50,170,38,120) for i in range(16))
s16=f'''<svg width="960" height="640" viewBox="0 0 960 640" font-family="Poppins">
<text x="480" y="66" text-anchor="middle" font-size="42" font-weight="600" fill="{B}">16 LiFePO4 cells in series (<tspan fill="{R}">16S</tspan>)</text>
<text x="480" y="108" text-anchor="middle" font-size="24" fill="{C}">the cell count behind a 51.2V pack</text>
{cells16}
<rect x="70" y="330" width="820" height="270" rx="20" fill="#fff" stroke="{G}" stroke-width="2"/>
<text x="110" y="395" font-size="30" font-weight="600" fill="{R}">58.4V</text><text x="300" y="395" font-size="27" fill="{B}">full charge · 16 × 3.65V</text>
<text x="110" y="465" font-size="30" font-weight="600" fill="{B}">51.2V</text><text x="300" y="465" font-size="27" fill="{B}">nominal · 16 × 3.2V</text>
<text x="110" y="535" font-size="30" font-weight="600" fill="{C}">40V</text><text x="300" y="535" font-size="27" fill="{B}">discharge cut-off · 16 × 2.5V</text>
<text x="480" y="585" text-anchor="middle" font-size="20" fill="{C}">Example: our 51.2V golf cart packs</text></svg>'''
def checklist(title,sub,items):
    rows=''.join(f'<circle cx="120" cy="{190+i*78}" r="22" fill="{R}"/><path d="M109 {190+i*78} l8 8 l15 -16" stroke="#fff" stroke-width="5" fill="none"/><text x="165" y="{200+i*78}" font-size="30" fill="{B}">{t}</text>' for i,t in enumerate(items))
    return f'''<svg width="960" height="640" viewBox="0 0 960 640" font-family="Poppins">
<text x="480" y="70" text-anchor="middle" font-size="42" font-weight="600" fill="{B}">{title}</text>
<text x="480" y="112" text-anchor="middle" font-size="24" fill="{C}">{sub}</text>{rows}</svg>'''
docs=checklist('What comes with your pack','documents you receive',['Quality test report in every shipment','Batch and cell date-code traceability','Cell datasheets and SDS/MSDS','Battery datasheet once the spec is locked','Transport review: UN 38.3 for your market'])
cert=checklist('Certification','what our standard models carry',['Tested to UN 38.3','Tested to IEC 62133','CE marked','IEC 62619, UL: by design and market','Manufacturing partner: ISO 9001'])
chips=''.join(f'<rect x="{90+i*162}" y="300" width="138" height="64" rx="32" fill="{R if i%2 else B}"/><text x="{159+i*162}" y="342" text-anchor="middle" font-size="26" font-weight="600" fill="#fff">{t}</text>' for i,t in enumerate(['CAN','RS485','UART','SMBus','Bluetooth']))
comm=f'''<svg width="960" height="640" viewBox="0 0 960 640" font-family="Poppins">
<text x="480" y="70" text-anchor="middle" font-size="42" font-weight="600" fill="{B}">BMS → your device</text>
<text x="480" y="112" text-anchor="middle" font-size="24" fill="{C}">state of charge and battery status over the interface you use</text>
<rect x="120" y="150" width="260" height="110" rx="18" fill="{B}"/><text x="250" y="200" text-anchor="middle" font-size="28" font-weight="600" fill="#fff">Battery + BMS</text><text x="250" y="238" text-anchor="middle" font-size="22" fill="{G}">protection · balancing</text>
<rect x="580" y="150" width="260" height="110" rx="18" fill="#fff" stroke="{B}" stroke-width="3"/><text x="710" y="200" text-anchor="middle" font-size="28" font-weight="600" fill="{B}">Your device</text><text x="710" y="238" text-anchor="middle" font-size="22" fill="{C}">controller · display</text>
<path d="M390 205 H 570" stroke="{R}" stroke-width="6" marker-end="url(#a)"/><defs><marker id="a" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="{R}"/></marker></defs>
{chips}
<text x="480" y="440" text-anchor="middle" font-size="28" fill="{B}">Robots, vehicles and machines read the charge level.</text>
<text x="480" y="485" text-anchor="middle" font-size="28" fill="{B}">Handhelds and medical devices too.</text>
<text x="480" y="560" text-anchor="middle" font-size="22" fill="{C}">Interface agreed per project</text></svg>'''
P=[('compact',f'Compact {kw("LiFePO4")} batteries','Small batteries,<br><em>long life</em>','6.4V and 12.8V, 4 to 30Ah, series and parallel up to 4S4P.','deep_compact5.webp',None),
   ('eskate','Electric skateboard & e-foil batteries','High power,<br><em>flat pack</em>','Cells arranged to fit the height and shape of your deck or board.','app_eskate.jpg',None),
   ('16s','Battery basics',f'Inside a <em>{kw("51.2V")}</em> pack','16 LiFePO4 cells in series: 58.4V full, 40V cut-off.',None,s16),
   ('handheld','Portable instrument batteries','Last the<br><em>working day</em>','Sized from your average and peak current and hours between charges.','app_handheld.jpg',None),
   ('documents','What you receive','The paperwork<br><em>comes with it</em>','QC report, batch and date-code traceability, datasheets and SDS/MSDS.',None,docs),
   ('drones','Drone & UAV batteries','Every gram,<br><em>every amp</em>','Cells compared on capacity and weight for your target flight time.','app_drones.jpg',None),
   ('medical2','Medical device batteries','Dependable power,<br><em>clear paper trail</em>','Named cells, batch traceability and a test report in every shipment.','app_medical.jpg',None),
   ('certification','Certification',f'{kw("UN 38.3")} and<br><em>{kw("IEC 62133")}</em>','Standard models are tested to both and CE marked.',None,cert),
   ('cells50','Battery cells','Genuine cells,<br><em>from 50 pieces</em>','Order named 18650, 21700, LiFePO4 and LiPo cells online.','cell_40t.jpg',None),
   ('bms-comm','BMS communication','Your device<br><em>knows the charge</em>','CAN, RS485, UART, SMBus or Bluetooth, agreed per project.',None,comm)]
print(' '.join(post(f'ee-{n}-1080x1350',1350,k,h,s,img,vis) for n,k,h,s,img,vis in P))
