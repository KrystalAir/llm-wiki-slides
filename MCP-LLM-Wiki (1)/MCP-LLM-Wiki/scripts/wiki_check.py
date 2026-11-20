#!/usr/bin/env python3
"""Offline MCP Wiki structural lint; not a factual accuracy checker."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors=[];warnings=[];tests=[]

def check(ok, msg, fatal=True):
    tests.append((ok,msg))
    if not ok: (errors if fatal else warnings).append(msg)

registry=json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
sources=registry.get('sources', [])
check(len(sources)>=5, f"來源數量至少五篇（目前 {len(sources)}）")
ids={s['id'] for s in sources}
for s in sources:
    note=ROOT / s['note_path']
    check(note.is_file(), f"來源紀錄存在 {s['id']}: {s['note_path']}")
    if note.is_file():
        content=note.read_text(encoding='utf-8')
        for key in ('id:', 'source_url:', 'accessed:', 'spec_baseline:'):
            check(key in content, f"{s['id']} 包含 {key}")
        check(s['url'] in content, f"{s['id']} 正文包含 registry URL")

for name in ('README.md','AGENTS.md','index.md','log.md','wiki/source-map.md'):
    check((ROOT/name).is_file(), f"必要檔案 {name} 存在")

wiki=list((ROOT/'wiki').glob('*.md'))
check(len(wiki)>=7, f"概念頁至少七頁（目前 {len(wiki)}）")
all_wiki_names={p.stem for p in wiki}
scanfiles=[ROOT/'index.md',*(ROOT/'wiki').glob('*.md'),*(ROOT/'raw').glob('s*.md'),*(ROOT/'workflow').glob('*.md')]
for path in scanfiles:
    body=path.read_text(encoding='utf-8')
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',body):
        # WikiLinks only for wiki/ or named files
        check(target in all_wiki_names, f"wikilink 解析 {path.relative_to(ROOT)} → {target}")
    # Markdown local links, excluding HTTP, mail, anchors, and syntactic blocks
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',body):
        if target.startswith(('http://','https://','mailto:','#')):continue
        target=target.split('#',1)[0]
        check((path.parent/target).is_file(),f"相對連結解析 {path.relative_to(ROOT)} → {target}")
    if path.parent.name=='wiki' and path.stem!='source-map':
        checks=re.findall(r'\[S(\d+)\]\(',body)
        check(len(checks)>0, f"內容頁有來源 ID {path.name}")
        for key in checks:
            check('S'+key in ids, f"{path.name} 引用存在的來源 S{key}")

# stale patterns in tutorial wiki, not in documentation about deprecations
for path in wiki:
    content=path.read_text(encoding='utf-8')
    if re.search(r'必須.*initialize|initialize.*必須',content,re.I):
        warnings.append(f"請人工確認 {path.name} 是否把舊式 initialize 當成必須")

print('MCP Wiki 靜態檢核 / '+registry['as_of'])
print(f'檢查項目數：{len(tests)} ；未通過：{len(errors)} ；需人工注意：{len(warnings)}')
for line in errors:print('ERROR:',line)
for line in warnings:print('WARN:',line)
print('說明：本腳本檢查檔案結構、相對連結、來源 ID 與簡易版本風險；不驗證官方文件事實、網路可達性或 HTML。')
sys.exit(1 if errors else 0)
