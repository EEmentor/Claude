kw = lambda t: f'<span style="text-transform:none">{t}</span>'
REELS = {
 'lipo': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Get a quote',
  end_kicker='Custom LiPo battery packs', end_h='Flat, light,<br><em>built for you</em>',
  end_chips=['Mobile robots', 'Portable power', 'RC models'], end_img='lipo_pvc.jpg',
  end_vo='Built to order in twenty-five to thirty days. Get your quote today.', note='Built to order · 25–30 days',
  scenes=[
   dict(img='lipo_unwrapped.jpg', k='LiPo battery packs', h='Flat cells.<br><em>No wasted space.</em>', s='', vo='Flat cells. No wasted space.'),
   dict(img='lipo_unwrapped.jpg', k='Lithium polymer', h='Pouch cells,<br><em>stacked tight</em>', s='Slim and light for the energy it carries', vo='Lipo pouch cells stack flat, so the pack stays slim and light for the energy it carries.'),
   dict(img='lipo_pvc.jpg', k='3S, 4S and 6S builds', h=f'<em>{kw("11.1V")} to {kw("22.2V")}</em>', s='Example packs from 1.35 Ah up to 12 Ah', vo='We build lipo packs from eleven point one to twenty-two point two volts.'),
   dict(img='lipo_abs.jpg', k='Protection', h='BMS <em>or balance lead</em>', s='Over-charge, over-discharge, over-current and short-circuit protection, or a balance lead for your charger', vo='Choose a protective B M S, or a balance lead for your own lipo charger.'),
   dict(img='lipo_steel.jpg', k='Enclosure', h='Heat-shrink,<br><em>ABS or steel</em>', s='Protected against bending and puncture', vo='Finish it in heat-shrink, an A B S case, or a steel case,'),
   dict(img='connectors.jpg', k='Connector', h=f'<em>{kw("XT60")}, {kw("XT90")},</em><br>Anderson, {kw("EC5")}…', s='Fitted to your specification', vo='with the connector you need.'),
  ]),
 'deep': dict(
  url='energy.eementor.co/pages/deep-cycle-batteries', button='See the range',
  end_kicker='Deep cycle batteries', end_h=f'Drop-in <em>{kw("LiFePO4")}</em>',
  end_chips=['RV', 'Marine', 'Golf carts', 'Solar'], end_img='deep_cold5.webp',
  end_vo='See the full range. The link is below.', ai=True,
  scenes=[
   dict(img='deep_compact5.webp', k='Lead-acid replacement', h='Still hauling<br><em>lead-acid?</em>', s='', vo='Still hauling lead-acid batteries?'),
   dict(img='deep_compact5.webp', k='Drop-in LiFePO4', h=f'<em>{kw("6.4V")} to {kw("51.2V")}</em>,<br>up to {kw("200Ah")}', s='Maintenance free, series and parallel ready', vo='Our drop-in lithium iron phosphate batteries run from six point four to fifty-one point two volts, up to two hundred amp-hours.'),
   dict(img='deep_cold5.webp', k='Low-temperature series', h='Made for<br><em>cold mornings</em>', s='Low-temperature charging and self-heating models', vo='Low-temperature and self-heating models are made for cold mornings in the camper or on the boat.'),
   dict(img='deep_smart5.webp', k='Smart series', h='Check it<br><em>on your phone</em>', s='Bluetooth and Wi-Fi monitoring on smart models', vo='Smart models show your battery on your phone, over Bluetooth or Wi-Fi.'),
   dict(img='deep_starter5.webp', k='LiFePO4 starter batteries', h='Up to <em>70% lighter</em><br>than lead-acid', s='For motorcycles, cars, jet skis, UTVs and ATVs', vo='And our starter batteries are up to seventy percent lighter than lead-acid.'),
   dict(img='deep_golf5.webp', k='Mobility packs', h='Golf carts<br><em>and wheelchairs</em>', s='51.2V golf cart packs up to 10.24 kWh', vo='There are packs for golf carts and wheelchairs, too.'),
  ]),
 'liion': dict(
  url='energy.eementor.co/pages/custom-battery-packs', button='Get a quote',
  end_kicker='Custom lithium-ion packs', end_h='Engineered for<br><em>your application</em>',
  end_chips=['Robots & AGVs', 'Drones', 'E-mobility', 'Medical'], end_img='li_pvc_52v.jpg',
  end_vo="Tell us what you're building. The link is below.", note='Prototypes: no MOQ · 25–30 days',
  scenes=[
   dict(img='hero_pack.webp', k='Custom battery packs', h='Your product.<br><em>Your battery.</em>', s='', vo='Your product is unique. Your battery should be too.'),
   dict(img='li_exploded_52v.jpg', k='Inside the pack', h='Engineered<br><em>inside and out</em>', s='Cells, holders, nickel strip and BMS (illustration)', vo='Every custom lithium-ion pack is engineered around your application: cells, holders, nickel strip and B M S.'),
   dict(img='li_open_52v.jpg', k='Genuine cells', h='Named cells from<br><em>known makers</em>', s='Samsung · LG · Molicel · Murata · Panasonic · EVE', vo='We use genuine cells from Samsung, L G, Molicel, Murata, Panasonic and EVE.'),
   dict(img='li_pvc_52v.jpg', k='Prototypes', h='<em>No minimum order</em><br>for prototypes', s='Typically ready in 25–30 days', vo='There is no minimum order for prototypes, and they are typically ready in twenty-five to thirty days.'),
   dict(img='li_steel_52v.jpg', k='Quality', h='Tested and<br><em>documented</em>', s='QC report with batch and date-code traceability', vo='Every shipment comes with a quality test report, with batch and date-code traceability.'),
   dict(img='connectors.jpg', k='Your choice', h='Your enclosure,<br><em>your connector</em>', s='PVC, ABS or steel · XT60, XT90, Anderson, EC5 and more', vo='Choose your enclosure and your connector.'),
  ]),
}
