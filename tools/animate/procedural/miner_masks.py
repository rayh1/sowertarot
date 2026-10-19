"""Masks for The Miner clip (2026-10-16): gold flecks on the ore (miner_gold.png) and lamplight on the rock walls and ceiling (miner_lamplight_rock.png). Run in tools/animate/procedural."""
from PIL import Image, ImageDraw; import numpy as np; from scipy import ndimage as nd
art=Image.open('../batch/the-miner/art.png').convert('RGB'); a=np.array(art).astype(float); R,G,B=a[...,0],a[...,1],a[...,2]; H,W=R.shape
def poly(pts):
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(pts,fill=255); return np.array(m)>128
coarse=poly([(400,620),(610,620),(770,830),(770,990),(700,1060),(725,1480),(560,1530),(170,1510),(160,1380),(255,1240),(265,1050),(285,850),(385,770)])
warm=((R-B>40)&(R>100))|((R-B>20)&(R>80))
fig=nd.binary_fill_holes(nd.binary_closing(warm&coarse,iterations=8))
lab,n=nd.label(fig); sz=nd.sum(fig,lab,range(1,n+1)); fig=lab==(np.argmax(sz)+1)
ore=poly([(598,882),(612,850),(650,836),(700,843),(738,853),(748,895),(738,937),(700,952),(640,950),(598,927)])
fig=nd.binary_dilation(fig,iterations=4)|ore
lampbox=poly([(760,1180),(960,1180),(960,1500),(760,1500)])
lamp=nd.binary_dilation(nd.binary_fill_holes(nd.binary_closing(((R-B>40)&(R>90))&lampbox,iterations=5)),iterations=4)
floor=poly([(0,1530),(100,1490),(110,1270),(300,1210),(700,1345),(790,1385),(940,1480),(1024,1505),(1024,1792),(0,1792)])
heap=poly([(50,1030),(130,1000),(210,1015),(270,1110),(260,1265),(80,1275),(50,1180)])
rock=~(fig|lamp|floor|heap)
Image.fromarray((rock*255).astype(np.uint8)).save('miner_rock_mask.png')
soft=nd.gaussian_filter(rock.astype(float),6)
Y,X=np.mgrid[0:H,0:W].astype(float); w=np.exp(-np.hypot(X-860,Y-1160)/850)
Image.fromarray((soft*w*255).astype(np.uint8)).save('miner_lamplight_rock.png')
gold=(R>170)&(G>140)&(R-B>90)&(G-B>70); box=np.zeros_like(gold); box[830:965,585:750]=True; gold&=box
lab,n=nd.label(gold); sz=nd.sum(gold,lab,range(1,n+1))
keep=nd.binary_dilation(np.isin(lab,[i+1 for i,s in enumerate(sz) if s>=6]),iterations=1)
Image.fromarray((keep*255).astype(np.uint8)).save('miner_gold.png')
