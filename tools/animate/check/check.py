import json, subprocess, sys, os, numpy as np
HERE=os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,os.path.join(HERE,'../../../skills/tarot-card-generator/scripts'))
from animate_compose import cover_resize
from PIL import Image, ImageDraw
from multiprocessing import Pool
B=os.path.normpath(os.path.join(HERE,'../batch')); OUT=HERE
W,H=1024,1792
def frames(p):
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,H,W,3)
def card(slug):
    res={}; clips={}
    for s in (2,3,4):
        p=f'{B}/{slug}/{slug}_s{s}.mp4'
        if os.path.exists(p): clips[s]=frames(p)
    # motion region: union over seeds of temporal std
    margin=round(W*0.020); border=max(2,round(W*0.008)); bh=round(H*0.085)
    il,it,ir,ib=margin+border,margin+border,W-margin-border,H-margin-border; bt=ib-bh
    def place(img,mode):
        full=Image.new(mode,(W,H),0); full.paste(cover_resize(img,ir-il,ib-it).crop((0,0,ir-il,bt-it)),(il,it)); return full
    mk=np.array(place(Image.open(f'{B}/{slug}/mask.png').convert('L'),'L'))
    orig=np.array(place(Image.open(f'{B}/{slug}/art.png').convert('RGB'),'RGB'))
    reg=mk>128
    ys,xs=np.nonzero(mk>24)
    if len(ys)==0: return slug,{'error':'no motion'},None
    y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max()
    for s,c in clips.items():
        f=c.astype(np.int16); m=reg
        d4=np.abs(f[4:]-f[:-4]).mean(-1)[:,m].mean()
        d1=np.abs(f[1:]-f[:-1]).mean(-1)[:,m].mean(1)
        jump=np.abs(f[0]-f[-1]).mean(-1)[m].mean()
        white=(c[...,:].min(-1)>240)[:,m].mean(1)
        res[s]=dict(motion=round(float(d4),1),step=round(float(np.median(d1)),2),stepmax=round(float(d1.max()),2),jump=round(float(jump),2),white0=round(float(white[0]),3),whitemax=round(float(white.max()),3))
    # sheet: rows seeds, cols frames, crop bbox padded
    pad=20; y0=max(0,y0-pad);y1=min(H,y1+pad);x0=max(0,x0-pad);x1=min(W,x1+pad)
    th=330; sc=th/(y1-y0); tw=int((x1-x0)*sc)
    if tw>420: sc=420/(x1-x0); tw=420; th=int((y1-y0)*sc)
    idx=[None,0,27,54,81,108]
    sheet=Image.new('RGB',(tw*len(idx)+10*len(idx),(th+20)*len(clips)+20),'white'); dr=ImageDraw.Draw(sheet)
    dr.text((5,3),f'{slug}  crop y{y0}-{y1} x{x0}-{x1}',fill='black')
    for r,(s,c) in enumerate(clips.items()):
        for k,i in enumerate(idx):
            im=Image.fromarray((orig if i is None else c[min(i,len(c)-1)])[y0:y1,x0:x1]).resize((tw,th))
            sheet.paste(im,(k*(tw+10),20+r*(th+20)))
            dr.text((k*(tw+10)+3,20+r*(th+20)+th+2),f's{s} '+('ORIG' if i is None else f'f{i}'),fill='black')
    sheet.save(f'{OUT}/{slug}.png')
    return slug,res,(int(y0),int(y1),int(x0),int(x1))
if __name__=='__main__':
    slugs=sorted({j['slug'] for j in json.load(open(f'{B}/jobs.json'))})
    with Pool(6) as p: out=p.map(card,slugs)
    json.dump({s:{'seeds':r,'bbox':b} for s,r,b in out},open(f'{OUT}/metrics.json','w'),indent=1)
    for s,r,b in out:
        print(s,b); [print('  ',k,v) for k,v in r.items()]
