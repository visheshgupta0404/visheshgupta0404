"""Animate the supplied ASCII portrait with a subtle terminal scan; Pillow only.
No AI face generation, facial morphing, cropping or stretching.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
P=Path(__file__).resolve().parents[1]; A=P/'assets'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
W,H=460,530
source=Image.open(A/'ascii-portrait.png').convert('RGB')
source.thumbnail((436,438),Image.Resampling.LANCZOS)
base=Image.new('RGB',(W,H),'#020709'); base.paste(source,((W-source.width)//2,48))
d=ImageDraw.Draw(base)
d.rounded_rectangle((1,1,W-2,H-2),10,outline='#126078',width=1)
for x,c in [(16,'#ff5f57'),(34,'#febc2e'),(52,'#28c840')]:d.ellipse((x,15,x+8,23),fill=c)
d.text((76,11),'VISHESH / ASCII TERMINAL',font=ImageFont.truetype(FONT,15),fill='#45d9ff')
d.line((1,36,W-2,36),fill='#126078')
d.line((1,492,W-2,492),fill='#126078')
d.text((14,505),'$ code . build . learn',font=ImageFont.truetype(FONT,16),fill='#00ed83')
frames=[]
for i in range(36):
 frame=base.copy(); draw=ImageDraw.Draw(frame)
 # One gentle scan sweep per 3.6 seconds; the original portrait stays visible.
 y=48+round(i*(source.height-1)/35)
 overlay=Image.new('RGB',(source.width,2),'#45d9ff')
 region=frame.crop(((W-source.width)//2,y,(W+source.width)//2,y+2))
 frame.paste(Image.blend(region,overlay,0.12),((W-source.width)//2,y))
 draw.line((3,y,8,y),fill='#45d9ff',width=2)
 draw.line((W-9,y,W-4,y),fill='#45d9ff',width=2)
 if i%18<9:draw.rectangle((257,509,266,522),fill='#45d9ff')
 frames.append(frame)
# Fixed palette avoids color flicker; differential frames keep the GIF small.
palette=base.quantize(colors=252,method=Image.Quantize.MEDIANCUT)
p=palette.getpalette();p[252*3:255*3]=[69,217,255,0,237,131,18,96,120];palette.putpalette(p)
frames=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
frames[0].save(A/'ascii-portrait-animated.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=1)
with Image.open(A/'ascii-portrait-animated.gif') as out:
 assert out.n_frames==36 and out.size==(W,H)
print((A/'ascii-portrait-animated.gif').stat().st_size,'bytes; 36 frames; 3.6-second loop')
