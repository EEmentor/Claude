kw = lambda t: f'<span style="text-transform:none">{t}</span>'
REELS = {
 'dropin': dict(url='energy.eementor.co/pages/energy-storage', button='Choose a model', end_kicker='Lead-acid replacement',
  end_h=f'{kw("12V")} &amp; {kw("24V")}<br><em>drop-in</em>', end_chips=['6Ah to 300Ah', 'Built-in BMS', 'Series or parallel'], end_img='ess_dropin.webp',
  note='What still runs on lead-acid? Tell us in the comments', ai=True,
  scenes=[
   dict(img='ess_dropin.webp', k='Lead-acid replacement', h='Same slot.<br><em>New chemistry.</em>', s=''),
   dict(img='lfp_12v.jpg', k='Weight', h='About <em>1/3</em><br>the weight', s='Compared with lead-acid'),
   dict(img='ess_dropin.webp', k='Cycle life', h='Up to <em>4×</em><br>the cycle life', s='Compared with lead-acid'),
   dict(img='deep_golf5.webp', k='Usable capacity', h='<em>100%</em><br>usable capacity', s='Built-in BMS with balancing and protection'),
   dict(img='ess_dropin.webp', k='The range', h=f'{kw("6Ah")} to<br><em>{kw("300Ah")}</em>', s='12V and 24V · connect in series or parallel'),
  ]),
 'lipo': dict(url='energy.eementor.co/pages/battery-design-studio', button='Design yours', end_kicker='LiPo pouch cells',
  end_h='Light, flat,<br><em>high current</em>', end_chips=['1,450–22,000 mAh', 'Up to 320 A', '3.7V or 3.8V'], end_img='lipo_steel.jpg',
  note='Drone, robot or racer? Tell us in the comments', ai=False,
  scenes=[
   dict(img='lipo_unwrapped.jpg', k='LiPo pouch cells', h='Flat cells,<br><em>big current</em>', s=''),
   dict(img='cell_lipo5000.jpg', k='Cell range', h=f'{kw("1,450")} to<br><em>{kw("22,000 mAh")}</em>', s='3.7V LiPo pouch cells in the Battery Design Studio'),
   dict(img='cell_lipo22000.jpg', k='High drain', h=f'Up to <em>{kw("320 A")}</em><br>per cell', s='LP90106212-25C · 22,000 mAh'),
   dict(img='lipo_pvc.jpg', k='High-voltage LiPo', h=f'<em>{kw("4.35V")}</em><br>full charge', s='3.8V nominal, vs 3.7V for standard LiPo'),
   dict(img='lipo_abs.jpg', k='Your own cell', h='Or enter<br><em>your cell data</em>', s='Capacity, C-rate, size and weight'),
  ]),
 'studio': dict(url='energy.eementor.co/pages/battery-design-studio', button='Try the Studio', end_kicker='Battery Design Studio',
  end_h='Type it,<br><em>see it in 3D</em>', end_chips=['18650 · 21700', 'Up to 24S / 30P', 'V1.0 beta'], end_img='diag_studio.png',
  note='What would you type first? Tell us in the comments', ai=False,
  scenes=[
   dict(img='diag_studio.png', k='Battery Design Studio', h='Type your pack.<br><em>See it in 3D.</em>', s=''),
   dict(img='diag_studio.png', k='Describe your pack', h=f'“{kw("48V")} e-bike,<br><em>{kw("20Ah")}</em>”', s='Voltage plus capacity'),
   dict(img='diag_studio.png', k='Or a runtime', h=f'“{kw("24V")} robot,<br><em>{kw("6h")} at {kw("15A")}</em>”', s='Runtime and current work too'),
   dict(img='ds_pack.png', k='Instant numbers', h='Voltage, energy,<br><em>size</em>', s='Pack voltage, capacity, energy and approximate block size'),
   dict(img='ds_pack.png', k='Then a quote', h='Send it to<br><em>our engineers</em>', s='We check the BMS, current and enclosure'),
  ]),
 'apps': dict(url='energy.eementor.co/pages/custom-battery-packs', button='See all 19', end_kicker='Custom battery packs',
  end_h='19 applications,<br><em>one process</em>', end_chips=['Named cells', 'No prototype MOQ', 'QC report'], end_img='app_robots.jpg',
  note='Which one is your application? Tell us in the comments', ai=True,
  scenes=[
   dict(img='app_robots.jpg', k='Applications', h='19 jobs,<br><em>one team</em>', s=''),
   dict(img='app_drones.jpg', k='In the air', h='Drones<br><em>&amp; UAVs</em>', s='Lightweight, high-discharge packs'),
   dict(img='app_medical.jpg', k='In the clinic', h='Medical<br><em>equipment</em>', s='Stable, dependable power for critical devices'),
   dict(img='app_rov.jpg', k='Under water', h='Underwater<br><em>vehicles</em>', s='Cells arranged for your pressure housing'),
   dict(img='app_robots.jpg', k='Around the clock', h='Robots,<br><em>AMRs &amp; AGVs</em>', s='High-cycle packs running around the clock'),
  ]),
 '14s8p': dict(url='energy.eementor.co/pages/custom-battery-packs', button='Configure in 3D', end_kicker='Custom battery packs',
  end_h=f'<em>{kw("14S8P")}</em>,<br>decoded', end_chips=['50.4 V', '28 Ah', '80 A'], end_img='li_steel_52v.jpg',
  note="What's your pack's S and P? Tell us in the comments", ai=False,
  scenes=[
   dict(img='diag_14s8p.png', k='Pack codes', h=f'What does<br><em>{kw("14S8P")}</em> mean?', s=''),
   dict(img='diag_14s8p.png', k='S = series', h=f'<em>14</em> in series<br>= {kw("50.4 V")}', s='14 × 3.6 V nominal'),
   dict(img='li_open_52v.jpg', k='P = parallel', h=f'<em>8</em> in parallel<br>= {kw("28 Ah")}', s='8 × 3.5 Ah cells'),
   dict(img='li_exploded_52v.jpg', k='Current', h=f'<em>{kw("80 A")}</em><br>discharge', s='8 parallel cells × 10 A'),
   dict(img='diag_14s8p.png', k='Energy', h=f'≈ <em>{kw("1.41 kWh")}</em>', s='112 cells · 50.4 V × 28 Ah'),
  ]),
}
_EL = '/home/claude/claude/tts/out'
for _n, _r in REELS.items():
    for _i, _s in enumerate(_r['scenes']):
        _s['vo'] = [('file', f'{_EL}/will_{_n}/s{_i+1}.mp3', 1.0)]
    _r['end_vo'] = [('file', f'{_EL}/will_{_n}/end.mp3', 1.0)]
