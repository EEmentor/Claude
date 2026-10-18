kw = lambda t: f'<span style="text-transform:none">{t}</span>'
REELS = {
 'lipo': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Get a quote',
  end_kicker='Custom LiPo battery packs', end_h='Flat, light,<br><em>built for you</em>',
  end_chips=['Mobile robots', 'Portable power', 'RC models'], end_img='lipo_pvc.jpg',
  end_vo='Built to order in twenty-five to thirty days. So... what are you building?', note='Built to order · 25–30 days',
  scenes=[
   dict(img='lipo_unwrapped.jpg', k='LiPo battery packs', h='Flat cells.<br><em>No wasted space.</em>', s='', vo='Flat cells. No wasted space!'),
   dict(img='lipo_unwrapped.jpg', k='Lithium polymer', h='Pouch cells,<br><em>stacked tight</em>', s='Slim and light for the energy it carries', vo='Lipo pouch cells stack flat, so your pack stays slim... and seriously light.'),
   dict(img='lipo_pvc.jpg', k='3S, 4S and 6S builds', h=f'<em>{kw("11.1V")} to {kw("22.2V")}</em>', s='Example packs from 1.35 Ah up to 12 Ah', vo='Need eleven volts? Twenty-two? We build three-S, four-S and six-S packs.'),
   dict(img='lipo_abs.jpg', k='Protection', h='BMS <em>or balance lead</em>', s='Over-charge, over-discharge, over-current and short-circuit protection, or a balance lead for your charger', vo='Want a full B M S? Or just a balance lead for your charger? Your call.'),
   dict(img='lipo_steel.jpg', k='Enclosure', h='Heat-shrink,<br><em>ABS or steel</em>', s='Protected against bending and puncture', vo='Heat-shrink, A B S, or steel...'),
   dict(img='connectors.jpg', k='Connector', h=f'<em>{kw("XT60")}, {kw("XT90")},</em><br>Anderson, {kw("EC5")}…', s='Fitted to your specification', vo='with the connector you actually use.'),
  ]),
 'deep': dict(
  url='energy.eementor.co/pages/deep-cycle-batteries', button='See the range',
  end_kicker='Deep cycle batteries', end_h=f'Drop-in <em>{kw("LiFePO4")}</em>',
  end_chips=['RV', 'Marine', 'Golf carts', 'Solar'], end_img='deep_cold5.webp',
  end_vo='Ready to upgrade? Check out the full range. Link below!', ai=True,
  scenes=[
   dict(img='deep_compact5.webp', k='Lead-acid replacement', h='Still hauling<br><em>lead-acid?</em>', s='', vo="Still hauling heavy lead-acid batteries? Let's fix that."),
   dict(img='deep_compact5.webp', k='Drop-in LiFePO4', h=f'<em>{kw("6.4V")} to {kw("51.2V")}</em>,<br>up to {kw("200Ah")}', s='Maintenance free, series and parallel ready', vo='Drop-in lithium iron phosphate. Six point four to fifty-one point two volts, up to two hundred amp-hours.'),
   dict(img='deep_cold5.webp', k='Low-temperature series', h='Made for<br><em>cold mornings</em>', s='Low-temperature charging and self-heating models', vo='Freezing morning in the camper? Low-temp and self-heating models have you covered.'),
   dict(img='deep_smart5.webp', k='Smart series', h='Check it<br><em>on your phone</em>', s='Bluetooth and Wi-Fi monitoring on smart models', vo='Wondering how much charge is left? Just check your phone.'),
   dict(img='deep_starter5.webp', k='LiFePO4 starter batteries', h='Up to <em>70% lighter</em><br>than lead-acid', s='For motorcycles, cars, jet skis, UTVs and ATVs', vo='Starter batteries? Up to seventy percent lighter than lead-acid. Yes, really.'),
   dict(img='deep_golf5.webp', k='Mobility packs', h='Golf carts<br><em>and wheelchairs</em>', s='51.2V golf cart packs up to 10.24 kWh', vo="Golf cart or wheelchair? We've got packs for those too."),
  ]),
 'liion': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Get a quote',
  end_kicker='Custom lithium-ion packs', end_h='Engineered for<br><em>your application</em>',
  end_chips=['Robots & AGVs', 'Drones', 'E-mobility', 'Medical'], end_img='li_pvc_52v.jpg',
  end_vo='So, what are you building? Tell us. Link below!', note='Prototypes: no MOQ · 25–30 days',
  scenes=[
   dict(img='hero_pack.webp', k='Custom battery packs', h='Your product.<br><em>Your battery.</em>', s='', vo='Your product is one of a kind. So why settle for a generic battery?'),
   dict(img='li_exploded_52v.jpg', k='Inside the pack', h='Engineered<br><em>inside and out</em>', s='Cells, holders, nickel strip and BMS (illustration)', vo='We engineer every pack around your application. Cells, holders, nickel strip, B M S. All of it.'),
   dict(img='li_open_52v.jpg', k='Genuine cells', h='Named cells from<br><em>known makers</em>', s='Samsung · LG · Molicel · Murata · Panasonic · EVE', vo='Genuine cells only. Samsung, L G, Molicel, Murata, Panasonic, EVE.'),
   dict(img='li_pvc_52v.jpg', k='Prototypes', h='<em>No minimum order</em><br>for prototypes', s='Typically ready in 25–30 days', vo='Just need one prototype? No problem. No minimum order, and typically ready in twenty-five to thirty days.'),
   dict(img='li_steel_52v.jpg', k='Quality', h='Tested and<br><em>documented</em>', s='QC report with batch and date-code traceability', vo='Every shipment comes with a test report, traceable down to batch and date code.'),
   dict(img='connectors.jpg', k='Your choice', h='Your enclosure,<br><em>your connector</em>', s='PVC, ABS or steel · XT60, XT90, Anderson, EC5 and more', vo='Pick your enclosure. Pick your connector. Done.'),
  ]),
}
REELS.update({
 'cells': dict(
  url='energy.eementor.co/collections/loose-cells', button='Shop cells',
  end_kicker='Battery cells', end_h='Genuine cells,<br><em>traceable</em>',
  end_chips=['18650', '21700', f'{kw("LiFePO4")} 32700', 'LiPo pouch'], end_img='cell_40pl.jpg',
  end_vo='Want them loose, or built into a pack? Either way... link below!', note='Batch and date-code traceability',
  scenes=[
   dict(img='cell_p42a.jpg', k='Battery cells', h='Genuine cells.<br><em>Named makers.</em>', s='', vo="Ever wondered what's really inside a cheap battery? With us, you know exactly."),
   dict(img='cell_40t.jpg', k='21700 cells', h='Samsung, Molicel,<br><em>EVE</em>', s='Samsung 40T · Molicel P42A · EVE 40PL', vo='Looking for twenty-one seven hundred cells? Samsung, Molicel, EVE.'),
   dict(img='cell_vtc6.jpg', k='18650 cells', h='The <em>18650</em><br>classics', s='LG MJ1 · Murata VTC6 · Panasonic GA · Molicel P28A', vo='Prefer eighteen-six-fifty? L G, Murata, Panasonic, Molicel. Take your pick.'),
   dict(img='cell_lfp32700.jpg', k=f'{kw("LiFePO4")} cells', h=f'<em>{kw("IFR32700")}</em><br>for storage', s='Lithium iron phosphate for long cycle life', vo='Building energy storage? Thirty-two seven hundred lithium iron phosphate cells.'),
   dict(img='cell_lipo22000.jpg', k='LiPo pouch cells', h=f'Flat, up to<br><em>{kw("22,000 mAh")}</em>', s='3.7V pouch cells from 5,000 to 22,000 mAh', vo='Need it flat? LiPo pouch cells, all the way up to twenty-two thousand milliamp-hours.'),
  ]),
 'process': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Send your brief',
  end_kicker='Prototype first', end_h='Start with<br><em>one prototype</em>',
  end_chips=['Start-ups', 'OEMs', 'Small volumes'], end_img='lfp_12v.jpg',
  end_vo='Got a product in mind? Send us the brief. Link below!', note='No minimum order for prototypes',
  scenes=[
   dict(img='hero_pack.webp', k='Custom battery packs', h='How a custom pack<br><em>gets made</em>', s='', vo="So how does a custom battery actually get made? Let's walk through it."),
   dict(img='li_exploded_52v.jpg', k='Step 1 · Your brief', h='It starts with<br><em>your application</em>', s='Voltage, capacity, peak current, size, BMS and connectors', vo='Step one. You tell us about your application. Voltage, current, size... the lot.'),
   dict(img='li_open_52v.jpg', k='Step 2 · Engineering review', h='Engineers choose<br><em>the right cells</em>', s='Genuine cells from named makers', vo='Step two. Our engineers review it, and choose the right cells.'),
   dict(img='li_pvc_52v.jpg', k='Step 3 · Prototype', h='<em>No minimum</em><br>order', s='Typically 25–30 days after the spec is agreed', vo='Step three. A working prototype. No minimum order, usually in twenty-five to thirty days.'),
   dict(img='abs_52v.jpg', k='Step 4 · Validate', h='Test it in<br><em>your product</em>', s='Then a pilot run', vo='Step four. You test it in your own product. Then, a pilot run.'),
   dict(img='li_steel_52v.jpg', k='Step 5 · Production', h='Scale up,<br><em>documented</em>', s='Typically around 30 days · test report with every shipment', vo='And step five? Production. Typically around thirty days, with a test report in every shipment.'),
  ]),
 'ess': dict(
  url='energy.eementor.co/pages/energy-storage', button='See the range',
  end_kicker='Energy storage systems', end_h='From home<br>to <em>industrial</em>',
  end_chips=['Home backup', 'Solar', 'Telecom', 'Off-grid'], end_img='ess_rack.webp',
  end_vo='Home, business, or off-grid? Find your system. Link below!', ai=True,
  scenes=[
   dict(img='ess_cabinet.webp', k='Energy storage', h='Power that<br><em>stays on</em>', s='', vo="Power cut... again? Let's talk energy storage."),
   dict(img='ess_aio.webp', k='All-in-one ESS', h=f'Battery +<br><em>{kw("5 kW")} inverter</em>', s='5–20 kWh LiFePO4 stack with MPPT solar input', vo='Want it all in one box? A five kilowatt inverter, solar input, and five to twenty kilowatt-hours of storage.'),
   dict(img='ess_wall.webp', k='Wall-mounted', h='On the wall,<br><em>out of the way</em>', s='2.4 to 10.24 kWh units, up to 15 in parallel', vo='Short on floor space? Put it on the wall. Up to fifteen units in parallel.'),
   dict(img='ess_rack.webp', k='Rack-mounted modules', h='Stack it<br><em>as you grow</em>', s='48V / 51.2V modules with an independent BMS in each', vo='Need more later? Stack rack modules. Each one has its own B M S.'),
   dict(img='ess_cabinet.webp', k='Cabinet systems', h=f'Up to<br><em>{kw("230 kWh")}</em>', s='LV and HV cabinets for telecom, data centres and industry', vo='Running a business? Cabinet systems scale up to two hundred and thirty kilowatt-hours.'),
   dict(img='ess_smart.webp', k='Drop-in batteries', h='Smaller jobs?<br><em>Drop-in</em>', s='12V and 24V, 6Ah to 300Ah, with Bluetooth and Wi-Fi models', vo='Smaller job? Drop-in twelve and twenty-four volt batteries, with Bluetooth on the smart models.'),
  ]),
})
REELS.update({
 'lfp': dict(
  url='energy.eementor.co/pages/energy-storage', button='See the range',
  end_kicker=f'{kw("LiFePO4")} energy storage', end_h='Built to <em>last</em>',
  end_chips=['Home backup', 'Solar', 'Telecom', 'C&I'], end_img='ess_wall.webp',
  end_vo="Planning storage for a home or a site? Let's size it together. Link below!", ai=True,
  scenes=[
   dict(img='ess_dropin.webp', k='Energy storage', h=f'Why <em>{kw("LiFePO4")}</em>?', s='', vo='Why do so many energy storage systems use lithium iron phosphate? Here is why.'),
   dict(img='cell_lfp32700.jpg', k='The chemistry', h='Lithium iron<br><em>phosphate</em>', s='Less energy per kilo, but long cycle life and high thermal stability', vo='It stores a bit less energy per kilo than other lithium cells... but it lasts, and it stays stable.'),
   dict(img='ess_rack.webp', k='Cycle life', h=f'<em>3,000+</em> cycles', s='Rack and cabinet modules: 3,000+ cycles at 80% and 5,000+ at 60% depth of discharge (25 °C, 0.5C)', vo='Our rack and cabinet modules are rated for over three thousand cycles at eighty percent depth of discharge.'),
   dict(img='ess_wall.webp', k='Wall-mounted units', h='Built for<br><em>hot climates</em>', s='Operating range −20 to 60 °C · 5,000+ cycles at 80% DOD (25 °C)', vo='The wall units work from minus twenty up to sixty degrees. Hot summers? No problem.'),
   dict(img='ess_cabinet.webp', k='Design life', h='<em>10 years</em><br>or more', s='Design life of 10+ years on wall and cabinet systems', vo='And they are designed to last ten years or more.'),
   dict(img='ess_aio.webp', k='Certified', h=f'{kw("UL 1973")} ·<br><em>{kw("IEC 62619")}</em>', s='Plus UN38.3 on standard rack and wall models (per datasheet)', vo='Standard models are certified to U L nineteen seventy-three, and I E C sixty-two six nineteen.'),
  ]),
 'quality': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Get a quote',
  end_kicker='Custom battery packs', end_h='Quality you<br>can <em>trace</em>',
  end_chips=['Genuine cells', 'Test reports', 'Traceability'], end_img='lfp_12v.jpg',
  end_vo='Want a pack you can trust? Tell us what you need. Link below!',
  scenes=[
   dict(img='cell_40t.jpg', k='Quality', h='Where do your<br><em>cells</em> come from?', s='', vo='Where do the cells in your battery actually come from? You should know.'),
   dict(img='cell_p42a.jpg', k='Genuine cells', h='Named makers<br><em>only</em>', s='Samsung · LG · Molicel · Murata · Panasonic · EVE', vo='We use genuine cells from named makers. Samsung, L G, Molicel, Murata, Panasonic, EVE.'),
   dict(img='li_open_52v.jpg', k='Traceability', h='Batch and<br><em>date code</em>', s='Traceable on every shipment', vo='Every shipment is traceable, down to batch and date code.'),
   dict(img='li_steel_52v.jpg', k='Tested', h='A test report<br><em>every time</em>', s='Every shipment is quality-checked and comes with a test report', vo='Every shipment is checked... and comes with a test report.'),
   dict(img='li_pvc_52v.jpg', k='Standards', h=f'<em>{kw("UN 38.3")}</em> and<br><em>{kw("IEC 62133")}</em>', s='Standard models tested and CE marked · custom designs certified for your market', vo='Standard models are tested to U N thirty-eight point three and I E C sixty-two one thirty-three.'),
   dict(img='abs_52v.jpg', k='Production', h=f'{kw("ISO 9001")}<br><em>production</em>', s='ISO 9001-certified manufacturing partner · up to 400,000 batteries a month', vo='Built with an I S O nine thousand one certified partner. Up to four hundred thousand batteries a month.'),
  ]),
 'studio': dict(
  url='energy.eementor.co/pages/battery-builder', button='Open the Studio',
  end_kicker='Battery Design Studio', end_h='Start<br><em>designing</em>',
  end_chips=['18650', '21700', 'LiPo', 'Up to 24S'], end_img='end_pack.png',
  end_vo='So... what would you build? Try it. Link below!',
  scenes=[
   dict(img='ds_pack.png', k='Battery Design Studio', h='Design your pack<br><em>in 3D</em>', s='', vo='What if you could design your battery pack right in your browser? You can.'),
   dict(img='ds_cells.png', k='Step 1 · Cells', h='Pick <em>real cells</em>', s='18650, 21700 or LiPo pouch from Samsung, LG, Molicel, Murata, EVE and more', vo='First, pick your cells. Eighteen-six-fifty, twenty-one seven hundred, or LiPo pouch.'),
   dict(img='ds_config.png', k='Step 2 · Layout', h='Series <em>×</em><br>parallel', s='Set the layout, up to 24S', vo='Then set series and parallel. Up to twenty-four in series.'),
   dict(img='ds_stats.png', k='Step 3 · Estimates', h='See the numbers<br><em>as you go</em>', s='Example 10S4P: 36 V, 14 Ah, 504 Wh (estimates from typical datasheet values)', vo='And watch voltage, capacity, energy and discharge update as you go.'),
   dict(img='end_pack.png', k='Not sure where to start?', h='Describe it<br><em>in plain words</em>', s='For example: "24V robot, 6h at 15A"', vo='Not sure where to start? Just describe it. Like... twenty-four volt robot, six hours at fifteen amps.'),
   dict(img='hero_pack.webp', k='Engineer review', h='We confirm<br><em>the final spec</em>', s='Our engineers review your design and reply with pricing and lead time', vo='Then our engineers review it, and reply with pricing and lead time.'),
  ]),
})
