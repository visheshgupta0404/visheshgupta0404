"""Refresh native README statistics and contribution calendar; Python standard library only.
Network or parse failures leave the previously committed output intact.
"""
import collections
import concurrent.futures
from datetime import datetime, timedelta, timezone
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'visheshgupta0404'
TOKEN = os.environ.get('GH_TOKEN', '')
START, END = '<!-- ACTIVITY:START -->', '<!-- ACTIVITY:END -->'


def request(url, payload=None):
    headers = {'User-Agent': 'vishesh-profile-refresh', 'Accept': 'application/vnd.github+json'}
    if TOKEN and url.startswith('https://api.github.com/'):
        headers['Authorization'] = 'Bearer ' + TOKEN
    data = None if payload is None else json.dumps(payload).encode()
    if data is not None:
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as response:
        return response.read()


def api(url):
    return json.loads(request(url))


def repositories():
    result = []
    for page in range(1, 101):
        batch = api(f'https://api.github.com/users/{OWNER}/repos?type=owner&per_page=100&page={page}')
        if not isinstance(batch, list):
            raise ValueError('Unexpected repository response')
        result.extend(batch)
        if len(batch) < 100:
            return [r for r in result if not r['fork']]
    raise ValueError('Repository pagination limit reached')


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'data-date' in a and 'data-level' in a:
            day = datetime.strptime(a['data-date'], '%Y-%m-%d').date()
            level = int(a['data-level'])
            if not 0 <= level <= 4:
                raise ValueError('Invalid contribution level')
            self.days[day.isoformat()] = {'level': level, 'count': None}


def calendar(now):
    if TOKEN:
        query = '''query($login: String!) { user(login: $login) {
          contributionsCollection { contributionCalendar { weeks {
            contributionDays { date contributionCount contributionLevel }
          } } }
        } }'''
        try:
            obj = json.loads(request('https://api.github.com/graphql', {'query': query, 'variables': {'login': OWNER}}))
            if obj.get('errors'):
                raise ValueError('GraphQL contribution query failed')
            levels = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}
            weeks = obj['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
            days = {d['date']: {'level': levels[d['contributionLevel']], 'count': d['contributionCount']}
                    for w in weeks for d in w['contributionDays']}
            return checked_calendar(days, now)
        except (ValueError, KeyError, TypeError, urllib.error.URLError):
            print('GraphQL unavailable; using public GitHub contribution calendar.')
    parser = CalendarParser()
    parser.feed(request(f'https://github.com/users/{OWNER}/contributions').decode())
    return checked_calendar(parser.days, now)


def checked_calendar(days, now):
    today = now.date()
    oldest = today - timedelta(days=365)
    result = {day: data for day, data in days.items() if oldest <= datetime.strptime(day, '%Y-%m-%d').date() <= today}
    if len(result) < 300 or today.isoformat() not in result:
        raise ValueError('Contribution calendar is incomplete; keeping previous output')
    return result


def svg_calendar(days, now):
    today = now.date()
    first = datetime.strptime(min(days), '%Y-%m-%d').date()
    first -= timedelta(days=(first.weekday() + 1) % 7)
    palette = ['#0b2225', '#074c37', '#087a4e', '#0bb76a', '#33f18b']
    weeks = (today - first).days // 7 + 1
    width = max(720, 42 + weeks * 15)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="174" viewBox="0 0 {width} 174" role="img" aria-labelledby="title desc">',
           '<title id="title">GitHub contribution calendar</title>',
           f'<desc id="desc">Actual daily GitHub contribution levels, refreshed {now:%Y-%m-%d %H:%M UTC}.</desc>',
           f'<rect width="{width}" height="174" rx="8" fill="#020709"/>',
           '<g font-family="monospace" font-size="12" fill="#92aab1">']
    seen_months = set()
    for key, data in sorted(days.items()):
        day = datetime.strptime(key, '%Y-%m-%d').date()
        offset = (day - first).days
        x, y = 20 + (offset // 7) * 15, 40 + (offset % 7) * 15
        month = key[:7]
        if month not in seen_months and day.day <= 7:
            seen_months.add(month)
            out.append(f'<text x="{x}" y="24">{day:%b}</text>')
        count = data['count']
        label = f'{key}: level {data["level"]}' if count is None else f'{key}: {count} contributions'
        out.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{palette[data["level"]]}"><title>{escape(label)}</title></rect>')
    out += [f'<text x="20" y="163">Updated {now:%Y-%m-%d %H:%M UTC}</text>', '</g></svg>']
    return ''.join(out)


def render_activity(repos, languages, now):
    total = sum(languages.values())
    lines = [START, '', f'**Last refreshed:** {now:%Y-%m-%d %H:%M UTC}', '',
             '| Public original repositories | Stars received | Forks received |', '| :---: | :---: | :---: |',
             f'| {len(repos)} | {sum(r["stargazers_count"] for r in repos)} | {sum(r["forks_count"] for r in repos)} |', '',
             '**Most-used languages**', '', '| Language | Share of code bytes |', '| :--- | ---: |']
    lines += [f'| {name} | {n / total:.1%} |' for name, n in languages.most_common(5)] if total else ['| No language data | — |']
    lines += ['', '**Recently pushed repositories**', '']
    for repo in sorted(repos, key=lambda r: r.get('pushed_at') or '', reverse=True)[:3]:
        date = (repo.get('pushed_at') or '')[:10]
        lines.append(f'- [{repo["name"]}]({repo["html_url"]}) · {date}')
    return '\n'.join(lines + ['', END])


def main():
    now = datetime.now(timezone.utc)
    repos = repositories()
    languages = collections.Counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(lambda repo: api(repo['languages_url']), repos):
            languages.update(result)
    days = calendar(now)
    readme = (ROOT / 'README.md').read_text()
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError('Expected one activity marker pair')
    updated = re.sub(re.escape(START) + r'.*?' + re.escape(END),
                     lambda _: render_activity(repos, languages, now), readme, flags=re.S)
    svg = svg_calendar(days, now)
    import xml.etree.ElementTree as ET
    ET.fromstring(svg)
    # Fetch and validate everything before changing any generated file.
    (ROOT / 'assets/contributions.svg').write_text(svg)
    (ROOT / 'README.md').write_text(updated)
    (ROOT / 'assets/profile-activity.json').write_text(json.dumps({
        'updated_at': now.isoformat(), 'repositories': len(repos),
        'stars': sum(r['stargazers_count'] for r in repos),
        'forks': sum(r['forks_count'] for r in repos),
        'language_bytes': dict(languages.most_common()), 'contributions': days,
    }, indent=2) + '\n')
    print(f'Refreshed {len(repos)} public original repositories and {len(days)} contribution days.')


if __name__ == '__main__':
    main()
