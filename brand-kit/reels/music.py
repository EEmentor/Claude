import numpy as np, soundfile as sf
from scipy.signal import butter, lfilter
SR=48000; BPM=112; beat=60/BPM; bars=16; L=int(bars*4*beat*SR)
rng=np.random.default_rng(7); mix=np.zeros((L,2))
def add(sig,t,pan=0.5,g=1.0):
    i=int(t*SR); n=min(len(sig),L-i)
    if n<=0: return
    mix[i:i+n,0]+=sig[:n]*g*(1-pan)*2*0.5; mix[i:i+n,1]+=sig[:n]*g*pan*2*0.5
def env(n,a=0.002,d=0.2):
    t=np.arange(n)/SR; return np.minimum(t/a,1)*np.exp(-t/d)
def bp(x,lo,hi):
    b,a=butter(2,[lo/(SR/2),hi/(SR/2)],'band'); return lfilter(b,a,x)
def hp(x,f):
    b,a=butter(2,f/(SR/2),'high'); return lfilter(b,a,x)
def lp(x,f):
    b,a=butter(2,f/(SR/2),'low'); return lfilter(b,a,x)
# drums
n=int(.35*SR); t=np.arange(n)/SR
kick=np.sin(2*np.pi*(45*t+ (110/18)*(1-np.exp(-18*t))))*np.exp(-t/0.16)
n2=int(.25*SR); clap=bp(rng.standard_normal(n2),900,3500)*env(n2,0.001,0.06)*0.8
n3=int(.06*SR); hat=hp(rng.standard_normal(n3),7000)*env(n3,0.0005,0.015)*0.35
# harmony Am F C G
roots=[45,41,48,43]  # midi bass notes
chords=[[57,60,64],[53,57,60],[52,55,60],[50,55,59]]
mf=lambda m:440*2**((m-69)/12)
for bar in range(bars):
    b0=bar*4*beat; ci=bar%4
    for k in range(4):
        add(kick,b0+k*beat,0.5,0.9 if bar>=1 else 0.0)
        if k in (1,3): add(clap,b0+k*beat,0.5,0.55 if bar>=2 else 0)
        for h in range(2): add(hat,b0+k*beat+h*beat/2,0.65 if h else 0.35,0.9 if bar>=1 else 0.5)
    # bass 8ths
    f=mf(roots[ci]); nb=int(beat/2*SR*0.9); tb=np.arange(nb)/SR
    saw=2*((f*tb)%1)-1; bass=lp(saw,600)*env(nb,0.003,0.18)*0.5
    for e in range(8): add(bass,b0+e*beat/2,0.5,1.0 if bar>=1 else 0)
    # plucky chord stabs on offbeats
    npk=int(.5*SR); tp=np.arange(npk)/SR
    pl=sum(np.sin(2*np.pi*mf(m+12)*tp)+0.3*np.sin(2*np.pi*2*mf(m+12)*tp) for m in chords[ci])*np.exp(-tp/0.12)*0.16
    for e in (1,3,5,7): add(pl,b0+e*beat/2,0.3 if e%4==1 else 0.7,1.0)
    # soft pad
    npd=int(4*beat*SR); td=np.arange(npd)/SR
    pad=sum(np.sin(2*np.pi*mf(m)*td+np.sin(2*np.pi*0.3*td)) for m in chords[ci])*0.05
    pad*=np.minimum(td/0.4,1)*np.minimum((4*beat-td)/0.4,1); add(pad,b0,0.5,1.0)
mix/=np.max(np.abs(mix))+1e-9; mix*=0.5
sf.write('music_bed.wav',mix,SR)
# whoosh
n=int(.55*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
out=np.zeros(n); seg=int(.01*SR)
for i in range(0,n,seg):
    fc=300+5000*(i/n)**1.5; out[i:i+seg]=bp(x[i:i+seg+200],fc,min(fc*2.5,20000))[:len(out[i:i+seg])]
w=out*np.sin(np.pi*t/t[-1])**2; w/=np.max(np.abs(w)); sf.write('whoosh.wav',np.stack([w*0.5,w*0.5],1),SR)
print(L/SR)
