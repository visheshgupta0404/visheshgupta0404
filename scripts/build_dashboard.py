"""Build the Option 1 dashboard with Pillow. No portrait cropping or recoloring.
Run from any directory: python scripts/build_dashboard.py
Statistics use the dated, verified snapshot in assets/dashboard-data.json.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,math,textwrap
P=Path(__file__).resolve().parents[1]; A=P/'assets'
BLACK='#020709'; CYAN='#45d9ff'; GREEN='#00ed83'; WHITE='#e4eeef'; DIM='#92aab1'; BORDER='#126078'; INK='#061216'
F='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'; B='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def font(s,b=False):return ImageFont.truetype(B if b else F,s)
DATA=json.loads((A/'dashboard-data.json').read_text())
TECH=[('Py','Python','#53b5e5'),('J','Java','#f1884e'),('JS','JavaScript','#f5d449'),('SQL','SQL','#70c6eb'),('⚛','React','#61dafb'),('N','Node.js','#85c96b'),('F','FastAPI','#23cbb2'),('PG','PostgreSQL','#70a7d4'),('▦','Docker','#34b5f0'),('◆','Git','#f56e51'),('sk','scikit-learn','#efa24c')]
PROJECTS=[('01','Syncora','Synchronized watch-together rooms.','Shared playback, playlists and chat.','React · Vite · Supabase'),('02','PlagLe','Document similarity and plagiarism','analysis with TF-IDF and cosine similarity.','Python · FastAPI · React · MySQL'),('03','ExamEngine','Assessment platform with authentication','and student, professor and admin roles.','JavaScript · Supabase · PostgreSQL'),('04','DispatchLens','Historical delivery-delay analytics.','SQL-backed investigation dashboard.','Python · SQLite · JavaScript')]
def build(mobile=False):
 w,h=(720,3260) if mobile else (1600,1940)
 im=Image.new('RGB',(w,h),BLACK);d=ImageDraw.Draw(im)
 def text(x,y,s,size=22,c=WHITE,b=False):d.text((x,y),s,font=font(size,b),fill=c)
 def box(x,y,ww,hh,outline=BORDER,fill=None,r=7):d.rounded_rectangle((x,y,x+ww,y+hh),r,outline=outline,fill=fill,width=1)
 def line(x,y,xx,yy,c=BORDER):d.line((x,y,xx,yy),fill=c,width=1)
 def section(y,title):
  text(30,y,'> '+title,23,GREEN,True)
  start=48+d.textlength(title,font=font(23,True))+30
  if start<w-30:line(start,y+17,w-30,y+17)
 def wrapped(x,y,s,width=43,size=23,c=WHITE,step=32):
  for a in textwrap.wrap(s,width):text(x,y,a,size,c);y+=step
  return y
 box(3,3,w-7,h-7)
 # Terminal chrome; matches the cyan, single-line frame in Option 1.
 line(3,72,w-4,72)
 for x,c in [(30,'#ff5f57'),(60,'#febc2e'),(90,'#28c840')]:d.ellipse((x,27,x+16,43),fill=c)
 text(130,24,'visheshgupta0404@github:~$',22,GREEN,True)
 if not mobile:text(1160,27,'PROFILE / DEVELOPER',20,CYAN)
 portrait=Image.open(A/'ascii-portrait.png').convert('RGB')
 portrait.thumbnail((550,540) if mobile else (570,565),Image.Resampling.LANCZOS)
 x=(w-portrait.width)//2 if mobile else 26;y=98
 im.paste(portrait,(x,y))
 x,y=(34,666) if mobile else (630,114)
 text(x,y,'// Hi there! Welcome to my terminal.',21,GREEN)
 # Outlined display lettering echoes the reference's ASCII title.
 for title,yy,col in [('VISHESH',y+44,WHITE),('GUPTA_',y+150,GREEN)]:
  d.text((x,yy),title,font=font(86 if mobile else 101,True),fill=BLACK,stroke_width=1,stroke_fill=col)
 yy=y+275
 text(x,yy,'// Computer Science Student',21,GREEN)
 text(x,yy+31,'// Developer | Problem Solver',21,GREEN)
 yy=wrapped(x,yy+81,'Building useful real-world products through software development, full-stack engineering, machine learning and data analysis.',42 if mobile else 44,22,WHITE,31)
 text(x,yy+22,'India  /  visheshg990@gmail.com',21,DIM)
 text(x,yy+58,'github   / visheshgupta0404',20,DIM)
 text(x,yy+91,'linkedin / visheshgupta0404',20,DIM)
 if not mobile:
  box(1272,166,292,145)
  for i,s in enumerate(['> BUILDING','> LEARNING','> EXPLORING','> GROWING...']):text(1290,181+i*29,s,21,CYAN)
  box(1272,339,292,208)
  for i,(s,c) in enumerate([('const mindset = {',CYAN),(' learn: "always",',WHITE),(' build: "useful",',WHITE),(' solve: "real",',GREEN),(' improve: "daily"',GREEN),('}',CYAN)]):text(1286,354+i*28,s,17,c)
 # One continuous background: no GitHub-colored gaps between visual sections.
 loop_y=1350 if mobile else 732
 box(28,loop_y,w-56,106 if mobile else 74)
 words=['CODE','BUILD','LEARN','COLLABORATE','INNOVATE','REPEAT'];colors=[GREEN,CYAN,'#ba94f8','#d991e5','#f1b967',CYAN]
 if mobile:
  for i,word in enumerate(words):text(50+(i%3)*218,loop_y+17+(i//3)*43,word,21,colors[i],True)
 else:
  for i,word in enumerate(words):
   x=52+i*253;text(x,loop_y+25,word,22,colors[i],True)
   if i<5:line(x+223,loop_y+19,x+223,loop_y+55)
 stack_y=1494 if mobile else 822
 section(stack_y,'TECH STACK')
 cols=3 if mobile else 6; tw=206 if mobile else 238; gap=18
 grid_y=stack_y+47; th=106 if mobile else 114
 for i,(symbol,label,color) in enumerate(TECH):
  x=30+(i%cols)*(tw+gap);y=grid_y+(i//cols)*(th+14)
  box(x,y,tw,th,fill=INK)
  if (A/'tech-icon-masks.png').exists() and i not in (3,11):
   mask=Image.open(A/'tech-icon-masks.png').crop((i*96,0,(i+1)*96,96)).resize((48,48),Image.Resampling.LANCZOS)
   im.paste(color,(int(x+(tw-48)/2),y+12,int(x+(tw-48)/2)+48,y+60),mask)
  else:
   sw=d.textlength(symbol,font=font(35,True));text(x+(tw-sw)/2,y+12,symbol,35,color,True)
  lw=d.textlength(label,font=font(18));text(x+(tw-lw)/2,y+70,label,18,WHITE)
 # Twelfth tile is a clear area of focus, not an invented technology.
 x=30+(11%cols)*(tw+gap); y=grid_y+(11//cols)*(th+14)
 box(x,y,tw,th,fill=INK);text(x+tw/2-23,y+12,'</>',29,GREEN);text(x+tw/2-57,y+70,'BUILD TOOLS',18,WHITE)
 project_y=2048 if mobile else 1140
 section(project_y,'FEATURED PROJECTS')
 cw=w-60 if mobile else 756;ch=155 if mobile else 180
 for i,(num,name,a,b,stack) in enumerate(PROJECTS):
  x=30 if mobile else 30+(i%2)*784;y=project_y+46+(i if mobile else i//2)*(ch+16)
  box(x,y,cw,ch,fill=INK)
  text(x+19,y+16,num,18,GREEN);text(x+67,y+13,name,26,CYAN,True)
  # Wrap from combined strings on narrow layouts; keep project descriptions accurate.
  description=a+' '+b
  wrapped(x+20,y+53,description,48 if mobile else 50,19,DIM,25)
  text(x+20,y+ch-35,stack,17,GREEN)
  text(x+cw-34,y+16,'↗',23,CYAN)
 activity_y=2802 if mobile else 1587
 def graph(gx,gy,cell,gap):
  from datetime import date,timedelta
  start=date(2026,5,3)
  palette=['#0b2225','#074c37','#087a4e','#0bb76a','#33f18b']
  for week in range(26):
   for day in range(7):
    dt=start+timedelta(days=week*7+day)
    value=DATA['contributions'].get(dt.isoformat(),0)
    xx=gx+week*(cell+gap);yy=gy+day*(cell+gap)
    d.rounded_rectangle((xx,yy,xx+cell,yy+cell),2,fill=palette[value])
 if mobile:
  section(activity_y,'GITHUB ACTIVITY')
  text(30,activity_y+47,f"{DATA['repositories']} public originals · {DATA['stars']} stars · {DATA['forks']} forks",21,WHITE)
  text(30,activity_y+88,'Languages: '+', '.join(list(DATA['languages'])[:3]),18,DIM)
  text(30,activity_y+143,'CONTRIBUTIONS / MAY–OCT 2026',19,GREEN)
  graph(30,activity_y+184,19,6)
  text(30,activity_y+384,'Snapshot / '+DATA['date'],18,DIM)
  text(30,activity_y+424,'"Turn ideas into code. Code into impact."',19,CYAN)
 else:
  section(activity_y,'GITHUB ACTIVITY')
  box(30,activity_y+48,552,210,fill=INK)
  text(52,activity_y+65,'PUBLIC ORIGINAL REPOSITORIES',18,CYAN)
  text(52,activity_y+105,f"Repositories   {DATA['repositories']}    Stars   {DATA['stars']}",21,WHITE)
  text(52,activity_y+140,f"Forks          {DATA['forks']}",21,WHITE)
  text(52,activity_y+184,' / '.join(list(DATA['languages'])[:4]),16,DIM)
  box(610,activity_y+48,960,210,fill=INK)
  text(632,activity_y+61,'CONTRIBUTIONS / MAY–OCT 2026',17,GREEN)
  graph(632,activity_y+97,14,10)
  text(30,activity_y+298,'"Turn ideas into code. Code into impact."',21,CYAN)
  text(1100,activity_y+298,'SNAPSHOT / '+DATA['date'],18,DIM)
 im.save(A/('option1-mobile.png' if mobile else 'option1-dashboard.png'),optimize=True)
 print('Built',im.size)
if __name__=='__main__':build();build(True)
