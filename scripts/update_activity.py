"""Refresh public GitHub statistics and language byte counts; no external widgets."""
import json, urllib.request, concurrent.futures, collections
from datetime import datetime, timezone
from pathlib import Path
from html import escape
A=Path(__file__).resolve().parents[1]/'assets'
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'vishesh-profile'})
    with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
def build(repos):
    repos=[r for r in repos if not r['fork']]
    langs=collections.Counter()
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        for result in pool.map(lambda r:get(r['languages_url']),repos):langs.update(result)
    date=datetime.now(timezone.utc).strftime('%Y-%m-%d')
    def text(x,y,s,size=17,color='#9cabb1'):return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{escape(str(s))}</text>'
    def save(name,body):
        (A/name).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="440" height="260" viewBox="0 0 440 260"><rect x="1" y="1" width="438" height="258" rx="12" fill="#050809" stroke="#24343b"/><g font-family="DejaVu Sans Mono,monospace">'+body+'</g></svg>')
    b=text(24,34,'GITHUB / PUBLIC REPOSITORIES',15,'#9ae6ac')
    for y,label,value in [(89,'Original repositories',len(repos)),(135,'Stars received',sum(r['stargazers_count'] for r in repos)),(181,'Forks received',sum(r['forks_count'] for r in repos))]: b+=text(24,y,label)+text(370,y,value,26,'#65e4ee')
    save('activity-stats.svg',b+text(24,235,'Snapshot / '+date,13))
    b=text(24,34,'MOST-USED LANGUAGES / BYTES',15,'#9ae6ac'); total=sum(langs.values())
    for i,(lang,n) in enumerate(langs.most_common(5)):
        y=70+i*31; b+=text(24,y,lang,16,'#65e4ee')+text(315,y,f'{n/total:.1%}',16)
    save('activity-languages.svg',b+text(24,245,'Public originals / '+date,13))
if __name__=='__main__':
    repos=[];page=1
    while True:
        batch=get(f'https://api.github.com/users/visheshgupta0404/repos?per_page=100&page={page}&type=owner')
        repos.extend(batch)
        if len(batch)<100:break
        page+=1
    build(repos)
