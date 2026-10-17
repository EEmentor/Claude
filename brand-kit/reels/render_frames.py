import sys,os,subprocess
from playwright.sync_api import sync_playwright
page_path,H,outdir,times=sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4]
os.makedirs(outdir,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':H})
    pg.goto('file://'+page_path); pg.wait_for_timeout(800)
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    if times=='all':
        END=float(sys.argv[5]); n=int(END*30)
        ts=[i/30 for i in range(n)]
    else: ts=[float(x) for x in times.split(',')]
    for i,t in enumerate(ts):
        pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t*1000})")
        pg.screenshot(path=f'{outdir}/f{i:05d}.jpg',type='jpeg',quality=92)
    b.close()
