#!/usr/bin/env python3
"""Check layout-only conversion against the source-derived formula inventory."""
from pathlib import Path
import hashlib,json,re,sys
from github_math_guard_v2 import scan_markdown
BASE=Path(__file__).resolve().parent
EXTRA='ell int ll gg asymp lfloor rfloor lceil rceil nmid bmod pmod'.split()
PAGE=BASE.parent/'dujella-problem-1.7/README.md'

def canonical(s):
    s=re.sub(r'\\(?:begin|end)\{(?:gathered|aligned|align\*?)\}', '', s)
    s=re.sub(r'\\(?:qquad|quad|enspace|thinspace)\b', '', s)
    s=re.sub(r'\\[!,;:]','',s)
    s=s.replace('\\\\','').replace('&','')
    return re.sub(r'\s+','',s)

result=scan_markdown(PAGE,strict=True,extra_allowed_macros=EXTRA)
expected=json.loads((BASE/'source_math.json').read_text())
actual=result.expressions
assert len(actual)==len(expected),(len(actual),len(expected))
for i,(a,e) in enumerate(zip(actual,expected),1):
    kind='display' if e['kind']=='DisplayMath' else 'inline'
    assert a.kind==kind,(i,a.kind,kind)
    assert canonical(a.tex)==canonical(e['tex']),(i,a.line,a.tex,e['tex'])
assert not result.findings,[f.format() for f in result.findings]
print(f'PASS: all {len(actual)} formula contents and their order match the source-derived inventory.')
