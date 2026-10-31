"""Rebuild terminal assets. Requires Pillow; preserves the source portrait pixels."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape
ROOT=Path(__file__).resolve().parents[1]; A=ROOT/'assets'
BG='#050809'; PANEL='#0a1013'; BORDER='#24343b'; CYAN='#65e4ee'; GREEN='#9ae6ac'; WHITE='#edf4f5'; MUTED='#9cabb1'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def hero(mobile=False):
    w,h=(720,1110) if mobile else (1440,660)
    im=Image.new('RGB',(w,h),BG); d=ImageDraw.Draw(im)
    def txt(x,y,s,size=20,c=WHITE): d.text((x,y),s,font=ImageFont.truetype(FONT,size),fill=c)
    d.rounded_rectangle((1,1,w-2,h-2),18,outline=BORDER,width=2)
    for x,c in [(30,'#ff5f57'),(54,'#febc2e'),(78,'#28c840')]: d.ellipse((x,24,x+12,36),fill=c)
    txt(114,22,'visheshgupta0404@github:~$',17,MUTED)
    d.line((1,60,w-2,60),fill=BORDER,width=2)
    portrait=Image.open(A/'ascii-portrait.png').convert('RGB')
    portrait.thumbnail((470,470) if mobile else (510,510),Image.Resampling.LANCZOS)
    px=(w-portrait.width)//2 if mobile else 30; py=88 if mobile else 94
    im.paste(portrait,(px,py))
    x,y=(36,590) if mobile else (596,116)
    txt(x,y,'01 / HELLO, WORLD',18,GREEN)
    txt(x,y+46,'VISHESH GUPTA',44 if mobile else 52,CYAN)
    txt(x,y+116,'Computer Science Student',22)
    txt(x,y+149,'Developer | Problem Solver',22)
    for i,line in enumerate(['Building useful real-world products','through software development,','full-stack engineering, machine','learning, and data analysis.']): txt(x,y+210+i*30,line,20,MUTED)
    txt(x,y+354,'$ whoami --details',19,GREEN)
    txt(x,y+390,'India / visheshg990@gmail.com',19)
    txt(x,y+424,'github   / visheshgupta0404',19,MUTED)
    txt(x,y+456,'linkedin / visheshgupta0404',19,MUTED)
    im.save(A/('terminal-hero-mobile.png' if mobile else 'terminal-hero.png'),optimize=True)
def svg(name,w,h,body):
    (A/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="{BG}" stroke="{BORDER}"/><g font-family="DejaVu Sans Mono,monospace">{body}</g></svg>')
def t(x,y,s,size=18,c=WHITE): return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}">{escape(s)}</text>'
hero(); hero(True)
svg('philosophy.svg',960,88,t(28,32,'DEVELOPER LOOP',12,GREEN)+t(28,62,'CODE → BUILD → LEARN → COLLABORATE → INNOVATE → REPEAT',21,CYAN))
projects=[('syncora','Syncora','01 / REALTIME',['A synchronized watch-together experience.','Shared YouTube playback, playlists and chat.'],'React · Vite · Supabase · PostgreSQL'),('plagle','PlagLe','02 / DOCUMENT INTELLIGENCE',['Document similarity and plagiarism analysis.','TF-IDF vectors and cosine similarity.'],'Python · FastAPI · React · MySQL'),('examengine','ExamEngine','03 / ASSESSMENT',['Assessments with authentication and roles.','Student, professor and administrator flows.'],'JavaScript · Supabase · PostgreSQL'),('dispatchlens','DispatchLens','04 / DATA ANALYSIS',['A delivery-delay investigation dashboard.','Historical order analysis with SQL evidence.'],'Python · SQLite · JavaScript')]
for slug,title,label,lines,stack in projects:
    svg(f'project-{slug}.svg',760,240,t(28,34,label,13,GREEN)+t(28,82,title,31,CYAN)+t(28,127,lines[0],17)+t(28,157,lines[1],17,MUTED)+f'<path d="M28 181H732" stroke="{BORDER}"/>'+t(28,215,stack,16,MUTED))
for slug,label,items in [('languages','LANGUAGES',['Python','Java','JavaScript','SQL']),('engineering','ENGINEERING',['React','Node.js','FastAPI','PostgreSQL']),('tooling','ML & TOOLING',['Docker','Git','scikit-learn'])]:
    b=t(24,32,label,13,GREEN)
    for i,item in enumerate(items):
        x=24+(i%2)*220; y=52+(i//2)*58
        b+=f'<rect x="{x}" y="{y}" width="204" height="44" rx="5" fill="{PANEL}" stroke="{BORDER}"/>'+t(x+14,y+28,item,18,CYAN)
    svg(f'stack-{slug}.svg',480,178,b)
print('Built terminal assets')
# Separate narrow cards keep descriptive text readable on phones.
import textwrap
for slug,title,label,lines,stack in projects:
    b=t(22,32,label,13,GREEN)+t(22,76,title,28,CYAN)
    y=114
    for line in lines:
        for part in textwrap.wrap(line,35): b+=t(22,y,part,17,MUTED); y+=25
    y+=14
    b+=f'<path d="M22 {y}H418" stroke="{BORDER}"/>'
    for part in textwrap.wrap(stack,35): y+=26; b+=t(22,y,part,16,GREEN)
    svg(f'project-{slug}-mobile.svg',440,y+24,b)
