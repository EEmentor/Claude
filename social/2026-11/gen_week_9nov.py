exec(open('template_photo_post.py').read().split('\ndef bat(')[0])
B='#1B3A7B'
def cell(x,y,w,h,fill=B,lab=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}"/><rect x="{x+w/2-12}" y="{y-10}" width="24" height="11" rx="2" fill="{fill}"/><text x="{x+w/2}" y="{y+h/2+10}" text-anchor="middle" font-size="26" font-weight="600" fill="#fff">{lab}</text>'
cells=''.join(cell(150+i*160,170,110,190,lab='3.2V') for i in range(4))
links=''.join(f'<path d="M{150+i*160+110} 265 H {150+(i+1)*160}" stroke="{R}" stroke-width="6"/>' for i in range(3))
s4=f'''<svg width="960" height="640" viewBox="0 0 960 640" font-family="Poppins">
<text x="480" y="70" text-anchor="middle" font-size="44" font-weight="600" fill="{B}">Inside a <tspan fill="{R}">12.8V</tspan> LiFePO4 battery</text>
<text x="480" y="112" text-anchor="middle" font-size="24" fill="{C}">four cells in series (4S)</text>
{cells}{links}
<text x="480" y="420" text-anchor="middle" font-size="34" font-weight="600" fill="{B}">4 × 3.2V = <tspan fill="{R}">12.8V</tspan></text>
<rect x="70" y="456" width="820" height="150" rx="20" fill="#fff" stroke="{G}" stroke-width="2"/>
<text x="480" y="505" text-anchor="middle" font-size="26" fill="{B}">2S = <tspan font-weight="600">6.4V</tspan>   ·   4S = <tspan font-weight="600">12.8V</tspan>   ·   8S = <tspan font-weight="600">25.6V</tspan></text>
<text x="480" y="550" text-anchor="middle" font-size="26" fill="{B}">16S = <tspan font-weight="600" fill="{R}">51.2V</tspan> · rack modules and cabinets</text>
<text x="480" y="588" text-anchor="middle" font-size="21" fill="{C}">LiFePO4 nominal 3.2V per cell</text></svg>'''
P=[('starter',f'{kw("LiFePO4")} starter batteries','Up to <em>70% lighter</em><br>than lead-acid',f'12.8V, 3 to 100Ah, 180 to 2,500 A cranking current.','deep_starter5.webp',None),
   ('iot','Industrial IoT batteries','Sized from your<br><em>power budget</em>','Packs for sensors, trackers and gateways, charged by solar, mains or vehicle.','app_iot.jpg',None),
   ('4s','Battery basics',f'Why <em>{kw("12.8V")}</em>?','Four LiFePO4 cells in series: 4 × 3.2V = 12.8V.',None,s4),
   ('rov','Underwater vehicle batteries','Thrusters draw<br><em>in bursts</em>','Packs specified for continuous and peak discharge, sized for mission time.','app_rov.jpg',None),
   ('ndaa','Procurement requirements','NDAA-compliant<br><em>configurations</em>','Available for qualifying projects, with US manufacturing options.','hero_pack.webp',None),
   ('wheelchair','Wheelchairs & mobility scooters','Range sized to<br><em>the daily routine</em>','LiFePO4 or Li-ion packs, fitted to your battery compartment.','app_wheelchair.jpg',None),
   ('forklift','Forklifts & material handling','Finish the shift,<br><em>charge in the break</em>','Capacity sized from shift length and average load.','app_forklift.jpg',None),
   ('golf','Golf cart batteries','Last the day,<br><em>charge overnight</em>','Packs matched to 36 V, 48 V or 72 V vehicle systems.','app_golf.jpg',None),
   ('lowtemp',f'Low-temperature {kw("LiFePO4")}','Built for<br><em>cold mornings</em>','12.8V, 50 to 200Ah. Low-temperature charging; self-heating LCD models.','deep_cold5.webp',None),
   ('garden','Garden & outdoor equipment','High current,<br><em>out in the yard</em>','Packs for mowers, trimmers and blowers, fitted to your slide interface.','app_garden.jpg',None)]
print(' '.join(post(f'ee-{n}-1080x1350',1350,k,h,s,img,vis) for n,k,h,s,img,vis in P))
