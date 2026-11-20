#!/usr/bin/env python3
"""Small no-dependency search over MCP Wiki pages; ASCII terms and CJK bigrams."""
from pathlib import Path
import re,sys,math
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)<2:
    print('用法: python scripts/search_wiki.py "tools/list" [最大結果數]')
    raise SystemExit(2)
query=' '.join(sys.argv[1:-1] if sys.argv[-1].isdigit() and len(sys.argv)>2 else sys.argv[1:]).strip().lower()
limit=int(sys.argv[-1]) if sys.argv[-1].isdigit() and len(sys.argv)>2 else 8

def tokens(s):
    s=s.lower(); ascii_terms=re.findall(r'[a-z0-9_/-]{2,}',s)
    han=re.findall(r'[\u3400-\u9fff]+',s)
    bigrams=[chunk[i:i+2] for chunk in han for i in range(len(chunk)-1)]
    return set(ascii_terms+bigrams)
q=tokens(query)
results=[]
for p in (ROOT/'wiki').glob('*.md'):
    content=p.read_text(encoding='utf-8')
    title=content.splitlines()[0].lstrip('# ').lower()
    matched=q & tokens(title+' '+content)
    score=len(matched)*2+sum(5 for x in q if x in tokens(title))
    if query and query in content.lower(): score+=8
    if score:results.append((score,p,content))
results.sort(key=lambda x:(-x[0],x[1].name))
print(f'搜尋：{query} ；匹配頁：{len(results)}')
for score,p,content in results[:limit]:
    lines=content.splitlines(); idx=next((i for i,line in enumerate(lines) if query in line.lower()),1)
    excerpt=' '.join(line.strip() for line in lines[max(0,idx-1):min(len(lines),idx+2)])[:140]
    print(f'[{score}] wiki/{p.name}\n      {excerpt}')
