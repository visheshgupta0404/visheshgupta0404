"""Build equal-sized local technology tiles from the existing Simple Icons masks."""
from pathlib import Path
from PIL import Image, ImageDraw
A=Path(__file__).resolve().parents[1]/'assets'
source=Image.open(A/'tech-icon-masks.png').convert('L')
icons=[('python',0,'#53b5e5'),('java',1,'#f1884e'),('javascript',2,'#f5d449'),('sql',3,'#70c6eb'),('react',4,'#61dafb'),('nodejs',5,'#85c96b'),('fastapi',6,'#23cbb2'),('postgresql',7,'#70a7d4'),('docker',8,'#34b5f0'),('git',9,'#f56e51'),('scikit-learn',10,'#efa24c')]
for slug,i,color in icons:
 im=Image.new('RGB',(96,96),'#020709');d=ImageDraw.Draw(im)
 d.rounded_rectangle((1,1,94,94),10,outline='#126078',width=1)
 if slug=='sql':
  # SQL has no single official language logo; use a standard database symbol.
  d.line((26,31,26,66),fill=color,width=3);d.line((70,31,70,66),fill=color,width=3)
  d.arc((26,55,70,77),0,180,fill=color,width=3)
  d.arc((26,38,70,60),0,180,fill=color,width=3)
  d.ellipse((26,20,70,42),outline=color,width=3)
 else:
  mask=source.crop((96*i,0,96*(i+1),96)).resize((52,52),Image.Resampling.LANCZOS)
  im.paste(color,(22,22,74,74),mask)
 im.save(A/f'tech-{slug}.png',optimize=True)
print('Built 11 consistent icon-only tiles')
