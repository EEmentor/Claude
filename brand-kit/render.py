import sys,os,re
from playwright.sync_api import sync_playwright
S=sys.argv[1]; files=sys.argv[2:]
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in files:
        html=open(os.path.join(S,f)).read(); w,h=map(int,re.search(r'data-size="(\d+)x(\d+)"',html).groups())
        pg=b.new_page(viewport={'width':w,'height':h})
        pg.goto('file://'+os.path.join(S,f)); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        out=os.path.join(S,'out',f.replace('.html','.png')); pg.screenshot(path=out,clip={'x':0,'y':0,'width':w,'height':h}); pg.close(); print(out)
    b.close()
