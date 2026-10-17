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
